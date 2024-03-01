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

   def add(self,value):
       new_node = Node(value)

       # The list is empty
       if self.head is None:
           self.head=new_node
           self.tail=new_node
        # The list is not empty
       else:
           self.tail.next=new_node
           self.tail=new_node

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

   def reverse_list(self):
       '''This function will reverse the linkedList in naitve way:
        Time complexity : O(n)'''
       conainter=list()
       index=self.head
       while index:
           conainter.append(index.value)
           index=index.next
       backward_linkedList= singleLinkedList()
       for i in range(len(conainter)-1,-1, -1):
           backward_linkedList.add(conainter[i])
       return backward_linkedList




incoming_list= singleLinkedList()
incoming_list.add(1)
incoming_list.add(2)
incoming_list.add(3)
incoming_list.add(4)

print("Input: ",end=" ")
incoming_list.print()
theReverseLinkedList=incoming_list.reverse_list()
print("Output: ", end=" ")
incoming_list.print_reverse(theReverseLinkedList)


















# def reverse(incoming_linked_list):







