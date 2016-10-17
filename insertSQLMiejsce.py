from faker import Factory

#INSERT INTO Miejsce(NazwaDzielnicy, Ulica) VALUES ();

fake = Factory.create('pl_PL')
output = open('insertSQLMiejsce.txt', 'w', encoding="utf8")
with open('streetAndDistrict', 'r+', encoding='utf8') as input:
    for record in input.readlines():
        firstName = fake.first_name()
        lastName = fake.last_name()
        output.write('INSERT INTO Miejsce(NazwaDzielnicy, Ulica) VALUES (' + firstName + ', ' + lastName + ');\n')


input().close()
output.close()