list1=[9,9,9,9,9,9,9]
list2=[9,9,9,9]
i=list1.index(list1[-1])
dynamic_answer=0
stack=[]
quotient=0
index=0
carry_list=[]
def calculate_carryOver(dynamic_answer,carry):
    # addition begins
        if len(carry_list) == 0:
            stack.append(dynamic_answer%10)
            carry_list.append(carry)
        else:
            current_carry=carry_list[-1]
            if current_carry != 0:
                remainder = dynamic_answer % 10
                new_value=remainder+current_carry
                stack.append(new_value)
            else:
                remainder = dynamic_answer % 10
                carry_list.append(carry)
                stack.append(remainder)




    # if remainder == 0 and 1<quotient:
    #     stack.append(remainder)
    #     print(stack)
    #
    # if carry == 0:
    #     stack.append(dynamic_answer)
    # if carry != 0:
    #     stack.append(dynamic_answer+carry)








while 0 <= i:
    dynamic_answer=list2[i] + list1[i]
    if 1<len(str(dynamic_answer)):
        carry_over=quotient = dynamic_answer // 10
        calculate_carryOver(dynamic_answer,carry_over)
    else:
        carry_over=quotient = dynamic_answer // 10
        calculate_carryOver(dynamic_answer,carry_over)
    i-=1
print(stack)

