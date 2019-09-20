from math import *

def hav(diff):
	cosd = cos(radians(diff))
	answer = (1-cosd)/2
	return answer

lat1 = float(input())
lon1 = float(input())
lat2 = float(input())
lon2 = float(input())

hav1 = hav(lat2 - lat1)
hav2 = hav(lon2 - lon1)

havTheta = hav1 + (cos(radians(lat1)))*(cos(radians(lat2)))*(hav2)
rootH = sqrt(havTheta)

radius = 6378

answer = 2*radius*asin(rootH)
print(answer)