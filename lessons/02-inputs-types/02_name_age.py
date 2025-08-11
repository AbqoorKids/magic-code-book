```python
# -*- coding: utf-8 -*-
# 02_name_age.py
# مثال: نسأل الاسم والعمر ونستخدم int() لتحويل العمر لرقم

name = input("ما اسمك؟ ")
age = int(input("كم عمرك؟ "))

if age <= 10:
    print("هل يمكنك أن تلعب معي يا", name, "؟")
else:
    print("تشرفت بمعرفتك يا", name, "!")
