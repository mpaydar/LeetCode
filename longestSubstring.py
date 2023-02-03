# case1 = "abcabcbb"
# case2 = "bbbbb"
case3 = "pwwkew"
test_cases = [case3]


def substringCombination(text):
    index = 0
    substringList = []
    substring = ""
    while index < len(text):
        for i in text:
            substring += i
            substringList.append(substring)
        index += 1
    print(substring)
    return substringList


def checkDuplicate(list):
    for curr_string in list:
        duplicate_helper(curr_string)



noDuplicate = set()

def duplicate_helper(current_string):
    for i in range(len(current_string)):
        j = i + 1
        while j < len(current_string):
            if current_string[i] == current_string[j]:
                current_string = current_string.replace(current_string, "")
                # substringList.remove(current_string)
            j += 1
        if current_string != "":
            noDuplicate.add(current_string)
            print(noDuplicate)
    return noDuplicate
    # print(noDuplicate)


#
def getLongestSubset(subset):
    convertList = list(subset)
    print(subset)
    longest = ""
    for i in convertList:
        if len(longest) < len(i):
            longest = i
    print("The largest substring is:", longest)
    longest=""


for test_case in test_cases:
    print(test_case)
    combinationList = substringCombination(test_case)
    # print(combinationList)
    duplicateFree=checkDuplicate(combinationList)
    print(duplicateFree)
    # getLongestSubset(duplicateFree)


# duplicate_helper("abc")
