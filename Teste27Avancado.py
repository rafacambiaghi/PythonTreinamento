def hello(name='Rafael'):
    
 def greet():
  return '\t This is inside the greet() function'
 def welcome():
  return '\t This is inside the welcome() function'

 if name == 'Rafael':
  return greet
 else:
  return welcome
x = hello()
print(x())

def hello():
 return 'Hi José!'

def other(func):
 print('outro código poderia vir aqui')
 print(func())
 print(other(hello))
