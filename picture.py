from PIL import Image
import ImageEnhance
import ImageChops
import ImageFilter
import os
import math

im = Image.open("test1.png")
R,G,B=0,1,2
imgwidth=im.size[0]
imgheight=im.size[1]
Source=im.split()
r=Source[R]
g=Source[G]
b=Source[B]

def BlackAndWhite():
  global im
  pixel=im.load()
  for width in range(imgwidth):
     for height in range(imgheight):
	pregray=im.getpixel((width,height))
  	gray=0.11*(pregray[0])+0.59*(pregray[1])+0.3*(pregray[2])
  	gray=int (gray)
  	pixel[width,height]=(gray,gray,gray)
  im=Image.merge("RGB",(r,r,r))


def MakeColor(Color):
  sum=Color[0]+Color[1]+Color[2]
  Color[0]=Color[0]/sum
  Color[1]=Color[1]/sum
  Color[2]=Color[2]/sum
  global im
  pixel=im.load()
  for width in range(imgwidth):
     for height in range(imgheight):
	gray=im.getpixel((width,height))
	rgray=gray[0]*Color[0]
	ggray=gray[1]*Color[1]
	bgray=gray[2]*Color[2]
  	pixel[width,height]=(int(rgray),int(ggray),int(bgray))
def ImageReversal():
  global im
  pixel=im.load()
  for width in range(imgwidth):
     for height in range(imgheight):
	gray=im.getpixel((width,height))
	rgray=255-gray[0]
	ggray=255-gray[1]
	bgray=255-gray[2]
  	pixel[width,height]=(int(rgray),int(ggray),int(bgray))
       

def exposure():
   global im
   value=[0,0,0]
   for width in range(imgwidth):
      for height in range(imgheight):
	 gray=im.getpixel((width,height))
	 pixel=im.load()
	 for i in range(3):
	    if gray[i]<128:
	       value[i]=255-gray[i]
	    else:
	       value[i]=gray[i]
	 pixel[width,height]=(value[0],value[1],value[2])
def sharpen(num):
   global im
   pregray=None
   for width in range(imgwidth):
      for height in range(imgheight):
	 pixel=im.load()
	 if width%num==0 or height%num==0:
	    if width+num>imgwidth or height+num>imgheight:
	       pass
	    else:
	       pregray=im.getpixel((width+num/2,height+num/2))
	 else:
	    pixel[width,height]=(pregray[0],pregray[1],pregray[2]) 

def mosaic(num):
   global im
   pregray=None
   for width in range(imgwidth):
      for height in range(imgheight):
	 pixel=im.load()
	 if width%num==0 or height%num==0:
	    if width+num>imgwidth or height+num>imgheight:
	       pass
	    else:
	       pregray=[0,0,0]
	       sum=num*num
	       for i in range(num):
		  for j in range(num):
	            pregray[0]+=im.getpixel((width+i,height+j))[0]
	            pregray[1]+=im.getpixel((width+i,height+j))[1]
	            pregray[2]+=im.getpixel((width+i,height+j))[2]
	            pixel[width,height]=(pregray[0]/sum,pregray[1]/sum,pregray[2]/sum) 
	 else:
	    pixel[width,height]=(pregray[0],pregray[1],pregray[2]) 

	 
def relief():
   global im
   pregray=None
   for width in range(imgwidth):
      for height in range(imgheight):
	 pixel=im.load()
	 if width==0:continue
	 pregray=im.getpixel((width-1,height))
	 gray=im.getpixel((width,height))
	 pixel[width,height]=(gray[0]-pregray[0]+128,gray[1]-pregray[1]+128,gray[2]-pregray[2]+128) 

def neoneffect():
   gray=rightgray=downgray=None
   pixel=im.load()
   for width in range(imgwidth-1):
      for height in range(imgheight-1):
	gray=im.getpixel((width,height))
	rightgray=im.getpixel((width+1,height))
	downgray=im.getpixel((width,height+1))
	r1=gray[0]-rightgray[0];r2=gray[0]-downgray[0]
	g1=gray[1]-rightgray[1];g2=gray[0]-downgray[1]
	b1=gray[0]-rightgray[2];b2=gray[0]-downgray[2]
	Red=2*math.sqrt(r1*r1+r2*r2)
	Green=2*math.sqrt(g1*g1+g2*g2)
	Blue=2*math.sqrt(b1*b1+b2*b2)
	pixel[width,height]=(int(Red),int(Green),int(Blue))

def ImageWrap1(center,degree):
   img=im.copy()
   centergray=im.getpixel((center[0],center[1]))
   pixel=img.load()
   backimg=im.copy()
   for width in range(imgwidth):
      for height in range(imgheight):
	 offsetx=width-center[0]
	 offsety=height-center[1]
	 if offsetx==0:
	    continue
	 p=offsetx*offsetx+offsety*offsety
	 Angle=math.atan(offsety/offsetx)
	 widthi=int(degree*math.sqrt(p)*math.cos(Angle)+center[0])
	 heighti=int(degree*math.sqrt(p)*math.sin(Angle)+center[1])
	 if widthi >imgwidth-1:
	    widthi=imgwidth-1;
	 if heighti >imgheight-1:
	    heighti=imgheight-1;
	 if widthi < 0:
	    widthi=0
	 if heighti <0:
	    heighti=0
	 gray=backimg.getpixel((widthi,heighti))
	 pixel[width,height]=(gray[0],gray[1],gray[2])
   img.save("wrap 1output"+str(degree)+".png")
def spherewrap(center,degree):
   global im
   img=im.copy()
   centergray=im.getpixel((center[0],center[1]))
   pixel=img.load()
   backimg=im.copy()
   for width in range(imgwidth):
      for height in range(imgheight):
	 offsetx=width-center[0]
	 offsety=height-center[1]
	 if offsetx==0:
	    continue
	 p=(offsetx*offsetx+offsety*offsety)
	 Angle=math.atan(offsety/offsetx)
	 widthi=int(p*p*math.cos(Angle)*degree/max(center[0],center[1])+center[0])
	 heighti=int(p*p*math.sin(Angle)*degree/max(center[0],center[1])+center[1])
	 if widthi >imgwidth-1:
	    widthi=imgwidth-1;
	 if heighti >imgheight-1:
	    heighti=imgheight-1;
	 if widthi < 0:
	    widthi=0
	 if heighti <0:
	    heighti=0
	 gray=backimg.getpixel((widthi,heighti))
	 pixel[width,height]=(gray[0],gray[1],gray[2])
   img.save("sphere output"+str(degree)+".png")
def wavewrap(center):
   global im
   centergray=im.getpixel((center[0],center[1]))
   pixel=im.load()
   backimg=im.copy()
   for width in range(imgwidth):
      for height in range(imgheight):
	 offsetx=width-center[0]
	 offsety=height-center[1]
	 if offsetx==0:
	    continue
	 p=math.sqrt(offsetx*offsetx+offsety*offsety)
	 Angle=math.atan(offsety/offsetx)
	 widthi=int(p*math.cos(Angle+degree*p)+center[0])
	 heigthi=int(p*math.sin(Angle+degree*p)+center[1])
	 if widthi >imgwidth-1:
	    widthi=imgwidth-1;
	 if heighti >imgheight-1:
	    heighti=imgheight-1;
	 if widthi < 0:
	    widthi=0
	 if heighti <0:
	    heighti=0
	 gray=backimg.getpixel((widthi,heighti))
	 pixel[width,height]=(gray[0],gray[1],gray[2])

def main():
   #BlackAndWhite()
 Color=[255,0,0]
 #MakeColor(Color)
 #ImageReversal()
 #exposure()
 mosaic(8)
 #relief()
 #neoneffect()
 im.save("mosaic.png")
 Center=[imgwidth/2,imgheight/2]
 i=5
 #while True:
 #   ImageWrap1(Center,i*0.01)
 #   spherewrap(Center,i*0.001)
 #   i=i+5
 #   print i
 #   os.system("sleep 1.5")


if __name__=="__main__":
   main()
