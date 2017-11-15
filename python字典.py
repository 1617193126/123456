Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = {'LGY':1617193126}
>>> dict1
{'LGY': 1617193126}
>>> dict1['LGY']
1617193126
>>>  users = {
    'A':{
    'first':'yu',
    'last':'lei',
    'location':'hs',
    },
    'B':{
    'first':'liu',
    'last':'wei',
    'location':'hs',    
    },
}
 
  File "<pyshell#3>", line 2
    users = {
    ^
IndentationError: unexpected indent
>>>  users = {
    'A':{
	    'first':'yu',
	    'last':'lei',
	    'location':'hs',
	    },
    'B':{
	    'first':'liu',
	    'last':'wei',
	    'location':'hs',
	    },}
 
  File "<pyshell#4>", line 2
    users = {
    ^
IndentationError: unexpected indent
>>>   users = {
    'A':{
	    'first':'yu',
	    'last':'lei',
	    'location':'hs',
	    },
    'B':{
	    'first':'liu',
	    'last':'wei',
	    'location':'hs',
	    },
    
  File "<pyshell#5>", line 2
    users = {
    ^
IndentationError: unexpected indent
>>>   users = {
    'A':{
	    'first':'yu',
	    'last':'lei',
	    'location':'hs',
	    },
    'B':{
	    'first':'liu',
	    'last':'wei',
	    'location':'hs',
	    },}
  
  File "<pyshell#6>", line 2
    users = {
    ^
IndentationError: unexpected indent
>>> users = {
	'A':{
	    'first':'yu',
	    'last':'lei',
	    'location':'hs',
	    },
	'B':{
	    'first':'liu',
	    'last':'wei',
	    'location':'hs',
	    },}
>>> 
>>> 
>>> 
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))

	
userid£ºA
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
userid£ºB
userinfo:{'last': 'wei', 'location': 'hs', 'first': 'liu'}
>>> dict = {'Name': 'Zara', 'Age': 7}
>>> print "Value : %s" % dict.keys()
Value : ['Age', 'Name']
>>> print "Key : %s" % dict.keys()
Key : ['Age', 'Name']
>>> for key in dick.keys():
	print key

	

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for key in dick.keys():
NameError: name 'dick' is not defined
>>> for key in dick.keys():
	print key

	

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    for key in dick.keys():
NameError: name 'dick' is not defined
>>>  for key in dick.keys():print key
 
  File "<pyshell#21>", line 2
    for key in dick.keys():print key
    ^
IndentationError: unexpected indent
>>> for key in dick.keys():
	print key

	

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    for key in dick.keys():
NameError: name 'dick' is not defined
>>> for key in dict.keys():print key

Age
Name
>>> for key in dict.keys():print dict[key]

7
Zara
>>> 
