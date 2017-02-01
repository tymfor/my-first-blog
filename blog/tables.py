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
    number_id = tables.columns.TemplateColumn(template_code=u"""<a href="{% url \'measure_detail\' record.id %}">{{ record.category_id }}.{{ record.sub_id }}""", orderable=True, verbose_name='ID')
    name = tables.columns.TemplateColumn(template_code=u"""<a href="{% url \'measure_detail\' record.id %}">{{ record.name }}</a>""", orderable=True, verbose_name='Name')
    sum = tables.columns.TemplateColumn(template_code=u"""{{ record.sum }}""", orderable=True, verbose_name='Functional pertinence score')
    constraints_score = tables.columns.TemplateColumn(template_code=u"""{{ record.constraints_score }}""", orderable=True, verbose_name='Overall score')

    class Meta:
        fields =("number_id","name",'sum',"constraints_score")
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue', 'width':'200%'}
        order_by = '-constraints_score'
        template = 'django_tables2/bootstrap.html'

class MeasureTable_for_selection(tables.Table):
    # name = tables.columns.TemplateColumn(template_code=u"""{{ record.title }}""", orderable=True, verbose_name='Name')
    number_id = tables.columns.TemplateColumn(template_code=u"""<a href="{% url \'measure_detail\' record.id %}">{{ record.category_id }}.{{ record.sub_id }}""", orderable=True, verbose_name='ID')
    name = tables.columns.TemplateColumn(template_code="""<a href="{% url \'measure_detail\' record.id %}">{{ record.name }}</a>""", orderable=True, verbose_name='Name')
    sum = tables.columns.TemplateColumn(template_code=u"""{{ record.sum }}""", orderable=True, verbose_name='Functional pertinence score')
    selection = tables.columns.TemplateColumn(template_code=u"""<input type="checkbox" value="{{ record.measure }}" name="selection"/>""", verbose_name="selection")

    class Meta:
        fields =("selection","number_id","name",'sum')
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue', 'width':'200%'}
        order_by = '-sum'
        template = 'django_tables2/bootstrap.html'
