# Print numbers from 1 to 100

# n = 1

# while n <=100:
#     print(n)
#     n=n+1




# Print numbers from 100 to 1

# n = 100

# while n>=1:
#     print(n)
#     n=n-1


# print the multiplication table of a number n 
# num = 2
# i = 1

# while i<=10:
#     print(num * i)
#     i=i+1



# Print the elements of the following list using the loop

# nums =  [1,4,9,16,25,36,49,64,81,100]
# idx = 0

# while idx < len(nums):
#     print(nums[idx])
#     idx = idx+1




# search for a number x in this tuple using loop

# nums = (1,2,4,5,6,13,36)

# x = 36

# i = 0

# while i <len(nums):
#     if(nums[i] == x):
#         print("FOUND")
#         break
#     i+=1
    
# else:
#     print("not found")


# i = 0

# while i <= 5:
#     if(i==3):
#         i=i+1
#         continue
#     print(i)
#     i=i+1


#for loop 

# heros = ["Me","You","Everyone"]

# for val in heros:
#     print(val)




# print the elements of the following list using a loop 

# [1,4,9,25,36,49,64,81,100]

# nums = [1,4,9,25,36,49,64,81,100]

# for val in nums: 
#     print(val)



# search for a number x in this tupple 
# nums = [1,4,9,25,36,49,64,81,100]

# nums = 1,4,9,25,36,49,64,81,100,25

# x = 25

# idx = 0
# for val in nums:
#     if(val==x):
#         print("found at idx " ,idx)
#         break

#     idx+=1
# else:
#     print("not found") 
   

# print numbers form 1 to 100

# for i in range(1,101,1):
#     print(i)

# print numbers from 100 to 1

# for i in range(100,0,-1):  #step size may be in negative
#     print(i)


# Print the multiplicaion table of a number n 

# n = int(input("Please enter a number"));

# for i in range(1,11):
#     print(n*i)


# pass statement : pass is a null statement that does nothing.It is used as a placeholder for future code


# WAP to find the sum of first natural numbers(using while loop)


#  using while loop
# n = 5
# i =0
# sum = 0

# while i <=n:
#     sum = sum + i
#     i=i+1

# print(sum)



#  using for loop 
# n = int(input("Please enter a number"))
# sum = 1
# for i in range(1,n):
#     sum = sum +i
# print("The sum of n =", sum)



# WAP to find the factorial of first n natural numbers(using for)


n = int(input("Please enter a number"))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("The factorial of n =", fact)

