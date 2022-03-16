Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
clvers = 'clover1', 'clover2', 'clover3'
print(clovers)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(clovers)
NameError: name 'clovers' is not defined. Did you mean: 'clvers'?
clovers = 'clover1', 'clover2', 'clover3'
print(clovers)
('clover1', 'clover2', 'clover3')
alice_blue = (240, 248, 255)
r, g, b = alice_blue
print('R:', r, 'G:', g, 'B:', b)
R: 240 G: 248 B: 255

A = 'mint'
B = 'berry'
print(1:, A, 2:, B)
SyntaxError: invalid syntax
print('1:', A, '2:', B)
1: mint 2: berry
A, B = B, A
print('1:', A, '2:', B)
1: berry 2: mint

my_dict1 = {}
print(my_dict1)
{}
clover = {'age': 27, 'job": 'soldier'}
          
SyntaxError: ':' expected after dictionary key
clover = {'age': 27, 'job': 'soldier'}
          
print(clover)
          
{'age': 27, 'job': 'soldier'}
clover['num'] = 9
          
print(clover)
          
{'age': 27, 'job': 'soldier', 'num': 9}
print(clover['num'])
          
9
clover['num'] = 6
          
print(clover['num'])
          
6
print(clover(get.('num'))
      
SyntaxError: invalid syntax
print(clover.get('num'))
      
6
del clover['age']
      
print(clover)
      
{'job': 'soldier', 'num': 6}


order = {'C': = 'nomal', 'D': = 'spicy'}
      
SyntaxError: invalid syntax
order = {'C': 'nomal', 'D': 'spicy'}
      
print(order)
      
{'C': 'nomal', 'D': 'spicy'}
order['E'] = 'curry'
      
print(order)
      
{'C': 'nomal', 'D': 'spicy', 'E': 'curry'}
order['D'] = 'chinese'
      
print(order)
      
{'C': 'nomal', 'D': 'chinese', 'E': 'curry'}
del order['C']
      
print(order)
      
{'D': 'chinese', 'E': 'curry'}
