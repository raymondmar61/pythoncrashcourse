#Python Crash Course Chapter 15 Generating Data
#Many data sets you work with will have missing data, improperly formatted data, or incorrect data. Use the tools to deal with these situations. Here we used a try-except-else block to handle missing data. Sometimes you’ll use continue to skip over some data or use remove() or del to eliminate some data after it’s been extracted.

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "sitka_weather_07-2014.csv"
with open (filename,"r") as fileobject:
	reader = csv.reader(fileobject)
	headerrow = next(reader) #The csv module contains a next() function, which returns the next line in the file when passed the reader object. We call next() once to get the first line of the file which contains the headers.  We store the data that’s returned in headerrow.
	print(headerrow) #print ['AKDT', 'Max TemperatureF', 'Mean TemperatureF', 'Min TemperatureF', 'Max Dew PointF', 'MeanDew PointF', 'Min DewpointF', 'Max Humidity', ' Mean Humidity', ' Min Humidity', ' Max Sea Level PressureIn', ' Mean Sea Level PressureIn', ' Min Sea Level PressureIn', ' Max VisibilityMiles', ' Mean VisibilityMiles', ' Min VisibilityMiles', ' Max Wind SpeedMPH', ' Mean Wind SpeedMPH', ' Max Gust SpeedMPH', 'PrecipitationIn', ' CloudCover', ' Events', ' WindDirDegrees']
	for index, columnheader in enumerate(headerrow): #enumerate() on the list to get the index of each item, as well as the value.
		print(index, columnheader) #print 0 AKDT\n 1 Max TemperatureF\n 2 Mean TemperatureF\n 3 Min TemperatureF . . .
	#We know high temperatures is column 1.  Print the high temperatures.
	highs = []
	for column in reader:
		high = int(column[1]) #convert from string to integer
		highs.append(high)
	print(highs) #print ['64', '71', '64', '59', '69', '62', '61', '55', '57', '61', '57', '59', '57', '61', '64', '61', '59', '63', '60', '57', '69', '63', '62', '59', '57', '57', '61', '59', '61', '61', '66']
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(highs, c="red")
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()

firstdate = datetime.strptime("7/1/14", "%m/%d/%y")
print(firstdate) #print 2014-07-01 00:00:00
firstdate = datetime.strptime("2014-7-1", "%Y-%m-%d")
print(firstdate) #print 2014-07-01 00:00:00

#Plot dates and high temperatures
filename = "sitka_weather_07-2014.csv"
with open (filename,"r") as fileobject:
	reader = csv.reader(fileobject)
	headerrow = next(reader)
	dates, highs = [], []
	for column in reader:
		currentdate = datetime.strptime(column[0], "%Y-%m-%d")
		dates.append(currentdate)
		high = int(column[1])
		highs.append(high)
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c="red")
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate() #fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()
#Plotting a Longer Timeframe using sitka_weather_2014.csv
filename = "sitka_weather_2014.csv"
with open (filename,"r") as fileobject:
	reader = csv.reader(fileobject)
	headerrow = next(reader)
	dates, highs = [], []
	for column in reader:
		currentdate = datetime.strptime(column[0], "%Y-%m-%d")
		dates.append(currentdate)
		high = int(column[1])
		highs.append(high)
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c="red")
plt.title("Daily high temperatures, 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate() #fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()
#Plotting a Longer Timeframe high temps and low temps using sitka_weather_2014.csv
filename = "sitka_weather_2014.csv"
with open (filename,"r") as fileobject:
	reader = csv.reader(fileobject)
	headerrow = next(reader)
	dates, highs, lows = [], [], []
	for column in reader:
		currentdate = datetime.strptime(column[0], "%Y-%m-%d")
		dates.append(currentdate)
		high = int(column[1])
		highs.append(high)
		low = int(column[3])
		lows.append(low)
fig = plt.figure(dpi=128, figsize=(10,6))
#Shading an Area in the Chart
plt.plot(dates, highs, c="red", alpha=0.5) #alpha controls a color's transparency between 0 transparent and 1 opaque
plt.plot(dates, lows, c="blue", alpha=0.5) #alpha controls a color's transparency between 0 transparent and 1 opaque
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) #fill_between() the list dates for the x-values and then the two y-value series highs and lows. The facecolor  determines the color of the shaded region
plt.title("Daily high and low temperatures, 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate() #fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()

#Example of missing data.  Use death_valley_2014.csv
filename = "death_valley_2014.csv"
with open (filename,"r") as fileobject:
	reader = csv.reader(fileobject)
	headerrow = next(reader)
	dates, highs, lows = [], [], []
	for column in reader:
		try:
			currentdate = datetime.strptime(column[0], "%Y-%m-%d")
			high = int(column[1])
			low = int(column[3])
		except:
			print(currentdate, "missing data")
		else:
			dates.append(currentdate)
			highs.append(high)
			lows.append(low)
fig = plt.figure(dpi=128, figsize=(10,6))
#Shading an Area in the Chart
plt.plot(dates, highs, c="red", alpha=0.5) #alpha controls a color's transparency between 0 transparent and 1 opaque
plt.plot(dates, lows, c="blue", alpha=0.5) #alpha controls a color's transparency between 0 transparent and 1 opaque
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) #fill_between() the list dates for the x-values and then the two y-value series highs and lows. The facecolor  determines the color of the shaded region
plt.title("Daily high and low temperatures, 2014\nDeath Valley, CA", fontsize=18)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate() #fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()
#Many data sets you work with will have missing data, improperly formatted data, or incorrect data. Use the tools you learned in the first half of this book to deal with these situations. Here we used a try-except-else block to handle missing data. Sometimes you’ll use continue to skip over some data or use remove() or del to eliminate some data after it’s been extracted.

#Skipped JSON format starting page 362.