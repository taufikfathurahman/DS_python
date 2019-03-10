# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data	# Assign data
		self.next = None	# Initialize next as null

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function prints content of linked list
	# starting from head
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next

# Code execution starts here
if __name__=='__main__':
	# Start with the empty list
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	'''
    Three nodes have been created.
    We have references to these three blocks as first,
    second and third
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''

	llist.head.next = second	# Link first node with second
	second.next = third			# Link second node with third

	'''
    Now next of second Node refers to third.  So all three
    nodes are linked.
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''

	llist.printList()