#use for loop to find the index of 50

# a = [1,45,23,40,60,50,90,100]


# for i in range(len(a)):
    
#     if(a[i] == 50):
#         print("The index of given number is ", i)


# break statement:
# this is used to break the loop execution

# sort () in list:it will sort the data


# a = [1,4,5,6,3,2,7,8,9,0,1,]
# a.sort()
# print(a)

# if you wnt to sort in reverse order 

# a = [1,4,5,6,3,2,7,8,9,0,1,]

# a.sort(reverse=True)

# print(a)

# Reverse () : used to reverse a list

# a = [1,2,3,4,5,6,7]
# a.reverse()
# print(a)


# membership 
# a = [10,20,40,9,78]

# if 8 in a:
#     print(a)


# slicing of list: extracting some slice of a list

# a = [1,2,3,4,5,6]

# b = a[0:5]
# print(b)

# how to take list as a input in single line 



# a = list(map(int,input().split()))

# print sum of al even numbers of a list

# a=[10,10,40,3,5,7]
# sum = 0
# for i in range(len(a)):
#     if a[i]%2==0:
#         sum = sum + a[i]
# print(sum)        


# take int list as input and print maximum element from it.

# a  = []
# max = -1
# for i in range(5):
#     num = int(input("Please enter a number"))
#     a.append(num)
# for num in a[:]:
#     if num > max:
#         max = num
# print(max)        

# another method

# a = list(map(int,input().split()))
# maxEle = -1
# for i in a:
#     if i>maxEle:
#         maxEle = i
# print(maxEle)        


# a = list(map(int,input().split()))
# minEle = a[0]
# for i in a:
#     if i<minEle:
#         minEle = i
# print(minEle)        


# Print reverse of a list without using reverse 

# a = [1,2,3,4,5]

# rev = []

# for i in range(len(a)-1,-1,-1):
#     rev.append(a[i])

# print(rev)    


# take an int list as user input and take a number x, find the frequency of x in the list.
# a = list(map(int,input().split()))

a = list(map(int,input().split()))
x=int(input())
count=0
for i in a:
    if i == x:
        count = count+1
print(count)

