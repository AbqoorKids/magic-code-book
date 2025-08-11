## **2) ملف المثال الأساسي** 

```python
# -*- coding: utf-8 -*-
# 03_cake.py
# مثال: الشروط المركبة مع and
# سخّن الفرن على درجة حرارة 180 درجة مئوية

temperature = int(input("كم درجة الحرارة؟ "))
time = int(input("كم دقيقة؟ "))

if temperature >= 180 and time > 20:
    print("🍰 الكعكة جاهزة!")
else:
    print("⏳ غير جاهزة بعد")
