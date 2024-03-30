
def countSubarrays(a,k,max_element):
    # [1, 3, 2, 3, 3]
    left=0
    Notreset_right=True
    subarrays=list()
    possibeSubArrays=0
    if legitArray(a, max_element, k):
        while left < len(a):
            max_count = 0
            right = left + 1
            temp_list= list()
            temp_list.append(a[left])
            if a[left] == max_element:  max_count+=1
            while right < len(a):
                temp_list.append(a[right])
                if a[right] == max_element: max_count+=1
                if max_count >= k:
                    if temp_list not in subarrays:
                        subarrays.append(temp_list)
                        possibeSubArrays+=1
                        right=left+1
                        max_count = 0
                        Notreset_right=False
                        temp_list=list()
                        temp_list.append(a[left])

                if Notreset_right:
                    right += 1
                Notreset_right=True

            left+=1
        print(subarrays)
    else:
        print(f'No subarray contains the element {max(a)} at least {k} times')
    return possibeSubArrays









def legitArray(a, max_e, k):
    countAppearance=0
    for number in a:
        if number == max_e:
            countAppearance+=1
    if countAppearance >= k:
        return True
    return False


base_array= [1,3,2,3,3]
test_case= [1,4,2,1]
test_case3=[1,2,3,4,3,4,4]


k= 2
maximum_element= max(base_array)
maximum_element2= max(test_case)
maximum_element3= max(test_case3)



subarraysNumber=countSubarrays(base_array,2,maximum_element)
print(f'Output: {subarraysNumber}')

subarraysNumber2=countSubarrays(test_case,k,maximum_element2)
print(f'Output: {subarraysNumber2}')


subarraysNumber2=countSubarrays(test_case3,k,maximum_element3)
print(f'Output: {subarraysNumber2}')

