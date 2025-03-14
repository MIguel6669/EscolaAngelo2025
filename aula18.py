#funções

#len() => tamanho
lista=[1,2,3,4,5,6,7,8,9,0]
print(len (lista))
print(lista[2:len(lista)])
print(lista[len(lista)-1])

#max() => valor maximo
print(max(lista))

#min() => menor valor
print(min(lista))

#sum()=> soma todos os elementos numericos
print(sum(lista))

tamanho= len(lista)
print(tamanho)

lista.insert(2 ,99)
print(lista)

while 7 in lista:
 lista.remove(7)
 print(lista)
