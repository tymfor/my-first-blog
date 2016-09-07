from django.db import models
from django.utils import timezone
from geoposition.fields import GeopositionField
from geoposition import Geoposition
from .choices import *

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    TypeOfMovement = models.IntegerField(choices=TypeOfMovement_CHOICE, default=1)
    Material = models.IntegerField(choices=Material_CHOICE, default=1)
    DepthOfMovement = models.IntegerField(choices=DepthOfMovement_CHOICE, default=1)
    RateOfMovementAtTimeOfWorks = models.IntegerField(choices=RateOfMovementAtTimeOfWorks_CHOICE, default=1)
    Groundwater = models.IntegerField(choices=Groundwater_CHOICE, default=1)
    SurfaceWater = models.IntegerField(choices=SurfaceWater_CHOICE, default=1)
    position = GeopositionField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    available_measures_category_id = models.CommaSeparatedIntegerField(max_length=200,default = [])
    available_measures_sub_id = models.CommaSeparatedIntegerField(max_length=200,default = [])
    available_measures_sum_tech_criteria = models.CommaSeparatedIntegerField(max_length=200,default = [])

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class SelectedMeasures(models.Model):
        name = models.CharField(max_length=200)
        category_id = models.IntegerField(default=0)
        sub_id = models.IntegerField(default=0)
        selected_tech_criteria = models.CommaSeparatedIntegerField(max_length=200)
        performance_and_reliability_criteria = models.CommaSeparatedIntegerField(max_length=200)
        sum_tech_criteria = models.IntegerField(default=0)
        def __str__(self):
            return self.name

class StructuralMeasures(models.Model):
        name = models.CharField(max_length=200)
        category_id = models.IntegerField(default=0)
        sub_id = models.IntegerField(default=0)
        tech_criteria_AtoF = models.CommaSeparatedIntegerField(max_length=200)
        performance_and_reliability_criteria = models.CommaSeparatedIntegerField(max_length=200)
        def __str__(self):
            return self.name
