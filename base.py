import math

ang = [20, 45, 70, 110, 135, 160, 200, 225, 250, 290, 315, 340]
r1 = 110
r2 = 130

idx = 0
for i in ang:
    idx += 1
    if idx % 3 == 2:
        print str(idx) + " -> " + str(128 + r2*math.cos(math.radians(i))) + ":" + str(128 + r2*math.sin(math.radians(i)))
    else:
        print str(idx) + " -> " + str(128 + r1*math.cos(math.radians(i))) + ":" + str(128 + r1*math.sin(math.radians(i)))