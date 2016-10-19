from faker import Factory
import GeneratorPesel
import GeneratorIDCard

class MandateNumber:
    mandateNumber = 0

    def getMandateNumber(self):
        self.mandateNumber += 1
        return self.mandateNumber


numberOfRecrods = 1000
output = open('insertSQLMandat.txt', 'w', encoding="utf8")
fake = Factory.create('pl_PL')

for record in range(0,numberOfRecrods):
    random.randint(0, 9)

    output.write('INSERT INTO Obywatel (NumerMandatu, KwotaMandatu, TypPlatnosci, ) VALUES (' +  + ', ' + firstName + ', ' + lastName + ', ' + idCardNumber + ', ' + fatherName + ');\n')


output.close()



KwotaMandatu INT,
TypPlatnosci
Data DATETIME ,
Czas

FOREIGN KEY (PESELKaranego) REFERENCES Obywatel(PESEL),
FOREIGN KEY (NumerSluzbowyFunkcjunariusza) REFERENCES Funkcjonariusz(NumerSluzbowy),
FOREIGN KEY (NazwaDzielnicy, Ulica) Miejsce(NazwaDzielnicy, Ulica),
FOREIGN KEY (Wykroczenie) Wykroczenie(NumerWykroczenia)