name = 'gokul'
print(name)
age =21
print(age)
print(type(age))

#varible cannot start with number , canot use %, !,and keywords in python
greet = "hi"; print(greet)

age = 23
name = "Gokul"
name = "Seshu"
city = "Anaparthi"
print(age,name,city)

a=b=c = 10
print(a,b,c)

a,b,c=1,2.5,"python"
print(a,b,c)

#share reference-->
x= 5
y = 6

print(id(x))
print(id(y))

k = 5  
print(id(k))

# in above reference are a, b, k.  a and k are same both refers to same address.


name = "Gokul"
name1 = "sarayu"
print(id(name))
print(id(name1))
name = "sarayu"
print(name)
print(id(name)) # garabage collection name is updated to sarayu not gokul


#String interning ..

#above is string interning . But not for large sentences in script based compile.example below..
a= 'my fav color is blue'
print(a)
print(id(a))
b= 'my fav color is blue'
print(b)
print(id(b))

c = 100000
print(id(c))
d = 100000
print(id(d))

