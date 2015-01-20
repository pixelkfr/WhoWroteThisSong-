#!/bin/bash
emergents="emergentsInf"
value="1000"
python ../emergence.py -t $value motifs_extraits_tdg.txt motifs_extraits_a7x.txt classifieurs/$emergents/classifieur1/motifsEm_1_2.txt
python ../emergence.py -t $value motifs_extraits_a7x.txt motifs_extraits_tdg.txt classifieurs/$emergents/classifieur1/motifsEm_2_1.txt

python ../emergence.py -t $value motifs_extraits_tdg.txt motifs_extraits_alestorm.txt classifieurs/$emergents/classifieur2/motifsEm_1_3.txt
python ../emergence.py -t $value motifs_extraits_alestorm.txt motifs_extraits_tdg.txt classifieurs/$emergents/classifieur2/motifsEm_3_1.txt

python ../emergence.py -t $value motifs_extraits_tdg.txt motifs_extraits_al_a7x.txt classifieurs/$emergents/classifieur3/motifsEm5.txt
python ../emergence.py -t $value motifs_extraits_a7x.txt motifs_extraits_al_tdg.txt classifieurs/$emergents/classifieur3/motifsEm6.txt
python ../emergence.py -t $value motifs_extraits_alestorm.txt motifs_extraits_a7x_tdg.txt classifieurs/$emergents/classifieur3/motifsEm7.txt
