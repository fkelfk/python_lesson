Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def A():
    print('hello world!')

    
A()
hello world!

def add(a,b):
    return a + b
print(add(2,3))
SyntaxError: invalid syntax
print(add(2,3))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(add(2,3))
NameError: name 'add' is not defined
def add(a,b):
    return a + b

print(add(2,3))
5

def add(a,b)
SyntaxError: expected ':'
def add(a,b):
    return a+b, a*b

print(add(a,b))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(add(a,b))
NameError: name 'a' is not defined. Did you mean: 'A'?
print(add(a, b))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(add(a, b))
NameError: name 'a' is not defined. Did you mean: 'A'?
print(add(2, 3))
(5, 6)

def judge(name):
    print(name, '1 gilty')
    print(name, '2 gilty')

    
judge('heart')
heart 1 gilty
heart 2 gilty
judge('clover')
clover 1 gilty
clover 2 gilty
judge('heart', 'clover')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    judge('heart', 'clover')
TypeError: judge() takes 1 positional argument but 2 were given
judge('heart', 'clover')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    judge('heart', 'clover')
TypeError: judge() takes 1 positional argument but 2 were given

import random
animals = ['cat', 'duck', 'bird']
print(random.choice(amimals))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(random.choice(amimals))
NameError: name 'amimals' is not defined. Did you mean: 'animals'?
print(random.choice(animals))
cat
print(random.choice(animals))
duck
print(random.choice(animals))
bird
print(random.choice(animals))

duck
print(random.choice(animals))

cat
print(random.choice(animals))

cat
print(random.choice(animals))

cat
print(random.choice(animals))

cat
print(random.choice(animals))

cat
print(random.choice(animals))

duck
print(random.choice(animals))

cat
print(random.choice(animals))

cat
print(random.choice(animals))

duck
print(random.choice(animals))

cat
print(random.choice(animals))

bird
print(random.choice(animals))

duck
print(random.choice(animals))

duck
print(random.choice(animals))

duck
print(random.choice(animals))

cat
print(random.choice(animals))

cat
v
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    v
NameError: name 'v' is not defined
print(random.choice(animals))

bird
print(random.choice(animals))

cat
print(random.choice(animals))

duck
print(random.choice(animals))

cat

print(random.sample(animals, 2))
['cat', 'bird']
print(random.sample(animals, 2))
['duck', 'cat']
print(random.randint(1,3))
3
print(random.randint(1.9))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(random.randint(1.9))
TypeError: Random.randint() missing 1 required positional argument: 'b'
print(random.randint(1,9))
9
print(random,randint(1,9))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(random,randint(1,9))
NameError: name 'randint' is not defined
print(random.randint(1,9))

5
print(random.randint(1,9))

8
import random
cards = ['heart', 'clover', 'spade']
chosen_card = random.choice(cards)
print(chosen_card, 'gilty!')
heart gilty!
heart gilty!
SyntaxError: invalid syntax
import random
cards = ['heart', 'clover', 'spade']
chosen_card = random.choice(cards)
print(chosen_card, 'guilty!')

SyntaxError: multiple statements found while compiling a single statement
import random
cards = ['heart', 'clover', 'spade']
chosen_card = random.choice(cards)
print(chosen_card, 'guilty!')
spade guilty!

import random
cards = ['heart', 'clover', 'spade']
chosen_cards = random.choice(cards)
print(chosen_cards, 'guilty')
heart guilty

print('있는 바퀴를 다시 만들지 마라')
있는 바퀴를 다시 만들지 마라

num1 = 9
num2 = 2
print(rum1 // rum2)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    print(rum1 // rum2)
NameError: name 'rum1' is not defined. Did you mean: 'num1'?
print(num1 // num2)
4
print(num1 % num2)
1
print(num1 % num2)
1
print(8/2)
4.0
print(2*2)
4

nums = [1, 3]
nums.del[1]
SyntaxError: invalid syntax
del nums[1]
print(nums)
[1]
nums.append(3)

del.nums[1]
SyntaxError: invalid syntax
del nums[1]
print(nums)
[1]
nums =[1, 3]
nums[1] = 2
print(nums)
[1, 2]
nums.append(3)
nums.append(4)
print(nums)
[1, 2, 3, 4]
nums = [1, 2, 3, 4, 5]
print(nums[2:5])
[3, 4, 5]
print(nums[2:4])
[3, 4]
print(nums[1:3])
[2, 3]

fruits = ['멜론', '거봉', '레몬']
print(fruits)
['멜론', '거봉', '레몬']
fruits.sort()

print(fruits)
['거봉', '레몬', '멜론']

for num un [3, 1, 2]
SyntaxError: invalid syntax
for num in [3, 1, 2]
SyntaxError: expected ':'

for num in [3, 1, 2]:
    print(num)

    
3
1
2
for num in range(2)
SyntaxError: expected ':'
for num in range(2);
SyntaxError: expected ':'
for num in range(2):
    print(num)

    
0
1

star = *
SyntaxError: invalid syntax
star = ['*']
for stars in star
SyntaxError: expected ':'
for stars in star:
    print stars
    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
for num in range(1, 4):
    print('*' * num)

    
*
**
***

for num in range(1, 4):
    print('*')

    
*
*
*
for num im range(1, 4):
    
SyntaxError: invalid syntax
for num in range(1, 4):
    print('*' * num)

    
*
**
***

stars = [2, 1, 3]
for num in stars
SyntaxError: expected ':'
for num in stars:
    print('*' * num)

    
**
*
***

total = 0
card_nums = [1, 3, 6, 7]
for num in card_nums:
    total = total + num
print(total / 4)
SyntaxError: invalid syntax

input_number = -9
if input_number < 0:
    absolute_value = input_number * -1
else:
    absolute_value = input_number * 1
print(absolute_value)
SyntaxError: invalid syntax
year = 2016
if year % 400 == 0
SyntaxError: expected ':'
if year % 400 == 0:
    print(year, '년은 윤년입니다.')
elif year % 4 == 0 and year % 100 !=0:
    print(year, '년은 윤년입니다.')
else:
    print(year, '년은 윤년입니다.')

    
2016 년은 윤년입니다.
count = 0
while count <= 5:
    if count % 2 != 0:
        print(count)
    count = count + 1

    
1
3
5
total = 0
count = 1
while count <= 5:
    total = total + count
    count = count +1
print('total', total)
SyntaxError: invalid syntax

count = 3
while count == 0
SyntaxError: expected ':'
while count == 0:
    print(count)
    count = count + 1

    
count = 3
while count == 0:
    print(count)
    count = count +1

    
count = 3
while count == 0:
    pirnt(count)
    count = count - 1

    
count = 3
while count > 0:
    print(count)
    count = count - 1

    
3
2
1

num = 1
while Ture:
    if num > 3
    
SyntaxError: expected ':'
num = 1
while Ture:
    if num > 3:
        break
    print(num)
    num = num + 1

    
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    while Ture:
NameError: name 'Ture' is not defined

num = 1
while True:
    if num > 3:
        break
    print(num)
    num = num + 1

    
1
2
3

price = 0
while price != -1:
    price = int(input('가격을 입력하세요 (종료:-1):'))
    if price > 10000:
        print('너무 비싸요.')
    elif price > 5000
    
SyntaxError: expected ':'

while True:
    number = int(input('2 이상의 정수를 입력하세요 (종료:-1): '))
    if number == -1:
        break
    count = 2
    is_prime = True
    while count < number:
        if number % count == 0:
            is_prime = False
            break
        count = count + 1
    if is_prime:
        print(number, '은(는) 소수입니다.')
    else:
        print(number, '은(는) 소수가 아닙니다.')

        
2 이상의 정수를 입력하세요 (종료:-1): 13
13 은(는) 소수입니다.
2 이상의 정수를 입력하세요 (종료:-1): -1

num = [1, 2, 3,]
print(num)
[1, 2, 3]
nums = 1, 2, 3
print(nums)
(1, 2, 3)
