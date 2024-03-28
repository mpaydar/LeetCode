
unsorted_array =[32 ,17 ,12 ,19 ,45 ,16]




def selectionSort(array):
    minimum_value =1000000
    minimum_index =-1
    sorted_index =-1
    for i in range(sorted_index+1 ,len(array)):
        for k in range( sorted_index+1 ,len(array)):
            if array[k] < minimum_value:
                minimum_value =array[k]
                minimum_index =k
        for j in range(minimum_index ,-1 ,-1):
            if minimum_value<array[j]  :
                array[j+1] = array[j]
        array[sorted_index +1 ] =minimum_value
        sorted_index+=1
        minimum_value = 1000000
    print(array)


selectionSort(unsorted_array)




