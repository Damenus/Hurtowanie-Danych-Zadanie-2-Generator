from faker import Factory

#INSERT INTO Miejsce(NazwaDzielnicy, Ulica) VALUES ();

def generateMiejsca():
    districtAndStreetNameList = []
    fake = Factory.create('pl_PL')
    output = open('insertSQLMiejsce.txt', 'w', encoding="utf8")
    with open('streetAndDistrict — corect version edited in Netepad++.txt', 'r+', encoding='utf8') as input:
        for record in input.readlines():
            streetName = ""
            districtName = ""
            districtNameRevesed = ""
            kolumns = record.split(' ')

            while(kolumns[-1].isupper()):
                districtNameWithSlashN = kolumns[-1]
                districtNameRevesed = districtNameRevesed + ' ' + districtNameWithSlashN.replace('\n', '')
                del kolumns[-1]
            districtNameRevesedSplit = districtNameRevesed.split(' ')
            districtNameList = reversed(districtNameRevesedSplit)

            for word in districtNameList:
                districtName = districtName + ' ' + word

            for word in kolumns:
                streetName = streetName + ' ' + word

            districtAndStreetNameList.append((districtName,streetName))
            output.write('INSERT INTO Miejsce(NazwaDzielnicy, Ulica) VALUES (' + districtName + ', ' + streetName + ');\n')


    input.close()
    output.close()

    return districtAndStreetNameList