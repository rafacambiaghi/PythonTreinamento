#mexendo com strings
#Imprimindo uma string:
print('Hello World')

#Use /n para inserir uma nova linha:
print('pule\n a linha')

#Comprimento de uma string:
print(len('Este é o comprimento da string'))

#Criar objeto
#Define s como uma string:
s = 'Hello World'
#Printa o objeto:
print(s)

#Mostra o primeiro elemento
print(s[0])

#Retorna todos o elementos a partir do elemento de indice 1
print(s[:4])

#última letra
print(s[-1])

#multiplique se
print(s*10)

#Coloca toda string em caixa alta
print(s.upper())

#Coloca toda string em caixa baixa
print(s.lower())

#divide uma string nos espaços em branco
print(s.split())

#não inclui elemento que foi dividido
print(s.split('W'))

#pega tudo menos a última letra
print(s[:-1])
#espaçamentos de 2 em 2
print(s[::2])
#Escreve de trás para frente
print(s[::-1])


# ======//======
#% para formatar strings em suas instruções de impressão
print('Qual a primeira instrução de string que aprendemos? %s' %(s))

#numero flutuante:
print('números com pontos flutuantes: %1.2f' %(13.144))

#métodos de formato de conversão
print('Here is a number: %s. Here is a string: %s' %(123.1, 'hi'))
print('Here is a number: %r. Here is a string: %r' %(123.1, 'hi'))

#formatação multipla
print('First: %s, Second: %1.2f, Third: %r' %('hi',3.14,22))

#usando método  string.format()
print('This is a string with an {p}'.format(p='insert'))
print('One:{p}, Two:{p}, Three:{p}'.format(p='Hi!'))
print('Object 1:{a}, Object 2:{b}, Object 3: {c}'.format(a=1,b='Two', c=12.3))


