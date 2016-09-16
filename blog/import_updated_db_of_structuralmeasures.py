# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 19:07:59 2016

@author: jcc
"""

import pickle
from blog import classes_for_safeland_toolbox
from blog.models import Post, StructuralMeasures, Categories_descrption
import sys
sys.modules['classes_for_safeland_toolbox'] = classes_for_safeland_toolbox
from classes_for_safeland_toolbox import StructuralMeasures_back

db_file = r'P:\2015\01\20150145\WP3p2_Stabilization\SafeLand toolbox\AHP toolbox\AHP_algorithm\DB_updated_structural_measure.txt'
db_file_categ_title = r'P:\2015\01\20150145\WP3p2_Stabilization\SafeLand toolbox\AHP toolbox\AHP_algorithm\DB_category_titles.txt'


f = open(db_file,'rb')
measures_2 = pickle.load(f)
f.close()

f = open(db_file_categ_title,'rb')
categ_title = pickle.load(f)
f.close()


for measure in measures_2:
    try:
        temp_measure = StructuralMeasures.objects.get(name=measure.name)
        temp_measure.delete()
    except:
        pass
    temp_dict = {}
    for key in measure.__dict__.keys():
        if key in ['category_description','tech_criteria_AtoF','performance_and_reliability_criteria','note_all']:
            pass
        else:
            temp_dict[key] = getattr(measure,key)
    StructuralMeasures.objects.create(**temp_dict)

for count,categ in enumerate(categ_title):
    temp_categ = Categories_descrption.objects.get(name=categ)
    print(temp_categ.name)
    temp_categ.number=count+1
    print(temp_categ.number)
    temp_categ.save()


for measure in measures_2:
    temp_measure = StructuralMeasures.objects.get(name=measure.name)
    temp_measure.category_description = Categories_descrption.objects.get(number=measure.category_id)
    [[temp_measure.tech_1_1,temp_measure.tech_1_2,temp_measure.tech_1_3,temp_measure.tech_1_4,temp_measure.tech_1_5],
            [temp_measure.tech_2_1,temp_measure.tech_2_2,temp_measure.tech_2_3],
            [temp_measure.tech_3_1,temp_measure.tech_3_2,temp_measure.tech_3_3,temp_measure.tech_3_4,temp_measure.tech_3_5],
            [temp_measure.tech_4_1,temp_measure.tech_4_2,temp_measure.tech_4_3,temp_measure.tech_4_4],
            [temp_measure.tech_5_1,temp_measure.tech_5_2,temp_measure.tech_5_3,temp_measure.tech_5_4],
            [temp_measure.tech_6_1,temp_measure.tech_6_2,temp_measure.tech_6_3,temp_measure.tech_6_4,temp_measure.tech_6_5,temp_measure.tech_6_6]] = measure.tech_criteria_AtoF
    [temp_measure.tech_7,temp_measure.tech_8,temp_measure.tech_9,temp_measure.tech_10,
        temp_measure.tech_11,temp_measure.tech_12,temp_measure.tech_13,temp_measure.tech_14] = measure.performance_and_reliability_criteria
    [temp_measure.note_tech_1,temp_measure.note_tech_2,temp_measure.note_tech_3,temp_measure.note_tech_4,temp_measure.note_tech_5,
    temp_measure.note_tech_6,temp_measure.note_tech_7,temp_measure.note_tech_8,temp_measure.note_tech_10,temp_measure.note_tech_14] = measure.note_all
    temp_measure.save()
