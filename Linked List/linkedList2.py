# Node class 
class Node:
	# Function to initialise the node object
	def __init__(self, data):
		self.data = data	# Assign data
		self.next = None	# Initialize next as null

# Linked list class contains a node object
class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		# 1 & 2: Allocate the node & put in the data
		new_node = Node(new_data)
		# 3    : Make next of new Node as head
		new_node.next = self.head
		# 4    : Move the head to point to new Node
		self.head = new_node

	def insertAfter(self, prev_node, new_data):
		# 1. check if the given prev_node exists
		if prev_node is None:
			print("The given previous node must in LinkedList.")
			return
		# 2. create new node & put in the data
		new_node = Node(new_data)
		# 3. Make next of new Node as next of prev_node
		new_node.next = prev_node.next
		# 4. Make next of prev_node as new_node
		prev_node.next = new_node

	def append(self, new_data):
		'''
		1. Crate a new node
		2. Put in the data
		3. Set next as None
		'''
		new_node = Node(new_data)
		# 4. If the  linked list is empty, then make the new node as head
		if self.head is None:
			self.head = new_node
			return
		# 5. Else tranversal till the last node
		last = self.head
		while (last.next):
			last = last.next
		# 6. Change the next of last node
		last.next = new_node

	# utility function to print the linked list
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data, end = ' ')
			temp = temp.next

# code execution
if __name__=='__main__':
	# Make empty list
	llist = LinkedList()
	# insert data to list
	llist.append(6)
	llist.push(7)
	llist.push(1)
	llist.append(4)
	llist.insertAfter(llist.head.next, 8)

	print("created list is : ", end = '')
	llist.printList()