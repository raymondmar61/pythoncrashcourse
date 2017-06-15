#Python Crash Course Chapter 3 Introducing Lists

bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles) #print ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].upper()) #print TREK
print(bicycles[2]) #print redline
print(bicycles[-1]) #print specialized
print(bicycles[-3]) #print cannondale
message = "My first bicycle was a " +bicycles[0].title()+ "."
print(message) #print My first bicycle was a Trek.
print("\n")

motorcycles = ["honda","yamaha","suzuki"]
print(motorcycles) #print ["honda","yamaha","suzuki"]
motorcycles[0] = "ducati"
print(motorcycles) #print ["ducati","yamaha","suzuki"]
motorcycles = ["honda","yamaha","suzuki"]
print(motorcycles) #print ["honda","yamaha","suzuki"]
motorcycles.append("ducati")
print(motorcycles) #print ["honda","yamaha","suzuki","ducati"]
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles) #print ["honda","yamaha","suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles) #print ["ducati","honda","yamaha","suzuki"]
del motorcycles[0]
print(motorcycles) #print ["honda","yamaha","suzuki"]
#The pop() method removes the last item in a list, but it lets you work with that item after removing it.
motorcycles = ["honda","yamaha","suzuki"]
print(motorcycles) #print ["honda","yamaha","suzuki"]
poppedmotorcycle = motorcycles.pop()
print(motorcycles) #print ["honda","yamaha"]
print(poppedmotorcycle) #print suzuki
#You can use pop() to remove an item in a list at any position by including the index of the item you want to remove in parentheses.
motorcycles = ["honda","yamaha","suzuki"]
firstowned = motorcycles.pop(0)
print("The first motorcycle I owned was a " +firstowned.title()+ ".") #print The first motorcycle I owned was a Honda.
motorcycles = ["honda","yamaha","suzuki","ducati"]
print(motorcycles) #print ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove("ducati")
print(motorcycles) #print ["honda","yamaha","suzuki"]
motorcycles = ["honda","yamaha","suzuki","ducati"]
print(motorcycles) #print ['honda', 'yamaha', 'suzuki', 'ducati']
tooexpensive = "ducati"
motorcycles.remove(tooexpensive)
print(motorcycles) #print ["honda","yamaha","suzuki"]
motorcycles = ["honda","ducati","yamaha","suzuki","ducati"]
motorcycles.remove("ducati") #remove() deletes the first occurance in a list
print(motorcycles) #print ['honda', 'yamaha', 'suzuki', 'ducati']
print("\n")

guestlist = ["Steve Jobs","Mark Z.","Jennifer Lawrence","Buster Posey"]
print("I want wisdom " +guestlist[0])
print("I need a job " +guestlist[1])
print("Tell me stories, " +guestlist[2]+ " about movies.")
print("You're my favorite SF Giants Mr. " +guestlist[3])
print("I'm sorry you can't make it Mr. " +guestlist.pop())
guestlist.append("Madison Bumgarner")
print("I'm glad you can make it Mr. " +guestlist[3])
print(guestlist) #print ['Steve Jobs', 'Mark Z.', 'Jennifer Lawrence', 'Madison Bumgarner']
guestlist.insert(0,"Paul McCartney")
guestlist.insert(2,"Bill Clinton")
guestlist.insert(-1,"Pink") #why is Pink before Badison Bumgarner?
guestlist.append("Madonna")
print(guestlist) #print ['Paul McCartney', 'Steve Jobs', 'Bill Clinton', 'Mark Z.', 'Jennifer Lawrence', 'Pink', 'Madison Bumgarner', 'Madonna']
print("I can invite two guests.")
sorry = guestlist.pop()
print(sorry+ " you're removed.")
sorry = guestlist.pop()
print(sorry+ " you're removed.")
sorry = guestlist.pop()
print(sorry+ " you're removed.")
sorry = guestlist.pop()
print(sorry+ " you're removed.")
sorry = guestlist.pop()
print(sorry+ " you're removed.")
sorry = guestlist.pop()
print(sorry+ " you're removed.")
print(guestlist[0]+ " and " +guestlist[1]+ " are the final guests.")
del guestlist[0] #Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
del guestlist[0]
print(guestlist) #del guestlist <-- doesn't work because it deletes the entire list and the list variable.
print("\n")

cars = ["bmw", "audi", "toyota", "subaru"]
print(cars) #print ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars) #print ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars) #print ['toyota', 'subaru', 'bmw', 'audi']
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars) #print ["bmw", "audi", "toyota", "subaru"]
print(sorted(cars)) #The sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list. print ['audi', 'bmw', 'subaru', 'toyota']
print(sorted(cars, reverse=True)) #print ['toyota', 'subaru', 'bmw', 'audi']
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars) #print ["bmw", "audi", "toyota", "subaru"]
cars.reverse()
print(cars) #print ['subaru', 'toyota', 'audi', 'bmw']
#The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time.
cars.reverse()
print(cars) #print ["bmw", "audi", "toyota", "subaru"]
print(len(cars)) #print 4
print("\n")

seetheworld = ["Las Vegas","Yosemite","England","Zion","Washington D.C.","Disneyland"]
print(seetheworld) #print ['Las Vegas', 'Yosemite', 'England', 'Zion', 'Washington D.C.', 'Disneyland']
print(sorted(seetheworld)) #print ['Disneyland', 'England', 'Las Vegas', 'Washington D.C.', 'Yosemite', 'Zion']
print(seetheworld) #print ['Las Vegas', 'Yosemite', 'England', 'Zion', 'Washington D.C.', 'Disneyland']
print(sorted(seetheworld, reverse=True)) #print ['Zion', 'Yosemite', 'Washington D.C.', 'Las Vegas', 'England', 'Disneyland']
print(seetheworld) #print ['Las Vegas', 'Yosemite', 'England', 'Zion', 'Washington D.C.', 'Disneyland']
seetheworld.reverse()
print(seetheworld) #print ['Disneyland', 'Washington D.C.', 'Zion', 'England', 'Yosemite', 'Las Vegas']
seetheworld.reverse()
print(seetheworld) #print ['Las Vegas', 'Yosemite', 'England', 'Zion', 'Washington D.C.', 'Disneyland']
seetheworld.sort()
print(seetheworld) #print ['Disneyland', 'England', 'Las Vegas', 'Washington D.C.', 'Yosemite', 'Zion']
seetheworld.sort(reverse=True)
print(seetheworld) #print ['Zion', 'Yosemite', 'Washington D.C.', 'Las Vegas', 'England', 'Disneyland']
print("\n")