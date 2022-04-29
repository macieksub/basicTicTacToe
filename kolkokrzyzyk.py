import time

gra = True

#a = ' '
#b = ' '
#c = ' '
#d = ' '
#e = ' '
#f = ' '
#g = ' '
#h = ' '
#i = ' '
#wpisane = []
#g1 = ''
#g2 = ''

def pole ():
    print()
    print(a + ' | ' + b + ' | ' + c + '     7 | 8 | 9')
    print('---------     ---------')
    print(d + ' | ' + e + ' | ' + f + '     4 | 5 | 6')
    print('---------     ---------')
    print(g + ' | ' + h + ' | ' + i + '     1 | 2 | 3\n')



def inputt ():
    global a,b,c,d,e,f,g,h,i
    if ruch == '1' and g == ' ':
        g = gracz
    elif ruch == '2' and h == ' ':
        h = gracz
    elif ruch == '3' and i == ' ':
        i = gracz
    elif ruch == '4' and d == ' ':
        d = gracz
    elif ruch == '5' and e == ' ':
        e = gracz
    elif ruch == '6' and f == ' ':
        f = gracz
    elif ruch == '7' and a == ' ':
        a = gracz
    elif ruch == '8' and b == ' ':
        b = gracz
    elif ruch == '9' and c == ' ':
        c = gracz
    else :
        return False

#a == b == c
#d == e == f
#g == h == i
#a == d == g
#b == e == h
#c == f == i
#a == e == i
#c == e == g

print('Witaj w grze kółko i krzyżyk !\nPo każdym wyborze wciśnij enter.\n')
while gra:
    a = ' '
    b = ' '
    c = ' '
    d = ' '
    e = ' '
    f = ' '
    g = ' '
    h = ' '
    i = ' '
    ll = 0
    p = True
    z = False
    
    print('Kto zaczyna (o/x) ?')
    while p:
        zaczyna = input()
        if zaczyna.lower() == 'x':
            g1 = 'x'
            g2 = 'o'
            p = False
        elif zaczyna.lower() == 'o':
            g1 = 'o'
            g2 = 'x'
            p = False
        else :
            print('Zły znak. (o/x)')
    while gra :
        if (ll % 2) == 0:
            gracz = g1
        else:
            gracz = g2

            
        pole()

        
        print('Ruch ' + gracz + '. Wybierz pole.')
        ruch = input()
        if inputt() != False :
            ll = ll + 1
            #print(ll)
            if a == b == c != ' ' or d == e == f != ' ' or g == h == i != ' ' or a == d == g != ' ' or b == e == h != ' ' or c == f == i != ' ' or a == e == i != ' ' or c == e == g != ' ' :
                z = True
                pole()
                print (gracz + ' zwycięża !!!')
            elif  ll == 9 :
                pole()
                print('remis !')
                z = True
            if z :
                print ('\nChcesz zagrać ponownie ? tak/nie')
                ponownie = input ()
                if ponownie.lower() in ['y' , 't' , 'tak' , 'yes'] :
                    break
                else:
                    gra = False
        else :
            print ('\nNiepoprawny znak')

print('Dziękuję za grę !')
time.sleep(1)
