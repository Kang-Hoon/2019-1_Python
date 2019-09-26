Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 1000
>>> b = 1000
>>> c = 1000
>>> id(a)
4487675312
>>> id(b)
4487675344
>>> id(c)
4487675376
>>> id (a)
4487675312
>>> id (b)
4487675344
>>> id (c)
4487675376
>>> st = "KangHoon"
>>> st[1]
'a'
>>> st[0]
'K'
>>> st[5]
'o'
>>> st[4]
'H'
>>> st.count(o)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    st.count(o)
NameError: name 'o' is not defined
>>> st.count("o")
2
>>> st.count('l')
0
>>> sizeof(st)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    sizeof(st)
NameError: name 'sizeof' is not defined
>>> sizeof()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    sizeof()
NameError: name 'sizeof' is not defined
>>> getsizeof(st)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    getsizeof(st)
NameError: name 'getsizeof' is not defined
>>> sys.getsizeof(st)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    sys.getsizeof(st)
NameError: name 'sys' is not defined
>>> st[0:8]
'KangHoon'
>>> st[0:]
'KangHoon'
>>> st[:7]
'KangHoo'
>>> st[0:7]
'KangHoo'
>>> st[-8:-1]
'KangHoo'
>>> st[-8:]
'KangHoon'
>>> st[-8:0]
''
>>> st[4:-1]
'Hoo'
>>> st[2:-3]
'ngH'
>>> s = " I am still hungry - Hiddink "
>>> 'I' in s
True
>>> are in s
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    are in s
NameError: name 'are' is not defined
>>> 'are' in s
False
>>> 'is' in s
False
>>> 'am' in s
True
>>> s[0:10:3]
' asl'
>>> 
=============================== RESTART: Shell ===============================
>>> name = "lee kanghoon"
>>> name.upper()
'LEE KANGHOON'
>>> name
'lee kanghoon'
>>> name = name.upper()
>>> name
'LEE KANGHOON'
>>> name.lower()
'lee kanghoon'
\
>>> name = name.lower()
>>> name
'lee kanghoon'
>>> name.isalpha()
False
>>> name1 = 'lee'
>>> name1
'lee'
>>> name1.isalpha()
True
>>> name2 = '3179'
>>> name2
'3179'
>>> name2.isdigit()
True
>>> name.isspace()
False
>>> 
