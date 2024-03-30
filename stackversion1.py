

a= [1,2,3,4,5]

def generateStack(test_case):
    top=-1
    stack = [0] * len(test_case)
    for i in range(len(test_case)):
        top+=1
        stack[top] = test_case[i]
    return stack


def descendArrayOrdering(stack):
    stackSize=len(stack)
    descending_array= [0] * stackSize
    descend_index=0
    top=stackSize-1
    while top > -1:
        top_element=stack[top]
        descending_array[descend_index] = top_element
        descend_index+=1
        top-=1
    print(descending_array)

stack = generateStack(a)
descendArrayOrdering(stack)