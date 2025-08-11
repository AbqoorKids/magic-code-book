# -*- coding: utf-8 -*-
# 08_clean_music_room.py
# تابع ينظف غرفة الموسيقى ويستدعي تابع آخر لتنظيف الرفوف

def clean_music_room():
    # طباعة مهمة ري النباتات
    print("ري النباتات")
    # استدعاء التابع المسؤول عن تنظيف الرفوف
    clean_shelves()

def clean_shelves():
    # تكرار 3 مرات
    for shelf in range(1, 4):
        print("نظّف الرف رقم", shelf)

# استدعاء التابع الرئيسي
clean_music_room()
