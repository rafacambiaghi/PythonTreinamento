#funções

#def say_hello():
 # print('hello')

#def greeting(name):
 #   print('Hello, 5s' %name)
 #   greeting('Rafael')

def add_num(num1,num2):
 return num1+num2
add_num(4,5)
result = add_num(4,5)
print(result)

#duas strings
print(add_num('one','two'))
#numero primo

def is_prime(num):
    for n in range(2,num):
        if num % n == 0:
         print('Não é primo')
         break
        else:
         print('primo')
is_prime(16)            

#True
#import math

#def is_prime(num):
    #if num % 2 == 0 and num > 2:
     #   return False
    #for i in range(3, int(math.sqrt(num))
   # if num % i == 0:
  #  return False
 #   return True
#is_prime(11)
