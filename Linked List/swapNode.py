# Node class
class Node:
	def __init__(self, d):
		self.data = d
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None

	# Function to swap Nodes x and y in linked list by changing links
	def swapNodes(self, x, y):

		# Nothing to do if x and y are same
		if x == y:
			return

		# Search for x (keep track of prevX and currX)
		prevX = None
		currX = self.head
		while  currX != None and currX.data != x:
			prevX = currX
			currX = currX.next

		# Search for y ( keep track of prevY and currY)
		prevY = None
		currY = self.head
		while currY != None and currY.data != y:
			prevY = currY
			currY = currY.next

		# If either x or y is not present, nothing to do
		if currX == None or currY == None:
			return

		# If x is not head of linked list
		temp = currY.next
		if prevX != None:
			prevX.next = currY
		else: # Make y the new head
			self.head = currY

		# If y is not head of linked list
		if prevY != None:
			prevY.next = currX
		else: # Make x the new head
			self.head = currX

		# Swap next pointers
		temp = currX.next
		currX.next = currY.next
		currY.next = temp
		
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

if __name__ == '__main__':
	llist = LinkedList()
	llist.push(7)
	llist.push(6)
	llist.push(5)
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(1)
	print("Linked list before calling swapNodes() :")
	llist.printList()
	llist.swapNodes(4, 3)
	print("Linked list adter calling swapNodes() :")
	llist.printList()
