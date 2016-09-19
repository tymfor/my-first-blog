# -*- coding: utf-8 -*-
"""
This is functions for AHP process to consider
constrains of decision for Safeland toolbox

by JCC@ngi.no at 2016-09-19
"""


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
    import numpy as np
    comp_mtx = []
    for value_in_raw in points_list:
        temp_row = []
        for value_in_colum in points_list:
            temp_row.append(comparison_and_intesity(value_in_raw,value_in_colum))
        comp_mtx.append(temp_row)
    return np.array(comp_mtx)

def weight_matrix(comp_mtx):
    import numpy as np
    dA, VA = np.linalg.eig(comp_mtx)
    eigen_max = max(dA)
    max_index = np.argmax(dA)
    weight = np.real(VA[:,max_index])/sum(np.real(VA[:,max_index]))
    return weight


def weight_of_alternatives(list_of_points):
    comp_mtx = comparison_matrix(list_of_points)
    w_mtx = weight_matrix(comp_mtx)
    return w_mtx

def array_performance_and_reliability_criteria(measure):
    scores_of_alternatives = [measure.tech_7,measure.tech_8,measure.tech_9,measure.tech_10
                                ,measure.tech_11,measure.tech_12,measure.tech_13,measure.tech_14]
    return scores_of_alternatives

def weights_of_criteria(measure):
    weights_of_criteria = [measure.Perform_weight_1,measure.Perform_weight_2,measure.Perform_weight_3,measure.Perform_weight_4
                                ,measure.Perform_weight_5,measure.Perform_weight_6,measure.Perform_weight_7,measure.Perform_weight_8]
    return weights_of_criteria
#weights_of_criteria = [1,1,1,1,1,1,1,10]    # Example of weight criteria

# Calculate technical weights of alternatives

def AHP_process(availabe_measures,weights_of_criteria):
        import numpy as np
        # Calculate technical weights of alternatives
        num_of_criteria = len(weights_of_criteria)
        weights_matrix = []
        for i_sub_criteria in range(num_of_criteria):
            points_of_alternatives = []
            for measure in availabe_measures:
                scores_of_alternatives = array_performance_and_reliability_criteria(measure)
                points_of_alternatives.append(scores_of_alternatives[i_sub_criteria])
            weights_matrix.append(weight_of_alternatives(points_of_alternatives))
        weights_matrix_of_alternatives = np.array(weights_matrix).T

        # Calculate weights of criteria
        weights_array_on_criteria = weight_of_alternatives(weights_of_criteria)

        # Calculate weight sum of alternative in techncial section
        weight_sum = np.dot(weights_matrix_of_alternatives,weights_array_on_criteria)
        #    order = weight_sum.argsort()[::-1]
        #    ranks = order.argsort()
        return weight_sum
