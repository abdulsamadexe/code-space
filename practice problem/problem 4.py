#Suppose that the tuition for a university is $10,000 this year and increases 5% every year. Write a program that computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.
tuition=10000
count=1
while count<=10:
    tuition=tuition+(0.05*tuition)
    tuition=round(tuition,2)
    count+=1
print("tuition in 10 years will be $",tuition)
cost_of_four_years_of_tuition=0
for i in range(4):
    tuition=tuition+(0.05*tuition)
    cost_of_four_years_of_tuition=cost_of_four_years_of_tuition+tuition
    cost_of_four_years_of_tuition=round(cost_of_four_years_of_tuition,2)
print("total cost of four years’ worth of tuition starting ten years from now will be $",cost_of_four_years_of_tuition)


