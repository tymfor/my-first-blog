def make_list_array(measure):
    list = [[measure.tech_1_1,measure.tech_1_2,measure.tech_1_3,measure.tech_1_4,measure.tech_1_5],
            [measure.tech_2_1,measure.tech_2_2,measure.tech_2_3],
            [measure.tech_3_1,measure.tech_3_2,measure.tech_3_3,measure.tech_3_4,measure.tech_3_5],
            [measure.tech_4_1,measure.tech_4_2,measure.tech_4_3,measure.tech_4_4],
            [measure.tech_5_1,measure.tech_5_2,measure.tech_5_3,measure.tech_5_4],
            [measure.tech_6_1,measure.tech_6_2,measure.tech_6_3,measure.tech_6_4,measure.tech_6_5,measure.tech_6_6]]
    return list

def available_measures(selected_failure_mode,measures,post):
    sum_tech_criteria = []
    for measure in measures:
        selected_tech_criteria = []
        for count,tech_index in enumerate(selected_failure_mode):
            list_criteria = make_list_array(measure)
            selected_tech_criteria.append(list_criteria[count][tech_index-1])
        if not 0 in selected_tech_criteria:
            post.available_measures.add(measure)
            sum_tech_criteria.append(sum(selected_tech_criteria))
    post.available_measures_sum_tech_criteria = sum_tech_criteria
    return post

def scores(selected_failure_mode,measure):
    selected_tech_criteria = []
    for count,tech_index in enumerate(selected_failure_mode):
        list_criteria = make_list_array(measure)
        selected_tech_criteria.append(list_criteria[count][tech_index-1])
    return selected_tech_criteria
