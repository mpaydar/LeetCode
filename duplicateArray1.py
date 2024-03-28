test_case = [1,1,1,2,2,2,3]


def removeDuplicate(a,k):
    previous_duplicate=0
    for i in range(len(a)):
        current_number= a[i]
        numberOfOccurances = 1
        arbitary_start=i+1
        for j in range(arbitary_start,len(a)):

            if a[j] == current_number:
                numberOfOccurances +=1
                if numberOfOccurances > 2:
                    temp=a[j]
                    a=shiftLeft(a,j,temp)

            previous_duplicate = getPreviousDuplicate(a)
            if a[j] == previous_duplicate :
                print(str (previous_duplicate) + " and the a[j] " + str(a[j]) +" index: " +str(j))
                temp=a[j]
                a=shiftLeft(a,j,temp)
    print(a)







def shiftLeft(a,j,currentDuplicate):
    while j < len(a) - 1 and a[j + 1] >= currentDuplicate:
        a[j] = a[j + 1]
        j += 1
    a[j] = currentDuplicate
    return a

def getPreviousDuplicate(a):
    return a[len(a)-1]






removeDuplicate(test_case,5)