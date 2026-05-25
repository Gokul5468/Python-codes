s= {10,20,30}
print(s)

st= set([1,2,3,4])
print(st)

# a set cannot have duplicate values
s = {"Geeks", "for", "Geeks"}
print(s)

# values of a set cannot be changed
# s[1] = "Hello"
# print(s) error ->Only add() or remove() can modify a set.
 
s = {"Geeks", "for", 10, 52.7, True}
print(s)

#forzenset() in python--> immutable

f = frozenset(["apple","banana","orange"])
print(f)
# f.add("pappy") # error..
print(f)

#supports
# union ->

a = {2, 4, 5, 6}
b = {4, 6, 7, 8}
c = {7, 8, 9, 10}

print(a.union(b).union(c))
print(a.union(b, c))

#we can use | for shortcut.

#intersection-<>


a = {2, 4, 5, 6}
b = {4, 6, 7, 8}
c = {4, 6, 8}

print(a.intersection(b))
print(a.intersection(b, c))

#symmetric_difference..

a = {1, 2, 3, 4, 5}
b = {6, 7, 3, 9, 4}
print(a.symmetric_difference(b))

a = {2, 4, 5, 6}
b = {4, 6, 7, 8}
print(a.intersection(b))
print(a.symmetric_difference(b))

#differnece-->

a = {10, 20, 30, 40, 80}
b = {100, 30, 80, 40, 60}
print(a.difference(b))
print(b.difference(a))



