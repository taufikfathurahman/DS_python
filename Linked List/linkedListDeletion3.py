# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, position):
        if self.head == None:
            print("Linked list is empty")
            return

        temp = self.head
        if position < 1:
            print("List position is out of range")
            return
        elif position == 1:
            self.head = temp.next
            temp = None
            return
        else:
            i = 1
            while(temp is not None and i < position):
                i += 1
                prev = temp
                temp = temp.next
            if temp is None:
                print("List position is out of range")
            elif temp.next is None:
                prev.next = None
                temp = None
            else:
                prev.next = temp.next
                temp = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    # This function counts number of nodes in linked list
    def getCount(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count

if __name__=='__main__':
    llist = LinkedList()
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Created linked list : ")
    llist.printList()
    print("Count of nodes before deletion is :")
    print(llist.getCount())
    llist.deleteNode(0)
    print("After deletion : ")
    llist.printList()
    print("Count of nodes after deletion is :")
    print(llist.getCount())

