#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
السؤال 2: استخراج البيانات باستخدام BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup

def extract_books_data(url):
    '''
    استخراج بيانات جميع الكتب من صفحة books.toscrape.com
    '''
    try:
        # جلب محتوى الصفحة
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # تحليل HTML باستخدام BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # العثور على جميع عناصر الكتب
        books = soup.find_all('article', class_='product_pod')

        books_data = []

        for book in books:
            # استخراج عنوان الكتاب
            title = book.h3.a['title']

            # استخراج السعر
            price = book.find('p', class_='price_color').text

            # استخراج التقييم
            rating_class = book.find('p', class_='star-rating')['class']
            rating = rating_class[1]  # القيمة الثانية تحتوي على التقييم

            # استخراج رابط الكتاب
            link = book.h3.a['href']

            # استخراج توفر الكتاب
            availability = book.find('p', class_='instock availability').text.strip()

            # إضافة البيانات إلى القائمة
            books_data.append({
                'title': title,
                'price': price,
                'rating': rating,
                'link': link,
                'availability': availability
            })

        return books_data

    except Exception as e:
        print(f"خطأ في استخراج البيانات: {e}")
        return []

# البرنامج الرئيسي
if __name__ == "__main__":
    url = "https://books.toscrape.com"

    print("استخراج بيانات الكتب...")
    books_list = extract_books_data(url)

    if books_list:
        print(f"✓ تم استخراج {len(books_list)} كتاب بنجاح!\n")

        # عرض جميع الكتب المستخرجة
        print("="*80)
        print("البيانات المستخرجة:")
        print("="*80)

        for i, book in enumerate(books_list, 1):
            print(f"\nالكتاب {i}:")
            print(f"  العنوان: {book['title']}")
            print(f"  السعر: {book['price']}")
            print(f"  التقييم: {book['rating']}")
            print(f"  التوفر: {book['availability']}")
            print(f"  الرابط: {book['link']}")
    else:
        print("✗ لم يتم استخراج أي بيانات")
