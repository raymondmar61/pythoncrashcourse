#Python Crash Course Chapter 15 Generating Data
#Data visualization involves exploring data through visual representations. It’s closely associated with data mining, which uses code to explore the patterns and connections in a data set.
#You can see all the colormaps available in pyplot at http://matplotlib.org/; go to Examples, scroll down to Color Examples, and click colormaps_reference.  Specifically, http://matplotlib.org/examples/color/colormaps_reference.html.
#To see what kind of visualizations are possible with Pygal, visit the gallery of chart types: go to http://www.pygal.org/, click Documentation, and then click Chart types.

import matplotlib.pyplot as plt

inputvalues = [1, 2, 3, 4, 5] #When you give plot() a sequence of numbers, it assumes the first data point corresponds to an x-coordinate value of 0, but our first point corresponds to an x-value of 1. We can override the default behavior by giving plot() both the input and output values used to calculate the squares
squares = [1, 4, 9, 16, 25]
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
plt.tick_params(axis="both", labelsize = 14)
plt.plot(squares) #can plot more than one line in a chart
plt.plot(inputvalues, squares, linewidth = 5)
plt.show()
#To plot a single point, use the scatter() function. Pass the single (x, y) values of the point of interest to scatter().
plt.scatter(2, 4, s = 200) #s is size of dots
plt.show()
#To plot a series of points, we can pass scatter() separate lists of x- and y-values.  No line connecting the points.  Points only.
xvalues = [1, 2, 3, 4, 5]
yvalues = [1, 4, 9, 16, 25]
plt.scatter(xvalues, yvalues, s = 100)
plt.show()
#Let’s use a loop in Python to do the calculations for us. Here’s how this would look with 1000 points.
xvalues1000 = list(range(1, 1001))
yvalues1000 = [x**2 for x in xvalues1000]
plt.scatter(xvalues1000, yvalues1000, s=40) #default is blue dots with a black outline
plt.scatter(xvalues1000, yvalues1000, c="red", edgecolor="none", s=40) #remove onlines around points set edgecolor = "none". Set color of points or dots c="red" or c=(R, G, B) values between 0 and 1.
plt.scatter(xvalues1000, yvalues1000, c=yvalues1000, cmap=plt.cm.Blues, edgecolor="none", s=40) #A colormap is a series of colors in a gradient that moves from a starting to ending color. Colormaps are used in visualizations to emphasize a pattern in the data. For example, you might make low values a light color and high values a darker color.  Here’s how to assign each point a color based on its y-value in blue.
plt.axis([0, 1100, 0, 1100000]) #the axis() function to specify the range of each axis w. Requires four values: the minimum and maximum values for the x-axis and the y-axis. Here, we run the x-axis from 0 to 1100 and the y-axis from 0 to 1,100,000.
plt.show()
#If you want your program to automatically save the plot to a file, you can replace the call to plt.show() with a call to plt.savefig().  File saved in same directory of python file.
plt.savefig('squares_plot.png', bbox_inches='tight') #bbox_inches trims extra whitespace from the plot. If you want the extra whitespace around the plot, you can omit bbox_inches.

xvaluescube = list(range(1, 5001))
yvaluescube = [x**3 for x in xvaluescube]
plt.axis([0, 5100, 0, 126000000000])
plt.scatter(xvaluescube, yvaluescube, c=yvaluescube, cmap=plt.cm.Reds, edgecolor="none", s=30)
plt.show()
#save charts, replace plt.show() with plt.savefig().  bbox_inches="tight" trims extra whiltespace from the plot.
#plt.savefig("filename.png", bbox_inches="tight")

from random import choice
class RandomWalk():
	def __init__(self, numpoints=5000):
		self.numpoints = numpoints
		#initialize (x,y) at (0,0) using lists
		self.xvalues = [0]
		self.yvalues = [0]
	def getstep(self):
		direction = choice([1, -1])
		distance = choice([0, 1, 2, 3, 4])
		step = direction * distance
		return step
	def fillwalk(self):
		while len(self.xvalues) < self.numpoints:
			xstep = self.getstep()
			ystep = self.getstep()
			if xstep == 0 and ystep == 0:
				continue
			nextx = self.xvalues[-1] + xstep
			nexty = self.yvalues[-1] + ystep
			self.xvalues.append(nextx)
			self.yvalues.append(nexty)
	#original def fillwalk(self): before fillwalk(self) and getstep(self)
	# def fillwalk(self):
	# 	while len(self.xvalues) < self.numpoints:
	# 		xdirection = choice([1, -1])
	# 		xdistance = choice([0, 1, 2, 3, 4])
	# 		xstep = xdirection * xdistance
	# 		ydirection = choice([1, -1])
	# 		ydistance = choice([0, 1, 2, 3, 4])
	# 		ystep = ydirection * ydistance
	# 		if xstep == 0 and ystep == 0:
	# 			continue
	# 		nextx = self.xvalues[-1] + xstep
	# 		nexty = self.yvalues[-1] + ystep
	# 		self.xvalues.append(nextx)
	# 		self.yvalues.append(nexty)
rw = RandomWalk()
rw.fillwalk()
plt.figure(dpi = 128, facecolor="red", figsize=(15,5)) #set the resolution, background color outside chart, size of the plotting window (horizontal size width, vertical size height)
pointnumbers = list(range(rw.numpoints))
print(pointnumbers) #print list [0, 1, 2, . . . 4997, 4998, 4999]
print(rw.xvalues) #print rw.xvalues random list like [0, 3, 6, 5, 9, 13, 9, 12, 9, 10, 14, . . . ]
plt.scatter(rw.xvalues, rw.yvalues, c=pointnumbers, cmap=plt.cm.Blues, edgecolor = "none", s = 15) #we use range() to generate a list of numbers equal to the number of points in the walk. Then we store them in the list pointnumbers, which we’ll use to set the color of each point in the walk. We pass point_numbers to the c argument.
#plot the first and last points individually after the main series is plotted. Also, make the end points larger and color them differently to make them stand out.
plt.scatter(0,0, c="green", edgecolor="none", s=100)
plt.scatter(rw.xvalues[-1],rw.yvalues[-1], c="red", edgecolor="none", s=100)
#remove axes, hide axes
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
plt.plot(rw.xvalues, rw.yvalues, linewidth = 3)
plt.show()

#use Python visualization package Pygal to produce scalable vector graphics files
from random import randint
import pygal
class Die():
	def __init__(self, numsides = 6):
		self.numsides = numsides
	def roll(self):
		return randint(1,self.numsides)
sixsided = Die()
print(sixsided.roll()) #print a number between 1 and 6
die = Die()
results = []
for rollnum in range(0,100):
	result = die.roll()
	results.append(result)
print(results)
frequencies = []
for value in range(1,die.numsides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)
hist = pygal.Bar() #creating an instance of pygal.Bar(), which we store in hist
hist.Title = "Results of rolling one D6 100 times."
hist.x_labels = ["1","2","3","4","5","6"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6", frequencies)
#hist.show() #error message
hist.render_to_file("filename.svg")
#start page 353 rolling two dice