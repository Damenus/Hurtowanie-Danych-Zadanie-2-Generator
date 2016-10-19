from faker import Factory
import PESELGenerator
import IDCardGenerator

numberOfRecrods = 1000

#INSERT INTO Obywatel (PESEL, Imie, Nazwisko, NumerDowoduTozsamosci, ImieOjca) VALUES ();

output = open('insertSQLObywatel.txt', 'w', encoding="utf8")
fake = Factory.create('pl_PL')

for record in range(0,numberOfRecrods):
    pesel = PESELGenerator.pesel()
    firstName = fake.first_name()
    lastName = fake.last_name()
    idCardNumber = IDCardGenerator.idCard()
    fatherName = fake.first_name_male()
    output.write('INSERT INTO Obywatel (PESEL, Imie, Nazwisko, NumerDowoduTozsamosci, ImieOjca) VALUES (' + pesel + ', ' + firstName + ', ' + lastName + ', ' + idCardNumber + ', ' + fatherName + ');\n')


output.close()