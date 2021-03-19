#31 Python Program to Print all Prime Numbers in a given Interval
n1 = int(input("Enter Start: "))
n2 = int(input("Enter End: "))
print("Prime numbers between", n1, "and", n2, "are: ", end = " ")
for n in range(n1,n2+1):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
            print(n, end = " ")

#OUTPUT- Enter Start: 1
#Enter End: 10 
#Prime numbers between 1 and 10 are:  2 3 5 7

#32 Python Program to Display the multiplication Table
n = int(input("Enter number: "))
for i in range(1,11):
    print(n,"X", i, "=", n*i)

#OUTPUT - Enter number: 5
#5 X 1 = 5
#5 X 2 = 10
#5 X 3 = 15
#5 X 4 = 20
#5 X 5 = 25                                                                                                                                               
#5 X 6 = 30                                                                                                                                               
#5 X 7 = 35                                                                                                                                               
#5 X 8 = 40                                                                                                                                               
#5 X 9 = 45   
#5 X 10 = 50

#33 Python Program to Print the Fibonacci sequence
def fib(n):
    if n <= 1:
        return n 
        
    else:
        return fib(n-1) + fib(n-2)
        
n = int(input("Enter Number: "))
for i in range(0,n):
    print(fib(i), end = " ")

#OUTPUT - Enter Number: 5
# 0 1 1 2 3

#34 Python Program to Find the Sum of first N natural numbers
n = int(input("Enter Number: "))
sum = 0
for i in range(1,n+1):
	sum+=i 
	
print("Sum of N natural numbers: ", sum)

#OUTPUT - Enter Number: 5
# 		  Sum of Natural numbers: 15

#35 Python Program to Find the Factorial of a given number
n = int(input("Enter Number: "))
fac = 1
for i in range(1,n+1):
	fac *= i 

print("Factorial: ", fac)

#OUTPUT - 
#Enter Number: 5
#Factorial:  120

#36 Python Program to find sum of digits of a given number
N = int(input("Enter Number: "))
s = 0
for i in range(1,N+1):
	re = N%10
	s += re
	N = N//10
print("Sum: ", s)

#OUTPUT 
#Enter Number: 123
#Sum:  6

#37 Python Program to find reverse of a number
N = 123 
rev = 0
for i in range(1,N+1):
	if(N==0):
		break
	else:
		re = N%10
		rev = (rev*10)+re
		N = N//10
print("Reverse: ", rev)

#OUTPUT 
#Reverse: 321 

#38 Python Program to Find the Factors of a Number
n = 15
print("Factors of 15 are: ")
for i in range(1,n+1):
	if n%i == 0:
		print(i, end = " ")

#OUTPUT 
#Factors of 15 are:
#1 3 5 15

#42 Python Program to print following pattern
#A
#B A B
#A B A B A
#B A B A B A B
#A B A B A B A B A

f = 0
for i in range(1,10,2):
	for j in range(1,i+1):
		if(f==0):
			print("A", end = " ")
			f += 1
		else:
			print("B", end = " ")
			f -=1
	print()

#43 Python Program to find greatest among three number using function
def gre(a,b,c):
	if a>b and a>c:
		return a
	elif b>a and b>c:
		return b
	else:
		return c

a = 1
b = 2 
c = 3
print("Greatest Number: ",gre(a,b,c))

#OUTPUT-  Greatest Number: 3

#44 Python Program to find sum of following series using function
#1/1! + 2/2! + 3/3! + 4/4! + up to n terms
n = int(input("Enter Number: "))
fac = 1
s = 0
for i in range(1,n+1):
	fac *= i 
	s += i/fac 

print("Sum of series: ", s)

#OUTPUT- Enter Number: 2
#		 Sum of series: 2.0

#45 Python Program to implement nCr using function
def nCr(n,r):
	fac = 1
	fac1 = 1
	fac2 = 1
	c = 0
	for i in range(1,n+1):
		fac *= i
	for j in range(1,n-r+1):
		fac1 *= j
	for k in range(1,r+1):
		fac2 *= k
	c = fac/(fac1*fac2)
	return c

n = 5
r = 3

print("nCr: ",int(nCr(n,r)))

#OUTPUT- nCr:  10

#46 #Python Program to  find HCF and LCM of two numbers using function
def calc_hcf(x,y):
	smallest = 0
	if x>y:
		smallest = y
	else:
		smallest = x

	for i in range(1,smallest+1):
		if x%i ==0 and y%i ==0:
			hcf = i 
	return hcf

x = 54
y = 24

lcm = (x*y)//calc_hcf(x,y)
print("LCM: ",lcm)

print("HCF is: ", calc_hcf(x,y))

#OUTPUT - LCM:  216
#HCF is:  6

#47 Python Program to print factorial of a given number using function
def fac(n):
	fact = 1
	for i in range(1,n+1):
		fact *= i

	return fact
n = int(input("Enter Number: "))
print("Factorial: ", fac(n))

#OUTPUT - Enter Number: 5
#         Factorial:  120

#48 Python Program to print Fibonacci Series up to n terms
def fib(n):
	n1 = 0
	n2 = 1
	count = 0

	if n<=0:
		print("Enter positive number")

	else:
		for i in range(0,n):
			print(n1)
			nth = n1 + n2
			n1 = n2
			n2 = nth
			

n = int(input("Enter Number: "))
print(fib(n),end = " ")

#OUTPUT- Enter Number: 5
# 0 1 1 2 3

#49 Python Program to print factorial of a given number using recursion
def fac(n):
	fact = 1

	if n == 1:
		return n 
	else:
		return n*fac(n-1)

n = int(input("Enter number: "))
print("Factorial: ",fac(n))

#OUTPUT  Enter number: 6
#        Factorial:  720

#50 Python Program to find GCD of two numbers using recursion
def gcd(a,b):
	if b == 0:
		return a

	else: 
		return gcd(b, a%b)

a = 5
b = 15
GCD = gcd(a,b) 
print("GCD is ",GCD)

# OUTPUT - 
# GCD is 5

#51 Python Program to multiply two numbers using lambda function
a = lambda x,y : x*y
print("multiplication: ", a(4,5))

#Output - multiplication: 20

#53Implement various String methods 
a = "hello python"
print("capitalize:",a.capitalize())
print("count:",a.count("l"))# no of times a letter repeat
print("endswith:",a.endswith("n"))
print("startswith:",a.startswith("h",0))
print("find: ",a.find("n"))
print("Index:",a.index("e"))
print("Is alphanumeric: ", a.isalnum())
print("Is alphabet: ",a.isalpha())
print("Is digit: ",a.isdigit())
print("Is lowercase: ", a.lower())
print("Is Uppercase: ", a.upper())
print("Max: ", max(a))

#Output-
capitalize: Hello python
count: 2
endswith: True
startswith: True
find:  11
Index: 1
Is alphanumeric:  False
Is alphabate:  False
Is digit:  False
Is lowercase:  hello python
Is Uppercase:  HELLO PYTHON
Max:  y

#54 Implement various List methods
l = [2,4,6,1,3,5]
print(l)
l.append(7)
print("count no. of 5 :",l.count(5))
print("append 7 : ",l)
print("Index 1 : ",l.index(1))
print("pop: ", l.pop())
l.reverse()
print("Reverse: ",l )
l.sort()
print("sort: ", l)

#Output-
[2, 4, 6, 1, 3, 5]
count no. of 5 : 1
append 7 :  [2, 4, 6, 1, 3, 5, 7]
Index 1 :  3
pop:  7
Reverse:  [5, 3, 1, 6, 4, 2]
sort:  [1, 2, 3, 4, 5, 6]

#55 Implement various Tuple methods
#Implement various Tuple methods
t= (1,3,5,8,6,2,5)
x = t.count(5)
print("count no. of 5:",x)
y = t.index(3)
print("index of 3: ",y)

#OUTPUT- 
count no. of 5: 2
index of 3: 1

#56 Implement various Set methods
s = {1,2,8,6,4}
print(s)
s.update({7,5})
print("updating 7,5:",s)
s.add(11)
print("added 11: ", s)
s.remove(11)
print("Remove 11: ",s)
print("length: ", len(s))
print("max: ",max(s))
print("min: ", min(s))
print("sort: ", sorted(s))
s.clear()
print(s)

#OUTPUT - 
{1, 2, 4, 6, 8}
updating 7,5: {1, 2, 4, 5, 6, 7, 8}
added 11:  {1, 2, 4, 5, 6, 7, 8, 11}
Remove 11:  {1, 2, 4, 5, 6, 7, 8}
length:  7
max:  8
min:  1
sort:  [1, 2, 4, 5, 6, 7, 8]
set()

#57 Implement various Dictionary methods
d = {1:"key1",2:"key2",3:"key3",4:"key4"}
print(d)
print(d.get(2))
print(d.items())
print(d.keys())
print(d.values())
d.pop(3)
print("pop: ",d)

#OUTPUT- 
{1: 'key1', 2: 'key2', 3: 'key3', 4: 'key4'}
key2
dict_items([(1, 'key1'), (2, 'key2'), (3, 'key3'), (4, 'key4')])
dict_keys([1, 2, 3, 4])
dict_values(['key1', 'key2', 'key3', 'key4'])
pop:  {1: 'key1', 2: 'key2', 4: 'key4'}

#58 Python Program to make a list of 5 random numbers
import random
rand_list = []
for i in range(0, 5):
	n = random.randint(1,50)
	rand_list.append(n)
	
print(rand_list)

#OUTPUT-
[15, 27, 40, 8, 13]

#59 Python Program to find min, max and average of elements of a list having numeric data
l = [1,5,3,4]
print("Max: ",max(l))
print("Min: ", min(l))
size = len(l)
s = 0
for i in range(0,size):
	s+=l[i]
print("average: ", s/size)

#OUTPUT-
Max:  5
Min:  1
average:  3.25

#60 Python Program to print all even numbers of a list using list comprehension
l = [2,5,6,4,3]
x = [i for i in l if i%2==0]
print(x)

#OUTPUT
[2, 6, 4]

#61 Python Program to find sum of all even numbers and odd numbers separately in a list
l = [2,5,6,4,3]
s_even = 0
s_odd = 0
for i in l:
	if i%2==0:
		s_even += i
	else:
		s_odd +=i

print("Sum of even numbers: ",s_even)
print("Sum of odd number: ", s_odd)

#OUTPUT
Sum of even numbers:  12
Sum of odd number:  8

#62 Python Program that reverses a list using loop.
l = [2,6,4,3]
for i in range(len(l)-1,-1,-1):
	print(l[i], end = " ")

#OUTPUT
3 4 6 2 

#63 Python Program that prompts user to enter an alphabet and then print all the words that starts with that alphabet.
text = input("Enter text: ")
alpha = input("Enter alphabet: ")
words = text.split(" ")
for word in words:
	if word[0] == alpha:
		print(word)

#OUTPUT
Enter text: My name nikhil
Enter alphabet: n
name
nikhil

#64 Python Program to copy the contents of one file into another file
with open('first.text','r') as first:
	with open('second.text','w') as second: 
		for i in first:
			second.write(i)

#OUTPUT - 
first.txt
hi nikhil this side

second.txt
hi nikhil this side

#65 Python Program to count number of vowels in a text file
h = open("first.text")
str1 = h.read()
count = 0
for i in str1:
	if( i=='A' or i=='a' or i=='E' or i=='e' or i == 'I' or i == 'i' or i=='O' or i=='o' or i=='U' or i=='u'):
		count += 1
print("No. of vowel: ", count)

#OUTPUT- 
No. of vowel:  6

#66 Python Program to count number of words in a text file
h = open("first.text")
str1 = h.read()
s = str1.split(" ")
count = 0
for i in s:
	count += 1
print("No. of words: ", count)

#OUTPUT- 
No. of words:  4

#67 Python Program to Implement Sequential search to find an item in the list
def seq_search(x):

	for i in range(0,len(l)):
		if l[i] == x:
			return i
	
	return "Enter valid number"

l = [2,5,6,3,7,1]
x = int(input("Enter Number: "))
print("index of ",x,"is: ",seq_search(x))

#OUTPUT 
Enter Number: 7
index of  7 is:  4

#67 Python Program to Implement Binary search to find an item in the list

def bin_search(arr , low, high, x):
	if high >= low:
		mid = (high + low)//2

		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return bin_search(arr,low,mid-1,x)

		else:
			return bin_search(arr,mid+1,high,x)

	else:
		return -1

l = [1,2,3,5,7]
x = int(input("Enter Number: "))
print("index of ",x,"is: ",bin_search(l,0,len(l)-1,x))

#OUTPUT
Enter Number: 7
index of  7 is:  4

#69 Python Program to sort elements of a list using Selection Sort
def sel_sort(arr):
	for i in range(len(arr)):
		mini = i

		for j in range(i+1,len(arr)):
			if arr[j] < arr[mini]:
				mini = j

		arr[i],arr[mini]= arr[mini], arr[i]

	return arr

l = [2,3,1,6,4,5]
print(sel_sort(l))

#OUTPUT
[1, 2, 3, 4, 5, 6]

#70 Python Program to sort elements of a list using Merge Sort
def merg(left,right):
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i+=1

		else:
			result.append(right[j])
			j+=1

	result += left[i:]
	result += right[j:]

	return result

def merge_sort(l):
	if len(l) <= 1:
		return l
	else:
		mid = int(len(l)/2)
		left = merge_sort(l[:mid])
		right = merge_sort(l[mid:])
		return merg(left,right)

l = [5,3,1,2,4]
print(merge_sort(l))

#OUTPUT:
[1, 2, 3, 4, 5]

#Python Program to handle divide by zero exception
a = 1
b = 0

try:
	c = a/b
	print(c)
except:
	print("Cannot divide by zero")

#OUTPUT:
Cannot divide by zero


