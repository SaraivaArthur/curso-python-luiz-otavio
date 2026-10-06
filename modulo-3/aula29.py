numero_str = input('Vou dobrar o número que você digitar: ')

# numero_float = float(numero_str)
# print(f'O dobro de {numero_str} é {numero_float * 2}')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2}')
# else:
#     print('Por favor, digite um número válido.')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')