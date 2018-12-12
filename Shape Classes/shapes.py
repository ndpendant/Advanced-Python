#Dekai Rohlsen
#U50753261
import math

class Point(object):

	def __init__(self,x,y):

		self.xval = int(x)
		self.yval = int(y)
		
	def translate(self,dx,dy):
		self.xval = dx + self.xval
		self.yval = dy + self.yval
			
		

	def dist(A,B):
		a = (A.xval - B.xval)
		b = (A.yval - B.yval)
		sums = (pow(a,2)+pow(b,2))
		distance = sums**(.5)
		return distance
	
	def __repr__(self):
		a = str(self.xval)
		b = str(self.yval)
		coord = "("+ a + "," + b + ")"
		return coord

class Ellipse(Point):
	
	def __init__(self,center, x_extent,y_extent):
		self.x_extent = float(x_extent)
		self.y_extent = float(y_extent)
		self.center = (center.xval,center.yval)
	
	def translate(self,dx,dy):
		self.xval = dx + self.center[0]
		self.yval = dy + self.center[1]
		self.center = (self.xval,self.yval)
		return self.center

	def get_area(self):
		return 3.14*self.x_extent*self.y_extent
	
	def get_ellipse():
		pt_x = input("Enter x coordinate: ") 
		pt_y = input("Enter y coordinate: ")
		x = input("Enter x for extent: ")
		y = input("Enter y for extent: ")
		pt = Point(pt_x,pt_y)
		ellipse = Ellipse(pt,x,y)
		return ellipse


	def __repr__(self):
		a = str(self.center)
		x = str(2*self.x_extent)
		y = str(2*self.y_extent)
		string = "Ellipse with Center: "+a+"; Width: "+x+"; Height "+y
		return string

class circle(Ellipse):

	def __init__(self,center, radius):
		self.center = center
		self.radius = float(radius)

	def get_area():
		return 3.14*self.radius*self.radius	

	def translate(self,dx,dy):
		self.center = Ellipse.translate(self,dx,dy)
		#xval = dx + self.center[0]
		#yval = dx + self.center[1]
		#self.center = (xval,yval)
		
	def getCircle():
		x = input("Enter the x coordinate for your circle: ")
		y = input("Enter the y coordinate for your circle: ")
		r = input("Enter the radius for your circle: ")
		print("\n")
		new_circle = circle((int(x),int(y)),int(r))
		return new_circle
	
	def contain(a,b):
		inc = 0
		your_xr = [a.center[0] - a.radius ,  a.center[0] + a.radius]
		your_yr = [a.center[1] - a.radius ,  a.center[1] + a.radius]
		my_xr = [b.center[0] - b.radius ,  b.center[0] + b.radius]
		my_yr = [b.center[1]- b.radius ,  b.center[1] + b.radius]
			
		if(your_xr[0] >= my_xr[0] and your_xr[1] <= my_xr[1]) and (your_yr[0] >= my_yr[0] and your_yr[1] <= my_yr[1]):
			print("Your circle is contained by my circle!!")
			inc+=1
		if(my_xr[0] >= your_xr[0] and my_xr[1] <= your_xr[1]) and (my_yr[0] >= your_yr[0] and my_yr[1] <= your_yr[1]):
			print("My circle is contained by your circle!!")
			inc+=1
		if inc > 1:
			print("We have equivalent circles!!")	
		
		if inc < 1:
			print("Neither circle is contained by the other!!")
		
		print("\n")
		print("x range of your circle %s" % str(your_xr))
		print("y range of your circle %s" % str(your_yr))
		print("x range of my circle %s" % str(my_xr))
		print("y range of my circle %s" % str(my_yr))
	def __repr__(self):
		c = str(self.center)
		diameter = str(2*self.radius)
		radius = str(self.radius)
		
		string = "Circle with Center: "+c+"; radius: "+radius+"; Diameter: "+diameter
		return string

 
if __name__ == "__main__":
	

	print("PART 1 \n\n")
	a = Point( input("Enter x coordinate of point A: "), input("Enter y coordinate of point A: "))
	print("This is P: %s \n" % a)

	b = Point( input("Enter x coordinate of point B: "), input("Enter y coordinate of point B: "))
	print("This is P: %s \n" % b)
	
	a.translate(int(input("Enter dx to translate: ")),int( input("Enter dy to translate: ")))
	print("This is the new P(a): %s" % a)
	c = a.dist(b)
	print("The distance between points A and B are %f \n\n\n" % c)

	print("PART 2 \n\n")
	ell = Ellipse.get_ellipse()
	ell.translate(int(input("Enter dx to translate: ")),int( input("Enter dy to translate: ")))
	print(ell)
	print("\nThe Area of the ellipse is %f \n\n\n" % ell.get_area())
	
	print("PART 3 \n\n")
	default = circle((0,0),10)
	circ = circle.getCircle()
	circ.translate(int(input("Enter dx to translate: ")),int( input("Enter dy to translate: ")))
	

	print("\n\nLETS COMPARE CIRCLES!!")
	print("Here is mine: ")
	print(default)
	print("\n")
	print("Here is yours: ")
	print(circ)
	circle.contain(circ,default)
