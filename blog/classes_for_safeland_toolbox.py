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

class StructuralMeasures():
    def __init__(self):
        self.name = ""
        self.category_id = 0
        self.sub_id = 0
        self.tech_criteria_AtoF = []
        self.performance_and_reliability_criteria = []
    def __str__(self):
        return self.name