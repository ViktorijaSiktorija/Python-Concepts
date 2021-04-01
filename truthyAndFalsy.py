password = '123'  # bool('hello') -> truthy
username = 'pera'  # bool(5) -> truthy

if password and username:
    print('vozi')
# elif is_licenced:
    # print('ok')
else:
    print('check')

# automatski konvertuje vrednosti u bool
# 0 i "" falsy, none

x = 'hello'[0]
print(x)
