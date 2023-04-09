# oop

# ism = input ("ismingizni kiriting: ")
# fam = input ("familiyangizni kiriting: ")
# yosh = int(input ("yoshingizni kiriting: "))

# class ParendClass:
#     def __init__(self,name, firstname, age):
#         self.count = 0
#         self.lst = ["olma","banan","anor","nok","uzum"]
#         self.name = name
#         self.firstname = firstname
#         self.age = age

#     def full_name(self):
#         return f'Salom {self.name.title()} {self.firstname.title()}'
    
#     def user_name(self):
#         return self.name
    
#     def user_age(self):
#         return self.age
    
#     def user_age_reg(self):
#         if self.age >= 20:
#             return f"{self.name.title()} siz 20 yoshga teng yo kattasiz"
#         else:
#             return f"{self.name.title()} siz 20 yoshdan kichiksiz "
        
#     def List(self):
#         for i in self.lst:
#             print( i.title())

    
# newclass = ParendClass(ism,fam,yosh)
# print(newclass.full_name())
# print(newclass.user_age_reg())
# newclass.List()

#vazifa = kara jadvalini oop qilish

# 1- misol==================================
# a = int (input("butun son kiriting: "))
# b = int (input("ikkinchi butun sonni kiriting: "))
# class EKUB:
#     def __init__(self,a,b):
#         self.birinchi = a
#         self.ikkinchi = b
    


        
# newclass = EKUB (a,b)
# print(newclass.ekub())

# 2- misol
# a = int (input("butun son kiriting: "))
# x = 0
# class Daraja :
#     def __init__(self,a,x):
#         self.son = a
#         self.daraja = x

#     def natija (self):
#             if x == a%2 and type(x) == int :
#                 return "true"
#             else :
#                 return "false" 

# newClass = Daraja(a,x)
# print (newClass.natija())

# 3- misol
# a = int (input("butun son kiriting: "))
# x = 0
# class Daraja :
#     def __init__(self,a,x):
#         self.son = a
#         self.daraja = x

#     def natija (self):
#             if x == a%4 and type(x) == int :
#                 return "true"
#             else :
#                 return "false" 

# newClass = Daraja(a,x)
# print (newClass.natija())


# import random as r
# x = r.randint (1,10)
# y = r.randint (1,10)
# class KOPAYTMA :
#     def __init__(self,x,y):
#         self.birinchi = x
#         self.ikkinchi = y
    
#     def savol (self):
#         n = 0
#         for i in range (5):
#             x = r.randint (1,10)
#             y = r.randint (1,10)
#             kopaytma = int (input (f"{x} x {y} = "))
#         if kopaytma == x * y :
#            n +=1
#         else :
#            n -=1
#         print (i)

# newclass = KOPAYTMA (x,y)
# newclass.savol()

#code sendbox
#indet reinbow