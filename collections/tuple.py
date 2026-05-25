tup = ()
print(tup)

print(tuple("Gokul"))

tup = (5,"Gokukl",3.5,[1,3,4])
print(tup)

tup =(23)  # this is int not tuple.
tup =(34,)
print(type(tup)) # tup


a,b,c=("Geeks" ,"For","Geeks")
print(a,b,c)

# * used to geab a multiple items into list.
tup = [1,2,3,4,5]
a,*b,c = tup
print(a)
print(b) # gether the elements into list.
print(c)

# reverse function()..
name ="Sarayu"
print(tuple(reversed(name)))
print(str("".join((reversed(name)))))


#methodes--> count,index
score = (56,34,5,6,345,34,66)
print(score.count(34))

print(score.index(34))



# enumerate() returns tuples — you unpack them constantly
names = ["Rahul", "Priya", "Amit"]
for index, name in enumerate(names):   # (0,'Rahul'), (1,'Priya')...
    print(f"{index}: {name}")

# items() on dictionary returns tuples
salary_dict = {"Rahul": 45000, "Priya": 38000}
for name, salary in salary_dict.items():   # ('Rahul',45000)...
    print(f"{name} earns ₹{salary:,}")

# zip() returns tuples
names   = ["Rahul", "Priya", "Amit"]
salaries = [45000, 38000, 62000]
for name, salary in zip(names, salaries):  # ('Rahul',45000)...
    print(f"{name}: ₹{salary:,}")

# Define a named tuple 
from  collections import namedtuple;
Employee = namedtuple("Employee", ["name", "age", "dept", "salary"])

# Create instances
emp1 = Employee("Rahul", 25, "IT", 45000)
emp2 = Employee("Priya", 28, "HR", 38000)

# Access by NAME — much more readable!
print(emp1.name)    # "Rahul"
print(emp1.salary)  # 45000
print(emp2.dept)    # "HR"

# Use * to handle unknown length
coords=(12,34,56)
first, *rest = coords
print(first)   
print(rest)    