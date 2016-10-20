CREATE TABLE Obywatel
(
PESEL CHAR(11) PRIMARY KEY,
Imie VARCHAR(20) NOT NULL,
Nazwisko VARCHAR(30) NOT NULL,
NumerDowoduTozsamosci VARCHAR(9) NOT NULL,
ImieOjca VARCHAR(20) NOT NULL
);

INSERT INTO Obywatel (PESEL, Imie, Nazwisko, NumerDowoduTozsamosci, ImieOjca) VALUES ();

CREATE TABLE Miejsce
(
NazwaDzielnicy VARCHAR(50) NOT NULL,
Ulica VARCHAR(50) NOT NULL,
PRIMARY KEY(NazwaDzielnicy, Ulica)
);

INSERT INTO Miejsce(NazwaDzielnicy, Ulica) VALUES ();

CREATE TABLE Funkcjonariusz
(
NumerSluzbowy INT PRIMARY KEY,
Imie VARCHAR(20) NOT NULL,
Nazwisko VARCHAR(30) NOT NULL
);

INSERT INTO Funkcjonariusz (NumerSluzbowy, Imie, Nazwisko) VALUES ();

CREATE TABLE TypWykroczenia
(
NumerTypuWykroczenia INTEGER IDENTITY(1,1) PRIMARY KEY,
ArtykulWykroczenia VARCHAR(100) NOT NULL,
OpisWykroczenia VARCHAR(1000) NOT NULL
);

INSERT INTO TypWykroczenia (ArtykulWykroczenia, OpisWykroczenia) VALUES ();

CREATE TABLE Wykroczenie
(
ID IDENTITY(1,1) PRIMARY KEY,
KwotaMandatu INTEGER NOT NULL,
DataRozpoczeciaObowiazywania Date NOT NULL,
DataZakonczeniaObowiazywania Date,
FOREIGN KEY (NumerWykroczenia) REFERENCES TypWykroczenia(NumerTypuWykroczenia) NOT NULL,
);

INSERT INTO Wykroczenie (KwotaMandatu, DataRozpoczeciaObowiazywania, DataZakonczeniaObowiazywania) VALUES ();

CREATE TABLE Mandat
(
NumerMandatu INT IDENTITY(1,1) PRIMARY KEY,
TypPlatnosci NOT NULL,
Data DATETIME,
FOREIGN KEY (PESELKaranego) REFERENCES Obywatel(PESEL) NOT NULL,
FOREIGN KEY (NumerSluzbowyFunkcjunariusza) REFERENCES Funkcjonariusz(NumerSluzbowy) NOT NULL,
FOREIGN KEY (NazwaDzielnicy, Ulica) Miejsce(NazwaDzielnicy, Ulica) NOT NULL,
FOREIGN KEY (Wykroczenie) Wykroczenie(ID) NOT NULL
);

INSERT INTO Mandat (TypPlatnosci, Data, PESELKaranego, NumerSluzbowyFunkcjunariusza, NazwaDzielnicy, Ulica, Wykroczenie) VALUES ();