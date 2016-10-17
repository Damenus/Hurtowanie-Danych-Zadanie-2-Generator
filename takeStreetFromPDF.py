import re

count = 0
output = open('streetAndDistrict.txt', 'w', encoding="utf8")
with open('D:\Dysk Google\Studia\Semestr V\Hurtownie Danych\Hurtowanie Danych - Zadanie 2 - Generator\listOfStreet.txt', 'r+', encoding="utf8") as plik:
    for linia in plik.readlines():
        count = count + 1
        staraLinia = linia.split(' ')
        #lista = list(set(kolumny))
        lista = list();
        powtorzenie = 0
        for i in reversed(staraLinia):
            for j in lista:
                if(i == j):
                    powtorzenie = 1
                    break
            if(powtorzenie == 0):
                lista.append(i)
            powtorzenie = 0

        for slowo in reversed(lista):
            output.write(slowo + ' ')


print(count)
output.close()
#count = len(open('D:\Dysk Google\Studia\Semestr V\Hurtownie Danych\Hurtowanie Danych - Zadanie 2 - Generator\listOfStreet.txt', 'r+', encoding="utf8").readlines())
#print(count)