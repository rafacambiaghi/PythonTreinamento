def fahrenheit(T):
 return (9 / 5) * T + 32
def celsius(T):
 return (5 / 9) * T - 32
temp = [0, 22.5, 40, 100]
F_temps = list(map(fahrenheit, temp))
print(F_temps)

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

print(list(map(lambda x,y:x+y,a,b)))
print(list(map(lambda x,y,z:x+y+z, a,b,c)))
