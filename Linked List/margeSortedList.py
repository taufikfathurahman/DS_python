# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    '''
    Takes two lists sorted in increasing order, and splices their nodes together
    to make one big sorted list which is returned
    '''
    def margeList(self, head1, head2):

        # create a temp node null
        temp = None

        # if list1 is empty then eturn list2
        if head1 is None:
            return head2

        # if list2 is empty the return list1
        if head2 is None:
            return head1

        # if list1's data is smaller or equal to list2'2 data
        if head1.data <= head2.data:
            # assign temp to list1's data
            temp = head1
            # Again check list1's data is samller or equal list2's data and call margeList function
            temp.next = self.margeList(head1.next, head2)
        else:
            temp = head2
            temp.next = self.margeList(head1, head2.next)
        return temp

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    list1 = LinkedList()
    list1.push(10)
    list1.push(20)
    list1.push(30)
    list1.push(40)
    list1.push(50)

    list2 = LinkedList()
    list2.push(5)
    list2.push(15)
    list2.push(18)
    list2.push(35)
    list2.push(60)

    # Create linked list 3
    list3 = LinkedList()

    # Merging linked list 1 and linked list 2
    # in linked list 3
    list3.head = LinkedList().margeList(list1.head, list2.head)

    print(" Merged Linked List is : ")
    list3.printList()