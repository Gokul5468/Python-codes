data = {"name":"Gokul","age":12}
print(data)

print(data["name"])

print(data.get("age"))

d = {'a':1,'b':2,'c':3}
print(d)
d_copy = dict(d)
print(d_copy)
d_shallow = d
d_shallow['a'] = 10
print(d)
d_copy['b'] = 20
print(d_copy)
print(d)

# removing Dictionary--

# del =
d = {"a":1,"b" :2}
del d["a"]
#del ["b"] --> error
print(d)

#pop
d = {"a":1,"b" :2}
val=d.pop("a")
print(val)
print(d)

d = {"a": 1,"b":2}
print(d.popitem())  #-> removes and returns the last inserted key-value pair

#clear->
d = {"a": 1, "b": 2}
d.clear()
print(d)


d = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
print(d.keys())

d = {'A':10,'B':20}
k= d.keys()
d['c'] = 30
print(k)

#dict.items() -> return the all key value pair.
#d.items() returns a view object containing tuples of key and value pairs from d.
d = {"A":"Python","B":"java"}
print(d.items())

# nested dict->

students = {}
students["students1"] = {"name ":"Gokul","age": 21,"Grade": "A"}
students["students2"] = {"name ":"SarAYU","age": 19,"Grade": "A+"}
students["students3"] = {"name ":"Maha","age": 45,"Grade": "B"}
print(students)