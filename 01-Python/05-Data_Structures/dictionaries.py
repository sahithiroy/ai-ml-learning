'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''
#create a dictionarty
thisdict={
    "name":"ashithi",
    "age":12
}
print(thisdict)#output:{"name":"ashithi","age":12}

#length of the dictionary
print(len(thisdict))#Output: 2

# type 
print(type(thisdict))#Output :<class 'dict'>

#dict() constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)#Output:{"name":"John","age":36,"country":"Norway"}

#accesing the items
print(thisdict["name"])#Output:John
#accessing the elements using get method
print(thisdict.get("age"))#Output:36

#get keys in the dictionary
print(thisdict.keys())#Output:dict_keys(['name', 'age', 'country'])

#get value sin the dictionary
print(thisdict.values())#output:dict_values(['John',36,"Norway"])

#get the keys and values in dictinary
print(thisdict.items())#output:dict_items([('name', 'John'), ('age', 36), ('country', 'Norway')])

#update dictionary value by referringbit's key name
thisdict['age']=21
print(thisdict.items())#output:dict_items([('name', 'John'), ('age', 21), ('country', 'Norway')])
#add new item in the exiting dictionary using new index key value
thisdict['color']='red'
print(thisdict.items())#output:dict_items([('name', 'John'), ('age', 21), ('country', 'Norway'),('color','red')])

#update dictionary using update method
thisdict.update({"name":"sahithi"})
print(thisdict.items())##output:dict_items([('name', 'sahithi'), ('age', 21), ('country', 'Norway'),('color','red')])

#add new item in the dictionary using the update method
thisdict.update({"year":2000})
print(thisdict.items())#output:dict_items([('name', 'sahithi'), ('age', 21), ('country', 'Norway'),('color','red'),('year',2000)])

#removing items with the specified key name using pop method

thisdict.pop('year')
print(thisdict.items())#output:dict_items([('name', 'sahithi'), ('age', 21), ('country', 'Norway'),('color','red')])

#remove last inserted items using the popitem
thisdict.popitem()
print(thisdict.items())#output:dict_items([('name', 'sahithi'), ('age', 21), ('country', 'Norway')])


#del keyword removes the items in the specified key name
del thisdict['country']
print(thisdict.items())#Output:dict_items([('name', 'sahithi'), ('age', 21)])

#del keyword can also delete the dictionary completely
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

#clear() method empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) #Output:{}


#loop through dictionary
for x in thisdict:
    print(x)

#copy of a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)#Output:{"brand": "Ford","model": "Mustang","year": 1964}

#anotherway to make a copy is to use the dict()
mydict = dict(thisdict)
print(mydict)#Output:{"brand": "Ford","model": "Mustang","year": 1964}