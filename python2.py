Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hello word")
hello word
x=2
print (x)
2
print(x)
2

===== RESTART: C:/Users/aammr/OneDrive/Documents/latihan python batch 2.py =====
12
hallo
1+2*3
7
1+2*3**2
19
2**2**3
256

===== RESTART: C:/Users/aammr/OneDrive/Documents/latihan python batch 2.py =====
144

Traceback (most recent call last):
  File "C:/Users/aammr/OneDrive/Documents/latihan python batch 2.py", line 6, in <module>
    print(a**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
print("selamat datang di pelatihan python")
selamat datang di pelatihan python
print("selamat datang \ndi pelatihan python")
selamat datang 
di pelatihan python
print("selamat","datang","di","pelatihan python")
selamat datang di pelatihan python
print("masukan sebuah nilai : ",a)
masukan sebuah nilai :  hallo

===== RESTART: C:/Users/aammr/OneDrive/Documents/latihan python batch 2.py =====
144 
Traceback (most recent call last):
  File "C:/Users/aammr/OneDrive/Documents/latihan python batch 2.py", line 6, in <module>
    print(a ** 2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

===== RESTART: C:/Users/aammr/OneDrive/Documents/latihan python batch 2.py =====
144 144
print("selamat","datang di","DTS Pra", sep="-")
selamat-datang di-DTS Pra
print("selamat","datang di","DTS Pra", sep="\n")
selamat
datang di
DTS Pra
print("1")
1
print(1)
1
print(type("1"))
<class 'str'>
print(type(1))
<class 'int'>
a=10
print(type(a))
<class 'int'>
a="10"
print(type(a))
<class 'str'>
print(a+5)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(a+5)
TypeError: can only concatenate str (not "int") to str
print(a)
10
print(type(a))
<class 'str'>
print(int(a)+5)
15
print(type()a)
SyntaxError: invalid syntax
print(type(a))
<class 'str'>
b=1
print(a+b)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(a+b)
TypeError: can only concatenate str (not "int") to str
print(astr(b))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(astr(b))
NameError: name 'astr' is not defined. Did you mean: 'str'?
print(a+str(b))
101
print(0o11)
9
KeyboardInterrupt
print(0o10)
8
_
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    _
NameError: name '_' is not defined
>>> -
SyntaxError: invalid syntax
>>> _
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    _
NameError: name '_' is not defined
>>> print(0x10)
16
>>> print(0b10)
2
>>> a=.5
>>> print(a)
0.5
>>> a=5.
>>> print(a)
5.0
>>> print("hallo\n"*5)
hallo
hallo
hallo
hallo
hallo

>>> a=int(input("masukan nilai"))
masukan nilai
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a=int(input("masukan nilai"))
ValueError: invalid literal for int() with base 10: ''
>>> a=str(input("masukan nilai"))
masukan nilai
>>> print(a)

>>> print(type(a))
<class 'str'>
