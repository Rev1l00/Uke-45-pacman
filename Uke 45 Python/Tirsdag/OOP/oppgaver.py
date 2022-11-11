"""
Oppgave 1

Lag en klasse som representerer en: Hest
Den trenger ikke å ha noen egenskaper
"""

class Horse:
    def __init__(self):
        pass

"""
Oppgave 2

Opprett en kjøretøyklasse med egenskaper
for maks. Hastighet og kjørelengde 
"""

class car:
    def __init__(self, max_speed, max_drivinglength):
        self.max_speed = max_speed
        self.max_drivinglength = max_drivinglength

car_model = car(999, 999)
print(car_model.max_speed, car_model.max_drivinglength)

"""
Oppgave 3

Lag en klasse som representerer en: Datamaskin
Den skal inneholde egenskapene: cpu, ram, gpu, storage
"""

class computer:
    def __init__(self, cpu, ram, gpu, storage):
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.storage = storage

pc = computer("intel", 16, "nvidia", 999)
print(pc.cpu, pc.ram, pc.gpu, pc.storage)
"""
Oppgave 4

Bruk klassen du laget i forrige oppgave
og lag 2 objekter av den.
"""

pc1 = computer("intel", 16, "nvidia", 348)
pc2 = computer("intel", 16, "nvidia", 85)

"""
Oppgave 5

Med de to objektene så er laget så ønsker
jeg å vite hvilken av de som har mest lagring.
"""

if pc1.storage > pc2.storage:
    print("pc1 has more storage than pc2.")
else:
    print("pc2 has more storage than pc1.")