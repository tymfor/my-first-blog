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
    available_measures = models.ManyToManyField('StructuralMeasures')
    available_measures_sum_tech_criteria = models.CommaSeparatedIntegerField(max_length=200,default =0)
    available_measures_ahp_sume_peform_criteria = models.CommaSeparatedIntegerField(max_length=200,default =0)

    Perform_weight_1 = models.IntegerField(choices=one_to_ten_choice, default=10, verbose_name="Maturity of technology")
    Perform_weight_2 = models.IntegerField(choices=one_to_ten_choice, default=10, verbose_name="Reliability of performance")
    Perform_weight_3 = models.IntegerField(choices=one_to_ten_choice, default=10, verbose_name="Reliability Uncertainty in design")
    Perform_weight_4 = models.IntegerField(choices=one_to_ten_choice, default=10, verbose_name="Reliability Uncertainty in implementation")
    Perform_weight_5 = models.IntegerField(choices=one_to_ten_choice, default=10, verbose_name="Safety during construction")
    Perform_weight_6 = models.IntegerField(choices=one_to_ten_choice, default=10, verbose_name="Service life required (durability)")
    Perform_weight_7 = models.IntegerField(choices=one_to_ten_choice, default=10, verbose_name="Aesthetics")
    Perform_weight_8 = models.IntegerField(choices=one_to_ten_choice, default=10, verbose_name="Typical cost")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class StructuralMeasures(models.Model):
        name = models.CharField(max_length=200)
        title = models.CharField(max_length=200,default = '')
        category_id = models.IntegerField(default=0)
        # category_description = models.CharField(max_length=200,default = '')
        category_description = models.ForeignKey('Categories_descrption', default=0)
        sub_id = models.IntegerField(default=0)
        tech_1_1 = models.IntegerField(default=0, verbose_name="Rate:1_Falls")
        tech_1_2 = models.IntegerField(default=0, verbose_name="Rate:1_Topples")
        tech_1_3 = models.IntegerField(default=0, verbose_name="Rate:1_Slides")
        tech_1_4 = models.IntegerField(default=0, verbose_name="Rate:1_Spreads")
        tech_1_5 = models.IntegerField(default=0, verbose_name="Rate:1_Flows")
        tech_2_1 = models.IntegerField(default=0, verbose_name="Rate:2_Earth")
        tech_2_2 = models.IntegerField(default=0, verbose_name="Rate:2_Debris")
        tech_2_3 = models.IntegerField(default=0, verbose_name="Rate:2_Rock")
        tech_3_1 = models.IntegerField(default=0, verbose_name="Rate:3_Superficial")
        tech_3_2 = models.IntegerField(default=0, verbose_name="Rate:3_Shallow")
        tech_3_3 = models.IntegerField(default=0, verbose_name="Rate:3_Medium")
        tech_3_4 = models.IntegerField(default=0, verbose_name="Rate:3_Deep ")
        tech_3_5 = models.IntegerField(default=0, verbose_name="Rate:3_VeryDeep")
        tech_4_1 = models.IntegerField(default=0, verbose_name="Rate:4_ModeratelyToFast")
        tech_4_2 = models.IntegerField(default=0, verbose_name="Rate:4_Slow")
        tech_4_3 = models.IntegerField(default=0, verbose_name="Rate:4_VerySlow")
        tech_4_4 = models.IntegerField(default=0, verbose_name="Rate:4_ExtremelySlow")
        tech_5_1 = models.IntegerField(default=0, verbose_name="Rate:5_Artesian")
        tech_5_2 = models.IntegerField(default=0, verbose_name="Rate:5_High")
        tech_5_3 = models.IntegerField(default=0, verbose_name="Rate:5_Low")
        tech_5_4 = models.IntegerField(default=0, verbose_name="Rate:5_Absent")
        tech_6_1 = models.IntegerField(default=0, verbose_name="Rate:6_Rain")
        tech_6_2 = models.IntegerField(default=0, verbose_name="Rate:6_Snowmelt")
        tech_6_3 = models.IntegerField(default=0, verbose_name="Rate:6_Localized")
        tech_6_4 = models.IntegerField(default=0, verbose_name="Rate:6_Stream")
        tech_6_5 = models.IntegerField(default=0, verbose_name="Rate:6_Torrent")
        tech_6_6 = models.IntegerField(default=0, verbose_name="Rate:6_River")
        tech_7 = models.IntegerField(default=0, verbose_name="Rate:7 Maturity")
        tech_8 = models.IntegerField(default=0, verbose_name="Rate:8 Reliability_performance")
        tech_9 = models.IntegerField(default=0, verbose_name="Rate:9 Reliability_design")
        tech_10 = models.IntegerField(default=0, verbose_name="Rate:10 Implementation")
        tech_11 = models.IntegerField(default=0, verbose_name="Rate:11 Safety_during_construction")
        tech_12 = models.IntegerField(default=0, verbose_name="Rate:12 Service life required")
        tech_13 = models.IntegerField(default=0, verbose_name="Rate:13 Aesthetics")
        tech_14 = models.IntegerField(default=0, verbose_name="Rate:14 TypicalCost")
        note_tech_1 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_TypeOfMovement")
        note_tech_2 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_Material")
        note_tech_3 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_DepthOfMovement")
        note_tech_4 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_RateOfMovement")
        note_tech_5 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_Groundwater")
        note_tech_6 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_SurfaceWater")
        note_tech_7 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_Maturity")
        note_tech_8 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_Reliability_peformance")
        note_tech_9 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_Reliability_design")
        note_tech_10 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_Implementation")
        note_tech_11 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_Safety_during_construction")
        note_tech_12 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_Service life required")
        note_tech_13 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_Aesthetics")
        note_tech_14 = models.TextField(default = 'will be updated', verbose_name="Note_applicability_TypicalCost")

        # tech_criteria_AtoF = models.CommaSeparatedIntegerField(max_length=200)
        # performance_and_reliability_criteria = models.CommaSeparatedIntegerField(max_length=200)
        description_text = models.TextField(default = 'will be updated')
        design_text = models.TextField(default = 'will be updated')
        reference = models.TextField(default = 'will be updated')
        figure_captions = models.CommaSeparatedIntegerField(max_length=200, default = 0)
        img_src = models.CommaSeparatedIntegerField(max_length=200, default = 0)
        def __str__(self):
            return self.name

class Categories_descrption(models.Model):
        number = models.IntegerField(default=0)
        name = models.CharField(max_length=200,default = '')
        def __str__(self):
            return self.name
