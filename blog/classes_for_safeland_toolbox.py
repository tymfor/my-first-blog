class SelectedMeasures():
    def __init__(self):
        self.name = ""
        self.category_id = 0
        self.sub_id = 0
        self.selected_tech_criteria = []
        self.performance_and_reliability_criteria = []
        self.sum_tech_criteria = 0

    def __str__(self):
        return self.name

class StructuralMeasures_back():
    def __init__(self):
        self.name = ""
        self.title = ""
        self.category_id = 0
        self.category_description = ""
        self.sub_id = 0
        self.tech_criteria_AtoF = []
        self.performance_and_reliability_criteria = []
        self.description_text= ""
        self.design_text= ""
        self.figure_captions= []
        self.img_src= []
        self.reference= []
    def __str__(self):
        return self.name
