# -*- coding: utf-8 -*-
# 05_icecream.py
# مثال: عبقور يأكل آيس كريم طالما معه نقود وما جرب كل النكهات

money = 3
flavours = 4

while money > 0 and flavours > 0:
    print("🍦 عبقور يأكل آيس كريم!")
    money -= 1
    flavours -= 1

print("🧾 تبقى نقود:", money, " | تبقى نكهات:", flavours)
if money <= 0 or flavours <= 0:
    print("⏳ لا يستطيع أن يجرب أكثر الآن.")
