vowels = ['a','e','i','o','u']
word = raw_input()
for vowel in vowels:
  word = word.replace('%sp%s'%(vowel, vowel), vowel)
print word
