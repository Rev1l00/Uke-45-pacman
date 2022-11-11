import random

'''
Oppgave 1
VELG RIKTIG OUTPUT
alternative 1 = 'none'
alternative 2 = 'invalid syntax'
alternative 3 = 'the cat on the roof'
'''
word = 'the cat on the roof'
print(word)

# Output blir "The cat on the roof"

'''
Oppgave 2
VELG RIKTIG OUTPUT
alternative 1 = 'Eureka'
alternative 2 = 'IM- Åssiden vgs'
alterbative 3 = 'none'
'''
a =1
b =1
c =7
d =5

result = a + b + d
if result < c:
    print('Eureka')
else:
    print('IM- Åssiden vgs')

# Outpur blir "IM- Åssiden vgs" fordi a + b + c = 7 og 7 er ikke mindre enn 7.

'''
Oppgave 3 
Hvor mange ganger skal følgende loop kjøres?
VELG RIKTIG SVAR
 alternative 1 = 150
 alternative 2 = 50
 alternative 3 = 30
 alterbative 4 = uendelig mange ganger.
'''

r = 150
while r <= 200:
    print(r)
    r+=5

# Den skal kjøre fram til "r" er mer eller det samme som 200.

'''
oppgave 4
forklar linje for linje hva er det som skjer i funksjonen oddTall.
 VIKTIG!!!!! Forklar linjene først, før du tester den i editoren din.
'''

def oddeTall():     # Den definerer funksjonen "oddeTall".
     num1 = random.randint(1,10) #tilfeldig tall mellom 1 og 10     # Den velger et tilfeldig tall mellom 1 og 10
     num2 = random.randint(2,9) #tilfeldig tall mellom 2 og 9       # Den velger et tilfeldig tall mellom 2 og 9
     if num1%num2 ==0: ### symbol % betyr resten av tallet (deling)     # Den sjekker om det som er igjen etter at num1 og num2 har blitt delt på hverandre er null.
            result = num1/num2      # Den gjør variablen result til svaret av num1 dele på num2.
            
     return result      # Den returnerer resultatet fra funksjonen.