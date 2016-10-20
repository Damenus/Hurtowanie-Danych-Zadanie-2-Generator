from faker import Factory
import GeneratorPesel
import GeneratorIDCard

def generateFirst100Man():
    numberOfRecrods = 1000

    #INSERT INTO Obywatel (PESEL, Imie, Nazwisko, NumerDowoduTozsamosci, ImieOjca) VALUES ();

    output = open('insertSQLObywatel.sql', 'w', encoding="utf8")
    fake = Factory.create('pl_PL')
    listOfPesel = []

    for record in range(0,numberOfRecrods):
        pesel = GeneratorPesel.pesel()
        listOfPesel.append(pesel)
        firstName = fake.first_name()
        lastName = fake.last_name()
        idCardNumber = GeneratorIDCard.idCard()
        fatherName = fake.first_name_male()
        output.write('INSERT INTO Obywatel (PESEL, Imie, Nazwisko, NumerDowoduTozsamosci, ImieOjca) VALUES (' + pesel + ', ' + firstName + ', ' + lastName + ', ' + idCardNumber + ', ' + fatherName + ');\n')

    output.close()

    return listOfPesel

def generateObywatel():
    output = open('insertSQLObywatel.sql', 'a', encoding="utf8")
    fake = Factory.create('pl_PL')

    pesel = GeneratorPesel.pesel()
    firstName = fake.first_name()
    lastName = fake.last_name()
    idCardNumber = GeneratorIDCard.idCard()
    fatherName = fake.first_name_male()
    output.write('INSERT INTO Obywatel (PESEL, Imie, Nazwisko, NumerDowoduTozsamosci, ImieOjca) VALUES (' + pesel + ', ' + firstName + ', ' + lastName + ', ' + idCardNumber + ', ' + fatherName + ');\n')

    output.close()

    return pesel