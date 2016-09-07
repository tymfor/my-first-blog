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
