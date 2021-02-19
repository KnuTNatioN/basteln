# erste mal das ich aus dem kopf mit klassen arbeite...
# ja, ich lerne...

import time
class person:
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
#        Aufgewacht = datetime.now().strftime("%H:%M:%S")
        Aufgewacht = "17:10 Uhr" #noch falsch
        
        print("Hallo, mein Name ist" + self.name + ".")
        print("Ich bin gerade aufgewacht...")
        print("Es ist ",Aufgewacht,"...")
        print("und jetzt?...")
#        what_should_i_do()
        
        
    def arbeitstag():
        print("Aufstehen ...")
        print("Kaffee trinken...")
        print("am Po kratzen..")
        print("Duschen... & Zähne putzen...")
        print("Anziehen..")
        
        
    def feier_abend(Ankunft):
        #Feierabend ausrechnen
        pause = 30 #minuten
        arbeitszeit = 8*60 #8h * 60min = minuten je Arbeitstag
        
        
#    def what_should_i_do():
#        if arbeiten
#            arbeiten()
#        elif nix
#            nichts()
#        elif am handy spielen
#            extra_nichts()
        
someone = person("Sapi Hom", 35)
# weiteres:
# https://www.python-kurs.eu/python3_time_and_date.php