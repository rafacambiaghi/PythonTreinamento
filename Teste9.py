#loop for:

l = [1,2,3,4,5,6,7,8,9,10]
for num in l:
    print(num)
#verificar par ou impar:
l = [1,2,3,4,5,6,7,8,9,10]
for num in l:
 if num % 2 == 0:
    print(num)
 else:
     print('Número ímpar')

#loop que soma a lista:
list_sum = 0
for num in l:
 list_sum = list_sum + num
 print(list_sum)
    
#loop de string:

# for letter in 'Esse é um teste de loop com string':
# print(letter)

#loop com tuplas:
tup = (1,2,3,4,5)
for t in tup:
    print(t)
#outro exemplo com tupla(embalando):

l = [(2,4),(6,8),(10,12)]
for tup in l:
    print(tup)

#desembalando:
# for (t1,t2) in l:
# print(t1)

#usando dicionário:
d = {'k1': 1, 'k2':2, 'k3':3}
for item in d:
    print(item)
#iterar através das chaves e valores de um dicionario:
for k,v in d.items():
 print(k)
 print(v)
