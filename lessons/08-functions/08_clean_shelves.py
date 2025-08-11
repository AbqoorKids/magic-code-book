# -*- coding: utf-8 -*-
# 08_clean_shelves.py
# تابع لتنظيف الرفوف

def clean_shelves():
    # تكرار 3 مرات
    for shelf in range(1, 4):
        # تتوقف قبل الرقم الأخير (لن تصل للتكرار رقم 4)
        print("نظّف الرف رقم", shelf)

# استدعاء التابع
clean_shelves()
