#String are commonly used for text handling and manipulation..

a = "gfg"
b ='gfg'
print(a)
print(b)

#multiple lines
a  = """ i  am gokul
Learning the data science"""
print(a)

# String Slicing-> used for text manipluation and data parsing..

a = "Hello, world"
print(a[0:6]) ## index 6 is not included.

# negative slicing..
a = [5,10,15,20,25]
print(a[-2:])
print(a[-2])


#Reverse a slicing ->
print(a[::-1])

#reverse a string-->
name ="Gokul"
print(name[::-1])
print(name)

print(str("".join((reversed(name)))))

s = "abcdefghijlmno"
print(s[-8:-1:2])

#Retrive all characters.
s = "Hello, world"
print(s[:])
print(s[::])

s = "abcdefghi"
print(s[::2]) # skips every 2 character..
print(s[::3])
print(s[1:8:3])


l = "python"
for char in l:
    print(char)
    print()
print(list(l))

#updation of string.
k = "gokul"
h = "s" +k[1:]
print(h)
g = k.replace("l","uuu")
print(g)

#methods..
#len(),upper(),lower()

#strip()-->trims the removes leading and trailing whitespace from the string
s = "    gfg    "
print(s.strip())

#Repetition-->

s = "Hello "
print(s * 3)

#f- strings()

name = "Gokul"
age = 21;
print(f"my name is: {name}, and is: {age}")
name   = "Rahul"
age    = 25
salary = 45000.5678
# ── WAY 2: .format() method (older but still used) ─────
print("Name: {}, Age: {}".format(name, age))
print("Salary: ₹{:,.2f}".format(salary))
print("Salary: ₹{:,}".format(salary))

 # using format.
t = "my name is {} and i a have done a intership in {}".format("Sarayu","Coditas")
print(t)

s = "geeksforgeeks"
print(s.startswith("for",5)) # at index 5

s = "geeksforgeeks"
print(s.startswith("for",5,8)) # check index btw 5  and 8.


# convert int to string-->

n = 34
s = str(n) #  or s = f"{n}   {}.format(n) , "%s" % n
print(s)

m = repr(n) # most used for debugging.
print(m)

# converting  BYTE OBJECT to String.(with encoding)
bd = b'Python programming'
print(str(bd,encoding='utf-8'))

# Regex Bsics..
import re

# ── Find all numbers in a string ──────────────────────
text = "Salary is ₹45000 and bonus is ₹5000"
numbers = re.findall(r'\d+', text)
print(numbers)   # ['45000', '5000']

# ── Validate email format ─────────────────────────────
email = "rahul@gmail.com"
pattern = r'^[\w]+@[\w]+\.[a-z]{2,4}$'
if re.match(pattern, email):
    print("Valid email")

# ── Extract phone numbers ─────────────────────────────
text = "Call me at 9876543210 or 8765432109"
phones = re.findall(r'\d{10}', text)
print(phones)   # ['9876543210', '8765432109']

# ── Remove special characters ─────────────────────────
messy = "Hello!!! How@are#you???"
clean = re.sub(r'[^a-zA-Z\s]', '', messy)
print(clean)   # "Hello How are you"
# Used in NLP text cleaning!

# ── Split on multiple delimiters ──────────────────────
text = "apple,banana;orange mango"
parts = re.split(r'[,; ]+', text)
print(parts)   # ['apple', 'banana', 'orange', 'mango']

#tab sapce.
print("Name:\tRahul")

print("He said \"python is aswesome\"")

# r"" = raw string — ignores escape characters
# Used heavily for file paths and regex
#path = r"C:\Users\Rahul\new_data\sales.csv"

text = "    Data Science Is Amazing  "
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.swapcase())

messy = "$  45000/-"
clean = messy.replace("$","").replace("/-", "/").replace("4","5").replace(" ","")
print(clean)


#split with limit.
text = "first:second:third:fourth"
print(text.split(":",2))

# join() — opposite of split, combines list into string
words = ['Rahul', 'Sharma']
full_name = " ".join(words)
# "Rahul Sharma"

#zfill -->padding numbers.
emp_id = "45"
print(emp_id.zfill(5))

