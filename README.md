# TP01: Python Web Scraping Project

## 📚 وصف المشروع
مشروع تطبيقي لتعلم تقنية Web Scraping باستخدام Python، يستهدف استخراج بيانات الكتب من موقع books.toscrape.com

## 🎯 الأهداف التعليمية
- تعلم استخدام مكتبة Requests لجلب محتوى صفحات الويب
- إتقان BeautifulSoup لتحليل واستخراج البيانات من HTML
- حفظ البيانات المستخرجة بصيغة CSV باستخدام pandas

## 📦 المتطلبات
```bash
pip install requests beautifulsoup4 pandas
```

## 📂 محتويات المشروع
- `question1_fetch_html.py` - السؤال 1: جلب محتوى HTML
- `question2_extract_data.py` - السؤال 2: استخراج البيانات
- `question3_save_csv.py` - السؤال 3: حفظ البيانات في CSV
- `complete_solution.py` - الحل المتكامل الكامل
- `books_data.csv` - البيانات المستخرجة

## 🚀 طريقة الاستخدام

### تشغيل الأسئلة بشكل منفصل:
```bash
python question1_fetch_html.py
python question2_extract_data.py
python question3_save_csv.py
```

### تشغيل الحل الكامل:
```bash
python complete_solution.py
```

## 📊 البيانات المستخرجة
- العنوان الكامل
- السعر
- التقييم (1-5 نجوم)
- حالة التوفر
- الرابط

## ✅ النتائج
- تم استخراج 20 كتاب من الصفحة الأولى بنجاح
- جميع البيانات محفوظة في `books_data.csv`

## 👨‍💻 المطور
[Radebr](https://github.com/Radebr)

## 📝 ملاحظات
- الموقع المستخدم هو موقع تعليمي مخصص لتعلم Web Scraping
