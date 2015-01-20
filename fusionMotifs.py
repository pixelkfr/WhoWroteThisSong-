#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fusion des motifs de deux artistes, en accroissant le support
"""

import getopt, sys, os, re

def calcul_em(fileB1 , fileB2 , fileOut):

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
    for line in fileB1_obj:
        if line != "\n":
            motif = (re.split("sup",line)[0]).strip()
            support = line.split("sup=")[1] 
            dicoB1[motif] = support

    for line2 in fileB2_obj:
        if line2 != "\n":
            motif = (re.split("sup",line2)[0]).strip()
            support = line2.split("sup=")[1]  
            if motif in dicoB1.keys():
                print "deja dans le dico " + str(support) + " et yavait deja " + str(dicoB1[motif])
                dicoB1[motif] = int(dicoB1[motif]) + int(support)
                print "somme = " + str(dicoB1[motif])                
            else:                 
                dicoB1[motif] = support

    for cle, valeur in dicoB1.items():
        fileOut_obj.write(cle + " sup=" + str(valeur) + "\n")

if __name__ == "__main__":

    def usage():
        msg = """Usage: script.py FILE1 FILE2 FILEOUT """
        sys.stderr.write( msg.encode( 'UTF-8' ) )

    args = sys.argv[1:]

    if len( args ) != 3:
        usage()
        sys.exit(2)
    else:
        fileB1 = args[0]
        fileB2 = args[1]
        fileOut = args[2]

    calcul_em( fileB1 , fileB2 , fileOut )
