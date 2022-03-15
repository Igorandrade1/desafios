


# #forma1
# lista = sorted([12,5,86,3,56,25,95,14,5] + [84,24,63,74,15,7,10])
# print(lista)
# print(len(lista))
#
# #forma2
# lista2 = [len(sorted([12,5,86,3,56,25,95,14,5] + [84,24,63,74,15,7,10]))]
# print(lista2)

#forma3
y = [12,5,86,3,56,25,95,14,5]
x = [84,24,63,74,15,7,10]
z = y + x
print('ordenada em forma crescente:%s, quantidade de elementos: %s'%(sorted(z), len(z)))
