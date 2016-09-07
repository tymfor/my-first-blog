# -*- coding: utf-8 -*-
"""
Select potential mitigation measures
@author: jcc@ngi.no
"""
# defined failure mode
selected_failure_mode = [5,2,3,2,2,2]   # size of technical criteria

def Measures_by_criteria(measures,selected_failure_mode):
    # function to select all available measures by failure criteria
    # it needs oject class 'SelectedMeasures()' from classes_for_safeland_toolbox
    avalilable_measures = []
    for measure in measures:
        selected_tech_criteria = []
        for count,tech_index in enumerate(selected_failure_mode):
            selected_tech_criteria.append(measure.tech_criteria_AtoF[count][tech_index-1])
        if not 0 in selected_tech_criteria:
            temp_measure = SelectedMeasures()
            temp_measure.name = measure.name
            temp_measure.category_id = measure.category_id
            temp_measure.sub_id = measure.sub_id
            temp_measure.performance_and_reliability_criteria = measure.performance_and_reliability_criteria
            temp_measure.selected_tech_criteria = selected_tech_criteria
            temp_measure.sum_tech_criteria = sum(selected_tech_criteria)
            avalilable_measures.append(temp_measure)
    return avalilable_measures

avalilable_measures = Measures_by_criteria(measures,selected_failure_mode)


# print selected measures sorted by technical criteria
for avalilable_measure in sorted(avalilable_measures, key = lambda x:x.sum_tech_criteria, reverse=True):
    print ("%d.%d %s \t\t %d \t %s \t %s"%(avalilable_measure.category_id,avalilable_measure.sub_id,avalilable_measure.name,avalilable_measure.sum_tech_criteria," ".join([str(a) for a in avalilable_measure.selected_tech_criteria])," ".join([str(a) for a in avalilable_measure.performance_and_reliability_criteria])))

# print selected measures sorted by cost and technical criteria
for avalilable_measure in sorted(avalilable_measures, key = lambda x:(x.sum_tech_criteria,x.performance_and_reliability_criteria[-1]), reverse=True):
    print ("%d.%d %s \t\t %d \t %s \t %s"%(avalilable_measure.category_id,avalilable_measure.sub_id,avalilable_measure.name,avalilable_measure.sum_tech_criteria," ".join([str(a) for a in avalilable_measure.selected_tech_criteria])," ".join([str(a) for a in avalilable_measure.performance_and_reliability_criteria])))

# print selected measures sorted by cost and technical criteria
for avalilable_measure in avalilable_measures:
    print ("%d.%d %s \t\t %d \t %s \t %s"%(avalilable_measure.category_id,avalilable_measure.sub_id,avalilable_measure.name,avalilable_measure.sum_tech_criteria," ".join([str(a) for a in avalilable_measure.selected_tech_criteria])," ".join([str(a) for a in avalilable_measure.performance_and_reliability_criteria])))

points_of_alternatives = [5,1,3,4];

def comparison_and_intesity(A,B):
    # Return importance of intensity between A and B
    # A and B ranges between 1 to 10
    # intensity is estimated by A-B.
    # if abs(A-B) is equal to zero, intensity = 1
    # if abs(A-B) is equal to 1, intensity = 2
    # in other cases, intensity = int(abs(A-B)/2)*2+1
    import numpy as np
    difference = A-B
    if np.abs(difference)>1:
        intensity_of_importance = int(np.abs(difference)/2)*2+1
        intensity_of_importance = np.minimum(9,intensity_of_importance)

    elif difference == 0:
        intensity_of_importance = int(1)
    else:
        intensity_of_importance = int(2)

    if difference<0:
        intensity_of_importance = 1./intensity_of_importance
    return intensity_of_importance

def comparison_matrix(points_list):
    comp_mtx = []
    for value_in_raw in points_list:
        temp_row = []
        for value_in_colum in points_list:
            temp_row.append(comparison_and_intesity(value_in_raw,value_in_colum))
        comp_mtx.append(temp_row)
    return np.array(comp_mtx)

def weight_matrix(comp_mtx):
    dA, VA = np.linalg.eig(comp_mtx)
    eigen_max = max(dA)
    max_index = np.argmax(dA)
    weight = np.real(VA[:,max_index])/sum(np.real(VA[:,max_index]))
    return weight


def weight_of_alternatives(list_of_points):
    comp_mtx = comparison_matrix(list_of_points)
    w_mtx = weight_matrix(comp_mtx)
    return w_mtx



# Calculate technical weights of alternatives
num_of_criteria = 6
weights_matrix = []
for i_sub_criteria in range(num_of_criteria):
    points_of_alternatives = []
    for measure in avalilable_measures:
        points_of_alternatives.append(measure.selected_tech_criteria[i_sub_criteria])
    weights_matrix.append(weight_of_alternatives(points_of_alternatives))
weights_matrix = np.array(weights_matrix).T

# Calculate weights of criteria
weights_of_criteria = []
for i in range(num_of_criteria):
    weights_of_criteria.append(1)
weights_of_criteria = weight_of_alternatives(weights_of_criteria)

# Calculate weight sum of alternative in techncial section
weight_sum = np.dot(weights_matrix,weights_of_criteria)
order = weight_sum.argsort()[::-1]
ranks = order.argsort()

# print selected measures sorted by cost and technical criteria
for i in order:
    avalilable_measure=avalilable_measures[i]
    print ("%d.%d %s \t\t %d \t %s \t %s"%(avalilable_measure.category_id,avalilable_measure.sub_id,avalilable_measure.name,avalilable_measure.sum_tech_criteria," ".join([str(a) for a in avalilable_measure.selected_tech_criteria])," ".join([str(a) for a in avalilable_measure.performance_and_reliability_criteria])))

# print selected measures sorted by cost and technical criteria
for avalilable_measure,rank,weight in zip(avalilable_measures,ranks,weight_sum):
    print ("%d\t%d.%d %s \t\t\t %d %.5f"%(rank,avalilable_measure.category_id,avalilable_measure.sub_id,avalilable_measure.name,avalilable_measure.sum_tech_criteria,weight))

# print selected measures sorted by cost and technical criteria
for avalilable_measure,rank,weight in sorted(zip(avalilable_measures,ranks,weight_sum), key = lambda t: t[1]):
    print ("%2d %2d.%d %50s %d %.5f"%(rank,avalilable_measure.category_id,avalilable_measure.sub_id,avalilable_measure.name,avalilable_measure.sum_tech_criteria,weight))
