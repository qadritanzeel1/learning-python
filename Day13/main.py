# Count Positive, Negative, and Zero


# arr = [1 ,-3, 0, 5, 7, -2, 0, -8]

# count_z = 0
# count_n=0
# count_p =0

# for i in range(len(arr)):
#     if(arr[i]==0):
#         count_z+=1

#     elif(arr[i]<0):
#         count_n+=1
        
#     else:
#         count_p+=1
        

# print("positive",count_p)
# print("negative",count_n)
# print("zeros",count_z)        



# another method

# arr = [0,0,12,-1,20,30,90,-1,-3,-9,0,0,-8]

# positive = negative = zero = 0

# for i in arr:
#     if i==0:
#         zero+=1
#     elif i<0:
#         negative+=1
#     else:
#         positive+=1

# print(positive,negative,zero)

# Separate Even and Odd Numbers

# arr = [1,2,3,4,5,6,7,8,9,10]

# even = []
# odd = []

# for i in arr:
#     if i%2 ==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)        

# Merge two lists

# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]

# mergelist = list1+list2
# print(mergelist)

# Remove duplicate elements

# arr = [1,2,1,3,4,5,1]
# unArr = []

# for i in arr:
#     if i not in unArr:
#         unArr.append(i)

# print(unArr)     


# Find second largest element


# arr = [0,3,4,5,67,99,88]
# largest = arr[0]
# second_largest = arr[0]
# for num in arr:
#     if num>largest:
#         largest = num
# for num in arr:
#     if num>second_largest and num!=largest:
#         second_largest = num 
# print(largest) #first largest number
# print(second_largest) #second largest number 




# find the second smallest number


# arr = [9,5,4,3,2]

# smallest = arr[0]
# second_smallest = arr[0]

# for num in arr:
#     if num<smallest:
#         smallest = num
# for num in arr:
#     if num<second_smallest and num>smallest:
#         second_smallest=num
# print(second_smallest)        

# Left rotate a list by one position

arr = [1,2,3,5,6,7,23]
first = arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]

arr[len(arr)-1]=first
print(arr) 


# right rotate a list bye one position

arr = [1,2,3,4]

last = arr[len(arr)-1]

for i in range(len(arr)-1,0,-1):
    arr[i] = arr[i-1]
arr[0]=last
print(arr)  
    




