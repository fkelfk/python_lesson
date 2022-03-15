Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
if true:
    print('true')

    
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    if true:
NameError: name 'true' is not defined. Did you mean: 'True'?
if True:
    print('true')

    
true
if False:
    print('true')

    
score = 90
if score > 80:
    print('pass')

    
pass
if score < 80:
    print('pass')

    
if score < 80:
    print('pass')
else:
    print('fail')

    
fail
if score < 95:
    print('pass')
else:
    print('fail')

    
pass
if score < 95:
    print('pass')
else:
    print('fail')

    
pass
if score >= 90:
    print('pass')
else:
    print('fail')

    
pass
group_A = ['A','B','c','D']
A = [80]
B = [85]
C = [90]
D = [95]

if group_A >= 90:
    print('pass')
else:
    print('fail')

    
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    if group_A >= 90:
TypeError: '>=' not supported between instances of 'list' and 'int'
print group_A
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(group_A)
['A', 'B', 'c', 'D']

print('A')
A
A= 80
A = 80
print(A)
80
print(B)
[85]
A = 80
B = 85
C = 90
D = 95

if group_A >= 90:
    print('pass')
else:
    print('fail')

    
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    if group_A >= 90:
TypeError: '>=' not supported between instances of 'list' and 'int'
for grades in group_A
SyntaxError: expected ':'
for grades in group_A:
    if group_A >= 90:
        print('pass')
    else:
        print('fail')

        
Traceback (most recent call last):
  File "<pyshell#71>", line 2, in <module>
    if group_A >= 90:
TypeError: '>=' not supported between instances of 'list' and 'int'
for grades in A:
    if A >= 90:
        print('pass')
    else:
        print('fail')

        
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    for grades in A:
TypeError: 'int' object is not iterable
total price = 0
SyntaxError: invalid syntax
total_price = 0
ages = [22, 21, 17, 32, 4, 28, 19, 8]
ages = [22, 21, 17, 32, 4, 28, 19, 8]
for age in ages:
    if age >= 20:
        total_price = total_price + 8000
    elif age >= 10:
        total_price = total_price + 5000
    else:
        total_price = total_price + 2500

        
print('total_price')
total_price

print(total_price)
47000

math = 80
science = 91

if math >= 80 and science >= 90:
    print('pass')

    
pass
pass
for 점수 in group_A:
    if 점수 >= 80:
        print('pass')

        
Traceback (most recent call last):
  File "<pyshell#105>", line 2, in <module>
    if 점수 >= 80:
TypeError: '>=' not supported between instances of 'str' and 'int'
print(group_A)
['A', 'B', 'c', 'D']
class1 = [A,B,C,D]
print(class1)
[80, 85, 90, 95]

for 점수 in class1:
    if 점수 >= 80:
        print('pass')

        
pass
pass
pass
pass
for 점수 in class1:
    if 점수 >= 90:
        print([] 'pass')
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?

for 점수 in class1:
    if 점수 >= 90:
        print(점수, 'pass')

        
90 pass
95 pass
for data in class1:
    if data >= 90:
        print(class1, 'pass')

        
[80, 85, 90, 95] pass
[80, 85, 90, 95] pass
