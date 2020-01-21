#Criar dicionário com {}
my_dict = {'key1' : 'value1','key2' : 'value2'}
#chamando valores pela chave
print(my_dict['key2'])
#Dicionario extenso
my_dict = {'key1' : 123,'key2' : [12,23,33], 'key3': ['abacaxi','maçã','maracujá']}
print(my_dict['key3'])
#Chamar itens de uma lista
print(my_dict['key3'][1])
#métodos nos itens
print(my_dict['key3'][1].upper())
my_dict['key1'] = my_dict['key1']+ 123 / 2 + 555.50
print(my_dict['key1'])
#novo dicionario
d={}
d['animal'] = 'dog'
d['answer'] = 42
print(d)

#aninhamento de dicionários

d = {'key1':{'nestkey':{'subnestkey': 'value'}}}
print(d['key1']['nestkey']['subnestkey'])

#métodos de dicionários
d = {'key1':1,'key2':2,'key3':3}
print(d.keys())

#pega todos os valores
print(d.values())

#Método para retornar as tuplas de todos os itens
print(d.items())
