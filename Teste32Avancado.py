import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
 print('Searching for "%s" in: \n"%s"'%(pattern,text))
 if re.search(pattern, text):
  print('\n')
  print('Match was found. \n')
 else:
  print('\n')
  print('No Match was found.\n')

pattern = 'term1'

text = 'This is a string with term1, but it does not have the other term.'

match = re.search(pattern,text)
type(match)
print(match.start())
print(match.end())

split_term = '@'
phrase = 'What is the domain name of someone with the email:hello@email.com'
print(re.split(split_term,phrase))

print(re.findall('match', 'test phrase match is in middle'))


def multi_re_find(patterns,phrase):
 for pattern in patterns:
  print('Searching the phrase using the re check: %r'%pattern)
  print(re.findall(pattern, phrase))
  print('\n')
    
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dssss...sdddd'
test_patterns = ['sd*','sd+','sd?','sd{3}','sd{2,3}',]
print(multi_re_find(test_patterns,test_phrase))


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dssss...sdddd'
test_patterns = ['[sd]', 's[sd]+']
print(multi_re_find(test_patterns,test_phrase))

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall('[^abcdefgh]+', test_phrase))

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'
test_patterns=[ '[a-z]+', '[A-Z]+', '[a-zA-Z]+', '[A-Z][a-z]+']
print(multi_re_find(test_patterns,test_phrase))

