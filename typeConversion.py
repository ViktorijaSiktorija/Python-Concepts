# str - pretvara u string

print(type(str(100)))

a = str(100)
b = int(a) #prevara u int
c = type(b)
print(c)


pitanje = 'Kad si rodjen?'
birth_year = 1992
age = 2021 - int(birth_year)
print('Imam {0} godina'.format(age))

# Vezba
username = 'vika'
password = 'jasezovemviktorija'
pass_length = len(password)
password_new = password.replace(password, '*' * len(password))
#Drugo resenje: tajni_pas = '*' * password_length
print('hi {0}, your password {1} is {2} letters long'.format(username,password_new,pass_length))