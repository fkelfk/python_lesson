Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
new file
SyntaxError: invalid syntax

============= RESTART: /Users/junghoonlee/Documents/hello_world.py =============
hello world

============= RESTART: /Users/junghoonlee/Documents/hello_world.py =============
hello world!
for num in [0,1,2]:
    print(num)

    
0
1
2
for num in ['a','b','c']
SyntaxError: expected ':'
for num in ['a','b','c']:
    print(num)

    
a
b
c
color = ['red','white','blue']
print(color)
['red', 'white', 'blue']
for color in color:
    print(color)

    
red
white
blue
blue
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    blue
NameError: name 'blue' is not defined
for color in color:
    print(color, 'eyes')

    
b eyes
l eyes
u eyes
e eyes
colors = ['red','blue','brown')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
colors = ['red','blue','brown']
print(colors)
['red', 'blue', 'brown']
colors.append('black')
print(colors)
['red', 'blue', 'brown', 'black']
for color in colors
SyntaxError: expected ':'
for color in colors:
    print(color, 'eyes')

    
red eyes
blue eyes
brown eyes
black eyes

for y in range(1,11):
    print(3,'x',y,'=','3*y)
          
SyntaxError: unterminated string literal (detected at line 2)
for y in rnage(1,11):
    print(3,'x',y,'=','3*y')

          
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    for y in rnage(1,11):
NameError: name 'rnage' is not defined. Did you mean: 'range'?
for y in range(1,11):
    print(3,'x',y,'=','3*y')

          
3 x 1 = 3*y
3 x 2 = 3*y
3 x 3 = 3*y
3 x 4 = 3*y
3 x 5 = 3*y
3 x 6 = 3*y
3 x 7 = 3*y
3 x 8 = 3*y
3 x 9 = 3*y
3 x 10 = 3*y
for y in range(1,11):
    print(3,'x',y,'=',3*y)

          
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

roses= ['red','red','red]
        
SyntaxError: unterminated string literal (detected at line 1)
roses = ['red','red','red']
        
for i in range(3):
        roses[i] = 'red'
print(roses)
        
SyntaxError: invalid syntax

for i in range(3):
    roses[i] = 'red'
print(roses)
        
SyntaxError: invalid syntax
for i in range(3):
    roses[i] = 'red'

        
print(roses)
        
['red', 'red', 'red']

for i in range(3)
        
SyntaxError: expected ':'
for i in range(3):
    print(i)

        
0
1
2
for i in range(3)
        
SyntaxError: expected ':'
for i in range(3):
    roses[i] = 'white'

        
print(roses)
        
['white', 'white', 'white']

print(roses)
        
['white', 'white', 'white']
