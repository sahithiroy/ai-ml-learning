#Swap two variables without a third variable.
a=int(input())
b=int(input())
#a,b=map(int,input().split()) using map
#Using List C0mprehension
a,b=[int(x) for x in input().split()]
print("before Swapping")
print(a,b)
a,b=b,a
print("afterswapping")
print(a,b)


#2.Find the largest three numbers of in a list
def largetThreeNumbers(arr):
    first=float('-inf')
    second=float('-inf')
    third=float('-inf')
    for num in arr:
        if num>first:
            third=second
            second=first
            first=num
        elif second<num:
            third=second
            second=num
        elif third<num:
            third=num
    print(first,second,third)
    return[first,second,third]
    
n=int(input())
arr=list(map(int,input().split()))
print(arr)
largetThreeNumbers(arr)

#3.Check if a number is even or odd.
def evenOrOdd(num):
    if num<0:
        print('give positive intger')
        return
    
    if num%2==0:
        print("Even NUmber",num)
    else:
        print("odd Number",num)
n=int(input())
evenOrOdd(n)

#Reverse a string.

def reverseString(name):
    return name[::-1]
n=input()
print(reverseString(n))


#Count vowels in a string.
def countVowels(word):
    count=0
    word=word.lower()
    for num in word:
        if num=='a' or num=='e' or num=='i' or num=='o' or num=='u':
            count+=1
    return count

n=input()
countVowels(n)


#Remove duplicates from a list.
def removeDuplicates(arr):
   
    return list(set(arr))

n=int(input())
arr=list(map(int,input().split()))
removeDuplicates(arr)

#Find the second largest number in a list.
def largetTwoNumbers(arr):
    first=float('-inf')
    second=float('-inf')
   
    for num in arr:
        if num>first:
            second=first
            first=num
        elif second<num:
            second=num
      
    print(first,second)
    return[first,second]

n=int(input())
arr=list(map(int,input().split()))
print(arr)
largetTwoNumbers(arr)

#Find common elements between two lists.
def commonElements(arr1,arr2):
    for num in arr1:
        if num in arr2:
            print(num)
n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(arr1,arr2)
commonElements(arr1,arr2)

#Count occurrences of each element in a list.
from collections import Counter
def countOccurences(arr):
    return Counter(arr)
arr=list(map(int,input().split()))
countOccurences(arr)

#Flatten a nested list (1 level).
# Original list
lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]

# iterate through the sublist using List comprehension
flatList = [element for innerList in lis for element in innerList]

# printing original list
print('List', lis)
# printing flat list
print('Flat List', flatList)

