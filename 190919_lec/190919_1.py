Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 100
>>> id(x)
4439197968
>>> id(x)
4439197968
>>> 이강훈 = 1000
>>> 이강훈
1000
>>> id(이강훈)
4490951888
>>> c = 1000
>>> 이강훈 == c
True
>>> 이강훈 is c
False
>>> id(이강훈)
4490951888
>>> id(c)
4490952176
>>> 
