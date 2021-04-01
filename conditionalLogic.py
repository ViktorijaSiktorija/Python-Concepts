is_old = False
is_licenced = False

if is_old and is_licenced:
    print('vozi')
# elif is_licenced:
    # print('ok')
else:
    print('check')

# Ternarni operator / conditional expresions

is_friend = False
is_user = True
can_message = "message allowed" if is_friend else "not allowed"
print(can_message)

# Short circuting - or
if is_friend or is_user:
    print('drugari')
