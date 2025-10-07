#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
السؤال 1: جلب محتوى صفحة الويب وعرض HTML
"""

import requests

def fetch_webpage_html(url):
    '''
    جلب محتوى صفحة الويب وإرجاع الكود المصدري HTML
    '''
    try:
        # إرسال طلب GET للصفحة
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)

        # التحقق من نجاح الطلب
        response.raise_for_status()

        return response.text

    except requests.exceptions.RequestException as e:
        print(f"خطأ في جلب الصفحة: {e}")
        return None

# البرنامج الرئيسي
if __name__ == "__main__":
    # رابط الموقع المراد استخراجه
    url = "https://books.toscrape.com"

    print("جلب محتوى الصفحة...")
    html_content = fetch_webpage_html(url)

    if html_content:
        print("✓ تم جلب الصفحة بنجاح!")
        print(f"✓ طول محتوى HTML: {len(html_content)} حرف")
        print("\n" + "="*60)
        print("الكود المصدري HTML:")
        print("="*60)
        print(html_content)

        # حفظ HTML في ملف نصي (اختياري)
        with open('webpage_source.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("\n✓ تم حفظ HTML في ملف: webpage_source.html")
    else:
        print("✗ فشل في جلب الصفحة")
