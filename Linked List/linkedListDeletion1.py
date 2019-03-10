# Node class
class Node:

	# Consructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the begining
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	'''
	Given a reference to the head of the list and a key
	delete the first occure of the key in the list
	'''
	def deleteNode(self, key):

		# Store head node
		temp = self.head

		# If head node itself holds the key to be deleted
		if (temp is not None):
			if (temp.data) == key:
				self.head = temp.next
				temp = None
				return

		'''
		Search for the key to be deleted, keep track of the
		previous node as node as we need to change 'prev.next'
		'''
		while (temp is not None):
			if (temp.data == key):
				break
			prev = temp
			temp = temp.next

		# If the key was not present in linked list
		if(temp == None):
			return

		# Unlink teh node from linked list
		prev.next = temp.next
		temp = None

	# Utility funtion to print th linked list
	def printList(self):
		temp =  self.head
		while(temp):
			print(temp.data)
			temp = temp.next

if __name__ == '__main__':
	llist = LinkedList()
	llist.push(7)
	llist.push(1)
	llist.push(3)
	llist.push(2)

	print("Created linked list: ")
	llist.printList()
	llist.deleteNode(3)
	print("Lined list after deletion: ")
	llist.printList()