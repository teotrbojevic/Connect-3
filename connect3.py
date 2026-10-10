import os
class LKG:
    def __init__(self, seed):
        self.u = seed
        self.a = 429493445
        self.c = 907633385
        self.m = 2 ** 32

    def odradi(self):
        self.u = (self.u * self.a + self.c) % self.m
        return self.u / self.m
class Elem:
    def __init__(self, data):
        self.podatak=data
        self.sledeci=None
class KruznaLista:
    def __init__(self):
        self.zagl=Elem(None)
        self.zagl.sledeci=self.zagl
        self.br_elem=0
    def dodaj_na_pocetak(lista, element):
        element.sledeci=lista.zagl.sledeci
        lista.zagl.sledeci=element
        lista.br_elem+=1
    def dodaj_na_kraj(lista, element):
        tren=lista.zagl
        while tren.sledeci!=lista.zagl:
            tren=tren.sledeci
        tren.sledeci=element
        element.sledeci=lista.zagl
        lista.br_elem+=1
    def ukloni_sa_pocetka(lista):
        if (lista.zagl.sledeci!=lista.zagl):
            tren=lista.zagl.sledeci
            lista.zagl.sledeci=tren.sledeci
            izbrisani=tren.podatak
            del tren
            lista.br_elem-=1
            return izbrisani
        else:
            return 0
    def ukloni_sa_kraja(lista):
        if lista.zagl.sledeci!=lista.zagl:
            tren=lista.zagl
            while tren.sledeci!=lista.zagl:
                pret=tren
                tren=tren.sledeci
            pret.sledeci=lista.zagl
            izbrisani=tren.podatak
            del tren
            lista.br_elem-=1
            return izbrisani
        else:
            return 0
    def pogledaj_pocetak(lista):
        if lista.zagl.sledeci!=lista.zagl:
            tren=lista.zagl.sledeci
            return tren.podatak
        else:
            return 0
    def pogledaj_kraj(lista):
        if lista.zagl.sledeci!=lista.zagl:
            tren = lista.zagl
            while tren.sledeci != lista.zagl:
                tren = tren.sledeci
            return tren.podatak
        else:
            return 0
    def je_prazna(lista):
        if lista.zagl.sledeci==lista.zagl:
            return True
        else:
            return False
    def velicina(lista):
        return lista.br_elem
class Stek:
    def __init__(self):
        self.kula=KruznaLista()
    def push(lista, element):
        lista.kula.dodaj_na_kraj(element)
    def pop(lista):
        if lista.kula.velicina()!=0:
            return lista.kula.ukloni_sa_kraja()
        else:
            return 0
    def pogledaj_vrh_steka(lista):
        if lista.kula.velicina()!=0:
            return lista.kula.pogledaj_kraj()
        else:
            return 0
    def je_prazan(lista):
        return lista.kula.je_prazna()
proba=[['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
def ispis(aaa):
    for i in range(3, -1, -1):
        for j in range(4):
            if j==3:
                print(aaa[i][j])
            else:
                print("{}".format(aaa[i][j]), end=" ")

def potez(aaa, br, igrac):
    for i in range(4):
        if aaa[i][br-1]=='.':
            aaa[i][br-1]=igrac
            break
def ispravnost(aaa, br):
    if br<1 or br>4:
        return False
    elif aaa[3][br-1]!='.':
        return False
    else:
        return True
def zavrsno(aaa):
    for i in range(4):
        for j in range(2):
            if aaa[j][i]==aaa[j+1][i] and aaa[j][i]==aaa[j+2][i]:
                if aaa[j][i]=='X':
                    return 'X'
                elif aaa[j][i]=='O':
                    return 'O'
    for i in range(4):
        for j in range(2):
            if aaa[i][j]==aaa[i][j+1] and aaa[i][j]==aaa[i][j+2]:
                if aaa[i][j]=='X':
                    return 'X'
                elif aaa[i][j]=='O':
                    return 'O'
    for i in range(2):
        for j in range(2):
            if aaa[i][j]==aaa[i+1][j+1] and aaa[i][j]==aaa[i+2][j+2]:
                if aaa[i][j]=='X':
                    return 'X'
                elif aaa[i][j]=='O':
                    return 'O'
    for i in range(2):
        for j in range(2):
            if aaa[3-i][j]==aaa[3-i-1][j+1] and aaa[3-i][j]==aaa[3-i-2][j+2]:
                if aaa[3-i][j]=='X':
                    return 'X'
                if aaa[3-i][j]=='O':
                    return 'O'
    for i in range(4):
        for j in range(4):
            if aaa[i][j]=='.':
                return 'NI'
    return 'NE'
def pocetak():
    mat = [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
    while True:
        print("1.Generisanje sa svim slobodnim poljima\n2.Generisanje na osnovu unosa ili datoteka")
        tas = int(input())
        brx=0
        bro=0
        if tas==1:
            return mat, 'X'
        elif tas==2:
            while True:
                print("1.Generisanje na osnovu unosa\n2. Generisanje na osnovu datoteke")
                dru = int(input())
                if dru == 1:
                    for i in range(4):
                        red = input().split()
                        for j in range(4):
                            mat[3 - i][j] = red[j]
                    for i in range(4):
                        for j in range(4):
                            if mat[i][j]=='X':
                                brx+=1
                            if mat[i][j]=='O':
                                bro+=1
                    if brx>bro:
                        return mat, 'O'
                    else:
                        return mat, 'X'
                elif dru == 2:
                    while True:
                        print("Unesi datoteku")
                        tekst = input()
                        if os.path.exists(tekst):
                            with open(tekst, "r+", encoding="utf-8") as f:
                                tre = []
                                for line in f:
                                    tre.append(line.strip())
                                for i in range(4):
                                    tre[i] = tre[i].split()
                                    for j in range(4):
                                        mat[3 - i][j] = tre[i][j]
                            for i in range(4):
                                for j in range(4):
                                    if mat[i][j] == 'X':
                                        brx += 1
                                    if mat[i][j] == 'O':
                                        bro += 1
                            if brx > bro:
                                return mat, 'O'
                            else:
                                return mat, 'X'
                        else:
                            print("Ne postoji ta datoteka")
                else:
                    print("Nije dobro unet broj")
        else:
            print("Nije dobro unet broj")


class Cvor:
    def __init__(self, tabla, napot, dubina, pretpot=None):
        self.tabla = tabla
        self.napot = napot
        self.dubina = dubina
        self.pretpot = pretpot
        self.deca = KruznaLista()
        self.ishod = zavrsno(tabla)
        self.vrednost = 0
def stablo(poc_tab, poc_igr):
    while True:
        print("Unesi visinu")
        h=int(input())
        if h>=0:
           koren=Cvor(poc_tab, poc_igr, 0)
           red=KruznaLista()
           red.dodaj_na_kraj(Elem(koren))
           while not red.je_prazna():
               trenutni=red.ukloni_sa_pocetka()
               if trenutni.dubina ==h or trenutni.ishod != 'NI':
                   continue
               if trenutni.napot == 'X':
                   sledeci='O'
               else:
                   sledeci='X'
               for i in range(1, 5):
                   if ispravnost(trenutni.tabla, i):
                       nov=[['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
                       for l in range(4):
                           for m in range(4):
                               nov[l][m]=trenutni.tabla[l][m]
                       potez(nov, i, trenutni.napot)
                       dete=Cvor(nov, sledeci, trenutni.dubina+1, i)
                       trenutni.deca.dodaj_na_kraj(Elem(dete))
                       red.dodaj_na_kraj(Elem(dete))
           return koren, h
        else:
            print("Nije dobro unet broj")
def listvred(dete):
    if dete.ishod == 'X':
        dete.vrednost=-1000
    if dete.ishod == 'O':
        dete.vrednost=1000
    if dete.ishod == 'NE':
        dete.vrednost=0
    if dete.ishod == 'NI':
        Fc=0
        Fp=0
        for i in range(4):
            if 'X' in dete.tabla[i] and 'O' not in dete.tabla[i]:
                Fp+=1
            if 'O' in dete.tabla[i] and 'X' not in dete.tabla[i]:
                Fc+=1
            if (('X' == dete.tabla[0][i]) or ('X' == dete.tabla[1][i]) or ('X' == dete.tabla[2][i]) or ('X' == dete.tabla[3][i])) and (('O' != dete.tabla[0][i]) and ('O' != dete.tabla[1][i]) and ('O' != dete.tabla[2][i]) and ('O' != dete.tabla[3][i])):
                Fp+=1
            if (('O' == dete.tabla[0][i]) or ('O' == dete.tabla[1][i]) or ('O' == dete.tabla[2][i]) or (
                    'O' == dete.tabla[3][i])) and (
                    ('X' != dete.tabla[0][i]) and ('X' != dete.tabla[1][i]) and ('X' != dete.tabla[2][i]) and (
                    'X' != dete.tabla[3][i])):
                Fc+=1
        dete.vrednost=7*(Fc-Fp)
def minimaks(koren):
    stek1=Stek()
    stek2=Stek()
    stek1.push(Elem(koren))
    while not stek1.je_prazan():
        trenutni=stek1.pop()
        stek2.push(Elem(trenutni))
        if not trenutni.deca.je_prazna():
            pomoc=trenutni.deca.zagl.sledeci
            while not pomoc==trenutni.deca.zagl:
                kon=pomoc.podatak
                stek1.push(Elem(kon))
                pomoc=pomoc.sledeci
    while not stek2.je_prazan():
        res=stek2.pop()
        if res.deca.je_prazna():
            listvred(res)
        else:
            maxi=-2000
            mini=2000
            if res.napot == 'X':
                pomoc=res.deca.zagl.sledeci
                while not pomoc==res.deca.zagl:
                    if pomoc.podatak.vrednost < mini:
                        mini=pomoc.podatak.vrednost
                    pomoc=pomoc.sledeci
                res.vrednost=mini
            if res.napot == 'O':
                pomoc=res.deca.zagl.sledeci
                while not pomoc==res.deca.zagl:
                    if pomoc.podatak.vrednost > maxi:
                        maxi=pomoc.podatak.vrednost
                    pomoc=pomoc.sledeci
                res.vrednost=maxi
def preorder(koren):
    stek1=Stek()
    stek2=Stek()
    stek1.push(Elem(koren))
    while not stek1.je_prazan():
        trenutni=stek1.pop()
        spejs = "    " * trenutni.dubina
        if trenutni.pretpot is None:
            pret="Koren"
        else:
            pret="Kolona {}".format(trenutni.pretpot)
        print("{} -> Dubina: {}  Na potezu: {}  Potez: {}  Vrednost: {}".format(spejs, trenutni.dubina, trenutni.napot, pret, trenutni.vrednost))
        for p in range(4):
            print(f"{spejs}   " + " ".join(trenutni.tabla[3-p]))
        if not trenutni.deca.je_prazna():
            pomoc=trenutni.deca.zagl.sledeci
            while not pomoc==trenutni.deca.zagl:
                stek2.push(Elem(pomoc.podatak))
                pomoc=pomoc.sledeci
            while not stek2.je_prazan():
                grr=stek2.pop()
                stek1.push(Elem(grr))
print("Pocinje igra")
print("1. Kreiraj tablu\n0.Zavrsi igru")
ulaz=int(input())
pret=-10
siu=0
while ulaz!=1 and ulaz!=0:
    print("Niste uneli dobar broj")
    ulaz=int(input())
if ulaz==1:
    mat, poc_pot=pocetak()
    siu=0
    bx=0
    bo=0
    for i in range(4):
        for j in range(4):
            if mat[i][j]=="X":
                bx+=1
            if mat[i][j]=="O":
                bo+=1
    if bx==bo:
        print("Ko zelis da prvi igra\nX.Igrac\nO.Racunar")
        while True:
            re=input()
            if re=='X':
                poc_pot='X'
                break
            elif re=='O':
                poc_pot='O'
                break
            else:
                print("Unesi ispravno")
    koren, h= stablo(mat, poc_pot)
    minimaks(koren)
    trenutni=koren
    ispis(koren.tabla)
    if zavrsno(koren.tabla)!="NI":
        if zavrsno(koren.tabla)=="NE":
            print("Nereseno")
        if zavrsno(koren.tabla)=="X":
            print("Pobedio si")
        if zavrsno(koren.tabla)=="O":
            print("Pobedio te racunar")
        siu+=1
    elif poc_pot=='O':
        if h>trenutni.dubina:
            if not trenutni.deca.je_prazna():
                pomoc=trenutni.deca.zagl.sledeci
                while not pomoc==trenutni.deca.zagl:
                    if pomoc.podatak.vrednost == trenutni.vrednost:
                        trenutni=pomoc.podatak
                        break
                    pomoc=pomoc.sledeci
            print("Potez racunara")
            ispis(trenutni.tabla)
            if zavrsno(trenutni.tabla) != "NI":
                if zavrsno(trenutni.tabla) == "NE":
                    print("Nereseno")
                if zavrsno(trenutni.tabla) == "X":
                    print("Pobedio si")
                if zavrsno(trenutni.tabla) == "O":
                    print("Pobedio te racunar")
                siu += 1
        else:
            while True:
                print("Dostigla se visina. Unesi seme")
                gen=LKG(float(input()))
                k=0
                for i in range(2):
                    t=gen.odradi()
                    if t>0.5:
                        k=2*k+1
                    else:
                        k=2*k
                k+=1
                for i in range(4):
                    if ispravnost(trenutni.tabla, k):
                        break
                    else:
                        k+=1
                        if k==5:
                            k=1
                if ispravnost(trenutni.tabla, k):
                    nova_tabla = [red[:] for red in trenutni.tabla]
                    potez(nova_tabla, k, 'O')
                    novi_cvor = Cvor(nova_tabla, 'X', trenutni.dubina+1, k)
                    trenutni.deca.dodaj_na_kraj(Elem(novi_cvor))
                    trenutni = novi_cvor
                    print("Potez racunara")
                    ispis(trenutni.tabla)
                    break
                else:
                    print("Unesi drugo seme.")
            if zavrsno(trenutni.tabla) != "NI":
                if zavrsno(trenutni.tabla) == "NE":
                    print("Nereseno")
                if zavrsno(trenutni.tabla) == "X":
                    print("Pobedio si")
                if zavrsno(trenutni.tabla) == "O":
                    print("Pobedio te racunar")
                siu += 1
while ulaz!=0:
    print("1.Novo stanje\n2.Igranje poteza\n3.Ispis Stabla\n0.Kraj")
    ulaz=int(input())
    if ulaz==1:
        mat, poc_pot=pocetak()
        siu=0
        bx=0
        bo=0
        for i in range(4):
            for j in range(4):
                if mat[i][j]=="X":
                    bx+=1
                if mat[i][j]=="O":
                    bo+=1
        if bx==bo:
            print("Ko zelis da prvi igra\nX.Igrac\nO.Racunar")
            while True:
                re=input()
                if re=='X':
                    poc_pot='X'
                    break
                elif re=='O':
                    poc_pot='O'
                    break
                else:
                    print("Unesi ispravno")
        koren, h= stablo(mat, poc_pot)
        minimaks(koren)
        trenutni=koren
        ispis(koren.tabla)
        if zavrsno(koren.tabla)!="NI":
            if zavrsno(koren.tabla)=="NE":
                print("Nereseno")
            if zavrsno(koren.tabla)=="X":
                print("Pobedio si")
            if zavrsno(koren.tabla)=="O":
                print("Pobedio te racunar")
            siu+=1
        elif poc_pot=='O':
            if h>trenutni.dubina:
                if not trenutni.deca.je_prazna():
                    pomoc=trenutni.deca.zagl.sledeci
                    while not pomoc==trenutni.deca.zagl:
                        if pomoc.podatak.vrednost == trenutni.vrednost:
                            trenutni=pomoc.podatak
                            break
                        pomoc=pomoc.sledeci
                print("Potez racunara")
                ispis(trenutni.tabla)
                if zavrsno(trenutni.tabla) != "NI":
                    if zavrsno(trenutni.tabla) == "NE":
                        print("Nereseno")
                    if zavrsno(trenutni.tabla) == "X":
                        print("Pobedio si")
                    if zavrsno(trenutni.tabla) == "O":
                        print("Pobedio te racunar")
                    siu += 1
            else:
                while True:
                    print("Dostigla se visina. Unesi seme")
                    gen=LKG(float(input()))
                    k=0
                    for i in range(2):
                        t=gen.odradi()
                        if t>0.5:
                            k=2*k+1
                        else:
                            k=2*k
                    k += 1
                    for i in range(4):
                        if ispravnost(trenutni.tabla, k):
                            break
                        else:
                            k += 1
                            if k == 5:
                                k = 1
                    if ispravnost(trenutni.tabla, k):
                        nova_tabla = [red[:] for red in trenutni.tabla]
                        potez(nova_tabla, k, 'O')
                        novi_cvor = Cvor(nova_tabla, 'X', trenutni.dubina + 1, k)
                        trenutni.deca.dodaj_na_kraj(Elem(novi_cvor))
                        trenutni = novi_cvor
                        print("Potez racunara")
                        ispis(trenutni.tabla)
                        break
                    else:
                        print("Unesi drugo seme.")
                if zavrsno(trenutni.tabla) != "NI":
                    if zavrsno(trenutni.tabla) == "NE":
                        print("Nereseno")
                    if zavrsno(trenutni.tabla) == "X":
                        print("Pobedio si")
                    if zavrsno(trenutni.tabla) == "O":
                        print("Pobedio te racunar")
                    siu += 1
    elif ulaz==2 and siu==0:
        if h>trenutni.dubina:
            print("Unesi kolonu")
            kolona=int(input())
            while True:
                if ispravnost(trenutni.tabla, kolona):
                    break
                else:
                    print("Ne moze")
                    kolona=int(input())
            pomoc=trenutni.deca.zagl.sledeci
            while not pomoc==trenutni.deca.zagl:
                if pomoc.podatak.pretpot == kolona:
                    trenutni=pomoc.podatak
                    break
                pomoc=pomoc.sledeci
            ispis(trenutni.tabla)
            if zavrsno(trenutni.tabla) != "NI":
                if zavrsno(trenutni.tabla) == "NE":
                    print("Nereseno")
                if zavrsno(trenutni.tabla) == "X":
                    print("Pobedio si")
                if zavrsno(trenutni.tabla) == "O":
                    print("Pobedio te racunar")
                siu += 1
            if siu==0:
                if h > trenutni.dubina:
                    if not trenutni.deca.je_prazna():
                        pomoc = trenutni.deca.zagl.sledeci
                        while not pomoc == trenutni.deca.zagl:
                            if pomoc.podatak.vrednost == trenutni.vrednost:
                                trenutni = pomoc.podatak
                                break
                            pomoc = pomoc.sledeci
                    print("Potez racunara")
                    ispis(trenutni.tabla)
                    if zavrsno(trenutni.tabla) != "NI":
                        if zavrsno(trenutni.tabla) == "NE":
                            print("Nereseno")
                        if zavrsno(trenutni.tabla) == "X":
                            print("Pobedio si")
                        if zavrsno(trenutni.tabla) == "O":
                            print("Pobedio te racunar")
                        siu += 1
                else:
                    while True:
                        print("Dostigla se visina. Unesi seme")
                        gen = LKG(float(input()))
                        k = 0
                        for i in range(2):
                            t = gen.odradi()
                            if t > 0.5:
                                k = 2 * k + 1
                            else:
                                k = 2 * k
                        k += 1
                        for i in range(4):
                            if ispravnost(trenutni.tabla, k):
                                break
                            else:
                                k += 1
                                if k == 5:
                                    k = 1
                        if ispravnost(trenutni.tabla, k):
                            nova_tabla = [red[:] for red in trenutni.tabla]
                            potez(nova_tabla, k, 'O')
                            novi_cvor = Cvor(nova_tabla, 'X', trenutni.dubina + 1, k)
                            trenutni.deca.dodaj_na_kraj(Elem(novi_cvor))
                            trenutni = novi_cvor
                            print("Potez racunara")
                            ispis(trenutni.tabla)
                            break
                        else:
                            print("Unesi drugo seme.")
                    if zavrsno(trenutni.tabla) != "NI":
                        if zavrsno(trenutni.tabla) == "NE":
                            print("Nereseno")
                        if zavrsno(trenutni.tabla) == "X":
                            print("Pobedio si")
                        if zavrsno(trenutni.tabla) == "O":
                            print("Pobedio te racunar")
                        siu += 1
        else:
            print("Unesi kolonu")
            kolona=int(input())
            while True:
                if ispravnost(trenutni.tabla, kolona):
                    break
                else:
                    print("Ne moze")
                    kolona=int(input())
            nova_tabla = [red[:] for red in trenutni.tabla]
            potez(nova_tabla, kolona, 'X')
            novi_cvor = Cvor(nova_tabla, 'O', trenutni.dubina + 1, kolona)
            trenutni.deca.dodaj_na_kraj(Elem(novi_cvor))
            trenutni = novi_cvor
            ispis(trenutni.tabla)
            if zavrsno(trenutni.tabla) != "NI":
                if zavrsno(trenutni.tabla) == "NE":
                    print("Nereseno")
                if zavrsno(trenutni.tabla) == "X":
                    print("Pobedio si")
                if zavrsno(trenutni.tabla) == "O":
                    print("Pobedio te racunar")
                siu += 1
            if siu==0:
                if h > trenutni.dubina:
                    if not trenutni.deca.je_prazna():
                        pomoc = trenutni.deca.zagl.sledeci
                        while not pomoc == trenutni.deca.zagl:
                            if pomoc.podatak.vrednost == trenutni.vrednost:
                                trenutni = pomoc.podatak
                                break
                            pomoc = pomoc.sledeci
                    print("Potez racunara")
                    ispis(trenutni.tabla)
                    if zavrsno(trenutni.tabla) != "NI":
                        if zavrsno(trenutni.tabla) == "NE":
                            print("Nereseno")
                        if zavrsno(trenutni.tabla) == "X":
                            print("Pobedio si")
                        if zavrsno(trenutni.tabla) == "O":
                            print("Pobedio te racunar")
                        siu += 1
                else:
                    while True:
                        print("Dostigla se visina. Unesi seme")
                        gen = LKG(float(input()))
                        k = 0
                        for i in range(2):
                            t = gen.odradi()
                            if t > 0.5:
                                k = 2 * k + 1
                            else:
                                k = 2 * k
                        k += 1
                        for i in range(4):
                            if ispravnost(trenutni.tabla, k):
                                break
                            else:
                                k += 1
                                if k == 5:
                                    k = 1
                        if ispravnost(trenutni.tabla, k):
                            nova_tabla = [red[:] for red in trenutni.tabla]
                            potez(nova_tabla, k, 'O')
                            novi_cvor = Cvor(nova_tabla, 'X', trenutni.dubina + 1, k)
                            trenutni.deca.dodaj_na_kraj(Elem(novi_cvor))
                            trenutni = novi_cvor
                            print("Potez racunara")
                            ispis(trenutni.tabla)
                            break
                        else:
                            print("Unesi drugo seme.")
                    if zavrsno(trenutni.tabla) != "NI":
                        if zavrsno(trenutni.tabla) == "NE":
                            print("Nereseno")
                        if zavrsno(trenutni.tabla) == "X":
                            print("Pobedio si")
                        if zavrsno(trenutni.tabla) == "O":
                            print("Pobedio te racunar")
                        siu += 1
    elif ulaz==3:
        preorder(koren)
    elif ulaz==0:
        continue
    else:
        print("Nije ispravno uneto")




print("Hvala sto ste igrali")

