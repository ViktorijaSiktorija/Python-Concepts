import re
# regex101, generate code
# r - raw string
pattern = re.compile(r"([a-zA-Z]).(a)")
# [a-zA-Z] - sve izmedju a i z
# . bilo sta
# i trazimo a
string = 'ja se zovem viktorija'

a = pattern.search(string)
print(a.group(1))  # i
print(a.group(2))  # a

# ^ pocetak stringa
regex = re.compile(r"^cao")
test_str = "caokakosi "
b = regex.search(test_str)
print(b)
