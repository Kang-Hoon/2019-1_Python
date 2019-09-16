Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: /Users/yongmin/Desktop/DanKook/Python/190412_12_lec/190412_5_4장 수업내용.py 
>>> int(100)
100
>>> int("100")
100
>>> price = 1000

>>> print("상품의 가격은 ", price, "원입니다. ")

상품의 가격은  1000 원입니다. 
>>> print("상품의 가격은"+str(price)+"원입니다. ")

상품의 가격은1000원입니다. 
>>> 
>>> print("상품의", a, "개의 가격은 ", price, "원입니다. ")

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print("상품의", a, "개의 가격은 ", price, "원입니다. ")
NameError: name 'a' is not defined
>>> a = 3
>>> print("상품의", a, "개의 가격은 ", price, "원입니다. ")

상품의 3 개의 가격은  1000 원입니다. 
>>> print("상품의"+ str(a)+ "개의 가격은 "str(price)+"원입니다. ")

SyntaxError: invalid syntax
>>> print("상품의"+ str(a)+ "개의 가격은 " +price

	  +"원입니다. ")
Traceback (most recent call last):
  File "<pyshell#10>", line 3, in <module>
    +"원입니다. ")
TypeError: can only concatenate str (not "int") to str
>>> 
