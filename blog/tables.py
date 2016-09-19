import django_tables2 as tables
from . models import Post, StructuralMeasures

class MeasureTable_wo_constraints(tables.Table):
    # name = tables.columns.TemplateColumn(template_code=u"""{{ record.title }}""", orderable=True, verbose_name='Name')
    name = tables.columns.TemplateColumn(template_code="""<a href="{% url \'measure_detail\' record.id %}">{{ record.name }}</a>""", orderable=True, verbose_name='Name')
    sum = tables.columns.TemplateColumn(template_code=u"""{{ record.sum }}""", orderable=True, verbose_name='Sum of tech criteria')

    class Meta:
        fields =("name",'sum')
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue', 'width':'200%'}
        order_by = '-sum'
        template = 'django_tables2/bootstrap.html'


class MeasureTable_w_constraints(tables.Table):
    # name = tables.columns.TemplateColumn(template_code=u"""{{ record.title }}""", orderable=True, verbose_name='Name')
    name = tables.columns.TemplateColumn(template_code="""<a href="{% url \'measure_detail\' record.id %}">{{ record.name }}</a>""", orderable=True, verbose_name='Name')
    sum = tables.columns.TemplateColumn(template_code=u"""{{ record.sum }}""", orderable=True, verbose_name='Sum of tech criteria')
    constraints_score = tables.columns.TemplateColumn(template_code=u"""{{ record.constraints_score }}""", orderable=True, verbose_name='Scores based on constraints priority')

    class Meta:
        fields =("name","constraints_score",'sum')
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue', 'width':'200%'}
        order_by = '-constraints_score'
        template = 'django_tables2/bootstrap.html'
