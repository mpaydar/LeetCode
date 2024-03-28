

## abcabcbb substring:
# trivial substrings: {abcabcbb,a,b,c}
# non trivial substrings:{ab,ac,aa,cc,bb,.........}

# s1= "abcabcbb"
# s2='bbbbb'
# s3='pwwkew'
input_test=["abcabcbb",'bbbbb','pwwkew']




def distinct_value_numbers(test):
    test_set=set()
    for i in test:
        test_set.add(i)
    print("test set: ",test_set)
    print(len(test_set))
    return len(test_set)





def process_all_combination(input_list):
    initial_point = 0
    start = 1
    dict_counter = 0
    hash_map = dict()

    for value in input_list:
        hash_map[dict_counter]=value
        dict_counter+=1


    for value in range(len(input_list)):
        temp_sub=input_list[initial_point]
        current_string=input_list[start:]
        for current_letter in current_string:
            temp_sub+=current_letter
            hash_map[dict_counter]=temp_sub
            dict_counter+=1
        start+=1
        initial_point+=1
    value_list=list(hash_map.values())
    print(value_list)
    return value_list




def filter_list(l,cap):
    my_set=set()
    print("This is ",l)
    for i in l:
        print("That is",i)
        if len(i) <= cap:
            my_set.add(i)
    print("my set",my_set)
    return  list(my_set)



def longestSubstring(l):
    longest=l[0]
    for index,value in enumerate(l):
        if len(longest)<len(l[index]):
            longest=l[index]
    return longest



def generate_answer(input):
    i = 1
    answers = []
    for substring in input:
        no_repeat = True
        for letter in substring:
            temp = substring[i:]
            if letter in temp:
                # print(letter)
                no_repeat = False
            i += 1
        i = 1
        if no_repeat:
            answers.append(substring)

    i = 0
    print("possible answers: ", answers)
    return answers


for i in input_test:
    value_list = process_all_combination(i)
    pigeon_hole = distinct_value_numbers(i)
    list_lenghtThree = list(filter_list(value_list, pigeon_hole))
    r=generate_answer(list_lenghtThree)
    final_result=longestSubstring(r)
    print(final_result)


# print(list_lenghtThree)






