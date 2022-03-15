# #FORMA1
# print(['JFAZLFD AZFFLRAZKF FSAAAZZZFLFALFAZAAZZKF'.replace('AZ','')])


#forma 2
tem = True
frase = ['JFAZLFD', 'AZFFLRAZKF', 'FSAAAZZZFLFALFAZAAZZKF']
contador = 0
while True:
    for c in range(0, len(frase)):
        if 'AZ' in frase[c]:
            print("tem")
            frase[c] = frase[c].replace('AZ', '')
            contador += 1

        else:
            print('nao')
            tem = False

    for c in range(0, len(frase)):
        if 'AZ' in frase[c]:
            tem = True
        else:
            tem = False

    if not tem:
        break

print('Frases Analisadas',contador)