print('parte 1:')
from collections import Counter
l = [1,2,2,2,2,2,2,2,3,3,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
print(Counter(l))
print(Counter('aabsbhdsufhdsiduha'))
s = 'How many times does each word show up in this sentence word times each word'
words = s.split()
print(Counter(words))
c = Counter(words)
print(c.most_common(2))

from collections import defaultdict
d = defaultdict(object)
d['one']
for item in d:
 print(item)

d = defaultdict(lambda: 0)
print(d['one'])

print('parte 2:')

print('Normal dictionary:')
d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
 print(k, v)   

from collections import OrderedDict

print('OrderedDict:')

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
 print(k, v)   

from collections import OrderedDict

print('Dictionaries are equal?')
d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'

d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'
print(d1 == d2)


t = (12,13,14)
print(t[0])


from collections import namedtuple

dog = namedtuple('dog', 'age breed name')
sam = dog(age=2, breed='Lab', name='Sammy')
frank = dog(age=2, breed='Sherpad', name='Frankie')
print(sam)
print(sam.age)
print(sam.breed)
print(sam[0])





























































