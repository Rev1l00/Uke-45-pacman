'''
Oppgave 1 
VELG RIKTIG OUTPUT:
Alternative 1 = {1,2}
Alternative 2 = {1, 'a', 2, 3, 'b', 4}
alternative 3 = {1, 4, 6}
alternative 4 = {1, 2, 3, 4, 'a', 'b', 'c', 5, 6}
forklar hvorfor alternativet du velger er riktig.
'''

list1 = {1, 2, 3, 4, 5, 6}
list2 ={1, 'a', 4, 'b', 'c', 6}
print(list1&list2)




'''
Oppgave 2
opprett et objekt med metoden middag. Deretter velg riktig kombinasjon av 
mat_porsjoner og antall_gjester for å få følgende melding i terminalen:
'alle gjester er mett'.
'''
class måltid():
    mat_porsjoner = 4
    antall_gjester = 4
    def middag(mat_porsjoner, antall_gjester):
        if mat_porsjoner != antall_gjester:
            sulten = True
            print('altfor lite mat')
        elif mat_porsjoner ==antall_gjester:
            sulter = False
            print('alle gjester er mett')
        else:
            print('altfor mye mat')

    middag(mat_porsjoner, antall_gjester)

'''
Oppgave 3
HVILKEN VERDI HAR VARIABEL sub3 etter 7 runder i loop? 
VELG RIKTIG SVAR
Alternative 1 = 14
Alternative 2 = 7
Alternative 3 = 36
Alternative 4 = 18
forklar hvorfor alternativet du velger er riktig.
'''

sub1 = 15
sub2 = 25
sub3 = 8
sub4 = 17

for x in range(15):
    sub1 += x
    if sub1 >sub2:
        sub3=+sub1

# Etter 7 runder i loop har sub3 verdien 36 fordi

'''
Oppgave 4 
Opprett en funskjon som summerer alle elementene i lister red og white
forklar med ord løsningen du valgte
'''

red = [1, 2, 5, 0, 3, 1, 2]
white = ['1', '2', '4', '0', '8']

# Jeg valgte og lage en funksjon som la alle numerene i listen sammen i en ny variabel og så printe den nye variabelen.

def sum_lists():
    sum_of_red = 0
    sum_of_white = 0
    for number in red:
        sum_of_red += int(number)
    for number in white:
        sum_of_white += int(number)
    print('The sum of red is', sum_of_red)
    print('The sum of white is', sum_of_white)
sum_lists()