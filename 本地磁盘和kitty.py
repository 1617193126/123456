Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> y = 'localpath C:code\cnkicraws'
>>> import re
>>> re.findall('[a-zA-Z]:\S+',y)
['C:code\\cnkicraws']
>>> y = 'Hello Kitty Hello Hello Kitty Kitty Hello'
>>> re.findall('(?:Hello){2}(?:Kitty ){2}'y)
SyntaxError: invalid syntax
>>> re.findall('(?:Hello ){2}(?:Kitty ){2}'y)
SyntaxError: invalid syntax
>>> re.findall('(?:Hello ){2}(?:Kitty ){2}',y)
['Hello Hello Kitty Kitty ']
>>> 
