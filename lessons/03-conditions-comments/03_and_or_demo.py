# -*- coding: utf-8 -*-
# 03_and_or_demo.py
# أمثلة على and و or

age = int(input("كم عمرك؟ "))
has_ticket = input("هل لديك تذكرة؟ (نعم/لا) ") == "نعم"

# باستخدام and
if age >= 18 and has_ticket:
    print("✅ يمكنك الدخول")
else:
    print("❌ لا يمكنك الدخول")

# باستخدام or
is_member = input("هل أنت عضو؟ (نعم/لا) ") == "نعم"
if age >= 18 or is_member:
    print("🎉 يمكنك الانضمام للنادي")
else:
    print("🚫 عذرًا، لا يمكنك الانضمام")
