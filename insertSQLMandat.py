from faker import Factory
import GeneratorPesel
import GeneratorIDCard
import random
import datetime
import insertSQLObywatel
import insertSQLMiejsce
import insertSQLTypyWykroczen
import get_badge_numbers


NUMBER_OF_RECORDS = 1000


fake = Factory.create('pl_PL')
listaDate = []

for record in range(0,NUMBER_OF_RECORDS):
    newDate = fake.date_time_between_dates(datetime.date(2016,1,1), datetime.date(2016,6,1), tzinfo=None)
    listaDate.append(newDate)
listaDate.sort()

insertSQLTypyWykroczen.generateOficers('police_officers_t1')

listOfPesel = insertSQLObywatel.generateFirst100Man()

listOfPlace = insertSQLMiejsce.generateMiejsca()

listOfWykroczenia = insertSQLTypyWykroczen.generateFirstDay()

listOfPaymantType = ['kredytowany','gotówkowy','zaoczny']


output = open('insertSQLMandat.sql', 'w', encoding="utf8")
outputBULK = open('insertSQLMandatBULK.sql', 'w', encoding="utf8")


for record in range(0,NUMBER_OF_RECORDS):
    if (random.randrange(0, 100) < 30):
        pesel = insertSQLObywatel.generateObywatel()
        listOfPesel.append(pesel)
    else:
        pesel = random.choice(listOfPesel)

    payment = random.choice(listOfPaymantType)

    law = random.choice(listOfWykroczenia)

    data = listaDate[record]

    place = random.choice(listOfPlace)

    officersList = get_badge_numbers.get_badge_numbers("police_officers_t1",True)
    officerData = random.choice(officersList)
    officer = officerData[0]

    pl1 = place[0]

    output.write('INSERT INTO Mandat (TypPlatnosci, Data, PESELKaranego, NumerSluzbowyFunkcjunariusza, NazwaDzielnicy, Ulica, Wykroczenie) VALUES (' +
                 payment + ', ' + str(data) + ', ' + str(pesel) + ', ' + officer + ', ' + place[0] + ', ' + place[1] + ',' + str(law) + ');\n')
    outputBULK.write( payment + ',' + str(data) + ',' + str(pesel) + ',' + officer + ', ' + place[0] + ',' + place[1] + ',' + str(law) + '\n')

outputBULK.close()
output.close()


def newMonth(numberOfRecordInNewMounth,nameFileOficer):
    listaDateNewMonth = []

    insertSQLTypyWykroczen.changeInLaw(listOfWykroczenia,'2016-06-01')

    for record in range(0, numberOfRecordInNewMounth):
        newDate = fake.date_time_between_dates(datetime.date(2016, 6, 1), datetime.date(2016, 7, 1), tzinfo=None)
        listaDateNewMonth.append(newDate)
    listaDateNewMonth.sort()


    output2 = open('insertSQLMandat2.sql', 'a', encoding="utf8")
    output2BULK = open('insertSQLMandat2BULK.sql', 'a', encoding="utf8")

    for record in range(0,numberOfRecordInNewMounth):
        if (random.randrange(0, 100) < 30):
            pesel = insertSQLObywatel.generateObywatel()
            listOfPesel.append(pesel)
        else:
            pesle = random.choice(listOfPesel)

        payment = random.choice(listOfPaymantType)

        law = random.choice(listOfWykroczenia)

        data = listaDateNewMonth[record]

        place = random.choice(listOfPlace)

        officersList = get_badge_numbers.get_badge_numbers(nameFileOficer, True)
        officerData = random.choice(officersList)
        officer = officerData[0]

        output2.write('INSERT INTO Mandat (TypPlatnosci, Data, PESELKaranego, NumerSluzbowyFunkcjunariusza, NazwaDzielnicy, Ulica, Wykroczenie) VALUES (' +
                     payment + ', ' + str(data) + ', '  +  str(pesle) + ', ' + officer + ', ' + place[0] + ', ' + place[1] + ', ' + str(law) + ');\n')
        output2BULK.write( payment + ',' + str(data) + ','  +  str(pesle) + ',' + officer + ', ' + place[0] + ',' + place[1] + ',' + str(law) + '\n')


    output2BULK.close()
    output2.close()

newMonth(100, 'police_officers_t1')