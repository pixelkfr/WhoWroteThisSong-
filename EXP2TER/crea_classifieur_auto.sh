#!/bin/bash
emergents="emergentsInf"
value="1000"
python ../emergence.py -t $value motifs_extraits_a7x.txt motifs_extraits_tdg.txt classifieurs/$emergents/classifieur1/motifsEm_1_2.txt
python ../emergence.py -t $value motifs_extraits_tdg.txt motifs_extraits_a7x.txt classifieurs/$emergents/classifieur1/motifsEm_2_1.txt
