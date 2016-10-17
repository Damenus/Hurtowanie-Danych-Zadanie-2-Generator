from faker import Factory
import PeselGen

numberOfRecrods = 1000

#INSERT INTO Obywatel (PESEL, Imie, Nazwisko, NumerDowoduTozsamosci, ImieOjca) VALUES ();

output = open('insertSQLObywatel.txt', 'w', encoding="utf8")
fake = Factory.create('pl_PL')

for record in range(0,numberOfRecrods):
    firstName = fake.first_name()
    lastName = fake.last_name()
    output.write('INSERT INTO Obywatel (PESEL, Imie, Nazwisko, NumerDowoduTozsamosci, ImieOjca) VALUES (' + firstName + ', ' + lastName + ');\n')


output.close()