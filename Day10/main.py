# lists in python

# list = [3,4,2,1,5,6,8,7]
# list.append(9)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)

# list.insert(1,19)
# print(list)

# tuple in python

# A built-in data type that lets us create immutable sequences of values

# WAP to ask the user to enter names of their favourite  movies and store them in a list

# movies = []

# mov1 = input("Please enter 1st favourite movie")
# mov2 = input("Please enter 2st favourite movie")
# mov3 = input("Please enter 3rd favourite movie")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)



# WAP to check if a list contains a palindrome of elements

list = [1,2,3,2,4]
copy_list=list.copy() 
copy_list.reverse()

if(copy_list==list):
    print("Palindrome")
else:
    print("Not a palindrome")