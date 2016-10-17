import re

int = 0

with open('D:\Dysk Google\Studia\Semestr V\Hurtownie Danych\Hurtowanie Danych - Zadanie 2 - Generator\listOfStreet.txt', 'r+', encoding="utf8") as plik:
    for linia in plik.readlines():
        int = int + 1

print(int)

count = len(open('D:\Dysk Google\Studia\Semestr V\Hurtownie Danych\Hurtowanie Danych - Zadanie 2 - Generator\listOfStreet.txt', 'r+', encoding="utf8").readlines())
print(count)