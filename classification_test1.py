#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getopt, sys, os, re

def classifie_test1( class1 , class2 , fileOut , dirname ):

    # Files - Initialization
    try:
        class1_obj = open( os.path.abspath( class1 ), 'r' )
    except Exception, err:
        msg = "[ERROR] cleaner.py: file %s cannot be open : %s\n" % ( class1, err )
        sys.exit( msg.encode( 'UTF-8' ) )	
    try:
        class2_obj = open( os.path.abspath( class2 ), 'r' )
    except Exception, err:
        msg = "[ERROR] cleaner.py: file %s cannot be open : %s\n" % ( class2, err )
        sys.exit( msg.encode( 'UTF-8' ) )
    try:
        fileOut_obj = open ( os.path.abspath ( fileOut ), 'a' )
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

    listeClassifieur1=[]
    for line in class1_obj:
        listeClassifieur1.append(line.strip())
    listeClassifieur2=[]
    for line2 in class2_obj:
        listeClassifieur2.append(line2.strip())

    #Code principal
    listeChansons = os.listdir(dirname)
    for chanson in listeChansons:
        print chanson
        song = os.path.join(dirname, chanson) 
        chanson_obj = open (song,"r")

        motifsCommuns1=0
        motifsCommuns2=0
        # analyse des motifs de la chanson
        for ligne in chanson_obj:
            if ligne != "\n":
                motif = (re.split("\s",ligne)[0]).strip()
                if motif in listeClassifieur1:
                    motifsCommuns1 = motifsCommuns1 + 1
                if motif in listeClassifieur2: 
                    motifsCommuns2 = motifsCommuns2 + 1

        #choix de l'artiste
        if motifsCommuns1 > motifsCommuns2:
            fileOut_obj.write(chanson + " ; artiste 1" +"\n")
        elif motifsCommuns2 > motifsCommuns1:
			fileOut_obj.write(chanson + " ; artiste 2" +"\n")
        else:
			fileOut_obj.write(chanson + " ; pas de decision prise" +"\n")

if __name__ == "__main__":

    def usage():
        msg = """Usage: classifie_test1( class1 , class2 , fileOut , dirname )
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

    if len( args ) != 4:
        usage()
        sys.exit(2)
    else:
        class1 = args[0]
        class2 = args[1]
        fileOut = args[2]
        dirname = args[3]

    classifie_test1( class1 , class2 , fileOut , dirname )
