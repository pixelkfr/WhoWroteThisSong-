#!/bin/bash
dossierTest="$1"
dossierSortie="$2"
for file in $dossierTest/*; do
    nomfichier=`echo $file | cut -d / -f5 | cut -d . -f1`
    echo $nomfichier
    python Cleaner_keep_sw.py $file $dossierSortie/$nomfichier.txt
done
