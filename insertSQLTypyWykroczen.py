from bs4 import BeautifulSoup
import urllib.request
import re
data = '2016-01-11'
count = 0
output = open('insertSQLTypywykroczen.txt', 'w', encoding="utf8")
outputWykroczenie = open('insertSQLWykroczenie.txt', 'w', encoding="utf8")
with open('D:\Dysk Google\Studia\Semestr V\Hurtownie Danych\Hurtowanie Danych - Zadanie 2 - Generator\wykroczenia.txt', 'r+', encoding="utf8") as plik:
    for linia in plik.readlines():
        count = count + 1
        dane = linia.split(' | ')
        opis = ''
        art = ''
        kwota = ''

        for i in dane:
            opis = dane[0]
            art = dane[1]
            kwota = dane[2].replace('\n', '')

        #output.write('INSERT INTO TypWykroczenia (NumerTypuWykroczenia, ArtykulWykroczenia, OpisWykroczenia) VALUES (' +  str(count)  + ', ' + art + ', ' + opis + ');\n')
        output.write('INSERT INTO TypWykroczenia (ArtykulWykroczenia, OpisWykroczenia) VALUES (' + art + ', ' + opis + ');\n')
        #outputWykroczenie.write('INSERT INTO TypWykroczenia (NumerWykroczenia, KwotaMandatu, DataRozpoczeciaObowiazywania, DataZakonczeniaObowiazywania) VALUES (' +
                    # str(count) + ', ' + kwota + ', ' + data + ', ' + 'NULL' + ');\n')
        outputWykroczenie.write(
            'INSERT INTO TypWykroczenia (NumerWykroczenia, KwotaMandatu, DataRozpoczeciaObowiazywania, DataZakonczeniaObowiazywania) VALUES (' +
            str(count) + ', ' + kwota + ', ' + data + ', ' + 'NULL' + ');\n')

outputWykroczenie.close()
output.close()