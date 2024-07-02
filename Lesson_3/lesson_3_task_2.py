from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Asus","Zenfone 11","+79002003030"))
catalog.append(Smartphone("Note","30i","+79048475167"))
catalog.append(Smartphone("Tecno","Spark Go","+79103181545"))
catalog.append(Smartphone("Xiaomi","14","+792029991254"))
catalog.append(Smartphone("Servo","KING7000","+79090032297"))

for i in catalog:
    print (f"{i.marka} - {i.model}. {i.nomer}")