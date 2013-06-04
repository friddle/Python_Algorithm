#author friddle
#just for fun
#if get the error


import sys,os
import random

MaxValue=20

class RBTNode:
  def __init__(self,key=None,obj=None,P=None,R=None,L=None,color=None,size=None):
   self.key=key
   self.obj=obj
   self.P=P
   self.R=R
   self.L=L
   self.color=color
   self.size=size

  def __getuncle__(self):
   """
   return the uncle node
   """
   if self.P==self.P.P.L:
    return self.P.P.R
   elif self.P==self.P.P.R:
    return self.P.P.L
   else:
	 print "get uncle error"
	 print "node "+str(self.key)
	 return None

  def __getsibling__(self):
	 """
	 return the sibling
	 """
	 if self==self.P.L:
		 return self.P.R
	 elif self==self.P.R:
		 return self.P.L
	 else:
		 print "get the sbling error"
		 return None


#####the RBTree #############################
class RBTree:
  def __init__(self):
   self.Root=None

  def Insert(self,obj=None,key=None):
	  if self.Root==None:
		  self.Root=RBTNode(obj=obj,key=key,color="black")
		  self.__InsertNodeCase1__(self.Root)
	  else:
		  self.InsertNode(node=self.Root,obj=obj,key=key)
  def InsertNode(self,node,obj,key):
   """
   insert the node
   """
   if node.key<key:
    if node.R!=None:
      self.InsertNode(node.R,obj,key)
    else:
      node.R=RBTNode(obj=obj,key=key,P=node,color="red")
      self.__InsertNodeCase1__(node.R)
   elif node.key>key:
    if node.L!=None:
     self.InsertNode(node.L,obj,key)
    else:
     node.L=RBTNode(obj=obj,key=key,P=node,color="red")
     self.__InsertNodeCase1__(node.L)
   else:
    return  
  

  def __InsertNodeCase1__(self,node):
   """
   when no parent.the insert must be rootnode
   """
   if node.P==None:
    node.color="black"
   else:
    self.__InsertNodeCase2__(node)

  def __InsertNodeCase2__(self,node):
   """
   when parent are Black.so nothing happened
   """
   if node.P.color=="black":
	 return
   else:
    self.__InsertNodeCase3__(node)
  def __InsertNodeCase3__(self,node):
    """
    when the uncle and father are red.Just change the father and uncle the color.
	 but we will face the situtation that:the grandparent->parent could be red
    """
    if node.__getuncle__()!=None:
     if node.__getuncle__().color=="red": 
      node.P.color="black"
      node.__getuncle__().color="black"
      node.P.P.color="red"
	   #the grandparent color be red will broken the rule 4:
	   #every red node has two black child node
	   #so test the GrandParent
      self.__InsertNodeCase1__(node.P.P)
     else:
      self.__InsertNodeCase4__(node)
    else:
     self.__InsertNodeCase4__(node)
  def __InsertNodeCase4__(self,node):
	  """
	  when parent is red and uncle is black or null
	  it means a broken line:
	  if node is parent rightchild and parent is the grandpa leftchild
	  LeftRotate
	  if node is paretn leftchild and parent is the grandpa rightchild
	  RightRotate
	  """
	  if node==node.P.R and node.P==node.P.P.L:
		  self.__LRotate__(node)
		  node=node.L
	  elif node==node.P.L and node.P==node.P.P.R:
		  self.__RRotate__(node)
		  node=node.R
	  self.__InsertNodeCase5__(node)
  def __InsertNodeCase5__(self,node):
   """
	it means a line
	when parent is red and unclue is black or null.
	if node is parent leftchild and parent is the grandpa leftchild
	Grandparent LeftRotate
	another situtation
	Grandparent RightRotate
   """
   node.P.color="black"
   node.P.P.color="red"
   if node==node.P.L and node.P==node.P.P.L:
		self.__RRotate__(node.P)
   elif node==node.P.R and node.P==node.P.P.R:
		self.__LRotate__(node.P)
   else:
		print "the case 4 or 5 error,please check in"

  def __RRotate__(self,node):
	  parent=node.P
	  root=parent.P
	  parent.L=node.R
	  if node.R!=None:
		  node.R.P=parent
	  if root==None:
		  self.Root=node
		  node.P=None
	  elif parent==root.L:
		  root.L=node
		  node.P=root
	  elif parent==root.R:
		  root.R=node
		  node.P=root
	  else:
		  print "error when RightRotate"
	  node.R=parent
	  parent.P=node

 
  def __LRotate__(self,node):
	  parent=node.P
	  root=parent.P
	  parent.R=node.L
	  if node.L!=None:
		  node.L.P=parent
	  if root==None:
		  self.Root=node
		  node.P=None
	  elif parent==root.L:
		  root.L=node
		  node.P=root
	  elif parent==root.R:
		  root.R=node
		  node.P=root
	  else:
		print "error when LeftRoatate"
	  node.L=parent
	  parent.P=node
  def Print(self):
	self.__printTree__(self.Root)
	

  def FindNode(self,key=key):
		pass
  def __findNode__():
	  pass

	

  def __printTree__(self,node):
	print "Value :"+str(node.key)+" color "+node.color
	if node.L==None and node.R==None:
		return 
	if node.R !=None:
		print ".node-(R)->"
		self.__printTree__(node.R)
		print '----back--->'
	if node.L !=None:
		print ".node-(L)->"
		self.__printTree__(node.L)
		print '----back--->'

def main():
   tree=RBTree()
   #for i in range(0,8):
    #value=random.randint(0,MaxValue)
    #tree.Insert(obj="none",key=i)
   #tree.Print()
   num=[12,1,9,2,0,11,7,19,4,15,18,5,14,13,10,16,6,3,8,17]
   for i in num:
    print "insert value " +str(i)
    tree.Insert(obj="none",key=i)
    if i==16 or i==10:
		 pass
     #tree.Print()
   tree.Print()

if __name__=="__main__":
	main()
