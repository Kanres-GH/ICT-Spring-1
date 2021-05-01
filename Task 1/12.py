import math
t1, g1 = float(input('t1:')), float(input('g1:'))
t2, g2 = float(input('t2:')), float(input('g2:'))
print('Distance:', 6371.01*math.acos(math.sin(math.degrees(t1))*math.sin(math.degrees(t2))+math.cos(math.degrees(t1))*math.cos(math.degrees(t2))*math.cos(math.degrees(g1-g2))), 'km')