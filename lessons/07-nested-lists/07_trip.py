# -*- coding: utf-8 -*-
# 07_trip.py
# قائمة رحلات: كل بلد مع الأنشطة التي قام بها عبقور هناك

trip = [
    ["بريطانيا", ["ساعة بيغ بن", "شاي إنجليزي"]],
    ["فرنسا", ["برج إيفل", "كرواسون"]],
    ["إيطاليا", ["برج بيزا", "بيتزا"]],
]

for country_and_activities in trip:
    print("بلد:", country_and_activities[0])
    for activity in country_and_activities[1]:
        print("  نشاط:", activity)
