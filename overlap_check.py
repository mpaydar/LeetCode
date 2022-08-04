
import numbers


def evaluation(x,y):
    return x<y





def over_lap_check(numbers):
    list_check1=[]
    list_check2=[]
    flag=False
    max_value=0
    min_value=0
    overlap_counter=0
    for n in range(len(numbers)):

        number_of_evaluated=len(list_check1)+len(list_check2)
       
        if number_of_evaluated==4:        
            max_value=max(list_check1)
            print("max_value:",max_value)

            min_value=min(list_check2)
            print("min_value:",min_value)
            
            
            if  (evaluation(min_value,max_value)==True):
                overlap_counter+=1
                print("Overlap#",overlap_counter)

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


      

    number_of_evaluated=len(list_check1)+len(list_check2)
    if number_of_evaluated==4:
        max_value=max(list_check1)
        min_value=min(list_check2)  
        if  (evaluation(min_value,max_value)==True):
                overlap_counter+=1
                print("Overlap",overlap_counter)
    

over_lap_check([1,4,3,8,9,10])