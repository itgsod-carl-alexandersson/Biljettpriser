# coding=utf-8
# Funktionen tickets kollar variabeln age och beroende på dess värde skriver funktionen
# ut hur mycket användaren ska betala i SEK.
# Om man skriver in något annat än positiva tal så kommer funktionen skriva ut vad man gjorde fel och sedan
# starta om sig själv.

def tickets(age):
    if age.isdigit() is True:
        age = int(age)
        if age < 0:
            print "You can't input negative numbers!"
            age = raw_input()
            tickets(age)
        elif 0 <= age <= 17:
            print "10SEK"
            age = raw_input()
            tickets(age)
        elif 18 <= age <= 64:
            print "20SEK"
            age = raw_input()
            tickets(age)
        elif age >= 65:
            print "15SEK"
            age = raw_input()
            tickets(age)
    else:
        print "You need to input a number!"
        age = raw_input()
        tickets(age)
