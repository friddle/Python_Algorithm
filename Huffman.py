#the Huffman Code
#first make the Huffman table


HuffmanString=[]
table={}
HuffmanCode={}

###tree class########

def SortNodes(Nodes):
	Nodes=sorted(Nodes,key=lambda x:x.v)
	return Nodes


class HuffmanNode:
	Recurit=False
	def	__init__(self,value=None,letter=None,
			lnode=None,rnode=None,parent=None):
		self.L=lnode
		self.R=rnode
		self.p=parent
		self.lt=letter
		self.v=value
	
class HuffmanTree:
	def	__init__(self,table=None):
		self.table=table
		self.nodes=[]
		self._MakeHuffmanNodeTable()
	
	def _MakeHuffmanNodeTable(self):
		for letters in self.table:
			node=HuffmanNode(value=self.table[letters],letter=letters)
			self.nodes.append(node)
		self.nodes=SortNodes(self.nodes)
	def _MakeHuffmanTree(self):
		self._pop_first_two_nodes()
		i=0
		while i<self.nodes.__len__()-1:			
				if self.nodes.__getitem__(i).p ==None:
					node1=self.nodes.__getitem__(i)
					node2=self.nodes.__getitem__(i+1)
					node3=HuffmanNode(value=node1.v+node2.v,letter=[],lnode=node1,rnode=node2,parent=None)
					node1.p=node3;
					node2.p=node3;
					self.nodes.append(node3)
					self.nodes=SortNodes(self.nodes)
					i=0 #this line can be delete ,but make to work safe.Add this
				i=i+1
	def _pop_first_two_nodes(self):
		Node1=self.nodes.__getitem__(0)
		Node2=self.nodes.__getitem__(1)
		Node3=HuffmanNode(value=Node1.v+Node2.v,letter=[],lnode=Node1,rnode=Node2,parent=None)
		Node1.p=Node3;
		Node2.p=Node3;
		self.nodes.append(Node3)
		self.nodes=SortNodes(self.nodes)

	def _MakeHuffmanCode(self):
		HuffmanCode={}
		for item in self.nodes:
			if item.lt!=	[]:
				HuffmanCode.update({item.lt:self._MakeCode(item)})
		return HuffmanCode

	def _MakeCode(self,item):
		code=0.0
		while item.p != None:
			if item.p.L==item:
				code=1+code*0.1
			elif item.p.R==item:
				code=0+code*0.1
			else:
				print "error"
			item=item.p
		code=code*0.1
		return "%0.6f" % code

	def print_test(self):
		for item in self.nodes:
			print item.v,item.lt

#####this is basic function######
def _SaveString():
	File=open('HuffmanString','w+')
	s=str(HuffmanString)
	File.write(s)

def _ReadString():
	global HuffmanString
	File=open('HuffmanString','r+')
	str=File.read()
	HuffmanString=str
	print 'HuffmanString:'+HuffmanString
	
def _SaveTable():
	File=open('HuffmanTable','w+')
	print table	
	s=str(table)
	File.write(s)

def _ReadTable():
	global table
	File=open('HuffmanTable','r+')
	table=eval(File.read())
	sorted(table.items(),key=lambda x:x[1])
	print table	


#####this is the main Function#########

def _PutString():
	global HuffmanString
	HuffmanString=raw_input("Huffmancode Input :")
	_SaveString()

def _MakeStringTable():
	global table
	global HuffmanString
	table={}
	for letter in HuffmanString:
		if letter not in table:
			newletter={letter:1}
			table.update(newletter)
		else:
			i=table[letter]
			i=i+1
			table[letter]=i
	_SaveTable()

def _SaveHuffmanCode(code):
	File=open('HuffmanCode','w+')
	s=str(code)
	File.write(s)
	print "Save Huffman Code"

def _ReadHuffmanCode(code):
	global HuffmanCode
	File=open('HuffmanCode','r+')
	HuffmanCode=eval(File.read())
	print "Reading Huffman Code"
	print HuffmanCode	
	return HuffmanCode

	

			

def Main():
	global HuffmanString,table,HuffmanCode
	while True:
		num=input("""
	please input the num:
	0	:	put	the	String
	1	:	read	the	String
	2	:	make	Huffman	code
	3	:	save	Huffman	code
	4	:	read	Huffman	code
	0	:	exit
	pleas input you num:\n\n
	""")
		if	num==0:
				_PutString()
				_MakeStringTable()
		elif num==1:
				_ReadString()
				_ReadTable()
		elif num==2:
			huffmantree=HuffmanTree(table)
			huffmantree._MakeHuffmanTree()
			HuffmanCode=huffmantree._MakeHuffmanCode()
			print HuffmanCode
		elif num==3:
			_SaveHuffmanCode(HuffmanCode)
		elif num==4:
			_ReadHuffmanCode(HuffmanCode)
		elif num==8:
				#for test
				_ReadString()
				_MakeStringTable()
				huffmantree=HuffmanTree(table)
				huffmantree._MakeHuffmanTree()
				print huffmantree._MakeHuffmanCode()

if __name__ == "__main__":
	Main()
