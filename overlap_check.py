
import numbers
from xmlrpc.client import Boolean

from numpy import integer
from pandas import array


def evaluation(x,y):
    return x<y


def over_lap_check(numbers:list):
    list_check1 : list=[]
    list_check2 : list=[]
    flag : Boolean=False
    max_value : integer=0
    min_value : integer=0
    overlap_counter : integer=0
    overlap_dictionary : dict={}
    x : list=[]
    for n in range(len(numbers)):
        number_of_evaluated=len(list_check1)+len(list_check2) 
        x=numbers[n] #[1,2]
        
        if number_of_evaluated==4:
        
            max_value=max(list_check1)
            min_value=min(list_check2)
                 
            if n!=len(numbers):
                list_check1=list_check2
                list_check2=[]

            if  (evaluation(min_value,max_value)==True):
                overlap_counter+=1
                overlap_dictionary[n]=(list_check1,list_check2)


        if len(list_check1)==2 and flag==False:
            flag=True

        if len(list_check2)==2 and flag==True:
            flag=False
            
        if flag==False:
            for i in range(2):
                list_check1.append(x[i])
            
       
        if flag==True:
            for i in range(2):
                list_check2.append(x[i])
            


    number_of_evaluated=len(list_check1)+len(list_check2)
    if number_of_evaluated==4:
        max_value=max(list_check1)
        min_value=min(list_check2)  
        if  (evaluation(min_value,max_value)==True):
                overlap_counter+=1
                overlap_dictionary[n]=(list_check1,list_check2)
    
    print("Total overlaps:",overlap_counter)
    print("The following intervals are overlap intervals:\n",overlap_dictionary)
    
    

over_lap_check([[1,4],[3,8],[7,10],[9,11]])