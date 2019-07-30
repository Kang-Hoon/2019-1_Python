Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=1
>>> b=2
>>> c=3
>>> d=4
>>> print(a+b)
3
>>> print('c'+'d')
cd
>>> 
=============================== RESTART: Shell ===============================
>>> a=1
>>> b-2
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b-2
NameError: name 'b' is not defined
>>> b=2
>>> c='3'
>>> d='4'
>>> print(a+b)
3
>>> print('c'+'d')
cd
>>> print(c+d)
34
>>> $money = 100
SyntaxError: invalid syntax
>>> #라라라
>>> _name = "psh"
>>> std_name = "psh"
>>> _7up = 100
>>> _7up
100
>>> import keyword
>>> keyword.keywordlist
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    keyword.keywordlist
AttributeError: module 'keyword' has no attribute 'keywordlist'
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> False false
SyntaxError: invalid syntax
>>> False f_alse
SyntaxError: invalid syntax
>>> False
False
>>> True
True
>>> true
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> False None True and as assert async await break class continue def del elif else except finally for from global del continue if import
SyntaxError: invalid syntax
>>> len(keyword)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    len(keyword)
TypeError: object of type 'module' has no len()
>>> ken("aaaaaaaaaaa")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ken("aaaaaaaaaaa")
NameError: name 'ken' is not defined
>>> len("aaaaaa")
6
>>> len("10000000)
	
SyntaxError: EOL while scanning string literal
>>> len("1090909u00")
	
10
>>> len("1")
	
1
>>> len(keyword.kwlist)
	
35
>>> len([100, 1, 2, 3])
	
4
>>> len(turtle.Turtle)
	
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    len(turtle.Turtle)
NameError: name 'turtle' is not defined
>>> import turtle
	
>>> turtle.Turtle()
	
<turtle.Turtle object at 0x1064a33c8>
>>> t1.turtle
	
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    t1.turtle
NameError: name 't1' is not defined
>>> t1 = turtle
	
>>> t1.fd(100)
	
>>> x2 = 1000
	
>>> x1 = x2
	
>>> x1
	
1000
>>> x2
	
1000
>>> n1, n2 = 100, 100
	
>>> n1
	
100
n
>>> n2
	
100
>>> 2
	
2
>>> 1000
	
1000
>>> x2=2000
	
>>> x1
	
1000
>>> x2
	
2000
>>> 
len(shape.turtle)
	
Traceback (most recent call last):
  File "<pyshell#55>", line 2, in <module>
    len(shape.turtle)
NameError: name 'shape' is not defined
>>> 
=== RESTART: /Users/yongmin/Desktop/DanKook/Python/190405_lec/190405_1.py ===
Traceback (most recent call last):
  File "/Users/yongmin/Desktop/DanKook/Python/190405_lec/190405_1.py", line 6, in <module>
    t.shape("turtle")
NameError: name 't' is not defined
>>> 
=== RESTART: /Users/yongmin/Desktop/DanKook/Python/190405_lec/190405_1.py ===
Traceback (most recent call last):
  File "/Users/yongmin/Desktop/DanKook/Python/190405_lec/190405_1.py", line 6, in <module>
    t.shape("turtle")
NameError: name 't' is not defined
>>> 
=== RESTART: /Users/yongmin/Desktop/DanKook/Python/190405_lec/190405_1.py ===
>>> 
=== RESTART: /Users/yongmin/Desktop/DanKook/Python/190405_lec/190405_1.py ===
>>> 
=== RESTART: /Users/yongmin/Desktop/DanKook/Python/190405_lec/190405_1.py ===
>>> === RESTART: /Users/yongmin/Desktop/DanKook/Python/190405_lec/190405_1.py ===
	
SyntaxError: invalid syntax
>>> 
	
>>> a
	
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
	
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> name = input()
	
LeeKangHoon
>>> name
	
'LeeKangHoon'
>>> 
	
>>> LastName = input("너의 성은?")
	
너의 성은?이
>>> FirstName = input("너의 이름은? ")
	
너의 이름은? 강훈
>>> print(LastName+FirstName)
	
이강훈
>>> countcandy = input("How many candies are there? ")
	
How many candies are there? 1000
>>> type(countcandy)
	
<class 'str'>
>>> int(countcandy)
	
1000
>>> countcandy = int(input("How many candies are there? ")

		     )
	
How many candies are there? 10000
>>> countcandy
	
10000
>>> countcandy * 10
	
100000
>>> heigt = float(input("How tall are you? "))
	
How tall are you? 173.5
>>> heigt
	
173.5
>>> height = float(input("How tall are you? "))
	
How tall are you? 173.5
>>> height
	
173.5
>>> 
