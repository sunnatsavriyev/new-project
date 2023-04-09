import random as r

ism = input ("ismingizni kiriting: ")
daraja = int (input ("savollar darajasini tanlang, 1,2,3,4,aralash: "))

class Matematika:
    def __init__(self,ism):
        self.ism = ism
    def first_degree(self):
        arifmetik = input ("arifmetik operatorni tanlang +,-,*,/: ")

        if arifmetik == "+":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} + {y} = "))
                if sv == x+y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} + {y} = "))
                if sv == x+y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "-":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} - {y} = "))
                if sv == x-y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta  savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} - {y} = "))
                if sv == x-y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta  savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "*":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} x {y} = "))
                if sv == x*y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} x {y} = "))
                if sv == x*y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "/":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = float (input(f"{x} / {y} = "))
                if sv == x/y:
                    togri +=1
                else:
                    xato +=1
            print (f" joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = float (input(f"{x} / {y} = "))
                if sv == x/y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")

    def second_degree(self):
        arifmetik = input ("arifmetik operatorni tanlang +,-,*,/: ")

        if arifmetik == "+":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} + {y} = "))
                if sv == x+y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} + {y} = "))
                if sv == x+y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "-":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} - {y} = "))
                if sv == x-y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta  savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} - {y} = "))
                if sv == x-y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta  savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "*":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} x {y} = "))
                if sv == x*y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} x {y} = "))
                if sv == x*y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "/":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = float (input(f"{x} / {y} = "))
                if sv == x/y:
                    togri +=1
                else:
                    xato +=1
            print (f" joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = float (input(f"{x} / {y} = "))
                if sv == x/y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
    
    def third_degree(self):
        arifmetik = input ("arifmetik operatorni tanlang +,-,*,/: ")

        if arifmetik == "+":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} + {y} = "))
                if sv == x+y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} + {y} = "))
                if sv == x+y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "-":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} - {y} = "))
                if sv == x-y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta  savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} - {y} = "))
                if sv == x-y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta  savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "*":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} x {y} = "))
                if sv == x*y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} x {y} = "))
                if sv == x*y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "/":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = float (input(f"{x} / {y} = "))
                if sv == x/y:
                    togri +=1
                else:
                    xato +=1
            print (f" joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = float (input(f"{x} / {y} = "))
                if sv == x/y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")

    def fourth_degree(self):
        arifmetik = input ("arifmetik operatorni tanlang +,-,*,/: ")

        if arifmetik == "+":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} + {y} = "))
                if sv == x+y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} + {y} = "))
                if sv == x+y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "-":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} - {y} = "))
                if sv == x-y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta  savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} - {y} = "))
                if sv == x-y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta  savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "*":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} x {y} = "))
                if sv == x*y:
                    togri +=1
                else:
                    xato +=1
            print (f"joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int (input(f"{x} x {y} = "))
                if sv == x*y:
                    togri +=1
                else:
                    xato +=1
            print (f"umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
        elif arifmetik == "/":
            togri = 0
            xato = 0
            for i in range(1,11):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = float (input(f"{x} / {y} = "))
                if sv == x/y:
                    togri +=1
                else:
                    xato +=1
            print (f" joriy 10 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")
            for i in range(10,21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = float (input(f"{x} / {y} = "))
                if sv == x/y:
                    togri +=1
                else:
                    xato +=1
            print (f" umumiy 20 ta savoldan {togri} ta to'g'ri {xato} ta xato topdingiz {self.ism}!")



matem = Matematika (ism)

if daraja == 1:
    matem.first_degree()
elif daraja == 2:
    matem.second_degree()
elif daraja == 3:
    matem.third_degree()
else:
    matem.fourth_degree()

