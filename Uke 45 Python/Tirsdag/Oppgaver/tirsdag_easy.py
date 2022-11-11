from matplotlib import pyplot # Install matplotlib før du begynner med oppgavene 

'''
oppgave 1

    Anne har laget et program som skal regne ut hvor mye mel ho trenger til å lage a antall liter vaffelrøre.


'''
a = 2
b = a * 4
print("Du trenger", b, " dl mel. ")

'''
Anne prøver å taste inn 4.5 liter vaffelrøre, men programmet skriver ut en feilmelding til skjermen.
Hjelp Anne med koden slik at den vil fungere også med desimaltall.
'''
#####################################################################################################################
'''
Oppgave 2

Kari har gjort en undersøkelse i klassen sin og spurt klassekameratene hvilke type kjæledyr de har hjemme.
Svarene ble:
Katt: 7
Hund: 5
Fugl: 3
Andre dyr: 4
Ingen:6

Kari ønsker å lage et Python- program der ho kan taste inn frekvensene til de ulike observasjonene og
hun vil at programmet skal skrive ut et stolpediagram til skjermen.
'''

x = ["katt", "hund","fugl","andre dyr","ingen dyr"] #lager en liste x med 5 elementer 
y = [7,5,3,4,6] #lager en liste y med frekvensene til elementene i liste x
pyplot.bar(x,y) # lager stolpediagram  med elementene fra x og y
pyplot.show() # skriver diagrammet til skjermen


#############################################################################################################################
'''
oppgave 3

Kjør programmet og forklar hva det gjør.
Prøv å skriv ut heltall fra og med 7 til og med 32
Prøv å skriv ut heltall fra og med -10 til og med 10

'''
for tall in range (4,19):
    print(tall)

###############################################################################################################################

'''
oppgave 4

Kjør programmet og forklar hva det gjør.
Endre 3 tallet til andre tall og se hva som skjer.
'''
for m in range (10):
    print(m, 3*m)

################################################################################################################################

'''
Oppgave 5

Kari har laget et program der bruker kan taste inn alder å få skrevet ut pris på kinobillett til skjermen.

Kjør programmet og forklar hvordan det fungerer.

Kinoen kommer med en tilbud til de mellom 18 og 25 år på 110 kroner per billett.
Gjør endringer på koden slik at det blir tilpasset tilbudet.
'''
b = 80  # pris for en billett barn(6-12 år)
u = 100 # pris for en billett ungdom(13-17)
v = 120 # pris for en billett voksen
g = 0   # under 6 år er gratis
alder = int(input("Tast inn alder: "))
if alder <= 5:
  pris = g
elif alder > 5 and alder < 13: 
  pris = b
elif alder > 12 and alder < 18:
  pris = u
else:
  pris = v
print("Prisen blir", pris, "kroner. ")

########################################################################################################################################

'''
Oppgave 6
En dag i Moss var det følgende temperaturer:
Klokkeslett - grader
kl 06.00 - 12
kl 12.00 - 14
kl 18.00 - 20
kl 22.00 - 21
Lag et linjediagram over temperaturutviklingen.
Tips: Bruk det du har lært i koden over i tillegg til det under.
'''
x = []  # lag en liste for klokkeslett
y = []  # lag en liste for temperaturen
pyplot.plot(x,y) # lager linjediagram med elementene fra x og y 
