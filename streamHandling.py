class Node:
    value=None
    next=None
    occurances=0
    previous= None

    def __init__(self,value):
        self.value=value


class doubleLinkedList:
        #(, addressOfNode)



    def __init__(self):
        self.hashMap = [[False, None] for _ in range(103)]
        self.head = None
        self.tail = None
        self.unique=-1

    def add(self, v):
        new_node = Node(v)
        hashValue = v % 103

        if self.hashMap[hashValue][0] and self.hashMap[hashValue][1].value == v:
            addressCheck = self.hashMap[hashValue][1]
            addressCheck.occurances += 1
            if addressCheck.next:
                self.unique = addressCheck.next
            if addressCheck == self.head:
                self.head = addressCheck.next
                if self.head:
                     self.head.previous = None
            elif addressCheck == self.tail:
                self.tail = self.tail.previous
                if self.tail:
                    self.tail.next = None
            else:
                addressCheck.previous.next = addressCheck.next
                addressCheck.next.previous = addressCheck.previous
            return

        if self.hashMap[hashValue][0] and self.hashMap[hashValue][1].value != v:
                # linear probing
            for i in range(hashValue + 1, len(self.hashMap) + hashValue % 103):
                if i == hashValue:
                    break
                elif not self.hashMap[i % 103][0]:
                    self.hashMap[i % 103][1] = new_node
                    self.hashMap[i % 103][0] = True
                    if self.head == None:
                        self.head = new_node
                        self.tail = new_node
                    else:
                        self.tail.next = new_node
                        new_node.previous = self.tail
                        self.tail = new_node
                    return

            # If the slot is empty
        self.hashMap[hashValue][0] = True
        self.hashMap[hashValue][1] = new_node
        new_node.occurances += 1
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def currentUniqueValue(self):
        current = self.head
        while current:
            if current.occurances == 1:
                print(current.value)
                return
            current = current.next
        print(-1)

    def print_stream(self):
        index=self.head
        while index.next:
            print(f'{index.value}',end=' -> ')
            index=index.next
        print(f'{index.value}')


stream=doubleLinkedList()
stream.add(3)
stream.add(2)
stream.add(1)
stream.add(4)
stream.add(2)
stream.add(1)

stream.print_stream()
stream.currentUniqueValue()

