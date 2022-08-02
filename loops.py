



a=[]
nums=[3,3]
target=6


# Time complexity=n^2
# for i in range(len(nums)):
#   for j in range(i+1,len(nums)):
#       if nums[i] + nums [j] == target:
#         a=[i,j]
# print(a)
#--------------------------------------------------------------------------------------------------------------------
# dictionaries keys are unique: so we will use those values as key, their index in the list as their value
# at any point we are going through the list, if we see the number we are interested is in the dictionary
#  we will use the difference , which an actual key in dictionary to get the value(index), as well as the index of the value
# we have in hand.... 
my_dictionary={}
for index,value in enumerate(nums):
    difference=target-value
    if value in my_dictionary:
        print (my_dictionary[difference],index)
    else:
        my_dictionary[value]=index




              