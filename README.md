# Python-Tasks
Daily Python practice tasks
#1. Check whether employee age is above 21 and salary is above 30000

age=int(input("enter the age:"))
salary=int(input("enter your salary:"))#
if age>21 and salary>30000:
    print("employee can do his job")
else:
    print("change to another company")


#2. Check whether student passed in two subjects

sub1=int(input("enter marks of sub1:"))
sub2=int(input("enter marks of sub2:"))
if sub1>=35 and sub2>=35:
      print("pass")
else:
    print("fail")


#3. Check whether entered value is between two ranges
num=int(input("enter a number:"))
max_value=int(input("enter a maximum value:"))
min_value=int(input("enter a minimum value:"))
if num>min_value and num<max_value:
    print("the number is between two ranges")


#4. Check whether username and password are correct
username="bhagya@123"
password=2005
user_name=input("enter your username:")
pass_word=int(input("enter your password:"))
if username==user_name and password==pass_word:
      print("user_name and password are correct")
else:
       print("user_name and password are  not correct")


#5. Check whether temperature is within safe range

lower_limit=float(input("enter the lower limit:"))
upper_limit=float(input("enter the upper limit:"))
temperature=float(input("enter the temperature:"))
if temperature>lower_limit and temperature<upper_limit:
    print("temperature is in safe range")
else:
    print("temperature is not in safe range")
"""

#6. Check whether both entered numbers are even

num1=int(input("enter first numner:"))
num2=int(input("enter second numner:"))
if num1%2==0 and num2%2==0:
    print("both are even numbers")
else:
    print("not even numbers")

#7. Check whether both entered numbers are positive

num1=int(input("enter first numner:"))
num2=int(input("enter second numner:"))
if num1>0 and num2>0:
    print("both are positive")
else:
    print("both are negative")


#8. Check whether person is eligible for driving
age=int(input("enter age:"))
license=input("have license?:")
if age>18 and license=="yes":
    print("eligible")
else:
    print("not eligible")


#9. Check whether project progress meets deadline condition

remaining_days=int(input("enter the value:"))
progress_percentage=int(input("enter the percentage:"))
if remaining_days<10 and progress_percentage>40:
    print("project progress meets deadline condition")
else:
    print("project progress doesnot meets deadline condition")


#10. Check whether attendance and marks satisfy eligibility
att=int(input("enter your attendence percentage:"))
marks=int(input("enter marks:"))
if att>=75 and marks>=35:
    print("eligible")
else:
    print("not eligible")


#11. Check whether entered role is Admin or Manager

role=input("enter role:")
if role=="Admin" or role=="Manager":
    print("entered role is Admin or Manager")
else:
    print("entered role is neither Admin nor Manager")
    
#12. Check whether student scored distinction in any one subject
sub1=int(input("enter sub1 marks:"))
sub2=int(input("enter sub2 marks:"))
sub3=int(input("enter sub3 marks:"))
sub4=int(input("enter sub4 marks:"))
if sub1>75 or sub2>75 or sub3>75 or sub4>75:
    print("student scored in distinction level")
else:
    print("not in distinction level")


#13. Check whether entered day is weekend

day=input("enter the day:")
if day=="saturday"or day=="sunday":
    print("its weekend")
else:
    print("not a weekend")


#14. Check whether selected category matches two possible values

category=input("enter the category1:")
val1=input("enter the val1:")
val2=input("enter the val2:")
val3=input("enter the val3:")
if category==val1 or category==val2 or category==val3:
    print("selected category matches two possible values")
else:
    print("selected category not matches two possible values")


#15. Check whether salary or experience satisfies requirement
salary=int(input("enter your salary expectation :"))
exp=int(input("enter your experience:"))
if salary<30000 or exp>2:
    print("eligible")
else:
    print("not eligible")


#16. Check whether temperature is extremely low or high
lower_limit=float(input("eneter the lower temperature:"))
upper_limit=float(input("eneter the higher temperature:"))
temperature=float(input("enter the temperature:"))
if temperature<lower_limit or temperature>upper_limit:
    print("temperature is extremely low or high")

#17. Check whether entered username matches predefined values



#18. Check whether selected option belongs to given choices

selected_option=int(input("enter the value:"))
given_choice1=int(input("enter the choice1 value:"))
given_choice2=int(input("enter the choice2 value:"))
given_choice3=int(input("enter the choice3 value:"))
if selected_option== given_choice1 or selected_option== given_choice2 or selected_option== given_choice3:
    print("selected option belongs to given choices")
else:
    print("selected option not belongs to given choices")


#19. Check whether entered city matches allowed cities
entered_city=input("enter the city:")
allowed_city1=input("enter the allowed city1:")
allowed_city2=input("enter the allowed city2:")
if entered_city==allowed_city1 or entered_city==allowed_city2:
    print("entered city matches allowed cities")
else:
    print("entered city doesnot matches allowed cities")


#20. Check whether entered number matches predefined values
entered_num=int(input("enter the number:"))
predefined_num1=int(input("enter the predefined value1:"))
predefined_num2=int(input("enter the predefined value2:"))
if entered_num==predefined_num1 or entered_num==predefined_num2:
    print("entered number matches predefined values")
else:
    print("entered number doesnot matches predefined values")
