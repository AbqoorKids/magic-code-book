# -*- coding: utf-8 -*-
# 06_total_weight.py
# جمع أوزان 3 أسماك دخلها المستخدم باستخدام for

total_weight = 0

for _fish in range(3):
    # نحاول تحويل الإدخال إلى عدد صحيح - لو كتب المستخدم نصًا سيحصل على خطأ
    weight = int(input("أدخل وزن السمكة (بالكغ): "))
    total_weight = total_weight + weight  # أو total_weight += weight

print("المجموع =", total_weight)
