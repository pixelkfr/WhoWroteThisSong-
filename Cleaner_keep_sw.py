#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt, sys, os, re
from nltk.corpus import stopwords

"""
Fichier de prétraitements des textes de chansons.
Les fichiers non nettoyés sont en format "une phrase par ligne".
Une séquence par ligne.
Ajout des points en fin de séquences (phrases).
Suppression des lignes vides.
"""

def cleaner( fileIn, fileOut, logFile=None ):

    # Files - Initialization
    try:
        fileInObj = open( os.path.abspath( fileIn ), 'r' )
    except Exception, err:
        msg = "[ERROR] cleaner.py: file %s cannot be open : %s\n" % ( fileIn, err )
        sys.exit( msg.encode( 'UTF-8' ) )	
    try:
        fileOutObj = open( os.path.abspath( fileOut ), 'a' )
    except Exception, err:
        msg = "[ERROR] cleaner.py: file %s cannot be open : %s\n" % ( fileOut, err )
        sys.exit( msg.encode( 'UTF-8' ) )
    if logFile:
        try:
            logFileObj = open( os.path.abspath( logFile ), 'a' )
        except Exception, err:
            msg = "[ERROR] cleaner.py: file %s cannot be open : %s\n" % ( logFile, err )
            sys.exit( msg.encode( 'UTF-8' ) )
    else:
        logFileObj = sys.stdout

    # Cleaning
    for line in fileInObj:

        newLine = ""
        # mise en minuscule
        line = line.lower()

        listOfWords = re.findall("\w+",line)

        # Si la ligne contient des mots, sinon, on arrête là le traitement
        if len(listOfWords)!=0:
            # suppression des mots outils
            for w in listOfWords:
                #convertion des abréviations en mots
                if w == "re":
                    w = "are"
                if w == "m":
                    w = "am"
                if w == "ve":
                    w = "have"
                if w == "ll":
                    w = "will"

                newLine = newLine + w + " "

            # on ajoute un point à la fin de la phrase si elle n'est pas vide à cause des stopwords
            if newLine.strip() != "":
                newLine = newLine.strip() + "."

                fileOutObj.write(newLine+"\n")

		
if __name__ == "__main__":

    def usage():
        msg = """Usage: cleaner.py [-L LOGFILE] FILEIN FILEOUT
               -l --log=FILE		write log and errors in a FILE """
        sys.stderr.write( msg.encode( 'UTF-8' ) )
    try:
		opts, args = getopt.getopt( sys.argv[1:], "l:", ["log="] )
    except getopt.GetoptError, err:
        sys.stderr.write( str( err ) )
        usage()
        sys.exit(2)

    logFile = None
    for o, a in opts:
        if o in ( "-l", "--log" ):
            logFile = a.strip()
        else:
            assert False, "unhandled option"

    if len( args ) != 2:
        usage()
        sys.exit(2)
    else:
        fileIn = args[0]
        fileOut = args[1]

    cleaner( fileIn, fileOut, logFile )
