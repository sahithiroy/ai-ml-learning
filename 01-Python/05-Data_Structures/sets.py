'''
Sets are used to store multiple items in a single variable.A set is a collection which is unordered, unchangeable*, and unindexed.
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

'''
#create a set
thisset = {"apple", "banana", "cherry","apple"}
print(thisset)#ouptut:{"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)#Output:{True, 2, 'banana', 'cherry', 'apple'}

#length of a set
print(len(thisset))#output:5

#type
print(type(thisset))#Output:<class 'set'>

#create aset using set constructor
arr=set(("honey","sahithi","ramu"))
print(arr)#Output:{"honey","sahithi","ramu"}

#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)#Output: True

#Once a set is created, you cannot change its items, but you can add new items.To add one item to a set use the add() method.
thisset.add("guava")
print(thisset)#Output: {"apple", "banana", "cherry","guava"}

#To add items from another set into the current set, use the update() method.
tropical={1,2,3}
thisset.update(tropical)
print(thisset)#Output:{"apple", "banana", "cherry","guava",1,2,3}

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)#Output:{"apple", "banana", "cherry","kiwi", "orange"}
#remove an item ,If the item to remove does not exist, remove() will raise an error.
thisset.remove("orange")
print(thisset)#Output:"apple", "banana", "cherry","kiwi"}
#discard an item , If the item to remove does not exist, discard() will NOT raise an error.

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
thisset.pop()

#Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)#Output:{"a","b","c",1,2,3}


