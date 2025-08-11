# -*- coding: utf-8 -*-
# 02_crowns.py
# مثال: نتحقق إن كان عدد التيجان زوجي أو فردي

crowns = int(input("كم تاج يملك الأسد؟ "))
if crowns % 2 == 0:
    print("عدد التيجان زوجي")
else:
    print("عدد التيجان فردي")
