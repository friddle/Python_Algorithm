#Kmp algorithms
#%%%%%% use kmp    
#%%%%%   next[0]=-1  first letter be -1
#%%%%%   next[j]=k   from the begin to k ->same as the j-k ->k  
#-------------------------------------
#a	b	 c	a		b		d
#-1	0	 0	0   1 	2
#d->(ab)=ab 2
#----------------------------------
#	a		b		c		a		c
#-1		0		0		0  	1 a->(a)1
#--------------------------------
##### 1   2   3   4   5   6   7   8
#####	a		b		c		a		b		c		a		d
##### -1	0		0		0	  1		2		3 	4
#####cnd     pos
#one#cnd          pos
##### -1	0  0
#two#cnd          pos->pos
##### -1  0  0    0    
#three#->cnd          pos->pos
#     -1  0  0    0   1
#four#       cnd          pos->pos  
#                           2  
#--------------------------------
#so the kmp_table algorithm function
#pos:2->leng
#pos:0->cnd



def kmp_table( ss ):
	"kmp function"
	table=range(-1,ss.__len__()-1)
	table[0]=-1;table[1]=0
	pos=2;cnd=0
	while pos<ss.__len__(): 
		#three
			if ss[pos-1]==ss[cnd]:
				cnd=cnd+1
				table[pos]=cnd
				pos=pos+1
			elif cnd>0 :
	  #step 
				cnd=table[cnd]
		#step one two 
			elif table[pos] :
				table[pos]=0
				pos=pos+1
	return table


######0 1 2 3 4 5 6 7 8 9
######a b a b c a b a b f
######a b a b f
#table-1 0 0 1 2 
######a b a b c a b a b f
######a b a b f
#one##    m i
#two##  i m  
#threei   m
#four#          m
#five#          

def kmp_search(s,ss):
	"kmp search"
	m=0;i=0
	table=kmp_table(ss)
	while m+i<s.__len__():
		if ss[i]==s[m+i]:         #when the ss[]=s[],i++,
			i=i+1
			if i==ss.__len__()-1:
				return i              #find it,return 
		else:
				m=m+i-table[i]        #when the i=0,m=m+1;if i!=0 return table[i]
				if table[i]>-1:
					  i=table[i]
				else:
						i=0
	return s.__len__()
print kmp_search("abcdfaababcababf","abcdfa")
