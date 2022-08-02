




nums=[3,3]
target=6


# Time complexity=n^2
a=[]
for i in range(len(nums)):
  for j in range(i+1,len(nums)):
      if nums[i] + nums [j] == target:
        a=[i,j]
print(a)
              