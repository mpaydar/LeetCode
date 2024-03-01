# Reverse Linked List( singular linked list) using recursion
# Example: input: LinkedList: 1-> 2 -> 3 -> 4      output: 4 -> 3 -> 2 -> 1

class Node:
    value=None
    next=None


    def __init__(self,value):
        self.value=value

class singleLinkedList:

   def __init__(self):
       self.head=None
       self.tail=None
       self.length=0

   def add(self,value):
       new_node = Node(value)

       # The list is empty
       if self.head is None:
           self.head=new_node
           self.tail=new_node
           self.length+=1
        # The list is not empty
       else:
           self.tail.next=new_node
           self.tail=new_node
           self.length+=1

   def print(self):
       temp=self.head
       while temp.next:
           print(temp.value,end=" -> ")
           temp=temp.next
       print(temp.value)

   def print_reverse(self,linkList):
       temp=linkList.head
       while temp.next:
           print(temp.value,end=" -> ")
           temp=temp.next
       print(temp.value)





       conainter=list()
       index=self.head
       while index:
           conainter.append(index.value)
           index=index.next
       backward_linkedList= singleLinkedList()
       for i in range(len(conainter)-1,-1, -1):
           backward_linkedList.add(conainter[i])
       return backward_linkedList
   def getHead(self):
       return self.head

   def getTail(self):
       return self.tail

   def getLength(self):
       return self.length



def reverse_list(index,originalList,output):
    '''This function will reverse the linkedList using recursion:
     Time complexity : O(n)'''

    # Base Case:
    if index is None:
        return

    current_node_value=index.value
    reverse_list(index.next,originalList,output) # recursion calls
    output.add(current_node_value)
    current_length=output.getLength()
    target_length=originalList.getLength()
    if current_length == target_length:
        return output






incoming_list= singleLinkedList()
incoming_list.add(1)
incoming_list.add(2)
incoming_list.add(3)
incoming_list.add(4)

print("Input: ",end=" ")
incoming_list.print()
_outputList= singleLinkedList()
starting_index=incoming_list.getHead()
reverse_output= reverse_list(index=starting_index,originalList=incoming_list,output=_outputList)
r_index=reverse_output.getHead()


reverse_output.print()

















# def reverse(incoming_linked_list):







