#Lists allow you to store sets of information in one place
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[3])
print("Return the last item use [-1] without knowing how long the list is " +bicycles[-1])
print("Return the second to last item use [-2] with title() method " +bicycles[-2].title())
print("\n")

#Most lists you create will be dynamic, meaning you’ll build a list and then add and remove elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' #replace an item on the list with another item
print(motorcycles)
motorcycles.append("honda")
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0,"ducati")
print(motorcycles)
del motorcycles[1]
print(motorcycles)
print("\n")

#Sometimes you’ll want to use the value of an item after you remove it from a list. For example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at that position.
#The pop method removes the last item in a list, but it lets you work with that item after removing it.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print("suzuki is removed (use comma to concatenate a list with text)" ,motorcycles)
print("what motorcycle was popped?" ,popped_motorcycles)
#You can actually use pop() to remove an item in a list at any position by including the index of the item you want to remove in parentheses.
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(motorcycles)
print(first_owned)
print("\n")

#Sometimes you won’t know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you can use the remove method.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles, too_expensive+ " was too expensive")
print("\n")

#Python’s sort method makes it relatively easy to sort a list.
#The sort method changes the order of the list permanently.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort(reverse=True)
print(cars)
#The sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)
print("Here is the sorted list reverse:")
print(sorted(cars, reverse=True))
print("\n")

#To reverse the original order of a list, you can use the reverse method. If we originally stored the list of cars in chronological order according to when we owned them, we could easily rearrange the list into reverse chronological order.  #Notice that reverse doesn’t sort backward alphabetically; it simply reverses the order of the list.
#The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)
print("\n")

#You can quickly find the length of a list by using the len() function
#Python counts the items in a list starting with one.
one errors when determining the length of a list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(len(cars))