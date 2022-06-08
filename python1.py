

def Longest_Collatz():
    temp=1
    i=13
    number=0
    max=0
    for i in range(1,1000000):
        current=i
        while i!=1:
            temp+=1
            if(i % 2 ==0):
                i=i/2
            elif(i % 2 !=0):
                i=(3*i)+1
        if max<temp:
            max=temp
            number=current
        temp=0   
    return [number,max]






def Factorial(n):
    r=1
    for i in range (n,0,-1):
        r*=i
    return r

def sum_digit(d):
    sum=0
    digit=Factorial(d)
    digit_string=str(digit)
    for i in digit_string:
        sum+=int(i)
    return sum









def maxArea(list):
    maxarea=0
    for i in range(len(list)):
        currentEndpoint=list[i]
        for j in range(len(list)):
            temp=list[j]
            if currentEndpoint<=list[j]:
                distance=abs(list.index(temp)-list.index(currentEndpoint))
                tempArea=currentEndpoint * distance
                if maxarea<tempArea:
                    maxarea=tempArea
    if maxarea==0:
        maxarea=list[0]*1
    
    return maxarea





dictionary={}
def dictionary_preparation(str):
    for i in range(len(str)):
        dictionary[str[i]]=[]

def dictionary_mapping(str):
    dictionary_preparation(str)
    for key in dictionary:
        if key=="2":
            value=dictionary[key]
            value.append("a")
            value.append("b")
            value.append("c")
        elif key=="3":
            value=dictionary[key]
            value.append("d")
            value.append("e")
            value.append("f")
        elif key=="4":
            value=dictionary[key]
            value.append("g")
            value.append("h")
            value.append("i")
        elif key=="5":
            value=dictionary[key]
            value.append("j")
            value.append("k")
            value.append("l")
        elif key=="6":
            value=dictionary[key]
            value.append("m")
            value.append("n")
            value.append("o")
        elif key=="7":
            value=dictionary[key]
            value.append("p")
            value.append("q")
            value.append("r")
        elif key=="8":
            value=dictionary[key]
            value.append("s")
            value.append("t")
            value.append("u")
        elif key=="9":
            value=dictionary[key]
            value.append("v")
            value.append("x")
            value.append("y")
            value.append("z")

        



def letterCombinations(str):
    result={} 
    temp=""
    list=[]
    j=1
    dictionary_mapping(str)
    for i in dictionary:
        item=(i,dictionary[i])
        list.append(item)
    string_length=len(str)
    if (string_length!=1 or string_length!=0):
        for i in range(len(list)-1):
            for k1 in range(0,3):
                for k2 in range(0,3):
                    temp+=list[i][1][k1]
                    temp+=list[j][1][k2]
                    result[temp]=True
                    temp=""
            j+=1
    if(string_length==1):
        for i in range(len(list)):
            for j in range(0,3):
                temp+=list[i][1][j]
                result[temp]=True
                temp=""
    return result
      

            
   


            




# Function Calls/invocation
print("Please wait....prcessing")
display_result=sum_digit(10)
l1=letterCombinations("2")
l2=letterCombinations("23")
height1=[1,8,6,2,5,4,8,3,7]
height3=[3,9,3,4,7,2,12,6]
height2=[1,2]                    
area1=maxArea(height1)
area2=maxArea(height2)
area3=maxArea(height3)
a=Longest_Collatz()



#Ouput:
print("Output for sum of the factorial digits:")
print("\t The sum of the digits of the factorial is:",display_result)
print("\n")

print("Ouput for letter combination problem")
print("\t",l1)
print("\t",l2)

print("\n")


print("Output for max area problem: ")
print("\t The max area is:",area1)
print("\t The max area is:",area2)
print("\t The max area is:",area3)


print("\n")



print("Output for Longest_Collatz function: ")
print("\t The number with longest chain is",a[0])
print("\t Length of the chain is",a[1])



        