# -*- coding: utf-8 -*-
# 05_circles.py
# مثال: لعب حلقة حتى يربح عبقور الدبدوب (يحتاج 3 محاولات)

circles_count = 0

while circles_count < 3:
    print("🎯 العب مرة أخرى — المحاولة رقم:", circles_count + 1)
    circles_count = circles_count + 1  # أو circles_count += 1

print("🎉 مبروك! ربحت الدبدوب")
