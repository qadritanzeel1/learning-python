#WAP to input user's first name and print its length

name = input("Please enter a name");

print(len(name));
print(name.count("$"))

# WAP to check if a number entered by the user is even or odd

# num = int(input("Please enter a number"));

if(num%2==0):
    print("even")
else:
    print("odd")


# WAP to find thegreatest of three numbers entered by the user

num1 = int(input("Please enter 1st number"))
num2 = int(input("Please enter 2nd number"))
num3 = int(input("Please enter 3rd number"))

if(num1>num2 and num1>num3) :
    print("1st number is greater")
elif(num2>num1 and num2>num3):
    print("2nd is greater")
else:
    print("3rd is greater")


# number = int(input("Please enter a number"))

if(number%7==0) :
    print("Number is multiple of 7")
else:
    print("Number is not multiple of 7")


#WAP to ask the user to enter names of their 3 favourite movies and store them in a list .

# movies = []

movies.append(input("Enter first fruit : "))
movies.append(input("Enter second fruit : "))
movies.append(input("Enter third fruit : "))

print(movies)



#WAP to check if a list contains a palindrome of elements 

list = ["m","a","a","m"]  #palindrome
list = ["m","a","a","n"]  #not palindrome

copy_list = list.copy()
copy_list.reverse()

if(list==copy_list):
    print("Palindrome")
else:
    print("Not palindrome")


# WAP to count the number of students with the A grade in the following tuple

# grade = ("C", "B", "A", "A", "D", "A");


# print(grade.count("A"))

#store the above values in a list and sort them from A to D
grade = ["C", "B", "A", "A", "D", "A"]

grade.sort()

print(grade)