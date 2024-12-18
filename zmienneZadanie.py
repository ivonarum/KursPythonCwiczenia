email = "janek.s@gmail.com"
title = "masz wiadomosc"
content = "tekst wiadomosci"
sender = "Ewa Jankowska"
liczbaZalacznikow = 2
nazwaZalacznika = "plik.txt"

print("tytuł maila: " + title)
print(type(email))

numComlex = 3 + 3j
print(type(numComlex))

averageNum = (4 + 6 + 3) / 3
print(averageNum)

bmi = 70 / (1.7 * 1.7)
print(bmi)

str = "Hello"

#operacje na łańcuchach tekstu:
print(str[0])
print(str[1])
print(str[2:4]) #zakres znakow od do,zakres 'otwarty'
print(str[0] * 3 + str[4])

tekst = """cos tutaj napisane
i reszta \"tekstu\"
w kolejnym wierszu... coś\\"""
print(tekst)

# \n nowa linia
# \t nowy tabulator

print(len(tekst))
print(tekst[4:10])
print(tekst[len(tekst)-1]) # drukowanie ostatniego znaku
str2 = str + tekst
print(str2)
print(str2[7:]) # drukuj od dowolnego znaku do końca