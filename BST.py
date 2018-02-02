class node:
	def __init__(self,value=None):
		self.value=value
		self.left_child=None
		self.right_child=None
		self.parent=None

class binary_search_tree:
	def __init__(self):
		self.root=None

	def insert(self,value):
		if self.root==None:
			# if no root set new value as root
			self.root=node(value)
		else:
			# if root already exists insert new value with the existing root
			self._insert(value,self.root)

	def _insert(self,value,cur_node):

		# This will recursivly call until a free left or right space will be avaliable to insert the node into.

		if value<cur_node.value:
			if cur_node.left_child==None:
				# If left child does not have a value insert it there and update new node parent value with current node
				cur_node.left_child=node(value)
				cur_node.left_child.parent=cur_node
			else:
				# Recurissvly go again but with the left child
				self._insert(value,cur_node.left_child)
		# If value is greater than current note
		elif value>cur_node.value:
			# If right child does not have a value insert it there and update new node parent value with current node
			if cur_node.right_child==None:
				cur_node.right_child=node(value)
				cur_node.right_child.parent=cur_node
			else:
				# Recurissvly go again but with the right child
				self._insert(value,cur_node.right_child)
		else:
			print "Value already in tree!"

	def print_tree(self):
		if self.root!=None:
			self._print_tree(self.root)

	# InOrder traversal
	def _print_tree(self,cur_node):
		# If current node exists
		if cur_node!=None:
			# If left child exists
			self._print_tree(cur_node.left_child)
			# Print current node value
			print str(cur_node.value)
			# CIf right child exists
			self._print_tree(cur_node.right_child)

	def height(self):
		if self.root!=None:
			return self._height(self.root,0)
		else:
			return 0

	def _height(self,cur_node,cur_height):
		# Keep going as far left or as far right until a node cannot be found. Return height.
		if cur_node==None: return cur_height
		left_height=self._height(cur_node.left_child,cur_height+1)
		right_height=self._height(cur_node.right_child,cur_height+1)
		return max(left_height,right_height)

	def find(self,value):
		if self.root!=None:
			return self._find(value,self.root)
		else:
			return None

	def _find(self,value,cur_node):
		# If value matches current node return value
		if value==cur_node.value:
			return cur_node
		# If value is less than current node value and has a left child, then recursivly search the current nodes left child
		elif value<cur_node.value and cur_node.left_child!=None:
			return self._find(value,cur_node.left_child)
		# Vice-versa for right child
		elif value>cur_node.value and cur_node.right_child!=None:
			return self._find(value,cur_node.right_child)

	def delete_value(self,value):
		return self.delete_node(self.find(value))

	def delete_node(self,node):

		# If node cannot be found
		if node==None or self.find(node.value)==None:
			print "Node to be deleted not found in the tree!"
			return None 

		# if node parent dosent exist return none
		if node.parent==None:
			self.root=None 
			return None 

		# Recursivly call all left children until you find the last one (lowest value)
		def min_value_node(n):
			current=n
			while current.left_child!=None:
				current=current.left_child
			return current

		# return number of children for each node
		def num_children(n):
			num_children=0
			if n.left_child!=None: num_children+=1
			if n.right_child!=None: num_children+=1
			return num_children


		node_parent=node.parent

		node_children=num_children(node)

		# CASE 1 (node has no children)
		# This is a straight removale as there are no children to be effected
		if node_children==0:
				# If node is the left child of its parent set it to none/empty
			if node_parent.left_child==node:
				node_parent.left_child=None
			else:
				# Vice-versa for right
				node_parent.right_child=None

		# CASE 2 (node has a single child)
		# Find which child exists then replace node with its child
		if node_children==1:

			# if left child exists set child as the left child
			if node.left_child!=None:
				child=node.left_child
			else:
				# Vice-versa for right
				child=node.right_child

			# If node is on the left child then replace parents right child thats vacated by the removed node with the removed node child.
			# If a dad dies, grandad will elect his grandson to take his place.
			if node_parent.left_child==node:
				node_parent.left_child=child
			else:
			# If the node is a right sided child do the same.
				node_parent.right_child=child

			# Update newly promted child to have the new parent of the grandad node.
			child.parent=node_parent

		# CASE 3 (node has two children)
		if node_children==2:

			# Find the minimum value in the rightmost child to be the sucessor to keep the tree structure.
			successor=min_value_node(node.right_child)

			# replace node value with the successors value, essntially removing it
			node.value=successor.value

			# Delete the successor as it has already been pushed up in the position of the deleted node.
			self.delete_node(successor)

	def search(self,value):
		# If root exists search for value
		if self.root!=None:
			return self._search(value,self.root)
		else:
			return False

	def _search(self,value,cur_node):
		# If value has been found return true
		if value==cur_node.value:
			return True
		# If value is less than current node valye and current node has a left child, recursivly call on that child to see if it holds the searched value
		elif value<cur_node.value and cur_node.left_child!=None:
			return self._search(value,cur_node.left_child)
		# Vice-versa but for the right node
		elif value>cur_node.value and cur_node.right_child!=None:
			return self._search(value,cur_node.right_child)
		# If not found return false
		return False 