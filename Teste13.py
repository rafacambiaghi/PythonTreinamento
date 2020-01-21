#x = 25
#def printer():
#    x = 50
#print(x)
#print(printer())   

#def local():
# x = 10
# print(x)
# local()

def local():
    a = 100
    print(locals())
local()    
    
#name = 'Este é um nome global'
#def greet():
#    name = 'Sammy'
#def hello():
#  print('Hello' + name)

#  hello()

#  greet()
#  print(name)

var_global = 'Variável global'
print(var_global)
print(globals())



def func(x):
 x = 50
 print('X is', x)
x = 2
print('Change local x to', x)
func(x)
print('x is still', x)

