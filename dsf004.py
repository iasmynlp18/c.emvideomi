n = input('Digite algo:')
print(type(n))
print(f'é alfabetico?{n.isalpha()}')
print(f'é alfanumerico?{n.isalnum()}')
print(f'só tem espaços?{n.isspace()}')
print(f'é numérico?{n.isnumeric()}')
print(f'está apenas em letras minúsculas?{n.islower()}')
print(f'está apenas em letras maiúsculas?{n.isupper()}')
print(f'pode ser impressa?{n.isprintable()}')