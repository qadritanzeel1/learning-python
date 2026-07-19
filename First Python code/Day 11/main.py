# lists in python : A list is an ordered collection of elements
# linear data structure

# a = [1,8,-1,12,0]  # a is a vriable in which list is stored 

# it can store different data types in the same list 
# eg it can have int float strings boolean etc

# data = [ 12, "july", "list", True,1.11]

# Properties 
# lists are mutable means we can alter the data eg add and remove the data
# dynamic size
# accessed by indexing
# indexing always starts from 0


# a=[10,20,25,24]
#   0  1  2  3

# index = position -1



# accessing the elements of the list 
# a= [10,20,30,40,90]

# print(a[3])

# declare the value of 5 integers and print all elements of the list using loop

# a = [1,2,3,4,5,6,7,8,9,10]

# for i in a:
#     print(i)

# negative indexing

# length function is used to find the length of the array

# print(len(a))

# traversing of a list

# modifying list elements
# a=[1,2,34,5]
# a[2]=4
# print(a)


# assign a list 10 positive integers and modify every element on odd position 

# a  = [1,2,3,4,5,6,7,8,9,10]

# for i in range(len(a)):
#     if i%2==0 :
#         a[i] = -1
# print(a)            



# standard list operations

# append() : adds elements at the end of the list

# time complexity for adding an element in the end of a list = O(1)


# take 10 inputs from user and append them after every input in an empty list

# H/W try this using loop
# list = []
# list.append(input("Please enter first input"))
# list.append(input("Please enter 2nd input"))
# list.append(input("Please enter 3rd input"))
# list.append(input("Please enter 4th input"))
# list.append(input("Please enter 5th input"))
# list.append(input("Please enter 6th input"))
# list.append(input("Please enter 7th input"))
# list.append(input("Please enter 8th input"))
# list.append(input("Please enter 9th input"))
# list.append(input("Please enter 10th input"))
# list.append(input("Please enter 11th input"))

# print(list)




#  take 100 inputs from the user, append into a list and find sum of all elements of that list

# list = []
# sum = 0 
# for i in range(5):
#     list.append(int(input("Please enter a number")))
#     sum = sum + list[i]

# print(sum)


# insert operation : used to insert an element on a particular index

# a = [1,2,3]

# a.insert(2,100)

# print(a)

# O(n)

# pop function : remove the element at the end
# a = [10,20,30,40]

# a.pop()

# print(a)


# remove op 
# take 10 inputs , append in empty list, remove all elements which are divisible by 5.

# numbers = []
# # taking input
# for i in range(10):
#     num = int(input(f"Please enter a number {i+1} "))
#     numbers.append(num)
# # removing elements that are divisible by 5

# for num in numbers[:]:
#     if(num%5==0):
#         numbers.remove(num)
# print(numbers)        


