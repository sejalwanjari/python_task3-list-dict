# append() method
print()
rainbow = ['violet','indigo','blue','green','yellow','orange']

print(f'rainbow before append =', rainbow)

rainbow.append('red')
print()

print(f'rainbow after append =', rainbow)

print()
print()


# clear() method

odd_no = [1,3,5,7,9,11,13,15,17,19]

print(f'odd no before clear =', odd_no)

odd_no.clear()
print()

print(f'odd no after clear =', odd_no)

print()
print()


# copy() method

colours = []

print(f'colours before copy =', colours)

colours = rainbow.copy()
print()

print(f'colours after copy =', colours)

print()
print()


# count() method

numbers = [2,5,7,3,5,2,9,3,5,6,7,6,2]

print(f'numbers =', numbers)

count = numbers.count(2)
print()

print(f'count of no 2 =', count)

print()
print()


# extend() method

name = ['sejal wanjari']

batch = ['da9','6PM']

print(f'name =',name)
print(f'batch =',batch)

name.extend(batch)
print()

print(f'after entend of name and batch =', name)

print()
print()


# index() method

sports = ['badminton','basketball','cycling','football','hockey','table tennis']

print(f'sports =',sports)

index = sports.index('football')
print()

print(f'index of football = ',index)

print()
print()


# insert() method

vegetables = ['tomato','potato','cabbage','carrot','onion','broccoli']

print(f'vegetables before insert =', vegetables)

vegetables.insert(2,'garlic')
print()

print(f'vegetables after insert =', vegetables)

print()
print()


# pop() method

planets = ['earth','jupiter','venus','saturn','mercury','mars','uranus','neptune']

print(f'planet before pop = ', planets)

planets.pop(3)
print()

print(f'planet after pop = ', planets)

print()
print()


# remove() method 

fruits = ['mango','banana','strawberry','pineapple','watermelon','cherry','kiwi','papaya']

print(f'fruits before remove = ', fruits)

fruits.remove('pineapple')
print()

print(f'fruits after remove = ', fruits)

print()
print()


# reverse() method

levels = ['level5','level4','level3','level2','level1']

print(f'level before reverse = ', levels)

levels.reverse()
print()

print(f'level after reverse = ', levels)

print()
print()


# sort() method

alphabets = ['d','g','f','b','e','a','h','c']

print(f'alphabets before sort = ', alphabets)

alphabets.sort()
print()

print(f'alphabets after sort = ',alphabets)
