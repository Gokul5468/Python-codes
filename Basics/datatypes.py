"""
name = "Gokul"
print(type(name))
print(type(name) == str)
print(isinstance(name,str))

#casting-->
number = "20"
age = int(number)
print(age)

#input-->
value = input("Enter the value: " )
print(value)
print(type(value))
value1 = int(input("enter the value: "))
print(value1)
print(type(value1))

floatnum = float(input("enter the number: "))
print(floatnum)

x,y = input("enter the value: ").split()
print(x)
print(y)


#Taking lists as input
a = list(input("List1 : "))
b = list(input("list2 :"))
for i in b:
    a.append(i)
print("final list is:" ,a)
"""
# a = 2
# b = 3
# c= complex(2,3)
# print(c)


#String Split()

# li = input("Enter the elements by space:" ).split()
# print(li)

#using loop 
"""
a=[]
n = int(input("Enter the number of elements:" ))
for i in range(n):
   # element = input("Enter the element: " + str(i+1) + ":")
    element = input(f"Enter the element: {i+1}: ")
    a.append(element)
print(a)
"""

"""
s ="one,two,three"
words = s.split(",") #separater ->(,)
print(words)

text = "Hello  world"
print(text.split())

word = 'geeks,for,geeks,hello'
print(word.split(", ", 1))

#using List-->
s = "Gokul"
name = list(s)
print(name)

name1 = [*s] #unpackig operator.
print(name1)

#using loop

s ="hello"
a = []
for i in s:
    a.append(i)
print(a)

"""
r = range(10) # 0 to 9 
print(r)
l = list(r)
print(l)
s = set(r)
print(s)

# using range..
print(list(range(2,11,2))) # we will print even number.

# using loop.
even = []
for i in range(11):
    if(i % 2 == 0):
        even.append(i);
print(even)


a,b,c = 1,2.5,3
print(a)
print(b)
print(c)

#input-->

char = input("Enter the character:" )[0]
print(char)














