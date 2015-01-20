#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pour gerer la croissance infinie, passer 1000 en parametre
"""

import getopt, sys, os, re

def calcul_em(taux , fileB1 , fileB2 , fileOut):

    # Files - Initialization
    try:
        fileB1_obj = open( os.path.abspath( fileB1 ), 'r' )
    except Exception, err:
        msg = "[ERROR] cleaner.py: file %s cannot be open : %s\n" % ( fileB1, err )
        sys.exit( msg.encode( 'UTF-8' ) )	
    try:
        fileB2_obj = open( os.path.abspath( fileB2 ), 'r' )
    except Exception, err:
        msg = "[ERROR] cleaner.py: file %s cannot be open : %s\n" % ( fileB2, err )
        sys.exit( msg.encode( 'UTF-8' ) )
    try:
        fileOut_obj = open ( os.path.abspath ( fileOut ), 'a' )
    except Exception, err:
        msg = "[ERROR] cleaner.py: file %s cannot be open : %s\n" % ( fileOut, err )
        sys.exit( msg.encode( 'UTF-8' ) )        


    #Code principal
    dicoB1 = dict()
    dicoB2 = dict()
    for line in fileB1_obj:
        if line != "\n":
            motif = re.split("\s",line)[0]
            support = (re.split("\s",line)[1]).split("=")[1] 
            dicoB1[motif] = support

    for line2 in fileB2_obj:
        if line2 != "\n":
            motif = re.split("\s",line2)[0]
            support = (re.split("\s",line2)[1]).split("=")[1]   
            dicoB2[motif] = support

    for key in dicoB1.keys():
        if key not in dicoB2.keys():
            #on a une croissance infinie de M dans B1 par rapport à B2 car M n'est pas dans B2
            fileOut_obj.write(key + "\n")
        else: #on a le motif dans les deux corpus
            if taux != 1000: #gestion du cas infini, on fait pas ce qui suit
                tauxDeCroissance = int(dicoB1[key]) / int(dicoB2[key])
                if tauxDeCroissance >= taux :
                    fileOut_obj.write(key + "\n")

if __name__ == "__main__":

    def usage():
        msg = """Usage: calcul_em.py [-t TAUX] FILE1 FILE2 FILEOUT """
        sys.stderr.write( msg.encode( 'UTF-8' ) )
    try:
		opts, args = getopt.getopt( sys.argv[1:], "t:", ["taux="] )
    except getopt.GetoptError, err:
        sys.stderr.write( str( err ) )
        usage()
        sys.exit(2)

    taux = None
    for o, a in opts:
        if o in ( "-t", "--taux" ):
            taux = a.strip()
        else:
            assert False, "unhandled option"

    if len( args ) != 3:
        usage()
        sys.exit(2)
    else:
        fileB1 = args[0]
        fileB2 = args[1]
        fileOut = args[2]

    calcul_em( taux, fileB1 , fileB2 , fileOut )
