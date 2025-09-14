str1= "Hello World!"
print(len(str1))
str2="hello woRld"
print(str2.title())
print(str1.lower())
print(str1.upper())
str3="Hello World! Hello Hello"
print(str3.count('Hello',12,24))
print(str3.count('Hello'))
print(str3.find('Hello',10,20))
print(str3.find('Hello',15,25))
print(str3.find('Hello'))
print(str3.find('Hee'))
# find e frst index ta de, start r stop dewa na thakle 0 theke start hobe
# print(str3.index('Hee'))
print(str1.endswith('World!'))
print(str1.endswith('!'))
print(str1.endswith('ide'))
print(str1.startswith('He'))
print(str1.startswith('Hee'))
print(str1.isalnum())
str4= "HelloWorld2"
print(str4.isalnum())
str5= ' \n \t \r'
print(str5.isspace())
str6= 'Hello    \n'
print(str6.isspace())
str7= "hello world!"
print(str7.islower())
str8= 'hello 1234'
print(str8.islower())
str9= 'heloo ??'
print(str9.islower())
str10= '1234'
print(str10.islower())
str11= 'Hello World'
print(str11.islower())
str12= 'HELLO'
print(str12.isupper())
print(str1.istitle())
print(str2.istitle())
str13= '  Hello World!  '
print(str13.lstrip())
str14= '  Hello World!  '
print(str14.rstrip())
str15= '   Hello World   '
print(str15.strip())
print(str1.replace('o','*'))
print(str1.replace('World','Country'))
str16= '-'
print(str16.join(str1))
str17= 'I am a man'
print(str17.partition('a'))
print(str17.partition('are'))
print(str17.split())
print(str17.split('a'))