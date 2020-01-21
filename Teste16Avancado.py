lst = [x for x in 'word']
print(lst)


lst = [x**2 for x in range(0,11)]
print(lst)

lst = [x for x in range(100) if x % 5 == 0]
lst = [x for x in range(100) if x % 3 == 0]
lst = [x for x in range(100) if x % 15 == 0]
print(lst)

#for x in range(1,100):
#    if x % 15 == 0:
#        print("FizzBuzz")
#    elif x % 3 == 0:
#        print("Fizz")
#    elif x % 5 == 0:
#        print("Buzz")
#    else:
#        print(x)

celsius = [0,10,2-.1,34.5]
fahrenheit = [((9 / 5) * temp + 32)for temp in celsius]
print(fahrenheit)

lst = [x**2 for x in[x**2 for x in range(11)]]
print(lst)
