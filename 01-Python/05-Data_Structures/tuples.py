'''
Tuples are used to store multiple items in a single variable.A tuple is a collection which is ordered and unchangeable.
Tuple items are ordered, unchangeable, and allow duplicate values.
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

'''
#create atuple
arr=("honey",1,2)
print(arr)#Output:("honey",1,2)
#length
print(len(arr))#Output :3

#create tuple with one item
arr=(1,)
print(arr)#Output:(1)

#datatype 
print(type(arr))#Output:<class 'tuple'>

#create a tuple using tuple() Constructor

arr=tuple(("sahithi",1,3))
print(arr)#Output: ("sahithi",1,3)

#access elements
print(arr[0]) #Output:sahithi

#updating tuples .tuples are immutable once created we cannot change .
#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)#Output: ("apple", "kiwi", "cherry")

#Add items in a tuple.Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


#Unpack tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)#Output:("a","b","c",1,2,3)
