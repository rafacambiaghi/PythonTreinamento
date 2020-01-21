#Tuplas
t = (1,2,3)
print(len(t))
#Variação tipos de dados
t = ('one', 2)
print(t)
#indexação
print(t[0])
#corte de dados
print(t[-1])
#Métodos basicos da Tupla
#use .index() com o valor de parâmetro para retornar o indice do mesmo
print(t.index('one'))
#use .count() com o valor de parâmetro para retornar o indice do mesmo
print(t.count('one'))
#imutabilidade
#t[0] = 'change'
#t.append('nope')
#As tuplas não podem crescer, as tuplas são imutáveis.Esses dois comandos se
#executados irá acarretar em erro.
