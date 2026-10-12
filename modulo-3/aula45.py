# texto = iter('Arthur') #.__iter__()
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

texto = 'Arthur'
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

# for letra in texto:
#     print(letra)