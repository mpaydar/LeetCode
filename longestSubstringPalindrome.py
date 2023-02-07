def longestPalindrome(s) :
    anchor=s[-1]

    if len(s) == 1 or len(s) == 0:
        return

    palindrome_collection=dict()
    for start in range(len(s)):
        current_subset=s[start:]
        in_result = helper_function(current_subset)
        if in_result and current_subset != "":
            palindrome_collection[len(current_subset)]=current_subset
        elif current_subset != "" and len(current_subset) != 1:
            s=s.replace(anchor,"")
            anchor =s [-1]

    return palindrome_collection



def helper_function(subset):
    tempOne = ""
    tempTwo = ""
    i_backward = len(subset) - 1
    i = 0
    while i < len(subset):
        tempOne += subset[i] + tempOne
        tempTwo += subset[i_backward] + tempTwo
        i += i + 1
        i_backward -= i_backward - 1
    if (tempOne == tempTwo):
        return True
    else:
        return False


cases=["cbbd","babad","a"]
for case in cases:
    a=longestPalindrome(case)
    if len(case) == 0 or len(case) == 1:
        print("No Palindrome exist in the following string", case)
    else:
        print("The longest palindrome in ",case, "is", list(a.values())[0])












# Anchor the last letter

# If i= last_letter_position -1 & we did not find a palindrome:
    # We will drop that last letter and reset the starting position to 0 and anchore the new ending letter

    # Then repeat the check again

# check from position 0:
# if it is a same:
    # add that subset to a string name "possible_palindrome"
    # Check the possible_palindrome for palindrome test
    # if it is a yes:
        # save it to confirmed palindroms
        # add it to a dictionary:
            # key: length
            # value: the formed palindrom
    # if not:
        # possible_palindrome=""
# else if :
    # increment starting position 1

# if the string length is 1 and dictionary length is 0:
    # No Palindrome Exist




