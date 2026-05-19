Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
"Gokul"
'Gokul'
'Gokul'
'Gokul'
2+3
5
"2+3+
SyntaxError: unterminated string literal (detected at line 1)
"2+3'
SyntaxError: unterminated string literal (detected at line 1)
"2+3"
'2+3'
num = 2
num
2
nums = [1,2,3,4,5,6]
nums
[1, 2, 3, 4, 5, 6]
nums[1]
2
nums[0]
1
nums[1:3]
[2, 3]
nums[1:3)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
len(nums)
6
nums[-1]
6
nums[:-3]
[1, 2, 3]
nums[-3]
4
nums[:4]
[1, 2, 3, 4]
nums[4:]
[5, 6]
 names= ["Sarayu","Gokul"]
 
SyntaxError: unexpected indent
names= ["Sarayu","Gokul"]
names
['Sarayu', 'Gokul']
mix = nums + names
mix
[1, 2, 3, 4, 5, 6, 'Sarayu', 'Gokul']
mix = [nums,names]
mix
[[1, 2, 3, 4, 5, 6], ['Sarayu', 'Gokul']]
mix[0]
[1, 2, 3, 4, 5, 6]
mix[0][1]
2
mix[1][0]
'Sarayu'
nums.append[5]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    nums.append[5]
TypeError: 'builtin_function_or_method' object is not subscriptable
nums.append(5)
nums
[1, 2, 3, 4, 5, 6, 5]
nums.append(7)
nums
[1, 2, 3, 4, 5, 6, 5, 7]
set1 = {23,34,56,34,65}










set1
{56, 65, 34, 23}
34 in set1
True
>>> len(set1)
4
>>> typr(set1)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    typr(set1)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> type(set1)
<class 'set'>
>>> set2 = {}
>>> set2
{}
>>> type(set2)
<class 'dict'>
>>> set1 = set("Sarayu")
>>> set3 = set("Gokul")
>>> set1
{'S', 'y', 'a', 'r', 'u'}
>>> set3
{'l', 'o', 'k', 'G', 'u'}
>>> set1-set3
{'r', 'y', 'a', 'S'}
>>> set1+set3
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    set1+set3
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> set4 = set(set1,set3)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    set4 = set(set1,set3)
TypeError: set expected at most 1 argument, got 2
>>> set1|set3
{'l', 'o', 'S', 'y', 'k', 'a', 'G', 'r', 'u'}
>>> set1 & set3
{'u'}
>>> set1 ^ set3
{'l', 'o', 'k', 'G', 'r', 'S', 'y', 'a'}
>>> data = { 0:1,"Gokul":5}
>>> data[2]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    data[2]
KeyError: 2
>>> data["Gokul"]
5
>>> data[0]
1
