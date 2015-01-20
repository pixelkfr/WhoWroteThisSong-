#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt, sys, os, re, codecs
from nltk.corpus import stopwords

alestormTrain = codecs.open("Artistes_raw/Alestorm/alestorm_train_clean.txt", "r", "utf-8")
tdgTrain = codecs.open("Artistes_raw/TDG/tdg_train_clean.txt", "r", "utf-8")
a7xTrain = codecs.open("Artistes_raw/A7X/a7x_train_clean.txt", "r", "utf-8")

nbMotsTotalAlestormTrain = 0
nbLignesAl = 0
for ligneAl in alestormTrain:
    nbLignesAl = nbLignesAl + 1
    listeMots = (ligneAl.strip()).split(" ")
    nbMots = len(listeMots)
#    print ligneAl
#    print "mot phrase : " + str(nbMots)
    nbMotsTotalAlestormTrain = nbMotsTotalAlestormTrain + nbMots

nbMotsMoyenAlestormTrain = nbMotsTotalAlestormTrain / nbLignesAl
#print "nb lignes alestorm : " + str(nbLignesAl)
#print "nb mots : " + str(nbMotsTotalAlestormTrain)
#print "nbMotsMoyenAlestormTrain : " + str(nbMotsMoyenAlestormTrain)

nbMotsTotalA7xTrain = 0
nbLignesA7x = 0
for ligneA7x in a7xTrain:
    nbLignesA7x = nbLignesA7x + 1
    listeMots = (ligneA7x.strip()).split(" ")
    nbMots = len(listeMots)
    nbMotsTotalA7xTrain = nbMotsTotalA7xTrain + nbMots

nbMotsMoyenA7xTrain = nbMotsTotalA7xTrain / nbLignesA7x
#print "nb lignes a7x : " + str(nbLignesA7x)
#print "nbMotsMoyenA7xTrain : " + str(nbMotsMoyenA7xTrain)

nbMotsTotalTdgTrain = 0
nbLignesTdg = 0
for ligneTdg in tdgTrain:
    nbLignesTdg = nbLignesTdg + 1
    listeMots = (ligneTdg.strip()).split(" ")
    nbMots = len(listeMots)
    nbMotsTotalTdgTrain = nbMotsTotalTdgTrain + nbMots

nbMotsMoyenTdgTrain = nbMotsTotalTdgTrain / nbLignesTdg
#print "nb lignes tdg : " + str(nbLignesTdg)
#print "nbMotsMoyenTdgTrain : " + str(nbMotsMoyenTdgTrain)

###############################################################

alestormTest = os.listdir("Artistes_raw/Alestorm/Test/chansons_clean")
tdgTest = os.listdir("Artistes_raw/TDG/Test/chansons_clean")
a7xTest =  os.listdir("Artistes_raw/A7X/Test/chansons_clean")


nbLignesTotalAlestorm = 0
nbMotsTotalAlestorm = 0
for chanson in alestormTest:
    cheminChanson = os.path.join("Artistes_raw/Alestorm/Test/chansons_clean", chanson) 
    chansonOpen = codecs.open(cheminChanson,"r","utf-8")
    for ligne in chansonOpen:
        nbLignesTotalAlestorm = nbLignesTotalAlestorm + 1
        listeMots = (ligne.strip()).split(" ")
        nbMots = len(listeMots)
        nbMotsTotalAlestorm = nbMotsTotalAlestorm + nbMots
nbMotsMoyenAlestorm = nbMotsTotalAlestorm / nbLignesTotalAlestorm
print "nb sentence alestorm : " + str(nbLignesTotalAlestorm)
print "nb mots moyen par ligne alestorm : " + str(nbMotsMoyenAlestorm)

nbLignesTotalA7x = 0
nbMotsTotalA7x = 0
for chanson in a7xTest:
    cheminChanson = os.path.join("Artistes_raw/A7X/Test/chansons_clean", chanson) 
    chansonOpen = codecs.open(cheminChanson,"r","utf-8")
    for ligne in chansonOpen:
        nbLignesTotalA7x = nbLignesTotalA7x + 1
        listeMots = (ligne.strip()).split(" ")
        nbMots = len(listeMots)
        nbMotsTotalA7x = nbMotsTotalA7x + nbMots
nbMotsMoyenA7x = nbMotsTotalA7x / nbLignesTotalA7x
print "nb sentence a7x : " + str(nbLignesTotalA7x)
print "nb mots moyen par ligne a7x : " + str(nbMotsMoyenA7x)

nbLignesTotalTdg = 0
nbMotsTotalTdg = 0
for chanson in tdgTest:
    cheminChanson = os.path.join("Artistes_raw/TDG/Test/chansons_clean", chanson) 
    chansonOpen = codecs.open(cheminChanson,"r","utf-8")
    for ligne in chansonOpen:
        nbLignesTotalTdg = nbLignesTotalTdg + 1
        listeMots = (ligne.strip()).split(" ")
        nbMots = len(listeMots)
        nbMotsTotalTdg = nbMotsTotalTdg + nbMots
nbMotsMoyenTdg = nbMotsTotalTdg / nbLignesTotalTdg
print "nb sentence tdg : " + str(nbLignesTotalTdg)
print "nb mots moyen par ligne tdg : " + str(nbMotsMoyenTdg)
    
