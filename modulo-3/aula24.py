# nome = 'Arthur'
# print(nome[2])
# print(nome[-4])

# print('A' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('iva' not in nome)
# print('zero' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'Encontrado {encontrar} em {nome}')
else:
    print(f'Não encontrado {encontrar} em {nome}')