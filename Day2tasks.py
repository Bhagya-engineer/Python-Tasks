#1. Check Employee promotion eligibility

age = int(input("Enter age: "))
experience = int(input("Enter experience: "))
salary = int(input("Enter salary: "))
if age > 25 and experience > 5 and salary > 50000:
    print("Eligible for Promotion")
else:
    print("Not Eligible")
else:
    print("Not Eligible")

# 2. Check student distinction category

mat=int(input("Enter maths marks: "))
sci=int(input("Enter science  marks : "))
eng=int(input("Enter english marks: "))
if mat >= 75 and sci >= 75 and eng >= 75:
    print("Distinction")
elif mat >= 35 and sci >= 35 and eng>= 35:
    print("Pass")
else:
    print("Fail")
  
# 3. Check website login system

username = "bhagya"
password = "123"
otp = "2627"
u = input("Enter username: ")
p = input("Enter password: ")
o = input("Enter OTP: ")
if u == username and p == password and o == otp:
    print("Login Successful")
else:
    print("Invalid Credentials") 

#4. Check internet package category

speed = int(input("Enter the speed: "))
data = int(input("Enter data usage: "))
days = int(input("Enter remaining days: "))

if speed > 100 and data > 500 and days > 20:
    print("Premium Plan")
elif speed > 50 and data > 200 and days > 10:
    print("Standard Plan")
else:
    print("Basic Plan")

# 5. Check job eligibility

degree = input("Do you have a degree: ")
experience = int(input("Enter experience: "))
age = int(input("Enter age: "))

if degree == "yes" and experience >= 2 and age > 21:
    print("Eligible for Interview")
else:
    print("Not Eligible")

#6. Check flight boarding eligibility

ticket = input("do you have ticket: ")
passport = input("do you have passport: ")
luggage = int(input("Enter luggage weight: "))
if ticket == "yes" and passport == "yes" and luggage < 30:
    print("Boarding Allowed")
else:
    print("Boarding Denied")

# 7. Check scholarship eligibility

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
income = int(input("Enter family income: "))
if marks >= 85 and attendance >= 90 and income < 300000:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")


# 8. Check mobile unlock system

pin = "1234"
pin= input("Enter PIN: ")
face = input("Face detected: ")
finger = input("Fingerprint detected : ")
if pin == pin and face == "yes" and finger == "yes":
    print("Mobile Unlocked")
else:
    print("Access Denied")


# 9. Check hotel booking eligibility

rooms = int(input("Enter number of rooms: "))
days = int(input("Enter number of days: "))
budget = int(input("Enter the budget: "))
if rooms >= 2 and days >= 3 and budget > 50000:
    print("Luxury Booking")
elif budget > 20000:
    print("Standard Booking")
else:
    print("Budget Booking")

# 10. Check exam topper category

sub1 = int(input("Enter subject 1 marks: "))
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))
total_marks = sub1 + sub2 + sub3
if total_marks >= 270:
    print("Topper")
elif total_marks >= 180:
    print("Average")
else:
    print("Needs Improvement")

# 11. Check gym membership category

age = int(input("Enter age: "))
weight = int(input("Enter weight: "))
height = float(input("Enter height: "))
if age > 18 and weight > 50 and height > 5.5:
    print("Fitness Category A")
elif age > 18 and weight > 40:
    print("Fitness Category B")
else:
    print("Basic Category")

# 12. Check traffic penalty system

helmet = input("Do you have helmet?: ")
license = input("Do you have License? : ")
speed = int(input("Enter speed: "))
if helmet == "yes" and license == "yes" and speed < 80:
    print("No Fine")
elif speed >= 80:
    print("Heavy Fine")
else:
    print("Normal Fine")

# 13. Check movie ticket pricing

age = int(input("Enter age: "))
day = input("Enter day: ")
member = input("Do you have Membership?: ")
if age < 18 and member == "yes" and day == "Sunday":
    print("50% Discount")
elif member == "yes":
    print("25% Discount")
else:
    print("No Discount")

# 14. Check weather alert system

temperature = int(input("Enter temperature: "))
wind = int(input("Enter wind speed: "))
rain = input("Rain status : ")
if temperature > 40 and wind > 50 and rain == "no":
    print("Heat Alert")
elif wind > 70 and rain == "yes":
    print("Storm Alert")
else:
    print("Normal Weather")

# 15. Check online shopping offer

amount = int(input("Enter purchase amount: "))
coupon = input("do you have coupon?: ")
member = input("Do you have Premium membership: ")
if amount > 10000 and coupon == "yes" and member == "yes":
    print("Maximum Discount")
elif amount > 5000 and coupon == "yes":
    print("Medium Discount")
else:
    print("No Discount")

# 16. Check server room access

idcard = input(" Do you have ID card : ")
fingerprint = input("Fingerprint available: ")
accesslevel = int(input("Enter the access level: "))
if idcard == "yes" and fingerprint == "yes" and accesslevel > 5:
    print("Access Granted")
else:
    print("Access Restricted")

# 17. Check sports team selection

speed = int(input("Enter speed score: "))
fitness = int(input("Enter fitness score: "))
discipline = int(input("Enter discipline score: "))
if speed > 80 and fitness > 80 and discipline > 80:
    print("Selected")
elif speed > 60 and fitness > 60:
    print("Waiting List")
else:
    print("Rejected")

# 18. Check laptop purchase recommendation

budget = int(input("Enter your  budget: "))
ram = int(input("Enter RAM: "))
storage = int(input("Enter storage: "))
if budget > 100000 and ram >= 16 and storage >= 512:
    print("Gaming Laptop")
elif budget > 50000 and ram >= 8:
    print("Office Laptop")
else:
    print("Basic Laptop")

# 19. Check bank loan approval

salary = int(input("Enter salary: "))
credit_score = int(input("Enter credit score: "))
experience = int(input("Enter experience: "))
if salary > 50000 and credit_score > 750 and experience > 3:
    print("Loan Approved")
elif salary > 30000 and credit_score > 650:
    print("Loan Under Review")
else:
    print("Loan Rejected")

# 20. Check smart home security system

door = input("Door status : ")
camera = input("Camera status: ")
alarm = input("Alarm status: ")
if door == "yes" and camera == "yes" and alarm == "yes":
    print("Home Secure")
else:
    print("Security Warning")
