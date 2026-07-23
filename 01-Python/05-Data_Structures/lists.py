'''
Lists are used to store multiple items in a single variable.List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.
List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

'''
#Create alist
arr=[1,2,3,"sahithi"]
print(arr)#output:[1,2,3,"sahithi"]

#length of the list
print(len(arr))#output: 4

#datatype
print(type(arr)) #Output: <class 'list'>

#using list constructor to create a list
arr=(("sahithi",1,2,True))
print(arr)# Output:["sahithi",1,2,True]

#Accesing elements
#first Element
print(arr[0])  #Output :sahithi
#last Element
print(arr[-1])# Output: True
#first three elements
print(arr[0:4])# Output:["sahithi",1,2,True]

#print(last two elements)
print(arr[-3:-1])# Output:[2,True]


#change items
arr[0]="kishore"
print(arr)#Output: ["kishore",1,2,True]

#change range of items
arr[1:3]=[4,5]
print(arr) #Output:["kishore",4,5,True]


#To insert a list item at a specified index, use the insert() method.

#The insert() method inserts an item at the specified index:
arr.insert(2,"honey")
print(arr)#Output :["kishore",4,"honey",5,True]
#To add an item to the end of the list, use the append() method:
arr.append(54)
print(arr)#Output: ["kishore",4,"honey",5,True,54]

#To append elements from another list to the current list, use the extend() method.
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
arr2=[3,4,6]
extendList=arr.extend(arr2)
print(extendList) #Output:["kishore",4,"honey",5,True,54,3,4,6]

#Remove specified element
arr.remove("honey")#Output :["kishore",4,5,True,54]

#The pop() method removes the specified index.
arr.pop(0)
print(arr)#Output :[4,5,True,54]

#If you do not specify the index, the pop() method removes the last item.
arr.pop()
print(arr)#Output: [2,5,True]
#The del keyword also removes the specified index:
del arr[-1]
print(arr)#Output:[2,5]
#del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #Output: this will cause an error because you have succsesfully deleted "thislist".

#clear() method empties the list.The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)#Output:[]

#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #Output:['banana', 'kiwi', 'mango', 'orange', 'pineapple']


#copy a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) #Output :["apple", "banana", "cherry"]

#join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)#Output :["a","b","c",1,2,3]

