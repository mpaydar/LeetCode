from collections import deque

def increasing():
    A=[7,6,5,4,3,2,1]
    queue_container= deque()
    incrasing_order=list()
    for i in range(len(A) - 1, -1, -1):
        queue_container.append(A[i])
    for j in range(0,len(A)):
        e=queue_container.popleft()
        incrasing_order.append(e)
    print(incrasing_order)

increasing()



class Node:
    def __init__(self,v):
        self.next=None
        self.v=v
class SingleLinkedList:
    def __init__(self):
        self.head=None
    def insert(self,x):
        v = Node(x)
        if self.head == None:
            v.next=None
            self.head=v
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=v
            v.next=None
    def print_list(self):
        current_index= self.head
        regular_list=list()
        while current_index:
            regular_list.append(current_index.v)
            current_index=current_index.next
        return regular_list
    def getHead(self):
        return self.head


def reverseRecursively(x):
    if x.next == None:
        return
    reverseRecursively(x.next)

def reverse(myNode):
    if myNode == None or myNode.next == None:
        return myNode
    temp = myNode.next
    reverse_head= reverse(temp)
    temp.next=myNode
    # print(temp.v)
    myNode.next= None
    return reverse_head







list_structure= SingleLinkedList()
list_structure.insert(1)
list_structure.insert(2)
list_structure.insert(3)
list_structure.insert(4)
v_list=list_structure.print_list()
print(v_list)
head_node= list_structure.getHead()
# reverseRecursively(head_node)
r=reverse(head_node)
while r:
    print(r.v)
    r=r.next



