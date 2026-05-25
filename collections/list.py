#list = [] or list()

#list() --> Constructor

a = list("python")
print(a)
print(type(a))

tuple = (10,20,50,40)
res1 = list(tuple)
print(res1)

print(res1.count(20))


tuple = (10,20,30,40)
res = list(tuple)
print(res)


d = {"A":10,"B":50,"C":30} # key value pair.
res = list(d) # it only store the keys.
print(res)

# greet = input("Enter the elements:")
# res = list(greet)
# print(res)

#list with repeated elements..
a = [2] * 5
print(a)

#indexing-->

a = [10,20,"gfg",True]
print(a[2])
print(a[-1]) # last index..


#Methodes in list..

#append--> at last.
a= [1,2]
a.append(3)
# a.append(6,7) takes only one argument.
print(a)

#insert(index, value)
a.insert(1, 10)
print(a)

#extend() -->extends multiple value to end of the list.
a.extend([4,5])
print(a)

#update-->
a[0] = 100
print(a)

#remove --> remove the element..

a.remove(2)
print(a)

#pop ->  remove element at index o last element if no index mentioned.
a.pop()
print(a)


# del --> delete an element at specified index..
del a[2]
print(a)

# clear -> remove all items..
a.clear()
print(a) # prints empty list.

scores = [85, 92, 78, 65, 88]

scores.sort()
# [65, 78, 85, 88, 92] — ascending, changes the original list

scores.sort(reverse=True)
# [92, 88, 85, 78, 65] — descending

# If you don't want to change the original:
sorted_scores = sorted(scores)   # returns new list, original unchanged

#iterating over lists..
a = ["Apple","Banana","Oragne"]
for i in a:
    print(i)

# nested list.
b = [[1,2],[3,4]]
print(b)
print(b[0])
print(b[1][0])

#list comprehension-->way to create new lists by applying an expression to each item in an existing iterable like a list, tuple or range. It helps to write clean, readable and efficient code compared to traditional loops.

c = [2,4,6,8]
res = [val**2 for val in c ]
print(res)

d = [1,2,3,4,5]
res = [val for val in d if val % 2 == 0]
print(res)

# creating list from a range

f = [i for i in range(1,10)]
print(f)

# using nested loops:
c = [[x,y] for x in range(3) for y in range(3)]
print(c)


#nested if esle -->
e = [1,2,3,4,5]
res = ['Divisible by 2' if val % 2 ==0 else 'Divisible by 3' if val % 3 ==0 else 'other' for val in e]
print(res)

#nested list..
# Always ensure all rows have the same number of columns
employee = [["Sarayu",21,"cse",7.6],
            ["gokul",21,"cse",7.3]]
print(employee)
print(employee[1][0])



