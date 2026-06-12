#TODAY LEARNING ABOUT OPERATORS
#basic arithmetic
a=10
b=23
sum=a+b
print(sum)
a1=22
b1=11
diff=a1-b1
print(diff)
a2=22
b2=11
product=a2*b2
print(product)
a3=22
b3=11
division=a3/b3
print(division)
a4=22
sqrt=22**2
print(sqrt)
a5=11
cube=11**3
print(cube)
age=21
print("Age after one year is ",age+1)
age2=23
print("Age after 10 years is:",age2+10)
height=1.63
height_centi=height*100
print(height_centi)
weight=53
print("Weight after gaining 5 kg is:",weight+5)

#mutiple operations
num1=17
num2=18
print(f"""Sum       : {num1+num2}
Difference: {num1-num2}
Product   : {num1*num2}
Division  : {num1/num2}
""")
a5=11
a6=22
a7=23
total=a5+a6+a7
print(total)

b5=12
b6=34
b7=35
average=(b5+b6+b7)/3
print(average)

price=230
quantity=2
total_bill=price*quantity
print(total_bill)

english=28
telugu=30
social=25
physics=29
biology=30
total_marks=english+telugu+social+physics+biology
print(total_marks)

cloud=29
operating_system=28
programming=27
average=(cloud+operating_system+programming)/3
print(average)

monthly_salary=86000
yearly_salary=monthly_salary*12
print(yearly_salary)

days=20
hours=days*24
print(hours)

hours_in=4
minutes=hours_in*60
print(minutes)

min=4
seconds=min*60
print(seconds)
print("")
#remainder and floor division
remainder=17%5
print(remainder)

num3=25
num4=4
remainder1=num3%num4
print(remainder1)

num6=12
print(num6%2)

num7=14
print(num7%10)

num8=23
num9=34
result=num8//num9
print(result)

print(100//9)
total_chocolates=16
num_of_children=3
chocolate_each_child=total_chocolates//num_of_children
remaining_chocolates=total_chocolates%num_of_children
print(chocolate_each_child)
print(remaining_chocolates)

#level 4 powers
c1=6
print(c1**2)
c2=3
print(c2**3)
print(2**5)
print(3**4)
base1=int(input("Enter the base number:"))
exponent=int(input("Enter the power value:"))
power=base1**exponent
print(power)

#COMPARSION OPERATORS

a=50
b=30
print(a!=b)
print(a>=b)
print(a<=b)
print(a==b)
print(a<b)
print(a>b)

#student eligibility analyzer
name=input("Enter your name:")
age=int(input("Enter your age:"))
marks=int(input("Enter your marks:"))
height=float(input("Enter your height:"))
weight=int(input("Enter your weight:"))
monthly_salary=int(input("Enter your salary:"))
print("---Student Eligibility Analyzer---")
print(f"Name                   : {name}")
print(f"Age>18                 : {age>18}")
print(f"Age==21                : {age==21}")
print(f"Age!=0                 : {age!=0}")
print(f"Marks>35               : {marks>35}")
print(f"Marks<=100             : {marks<=100}")
print(f"Marks==100             : {marks==100}")
print(f"Height>1.5             : {height>1.5}")
print(f"Height<2.5             : {height<2.5}")
print(f"Weight>50              : {weight>50}")
print(f"Weight<100             : {weight<100}")
print(f"Monthly salary>50000   : {monthly_salary>50000}")
print(f"Monthly salary==100000 : {monthly_salary==100000}")
print(f"Monthly salary!=0      : {monthly_salary!=0}")

#Personal growth tracker
name9=input("Enter your name:")
current_age=int(input("Enter your age:"))
current_savings=int(input("Enter your current savings:"))
curent_monthly_salary=int(input("Enter your monthly salary:"))
current_age+=1
current_savings+=5000
curent_monthly_salary+=10000
current_savings-=1000
current_savings*=2
curent_monthly_salary//=2
print("*" *24)
print("Personal Growth Tracker   ")
print("*" *24)
print(f"Name            : {name9}")
print(f"Updated Age     : {current_age}")
print(f"Updated Savings : {current_savings}")
print(f"Updated Salary  : {curent_monthly_salary}")

#logical operators
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("")
print(not True)
print(not False)
print(not (10 > 5))
print(not (10 < 5))
print("")
age = 21
print(age > 18 and age <60)
marks = 75
print(marks > 35 and marks <=100)
print("")
salary = 50000
print(salary > 30000 or salary > 100000)
height = 1.63
print(height > 1.5 and height < 2.5)
print("")
age9 = int(input("Enter your age : "))
print(age9 > 18 and age9 < 60)
marks9 = int(input("Enter your marks : "))
print(marks9 >35 and marks9 <= 100)
salary9 = int(input("Enter your salary : "))
print(salary9 > 50000 or salary9 == 50000)
height9 = float(input("Enter your height : "))
print(height9 > 1.5 and height9 < 2.5)
weight9 = int(input("Enter your weight : "))
print(weight9 > 40 and weight9 < 120)
#student eligibility and profile analyzer
name8 = input("Enter your name : ")
age8 = int(input("Enter your age : "))
marks8 = int(input("Enter your marks : "))
height8 = float(input("Enter your height : "))
weight8 = int(input("Enter your weight : "))
salary8 = int(input("Enter your salary : "))
print("--------Student eligibility and profile analyzer----------")
print(f"Name is                             : {name8}")
print(f"age8 > 18 and age8 < 60             : {age8 > 18 and age8 < 60}")
print(f"marks8 > 35 and marks8 <= 100       : {marks8 >35 and marks8 <= 100}")
print(f"height8 > 1.5 and height8 < 2.5     : {height8 > 1.5 and height8 < 2.5}")
print(f"weight8 > 40 and weight8 < 120      : {weight8 > 40 and weight8 < 120}")
print(F"salary8 > 50000 or salary8== 50000  : {salary8 > 50000 or salary8 == 50000}")
print(f"not(age8 < 18)           : {not(age8 < 18)}")
print(f"not(marks8 < 35)         : {not(marks8 < 35)}")
print(f"not(salary8 == 0)         : {not(salary8 == 0)}")
