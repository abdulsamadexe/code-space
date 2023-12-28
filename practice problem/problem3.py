# 3.	Print the following table to display the sin value and cos value of degrees from 0 to 360 with increments of 10 degrees. Round the value to keep four digits after the decimal point.
# Degree 		Sin 		Cos
# 0 			0.0000 		1.0000
# 10 			0.1736 		0.9848
# ...
# 350 		-0.1736 	0.9848
# 360 		0.0000 		1.0000
import math
degrees=0
print("Degree   Sin         Cos")
while degrees<=360:
    print(degrees,"     ",round(math.sin(degrees),4),"       ",round(math.cos(degrees),4))
    degrees+=10
