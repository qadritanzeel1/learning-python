# backward iteration using for loop

# for i in range(10,0,-1):
#     print(i)

    # through while loop


# backward iteration using while loop

# i=10

# while i>=1:
#     print(i)
#     i=i-1

# print all even numbers from 1 to 50

# using while loop

# num = int(input("Please enter a number "))

# i= 0

# while i <= num:
#     if(i%2==0):
#         print(i)
#     i=i+1    



# printing even numbers using for loop


# for i in range(1,51,):
#     if(i%2==0):
#          print(i)
    

# Print all odd numbers from 1 to 50

# using for loop
# for i in range(1,51):
#     if(i%2!=0):
#         print(i)

    

# using while loop

# num = int(input("Please enter a number"))
# i = 1

# while i<=num:
#     if(i%2!=0):
#         print(i)
#     i=i+1    


# Print the multiplication table of number entered by the user

# using while loop

# num = int(input("Please enter a number"))
# i=1
# while i<=10:
#     print(num*i)
#     i = i +1


#  table using for loop

# num = int(input("Please enter a number"))

# for i in range(1,11):
#     print(num*i)

# find the sum of numbers from  1 to n

# finding sum using while loop 

# num = int(input("Please enter a number"))

# i=0
# sum =0

# while i<=num:
#     sum=sum+i
#     i+=1

# print(sum)    

# finding sum using for loop

# num = int(input("Please enter a number"))

# sum = 0

# for i in range(1,num+1):
#     sum=sum+i


# print(sum)


# find priduct of numbers

# product of numbers using while loop

# num = int(input("Please enter a number"))

# i = 1
# product = 1
# while i<=num:
#     product=product*i
#     i+=1
# print(product)    


# product of numbers using for loop

# num = int(input("Please enter a number"))
# product = 1
# for i in range(1,num+1):
#     product*=i
    
# print(product)    

# count how many numbers are divisible by 3 between 1 to 100
# using while loop
# num = int(input("Please enter a number"))
# i=1
# count = 0

# while i<=num:
#     if(i%3==0):
#         count=count+1
#     i=i+1
# print(count)    


# using for loop

# num = int(input("Please enter a number"))

# count = 0

# for i in range(1,num):
#     if(i%3==0):
#         count+=1
# print(count)        


# Print the square of numbers from 1 to 10

# using while loop

# num = int(input("Please enter a number"))
# i=1
# sq=0
# while i<=10:
#     sq=i**2
#     i=i+1
#     print(sq)    


# using for loop 


sq=0
for i in range(1,11):
    sq = i**2
    print(sq)    

# write code to print sum of all odd numbers from 1 to 100000

# i=1
# sum = 0
# while i<=3:
#     if(i%2!=0):
#         sum=sum+i
#     i=i+1    
# print(sum)    


# write code to print sum of all even numbers

# i = 1
# sum =0

# while i<=10:
#     if(i%2==0):
#         sum=sum+i
#     i+=1
# print(sum)    


# without using step paremeter print sum of values between 1 and 1000
# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print(sum)    


# Print numbers from 1000 to 1 in desc order using for loop.


# for i in range(10,0,-1):
#     print(i)


# take n (an integer input from user) and print n number of "*" using for loop.

# n = int(input("Please enter a number"))

# for i in range(0,n):
#     print("*")


# take an integer and print table of that number

# n = int(input("Please enter a number"))

# for i in range(1,11):
#     print(n*i)


# print all the multiples of 8 between 50 and 500 using for loop.


# for i in range(50,501):
#     if(i%8==0):
#         print(i)

#count number of integers b/w 1 and 1000 which are divisible by 3 and 5 both


count = 0

# for i in range(1,1001):
#     if(i%3==0 and i%5==0):
#         print(i)


# factorial of a number
n=3
fact = 1

for i in range(1,n+1):
    fact*=i
print(fact)

