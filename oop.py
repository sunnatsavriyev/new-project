#  oop
# object oriented programming
#class

# ism = input ("ismingizni kiriting: ")
# fam = input ("familyangizni kiriting :")
# yosh = int (input ("yoshingizni kiriting: "))

# class Person:
#     def __init__(self,name,firstname,age):
#         self.name = name
#         self.firstname = firstname
#         self.age = age

#     def nameclick (self):
#         print(self.name)

#     def  firstnameclick (self):
#         print(self.firstname)

#     def ageclick (self):
#         print(self.age)

#     def fulname(self):
#         print(f"salom {self.name} {self.firstname} saytga xush kelibsiz!")

#     def yoshtekshir(self):
#         if self.age >=20:
#             print("Hush kelibsiz"+ " " + self.name)
#         else :
#             print("siz hali yoshsiz")

# newclass = Person(ism,fam,yosh)
# newclass.fulname()
# newclass.yoshtekshir()

# 1-misol
# a = 23,43,21,54,665
# b = []
# class Lst:
#    def __init__(self,a,b):
#        self.newlst=b
#        self.ozgaruvchi=a

#    def lst (self):
#        b.append(self.ozgaruvchi)
#        print(b)

# newclass = Lst(a,b)
# newclass.lst()

# 2-misol
# a = ["qizil","yashil","sariq","kok","qora"]
# b = []
# class Rang:
#    def __init__(self,a,b):
#        self.newlst = b
#        self.lst = a

#    def new (self):
#        b.append(a[-1:0])
#        print(b)

# newclass = Rang(a,b)
# newclass.new()



# 3-misol
# a = [2,33,43,55,3,44,5,3,33,55]
# b = int (input ("butun son kiriting: "))
# class Son:
#     def __init__ (self,a,b):
#         self.son = b
#         self.lst = a

#     def sonlar (self):
#         natija = 0
#         for i in a:
#             if i == b:
#                 natija +=1
#             else:
#                 natija
#         print(natija)

# newclass = Son(a,b)
# newclass.sonlar()

# 4-misol, 8-misol************
# a = [-2,33,-4,-22,12,234,4,-45,-3]
# class MusbatSon :
#     def __init__(self,a):
#         self.lst = a

#     def musbatson (self):
#         for i in a:
#             if i >=0:
#                 print (i)
    
#     def ortish (self):
#         a.sort()
#         print(a)

# newclass = MusbatSon (a)
# newclass.musbatson()
# newclass.ortish()

# 5-misol
#a = ["oq","qizil","yashil","qora","ko'k"]

# class Rang:
#     def __init__(self,a):
#         self.lst = a
    
#     def rang (self):
#         a.remove("oq")
#         print(a)
    
# newClass = Rang (a)
# newClass.rang()


# 6-misol
# import random as r
# a = ["salom","hello","dunyo","ism"]
# class Sozlar:
#     def __init__(self,a):
#         self.lst = a

#     def sonlarniaralashtir (self):
#         r.shuffle(a)
#         print(a)

# newClass = Sozlar(a)
# newClass.sonlarniaralashtir()

# 7-misol
# a = ["salom","hello","dunyo","ism"]
# b = []

# class Kopya :
#     def __init__(self,a,b):
#         self.lst = a
#         self.empty = b

#     def kopya (self):
#         b=a.copy()
#         print(b)

# newclass = Kopya(a,b)
# newclass.kopya ()

# 9-misol
# a = [12,-3,22,-8,24,31,-39]
# b = [13,23,12,22,8,-2,21]
# class Tekshir:
#     def __init__(self,a,b):
#         self.lst1 = a
#         self.lst2 = b

#     def tekshir (self):
#         for i in a:
#             for x in b:
#                 if i == x:
#                     print (i)

# class2 =Tekshir(a,b)
# class2.tekshir()


# 10-misol
# a = [12,-3,22,-8,24,31,-39]
# b = [13,23,12,22,8,-2,21]
# class Tekshir :
#     def __init__(self,a,b):
#         self.lst1 = a
#         self.lst2 = b

#     def tekshir (self):
#         for i in a:
#             for x in b:
#                 if i == x:
#                     a.remove(x)
#                     print (a)
# class2 = Tekshir(a,b)
# class2.tekshir()


# 11-misol 13-misol *****
# a = [1,2,3,4,5]
# k = 13,24,53,55
# b = [12,34,56,67]

# class Birlashtirish:
#     def __init__(self,a,k,b):
#         self.lst = a
#         self.son = k
#         self.newlst = b

#     def birlashma(self):
#         a.extend(k)
#         print(a)

#     def newbirlashma(self):
#         a.extend(b)
#         print(a)

# newclass = Birlashtirish(a,k,b)
# newclass.birlashma()
# newclass.newbirlashma()

# 12-misol
# a = [12,23,44,34,24,45]
# l = len(a)

# class Kopaytma:
#     def __init__(self,a,l):
#         self.lst = a
#         self.lenth = l

#     def natija (self):
#         print(sum(a) * l)

# newclass = Kopaytma(a,l)
# newclass.natija()

# 14-misol
# a = [12,3,0,4,0,43,34]
# class Ozgartirish:
#     def __init__(self,a):
#         self.lst = a

#     def natija (self):
#         a.sort()
#         a.reverse()
#         print(a)

# newclass = Ozgartirish(a)
# newclass.natija()

# 15-misol 16-misol
# a = ["hello","good","nice"]
# k = ["blue","green","white"]

# class Lugat:
#     def __init__(self,a,k):
#         self.lst = a
#         self.lst2 = k

#     def birlashma(self):
#         a.extend(k)
#         print(a)

#     def uzunlik(self):
#         print(max(a))
#         print(min(a))
#         print(max(k))
#         print(min(k))

# newclass = Lugat(a,k)
# #newclass.birlashma()
# newclass.uzunlik()

# d = {
#     "ism":"Sunnat"
# }
# class Dictionary:
#     def __init__(self,d):
#         self.dctt = d

#     def Dict(self):
#         print(d.values())

# class2 = Dictionary(d)
# class2.Dict()

