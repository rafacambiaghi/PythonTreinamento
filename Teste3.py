#Listas

#Atribui uma lista a uma variável
my_list = [1,2,3]
my_list = ['string',23,100.232,'list']
len(my_list)

#indexação e corte
my_list = ['one', 'two', 'three',4,5]
#pega o elemento de indice 0
print(my_list[0])
#pega o indice 1 e tudo depois
print(my_list[1:])
#pega tudo até o elemento de inidice 3
print(my_list[:3])
#concatenação
print(my_list + ['new item'])
#lista
print(my_list)
#reatribuição
my_list = my_list + ['new item']
print(my_list)
#dobrar a lista
print(my_list*2)


# ===========//=============

#Cria a lista
l = [1,2,3]
#Mostra a lista
print(l)
#Acresentar
l.append('append me!')
print(l)
#Retirar o item de indice 0 permanentemente
l.pop(0)
print(l)
#Atribui o elemento retirado
popped_item = l.pop()
print(popped_item)
#mostra a lista restante
print(l)
#nova lista
new_list = ['a','e','x','b','c']
print(new_list)
#Reverter a ordem da lista
new_list.reverse()
print(new_list)
#Classifica a lista(neste caso ordem alfabética
new_list.sort()
print(new_list)
#Matriz
lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = [7,8,9]
matriz = [lst_1, lst_2, lst_3]
print(matriz)
#Pega o primeiro item no objeto na matriz
print(matriz[0])
#Pega o primeiro item do primeiro item no objeto na matriz
print(matriz[0][0])
