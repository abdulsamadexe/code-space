#2.	Write a program that displays the following two tables side by side (note that 1 kilogram is 2.2 pounds and that 1 pound is .45 kilograms):
# Kilograms 		Pounds 		| 		Pounds 		Kilograms
# 1 			2.2 		| 		20 		9.09
# 3 			6.6 		| 		25 		11.36
# ...
# 197 		433.4 		| 		510 		231.82
# 199 		437.8 		|	 	515 		235.09
weight_in_kilos=1
weight_in_pounds=20
print("kilograms   pounds    pounds   kilograms")
while weight_in_kilos<=199:
    print(int(weight_in_kilos),"         ",round(weight_in_kilos*2.2,2),"     |",weight_in_pounds,"        ",float(round(weight_in_pounds*0.45)))
    weight_in_kilos+=2
    weight_in_pounds+=5
