s = 'hello world'
print(s.capitalize())
print(s.upper())
print(s.lower())
print('contagem:')
print(s.count('o'))
print('localização:')
print(s.find('o'))

print('\n' 'Formatação:')
print(s.center(20,'z'))
#print('hello\hi'.expandtabs()) - converte \t para tabulações
s = 'hello'
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isspace())
print(s.isupper())
print('\n''Endswith() método que faz verificação booleana em s[-1]')
print(s.endswith('o'))      
print('\n''Métodos embutidos:')
print(s.split('e'))
print(s.partition('e'))
print(s)
