def isPalindrome(x):
    original_number = str(x)
    tempOne = ""
    tempTwo = ""
    i_backward = len(original_number) - 1
    i = 0
    while i < len(original_number):
        tempOne += original_number[i] + tempOne
        tempTwo += original_number[i_backward] + tempTwo
        i += i + 1
        i_backward -= i_backward - 1
    if (tempOne == tempTwo):
        return True
    else:
        return False


case1=121
case2=-121
case3=10
listOfCases=[case1,case2,case3]
for integer in listOfCases:
    result=isPalindrome(integer)
    print(result)