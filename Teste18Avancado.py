#def square(num):
#    result = num**2
#    return result
#print(square(2))

#def square(num):
#    return  num**2
#print(square(2))

#def square(num): return num**2
#print(square(2))

#lambda num: num**2

square= lambda num: num**2
print(square(2))

even = lambda x: x % 2 == 0
print(even(3))
print(even(4))

first = lambda s: s[0]
print(first('Hello'))

rev = lambda s: s[::-1]
print(rev('Hello'))

adder = lambda x,y: x + y
print(adder(2,3))
