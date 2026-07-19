# Find the larger of two numbers.

a=10
b=20

if(a>b) :
    print(a , "is large")
else :
    print(b,"is large")



#check if a numer is even or odd

num = 4

if(num%2==0):
    print("even")
else:
    print("odd")


# Check if a number is positive, negative, or zero.

num = -1

if(num<0):
    print("The given number is negative")
elif(num>0):
    print("The given number is postive")
elif(num==0):
    print("The given number is 0")


# Check if a year is a leap year.

year = 2020

if((year%400==0) or (year%4==0 and year%100!=0)):
    print("Leap Year")
else:
    print ("not a leap year")

    # Find the largest of three numbers.


a = 40
b = 90
c = 30

if(a>b and a>c):
    print(a,"is greater")
elif(b>a and b >c):
    print(b,"is greater")
else:
    print(c,"is greater")

# Check whether a character is a vowel or consonant.


char = "e"

if char in "aeiou":
    print("The character is vowel")
else:
    print("The character is consonant")



# Calculate a student's grade based on marks.


marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: C")
elif 60 <= marks <= 69:
    print("Grade: D")
else:
    print("Grade: F")



char = "H"

if char.isupper():
    print("Upper Case")
elif char.islower():
    print("Lower Case")
else:
    print("Invalid Input")