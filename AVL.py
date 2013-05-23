#AVL Tree:
#author Friddle
#Inportant:when insert the value equal == 0
#return nothing


###AVL tree Node#####

import random
MaxValue=100


class AVLtreeNode:
	def __init__(self,lnode=None,rnode=None,value=None,blance=0,obj=None):
		self.l=lnode
		self.r=rnode
		self.v=value
		self.obj=obj
		self.b=blance

	def __Deepth__(self,node):
		if not node:
			return 0 
		else:
			ld=self.__Deepth__(node.l)
			rd=self.__Deepth__(node.r)
			if ld>rd:
				return rd+1
			else:
				return ld+1
	def __renewInfo__(self):
		self.b=self.__Deepth__(self.l) - self.__Deepth__(self.r)
	def __printbalance__(self):
		print self.__Deepth__(self.l) - self.__Deepth__(self.r)
		print " value: "+str(self.v)+" blance "+str(self.b)
		self.__renewInfo__()
		print " value: "+str(self.v)+" blance "+str(self.b)

###AVL Tree##########
class AVLTree:
	def __init__(self,RootNode=None):
		self.r=RootNode
		self.taller=False
	def Insert(self,value,obj):
		node=self.__insert__(self.r,value,obj)
		if node:self.r=node
	def __insert__(self,node,value,obj):
		if node==None:
			 node=AVLtreeNode(blance=0,obj=obj,value=value)
			 self.taller=True
			 return node
		else:
			if node.v==value:
				self.taller=False
				return None
			if value<node.v:
				newnode=self.__insert__(node.l,value,obj)
				if not newnode:
					return None
				if newnode:
					node.l=newnode	
				if self.taller==True:
					if node.b==1:
						node=self.__LeftBalance__(node)
						self.taller=False
					elif node.b==0:
						node.b=1
						self.taller=True
					elif node.b==-1:
						node.b=0
						self.taller=False
			if value>node.v:
				newnode=self.__insert__(node.r,value,obj)
				if not newnode:
					return None
				elif newnode:
					node.r=newnode	
				if self.taller==True:
					if node.b==1:
						node.b=0;self.taller=False
					elif node.b==0:
						node.b=-1;self.taller=True
					elif node.b==-1:
						node=self.__RightBalance__(node)
						self.taller=False	
			return node

####using this function to refresh the node####
####change all the tree blance value by flag->self.taller###
####if insert left hand:node.v++ 0->1 self.taller->true -1->1 self.taller=false.v 1->2 -->change the blance tree: the same as the right tree
####

	def __LeftBalance__(self,node):
		leftnode=node.l
		if leftnode.b == 1:
			node.b=0;leftnode.b=0
			node=self.__RRotation__(node)
		elif leftnode.b == -1:
			left_right_node=leftnode.r
			if left_right_node.b==1:
				node.b=1;leftnode.b=0
			elif left_right_node.b==0:
				node.b=0;leftnode.b=0
			elif left_right_node.b==-1:
				node.b=0;leftnode.b=1
			leftnode.b=0
			node.l=self.__LRotation__(node.l)
			node=self.__RRotation__(node)
		return node


	def __RightBalance__(self,node):
		rightnode=node.r
		if rightnode.b == -1:
			node.b=0;rightnode.b=0
			node=self.__LRotation__(node)
		elif rightnode.b == 1:
			right_left_node=rightnode.l
			if right_left_node.b==-1:
				node.b=1;rightnode.b=0
			elif right_left_node.b==0:
				node.b=0;rightnode.b=0
			elif right_left_node.b==1:
				node.b=0;rightnode.b=-1
			rightnode.b=0
			node.r=self.__RRotation__(node.r)
			node=self.__LRotation__(node)
		return node

#LL Rotation
#          a            a           b
#	      b     e  --->b     e  --->c   a
#     c   d       c    d        f   d   e
#               f

	def __RRotation__(self,node):
		 leftnode=node.l
		 node.l=leftnode.r
		 leftnode.r=node
		 node=leftnode
		 return node

#RR Rotation
#   a           a              c 
#b     c  -->b     c   ---> a     e
#    d   e       d   e    b   d     f
#                      f

	def __LRotation__(self,node):
		 rightnode=node.r
		 node.r=rightnode.l
		 rightnode.l=node
		 node=rightnode
		 return node

	def Find(self,value):
		obj=self.__find__(self.r,value)
		return obj
	def __find__(self,node,value):
		if value<node.v:
			return self.__find__(node.l,value)
		elif value>node.v:
			return self.__find__(node.r,value)
		elif value==node.v:
			return node.obj

	def Print(self):
		self.__printTree__(self.r)

	def __printTree__(self,node):
		if node:node.__renewInfo__()
		print "Value :"+str(node.v)+" Balance :"+str(node.b)
		#print "before blance:"+str(node.b)
		#print "after blance:"+str(node.b)
		if node.l==None and node.r==None:
			return 
		if node.r !=None:
			print ".node-(R)->"
			self.__printTree__(node.r)
			print '----back--->'
		if node.l !=None:
			print ".node-(L)->"
			self.__printTree__(node.l)
			print '----back--->'


def main():
	mNode=AVLtreeNode(value=MaxValue/2,obj="RootNode",blance=0)
	mTree=AVLTree(mNode)
	for i in range(1,9):
		lvalue=random.randint(0,MaxValue)
		print "The Value:"+str(lvalue)
		mTree.Insert(value=lvalue,obj=str(lvalue))
	#a=[14,34,19,48,35,48,56,23]
	#for i in range(0,7):
	#	print "value"+str(a[i])
	#	mTree.Insert(a[i],str(a[i]))
	print "the print tree"
	mTree.Print()
		



if __name__ =="__main__":
	main()
