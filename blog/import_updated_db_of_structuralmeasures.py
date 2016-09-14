# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 19:07:59 2016

@author: jcc
"""

import pickle
from blog import classes_for_safeland_toolbox
from blog.models import Post, StructuralMeasures
import sys
sys.modules['classes_for_safeland_toolbox'] = classes_for_safeland_toolbox
from classes_for_safeland_toolbox import StructuralMeasures_back

db_file = r'P:\2015\01\20150145\WP3p2_Stabilization\SafeLand toolbox\AHP toolbox\AHP_algorithm\DB_updated_structural_measure.txt'

f = open(db_file,'rb')
measures_2 = pickle.load(f)
f.close()

for measure in measures_2:
    temp_measure = StructuralMeasures.objects.get(name=measure.name)
    temp_measure.delete()
    temp_dict = {}
    for key in measure.__dict__.keys():
        temp_dict[key] = getattr(measure,key)
    StructuralMeasures.objects.create(**temp_dict)
