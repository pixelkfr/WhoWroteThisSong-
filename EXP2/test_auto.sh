#!/bin/bash
emergents="emergentsInf"
class="classInf"
python ../classification_test1.py classifieurs/$emergents/classifieur1/motifsEm_1_2.txt classifieurs/$emergents/classifieur1/motifsEm_2_1.txt Resultats/$class/test1.res TEST/test1
python ../classification_test2.py classifieurs/$emergents/classifieur2/motifsEm_1_3.txt classifieurs/$emergents/classifieur2/motifsEm_3_1.txt Resultats/$class/test2.res TEST/test2
python ../classification_test3.py classifieurs/$emergents/classifieur3/motifsEm5.txt classifieurs/$emergents/classifieur3/motifsEm6.txt classifieurs/$emergents/classifieur3/motifsEm7.txt Resultats/$class/test3.res TEST/test3
