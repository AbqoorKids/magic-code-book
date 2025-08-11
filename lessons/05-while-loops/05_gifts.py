# -*- coding: utf-8 -*-
# 05_gifts.py
# مثال: عبقور يعطي هدايا طالما عنده بالونات أو أزهار

balloons = 3
flowers = 2

while balloons > 0 or flowers > 0:
    print("🎁 عبقور يعطي هدية!")
    if balloons > 0:
        balloons -= 1
    elif flowers > 0:
        flowers -= 1

print("🎈 انتهت الهدايا — بالونات:", balloons, "ازهار:", flowers)
