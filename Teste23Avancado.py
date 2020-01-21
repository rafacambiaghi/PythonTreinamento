#def even_check(num):
# if num % 2 == 0:
#  return True
lst = [1, 4, 9, 16, 25]
#print(list(filter(even_check,lista1)))

print(list(filter(lambda x: x % 2 == 0, lst)))
