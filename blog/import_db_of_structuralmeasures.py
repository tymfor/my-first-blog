# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 19:07:59 2016

@author: jcc
"""

import pickle
from blog.classes_for_safeland_toolbox import *
from . models import Post, StructuralMeasures

db_file = r'P:\2015\01\20150145\WP3p2_Stabilization\SafeLand toolbox\AHP toolbox\AHP_algorithm\DB_criteria.txt'

f = open(db_file,'rb')
measures = pickle.load(f)
f.close()

    temp_measure=StructuralMeasures.objects.create()
    temp_measure.name = measure.name
    temp_measure.category_id = measure.category_id
    temp_measure.sub_id = measure.sub_id
    temp_measure.performance_and_reliability_criteria = measure.performance_and_reliability_criteria
    temp_measure.tech_criteria_AtoF = measure.tech_criteria_AtoF
    
for measure in measures:
    temp_dict = {}
    for key in measure.__dict__.keys():
        temp_dict[key] = getattr(measure,key)
    StructuralMeasures.objects.create(**temp_dict)
