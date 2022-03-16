Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
for num in range(1-4)
SyntaxError: expected ':'
for num in range(1-4):
    print('hello', num)

    
for num in range(1,4):
    print('hello', num)

    
hello 1
hello 2
hello 3

num = 0
while num < 3:
    print('hello',num)
    num = num+1

    
hello 0
hello 1
hello 2

num = 0
while count < 5:
    count = count+1
    print(count, 'round.')
print('end')
SyntaxError: invalid syntax

print('end')
end
num = 0
while count < 5:
    count = count+1
    print(count, 'round.')

    
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    while count < 5:
NameError: name 'count' is not defined. Did you mean: 'round'?

count = 0
while count < 5
SyntaxError: expected ':'
count = 0
while count < 5:
    count = count+1
    print(count, 'round.")
          
SyntaxError: unterminated string literal (detected at line 3)
count = 0
          

count = 0
          
while count < 5:
    count = count+1
    print(count, 'round')
print('end')
SyntaxError: invalid syntax

count = 0
while count < 5:
    count = count + 1
    print(count, 'round')
print('end')
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax

count = 0
while count < 5
SyntaxError: expected ':'
count = 0
while count < 5:
    count = count + 1
    print(count, 'round')
else:
    print('end')

    
1 round
2 round
3 round
4 round
5 round
end

count = 0
while count < 5:
    count = count + 1
    print(count, 'round')
    if count == 5
    
SyntaxError: expected ':'
count = 0
while count < 5:
    count = count + 1
    print(count, 'round')
    if count == 5:
        print('end')

        
1 round
2 round
3 round
4 round
5 round
end
end
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    end
NameError: name 'end' is not defined

name = input('what your name?')
what your name? atesi
print(name, 'hello')
 atesi hello

answer = ''
while answer != 'seoul':
    answer = input('where is the capital of south korea')
print('correct')
SyntaxError: invalid syntax

answer = ''
while answer != 'seoul':
    answer = input('where is the capital of south korea')
    print('correct')
    
SyntaxError: multiple statements found while compiling a single statement

answer = ''
while answer != 'seoul':
    answer = input( 'where is the capital of south korea')
print('correct')
SyntaxError: multiple statements found while compiling a single statement

answer = ''
while answer != 'seoul':
    answer = input('where is the capital of south korea? ')
print('correct')
SyntaxError: multiple statements found while compiling a single statement

answer = ''
while answer != 'seoul':
    answer = input('where is the capital of south korea')
 print('correct')
 
SyntaxError: multiple statements found while compiling a single statement

answer = ''
while answer != 'seoul':
    answer = input('where is the capital of south korea')
print('correct')
SyntaxError: multiple statements found while compiling a single statement

while True:
    answer = input('which is the capital of UK: Seoul,Paris or London?')
    if answer == 'London':
        print('correct')
        break
    elif answer == 'Paris':
        print('France')
    elif answer == 'seoul':
        print('Korea')
    else:
        print('choose from the options')

        
which is the capital of UK: Seoul,Paris or London?seoul
Korea
which is the capital of UK: Seoul,Paris or London?paris
choose from the options
which is the capital of UK: Seoul,Paris or London?Paris
France
which is the capital of UK: Seoul,Paris or London?London
correct
