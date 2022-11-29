import re

regexSub = re.compile(r'apple')
str1 = regexSub.sub('TOMATO','we love to eat apple, fresh apple in themorning is my favorite dessert')
print(str1)
regex = re.compile(r'apple (\w)\w*')
mo = regex.search('We just love apple A')
print(mo.group())
str1 = regex.sub(r'\1XXX','We just love apple banana')
print(str1)