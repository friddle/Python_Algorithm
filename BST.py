#Binary_Search_Tree
#author friddle
#just for fun 
#using python


####class####

class BSTtreeNode:
	def __init__(self,lnode=None,rnode=None,parent=None,value=None,obj=None):
		self.l=lnode
		self.r=rnode
		self.p=parent
		self.v=value
		self.obj=obj


class BSTree:
	def	__init__(self,RootNode=None):
		self.r=RootNode
	def Insert(self,value,obj):
		self.__insert__(self.r,value,obj)
	def __insert__(self,node,value,obj):
		if value<=node.v:
			if node.l==None:
				localnode=BSTtreeNode(lnode=None,rnode=None,parent=node,value=value,obj=obj)
				node.l=localnode
			elif node.l!=None:
				self.__insert__(node.l,value,obj)
		if value>node.v:
			if node.r==None:
				localnode=BSTtreeNode(lnode=None,rnode=None,parent=node,value=value,obj=obj)
				node.r=localnode
			elif node.r!=None:
				self.__insert__(node.r,value,obj)
		
	def __find__(self,node,value):
		if value<node.v:
			return self.__find__(node.l,value)
		elif value>node.v:
			return self.__find__(node.r,value)
		elif value==node.v:
			return node.obj

	def Find(self,value):
		obj=self.__find__(self.r,value)
		return obj
	def Print(self):
			self.__printTree__(self.r)	

	def __printTree__(self,node):
			if node.l==None and node.r==None:
				print node.v,node.obj
				return 
			elif node.r != None:
				self.__printTree__(node.r)
			elif node.l !=None:
				self.__printTree__(node.l)
			print node.v,node.obj
			

def main():
	mNode=BSTtreeNode(value=10,obj="first")
	bstree=BSTree(RootNode=mNode)
	bstree.Insert(value=20,obj="second")
	bstree.Insert(30,obj="second")
	bstree.Print()
	print bstree.Find(value=20)

if __name__ =="__main__":
	main()

