# nested loops in python

# for i in range(4):
#     print("outer",i)

#     for j in range(4):
#         print("inner",j)


# * * * * 
# * * * * 
# * * * * 
# * * * * 


# for i in range(4):
#     for j in range(4):
#         print("*", end = " ")
#     print()


# Print this pattern
# *
# *
# *
# *

# for i in range(4):
#     print("*")


# print this pattern
# 1111
# 2222
# 3333
# 4444


# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end = "")
#     print()    


# Print this pattern
# 1234
# 1234
# 1234
# 1234

# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end = " ")
#     print()    



# Print this pattern (level 2)
# *
# **
# ***
# ****    

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end = "")
#     print()    



# Print this pattern
# 1
# 12
# 123
# 1234


# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end = "")
#     print()    


# 1
# 22
# 333
# 4444

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end = "")
#     print()



# Print this pattern
# A
# AB
# ABC
# ABCD

# for i in range(0,6):
#     for j in range(1,i+1):
#         print(chr(64+j),end = " ")
#     print()    


# Reverse triangle
# ****
# ***
# **
# *    

for i in range(0,4,):
    for j in range(4,i,-1):
        print("*", end = "")
    print()    