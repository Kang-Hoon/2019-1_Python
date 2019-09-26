Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
state = 'mississippi'
>>> state
'mississippi'
>>> state.count('s')
4
>>> state.count('ssi')
2
>>> state.count('s',5)
2
>>> state.count('s',1,7)
4
>>> state.count('s',1,3)
1
>>> state.count('s',1,4)
2
>>> # .find() : 찾아서 첫번째 인덱스를 알려준다
>>> mse = ["이강훈", "박소연", "박근남"]
>>> mse[0]
'이강훈'
>>> mse[0] + mse[1] + mse[2]
'이강훈박소연박근남'
>>> dash = -
SyntaxError: invalid syntax
>>> dash = '-'
>>> dash.join(mse)
'이강훈-박소연-박근남'
>>> '-'.join(mse)
'이강훈-박소연-박근남'
>>> '#'.join(mse)
'이강훈#박소연#박근남'
>>> 
#스플릿 함수 많이 사용한다
>>> # .split()
>>> mse.split()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    mse.split()
AttributeError: 'list' object has no attribute 'split'
>>> mse = ' '.join(mse)
>>> mse
'이강훈 박소연 박근남'
>>> mse.split()
['이강훈', '박소연', '박근남']
>>> mse = mse.split()
>>> mse
['이강훈', '박소연', '박근남']
>>> 
