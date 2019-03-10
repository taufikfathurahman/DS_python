# Node Class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Funtion to initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to reverse linked list
    def ReverseLinkedList(self):
        prev = None
        curr = self.head
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def reverseRecursive(self, curr, prev):
        # If last node mark it head
        if curr.next is None:
            self.head = curr

            # Update next to prev node
            curr.next = prev
            return

        # Save curr.next node for recursive call
        next = curr.next

        # And update next
        curr.next = prev

        self.reverseRecursive(next, curr)

    def reverse(self):
        if self.head is None:
            return

        self.reverseRecursive(self.head, None)

    def PrintLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("Given Linked List :")
    llist.PrintLinkedList()

    llist.ReverseLinkedList()

    print("Reversed Linked List :")
    llist.PrintLinkedList()

    print("Reverse riversed linked list using recursion :")
    llist.reverse()
    llist.PrintLinkedList()
