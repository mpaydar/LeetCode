def over_lap_check(numbers):
    list_check1=[]
    list_check2=[]
    flag=False
    index_check=0
    max_value=0
    min_value=0
    for n in range(len(numbers)):

        number_of_evaluated=len(list_check1)+len(list_check2)
       
        if number_of_evaluated==4:        
            max_value=max(list_check1)
            print("max_value:",max_value)

            min_value=min(list_check2)
            print("min_value:",min_value)
            if  min_value<max_value :
                print("There is an overlap")

            if n!=len(numbers)-1:
                list_check1=list_check2
                list_check2=[]

        if len(list_check1)==2 and flag==False:
            flag=True

        if len(list_check2)==2 and flag==True:
            flag=False
        
        
        elif flag==False:
            list_check1.append(numbers[n])
       
        elif flag==True:
            list_check2.append(numbers[n])

      

        index_check+=1
    number_of_evaluated=len(list_check1)+len(list_check2)
    if number_of_evaluated==4:
        max_value=max(list_check1)
        min_value=min(list_check2)

        print("list_check1:",list_check1,"\n")
        print("list_check2:",list_check2,"\n")
        if  min_value<max_value :
                print("There is an overlap")

