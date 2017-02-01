from django import forms
from .models import Post,StructuralMeasures
from .choices import *

class Postform(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text','position','TypeOfMovement','Material','DepthOfMovement','RateOfMovementAtTimeOfWorks','Groundwater','SurfaceWater')

class Viewform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text','position','TypeOfMovement','Material','DepthOfMovement','RateOfMovementAtTimeOfWorks','Groundwater','SurfaceWater')

class Measuresform(forms.ModelForm):
    class Meta:
        model = StructuralMeasures
        fields = ('name','category_id','sub_id')

class Constraintform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Perform_weight_1','Perform_weight_2','Perform_weight_3','Perform_weight_4','Perform_weight_5','Perform_weight_6','Perform_weight_7','Perform_weight_8')
        help_texts = {
            'Perform_weight_1': 'High rating means that the maturity of technology is an important factor',
            'Perform_weight_2': 'High rating means that the performance of the mitigation measure is important',
            'Perform_weight_3': 'High rating means that simplicity in design is important',
            'Perform_weight_4': 'High rating means the solution needs to be easily to be constructed and implemented',
            'Perform_weight_5': 'High rating means that safety and security during construction are important',
            'Perform_weight_6': 'High rating means that the durability of the mitigation measure is important',
            'Perform_weight_7': 'High rating means the mitigation measure should have high aesthetic quality',
            'Perform_weight_8': 'High rating means that economic constraints are relevant',
        }
