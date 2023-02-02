list1=[9,9,9,9,9,9,9] # 0 1 2 3 4 5 6
list2=[9,9,9,9]   # 0 1 2 3
i=list1.index(list1[-1])
dynamic_answer=0
stack=[]
quotient=0
index=0
carry_list=[]





def convertListToInteger(l1,l2):
    combined_list=[]
    convert_list=[]
    # combine 2 list in one list:
    combined_list.append(l1)
    combined_list.append(l2)
    for current_list in combined_list:
        l=0
        the_number=""
        while l< len(current_list):
            the_number+=str(current_list[l])
            l+=1
        convert_list.append(the_number)
    return  convert_list

def sumTheList(intList):
    sum=0
    for i in intList:
        sum+=int(i)
    return str(sum)

def reverseString(n):
    index=len(n)-1
    reverseList=[]
    while 0<=index:
        reverseList.append(n[index])
        index-=1
    return reverseList



integerList=convertListToInteger(list1,list2)
sumString=sumTheList(integerList)
rList=reverseString(sumString)
print(rList)














