from bs4 import BeautifulSoup
import urllib.request
import re
import random

def generateFirstDay():
    data = '2016-01-01'
    count = 0
    listOfID = []
    output = open('insertSQLTypywykroczen.txt', 'w', encoding="utf8")
    outputWykroczenie = open('insertSQLWykroczenie.txt', 'w', encoding="utf8")
    with open('D:\Dysk Google\Studia\Semestr V\Hurtownie Danych\Hurtowanie Danych - Zadanie 2 - Generator\wykroczenia.txt', 'r+', encoding="utf8") as plik:
        for linia in plik.readlines():
            count = count + 1
            listOfID.append(count)
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
                'INSERT INTO Wykroczenie (NumerWykroczenia, KwotaMandatu, DataRozpoczeciaObowiazywania, DataZakonczeniaObowiazywania) VALUES (' +
                str(count) + ', ' + kwota + ', ' + data + ', ' + 'NULL' + ');\n')

    outputWykroczenie.close()
    output.close()

    return listOfID

def changeInLaw(listOfID, date):
    changingLaw = random.choice(listOfID)
    newAmount = random.randrange(50,1000,50)

    output = open('insertSQLTypywykroczenTIME2.txt', 'a', encoding="utf8")
    output.write('UPDATE Wykroczenia SET DataZakonczeniaObowiazywania=' + date + ' WHERE ID=' + str(changingLaw) + ';')
    output.write( 'INSERT INTO Wykroczenie (NumerWykroczenia, KwotaMandatu, DataRozpoczeciaObowiazywania, DataZakonczeniaObowiazywania) VALUES (' +
                  str(changingLaw) + ', ' + str(newAmount) + ', ' + date + ', ' + 'NULL' + ');\n')
    output.close()

    return listOfID