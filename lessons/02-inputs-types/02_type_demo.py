# -*- coding: utf-8 -*-
# 02_type_demo.py
# نعرض نوع القيم ولماذا نحتاج int()

name = input("اكتب اسمك: ")
print("نوع name هو:", type(name))

age_text = input("اكتب رقمًا مثلا 7: ")
print("نوع age_text هو:", type(age_text), "قيمة:", age_text)

# الآن نحول النص إلى عدد صحيح
age = int(age_text)
print("بعد التحويل:")
print("نوع age هو:", type(age), "وقيمته:", age)
