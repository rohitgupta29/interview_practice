


# def prime(n):
# 	if num > 1:
# 		for i in range(2, n):
# 			if (n % i) == 0:
# 				print(f'{n} is not prime')
# 				break
# 			else:
# 				print(f"{n} is Prime")
# 				break
# 	else:
# 		print(f"{n} is prime")


# num = 17
# prime(num)



## How to find Factorial of a Number


# def factorial(n):
# 	f = 1
# 	if n < 0:
# 		print("Please enter a positive number.")
# 	elif n == 0:
# 		return 1
# 	else:
		
# 		for i in range(1, n + 1):
# 			f *= i
# 		print(f)

# factorial(5)

## factorial using recusrsion

# def factorial_rec(n):
# 	if (n == 0 or n == 1):
# 		return 1
# 	else:
# 		return n* factorial_rec(n-1)

# print(factorial_rec(5))

# #turnary approach
# def fact_rec2(n):
# 	return 1 if (n==1 or n==0) else n*fact_rec2(n-1)

# print(fact_rec2(5)) 

#Fabinacci Series

def fabbinoci(n):
	n1 = 0
	n2 = 1
	print(n1)
	for i in range(2, n+1):
		sum = (n1 + n2)
		print(sum)
		n1 = n2
		n2 = sum
	return sum

print(fabbinoci(9))

#Sum of elements in an array

# def sum_array(ss):
# 	print(sum(ss))

# sum_array([1,2,3,4,5


#max and min in an array

# def max(arr):
# 	mx = arr[0]
# 	n = len(arr)
# 	for i in range(1, n):
# 		if arr[i] > mx:
# 			mx = arr[i]
# 		else:
# 			return mx
# 	return mx

# print(max([1,2,3,4,11,5]))

#min element

# def min(arr):
# 	min = arr[0]
# 	n = len(arr)
# 	for i in range(1,n):
# 		if arr[i] < min:
# 			min = arr[i]
# 		else:
# 			return min
# 	return min

# a = min([11,2,3,4,5])
# print(a)


## Find Length of a list

# def lenlist(n):		
# 	count = 0
# 	for i in n:
# 		count += 1
# 	return count

# print(lenlist([1,2,3,4,5]))

# Swap first and last element in a list

# def swaplist(n):
# 	temp = n[0]
# 	n[0] = n[-1]
# 	n[-1] = temp
# 	return n

# a = swaplist([1,2,3,45,5])

#using tuple
# def swaplist(n):
# 	get = (n[-1],n[0]) # packing
# 	n[0], n[-1] = get
# 	return n

# a = swaplist([1,2,3,4,5])
# print(a)

# #approach 4  *operand
# # def listswap(n):
# # 	start,*middle,end = n

# # 	n = [end,*middle, start]
# # 	return n
# # print(listswap([1,2,3,4,5]))

# # # Approach 5 ---using pop()
# # def listswap(n):
# # 	first = n.pop(0)
# # 	last = n.pop(-1)
# # 	n.insert(0,last)
# # 	n.append(first) 
# # 	return n

# # print(listswap([1,2,3,4,5]))

# #Swapping based on position

lsit  = ["geeks","for","geeks","geeks","geeks"]
word = "geeks"
n = 3
count = 0

for i in range(0, len(lsit) -1 ):
	if(lsit[i] == word):
		count += 1
		if count == n:
			del lsit[i]
# print(lsit)

# n = [1,2,3,4,5]
# ele = 100
# flag = 0

# for i in n:
# 	if (i == ele):
# 		print("Element Found")
# 		flag = 1
# 		break

# if (flag == 0):
# 	print("Element not found")

#Approach 2: using in Operator

# n = [1,2,3,4,5,6,67]
# ele = 5

# if(ele in n):
# 	print("Element found")
# else:
# 	print("Element not found")

# # #reverse a list
# n = [1,2,3,4]
# print(n[::-1])


# def count(n, x):

# 	count = 0
# 	for i in n:
# 		if(i == x):
# 			count = count + 1
# 	print(count)
# count([1,2,2,2,2,3,4,5,5,6], 2)

# from collections import Counter

# mylist = [1,2,3,4,5,5,3,3,3,3,3,3]
# x = 3
# dic = Counter(mylist)  #{k:v}
# print(dic[3])


#Sum of elements in a list
# def sums(n):
# 	sum = 0
# 	for i in n:
# 		sum += i
# 	print(sum)
# n = [5,10,15,20]
# sums(n)

#Multiply all numbers in the list

# list1 = [3,4,5]
# def prod(n):
# 	pro = 1
# 	for i in list1:
# 		pro *= i
# 	print(pro)
# #approach 2
# import numpy as np
# n = [1,2,3,4]
# print(np.prod(n))


#Largest and smallest number

# def large(n):
# 	sort = n.sort()
# 	min, max = n[0],n[-1]
# 	return min, max

# a = large([1,2,3,4,5])
# print(a)

# n = [1,2,3,4,5,6]
# max = n[0]
# for i in range(len(n)):
# 	if n[i] > max:
# 		n[i] = max
# print(max)

# Find 2nd largest number in a list

mylist = [70,11,20,4,100]

# mylist.sort()
# print(mylist[-2])

# new_list = set(mylist)
# print(new_list)


#Palindrome string

# word = madam

# if word == reverse(word):
# 	print(yes)
# print(no)

# def pdmn(n):
# 	if n == n[::-1]:
# 		return("yes")
# 	return("no")
# print(pdmn('mada'))

## Reverse Words in a String

# st = "welcome to python programming"
# st.split()
# print(" ".join(st.split()[::-1]))

# Find substring presence in a string

# st = "welcome to python Programming"
# sub_st = "python"
# print(st.find(sub_st))
# if (st.find(sub_st) == -1):
# 	print("Not found")
# else:
# 	print("Found")


word = "welcome"
counter = 0
# for i in word:
# 	counter += 1
# print(counter)

# while word[counter:]:
# 	counter = counter+ 1
# print(counter)

# random_str = "X"
# print((random_str).join(word).count(random_str) + 1)

#Check string contains Special Characters

# import re
# n1= "welcome@@2To%%Python**Programming@!!^%%@$"
# n2 = "hello World"
# regex = re.compile('[`~!@#$%^&*()_+=}{":><?]')

# if (regex.search(n2) == None):
# 	print("No Spl characters in String")
# else:
# 	print("Spl Characters there.")

#Check for URL in a String
import re

s = "Im blogger at http://www.pavantestingtools.com/"
s2 = "My Profile: https://pavantestingonline.com/about.html"
s3 = "My Profile: https://pavanonlinetrainings.com/about.html and MyBlog: http://www.pavantestingtools.com/"

url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9][$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',s3)

print(url)
