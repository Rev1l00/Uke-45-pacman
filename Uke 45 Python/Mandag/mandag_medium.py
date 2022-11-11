''''
Oppgave 1
Opprett en klasse 'bil' med følgende egenskaper:
1.- motor  ##
2.- antall_seter
3.- farge
4.- speed
5.- max_speed
6.- dimensjon_dekk (størrelse)
7.- drivstoff
8.- dimensjon_bil
9.- konsum
10.- distance_vision
i tillegg må du implementere følgende metoder:
## lag egne variabler som påvirker egenskaper 
weather_condition()
## været påvirker mange egenskaper f.eks: konsum, max_speed, distance_vision
## lag egne variabler som påvirker egenskaper 
daylight()
## megden av lys påvirker max_speed og andre egenskaper
Hurry_up()
## Speed påvirker distnace_vision, konsum osv.
'''

# Definerer klassen "bil" og alt den skal inneholde
class bil():
    def __init__(self, motor, antall_seter, farge, speed, max_speed, dimensjon_dekk, drivstoff, dimensjon_bil, konsum, distance_vision, weather_condition, speed_up):
        self.motor = motor
        self.antall_seter = antall_seter
        self.farge = farge
        self.speed = speed
        self.max_speed = max_speed
        self.dimensjon_dekk = dimensjon_dekk
        self.drivstoff = drivstoff
        self.dimensjon_bil = dimensjon_bil
        self.konsum = konsum
        self.distance_vision = distance_vision
        self.weather_condition = weather_condition
        self.speed_up = speed_up

# Definerer oppskriften til bil i en variabel som heter car
car = bil("Motor", 5, "Rød", 90, 200, 60, 40, 10, 35, 120, input("Snør det, Regner det eller er det sol ute?: "), input("Vill du kjøre raskt?: "))

# Bestemmer hva som skal skje vis det snør eller regner
def weather_condition():
    if car.weather_condition == "Snør":
        car.konsum += 10
        car.max_speed -= 15
        car.distance_vision -= 20
    elif car.weather_condition == "Regner":
        car.konsum += 7
        car.max_speed -= 5
        car.distance_vision -= 10

# Bestemmer hva som skal skje hvis det er sol
def daylight():
    car.max_speed += 3

# Bestemmer hva som skal skje hvis bilen skal kjøre fort
def hurry_up():
    car.max_speed += 30
    car.speed += 40
    car.konsum += 20
    car.drivstoff -= 7

# Skjekker om det er sol og så caller funksjonen "daylight"
if car.weather_condition == "sol":
    daylight()

# Skjekker om bilen skal kjøre fort og kaller funksjonen "hurry_up"
if car.speed_up == "ja":
    hurry_up()

# Kaller funksjonen "weather_condition"
weather_condition()

# Printer alt som bilen inneholder
print( )
print(car.motor)
print(car.antall_seter)
print(car.farge)
print(car.speed)
print(car.max_speed)
print(car.dimensjon_dekk)
print(car.drivstoff)
print(car.dimensjon_bil)
print(car.konsum)
print(car.distance_vision)
print( )

'''
Oppgave 2
opprett en klasse motorsykkel som har følgende egenskaper:
1.- speed
2.- max_speed
3.- motorstørrelse
4.- konsum
i tillegg må du implementere følgende metoder:
asfalt_in_badConditions()
#veitilstand vil påvirke speed, max_speed og andre egenskaper.
## lag egne variabler som påvirker egenskaper 
dancing_in_the_rain()
været påvirker mange egenskaper.
## lag egne variabler som påvirker egenskaper 
like_A_ferrari()
max_speed vil påvirker konsum, men også sikkerhet i trafikken.
## lag egne variabler som påvirker egenskaper 
'''

# Definerer klassen motorsykkel og alt den skal ineholde
class motorsykkel:
    def __init__(self, speed, max_speed, motorstørrelse, konsum, asfalt_in_badCondition, dancing_in_the_rain, like_A_ferrari):
        self.speed = speed
        self.max_speed = max_speed
        self.motorstørrelse = motorstørrelse
        self.konsum = konsum
        self.asfalt_in_badCondition = asfalt_in_badCondition
        self.dancing_in_the_rain = dancing_in_the_rain
        self.like_A_ferarri = like_A_ferrari

# Setter klassen motorsykkel til en variabel 
motorbike = motorsykkel(95, 240, 3, 5, input("Er veitilstanden dårlig?: "), input("Regner det?: "), input("Skal du kjøre kjapt?: "))

# Bestemmer hva som skal skje vis veitilstanden er dårlig
def asfalt_in_badConditions():
    motorbike.speed -= 10
    motorbike.max_speed -= 15
    motorbike.konsum += 10

# Bestemmer hva som skal skje hvis det regner
def dancing_in_the_rain():
    motorbike.speed -= 20
    motorbike.max_speed -= 20
    motorbike.konsum += 20

# Bestemmer hva som skal skje hvis motorsykkelen skal kjøre fort
def like_A_ferrari():
    motorbike.max_speed += 30
    motorbike.konsum += 15

# Skjekker om veitilstanden er dårlig
if motorbike.asfalt_in_badCondition == "ja":
    asfalt_in_badConditions()

# Skjekker om det regner
if motorbike.dancing_in_the_rain == "ja":
    dancing_in_the_rain()

# Skjekker om motorsykkelen skal kjøre fort
if motorbike.like_A_ferarri == "ja":
    like_A_ferrari()

# Printer ut de viktigste funksjonene til motorsykkelen
print( )
print(f"Speed: {motorbike.speed}")
print(f"Max Speed: {motorbike.max_speed}")
print(f"Motorstørrelse: {motorbike.motorstørrelse}")
print(f"Konsum: {motorbike.konsum}")