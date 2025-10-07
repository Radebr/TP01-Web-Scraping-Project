#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
السؤال 3: حفظ البيانات في ملف CSV باستخدام pandas
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_books_data(url):
    '''استخراج بيانات الكتب'''
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        books_data = []

        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            rating_class = book.find('p', class_='star-rating')['class']
            rating = rating_class[1]
            link = book.h3.a['href']
            availability = book.find('p', class_='instock availability').text.strip()

            books_data.append({
                'Title': title,
                'Price': price,
                'Rating': rating,
                'Link': link,
                'Availability': availability
            })

        return books_data

    except Exception as e:
        print(f"خطأ في استخراج البيانات: {e}")
        return []

def save_to_csv(data, filename='books_data.csv'):
    '''حفظ البيانات في ملف CSV باستخدام pandas'''
    try:
        # تحويل البيانات إلى DataFrame
        df = pd.DataFrame(data)

        # حفظ DataFrame في ملف CSV
        df.to_csv(filename, index=False, encoding='utf-8-sig')

        print(f"✓ تم حفظ البيانات بنجاح في الملف: {filename}")
        print(f"✓ عدد السجلات: {len(df)}")
        print(f"✓ عدد الأعمدة: {len(df.columns)}")

        # عرض معلومات عن البيانات
        print("\n" + "="*80)
        print("معاينة البيانات المحفوظة:")
        print("="*80)
        print(df.head(10))

        print("\n" + "="*80)
        print("إحصائيات البيانات:")
        print("="*80)
        print(df.describe())

        return True

    except Exception as e:
        print(f"✗ خطأ في حفظ الملف: {e}")
        return False

# البرنامج الرئيسي
if __name__ == "__main__":
    url = "https://books.toscrape.com"
    output_file = "books_data.csv"

    print("بدء عملية Web Scraping...")
    print("="*80)

    # الخطوة 1: استخراج البيانات
    print("\n[1/2] استخراج بيانات الكتب...")
    books = extract_books_data(url)

    if books:
        print(f"✓ تم استخراج {len(books)} كتاب")

        # الخطوة 2: حفظ في CSV
        print(f"\n[2/2] حفظ البيانات في {output_file}...")
        success = save_to_csv(books, output_file)

        if success:
            print("\n" + "="*80)
            print("✓ اكتملت العملية بنجاح!")
            print("="*80)
    else:
        print("✗ فشل في استخراج البيانات")
