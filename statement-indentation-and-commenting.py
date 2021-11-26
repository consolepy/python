#Backslash: the escape character.
aa = 1 + 2 + 3 + \
     4 + 5 + 6 + \
     7 + 8 + 9

#You can also group with () [] or {}.
ab = (1 + 2 + 3 +
      4 + 5 + 6 +
      7 + 8 + 9)

#Works the same for lists and dictionaries.
rgbcolors = ['red',
          'blue',
          'green']

definitions = ['red':"255,0,0",
               'blue':"0,255,0",
               'green':"0,0,255"]

#You can also use semicolons.
a = 1; b = 2; c = 3

#You can use two or four spaces of indentation.
for i in range(1,11):
    print(i)
    if i == 5:
        break
        
#Indentation can be ignored in line continuation, but it's always a good idea to indent.
if True:
    print('Hello')
    a = 5
    
#and

if True: print('Hello'); a = 5
  
#are valid, but the first style are clearer.

#These are different ways of commenting:

#Hello

#Long long
#long long
#long sentence

"""Woo hoo hoo
hoo hoo hoo
hoo hoo hoo"""
