import django_tables2 as tables
from . models import Post, StructuralMeasures

class MeasureTable(tables.Table):
    # name = tables.columns.TemplateColumn(template_code=u"""{{ record.title }}""", orderable=True, verbose_name='Name')
    name = tables.columns.TemplateColumn(template_code="""<a href="{% url \'measure_detail\' record.id %}">{{ record.name }}</a>""", orderable=True, verbose_name='Name')
    category_id = tables.columns.TemplateColumn(template_code=u"""{{ record.category_id }}""", orderable=True, verbose_name='Category ID')
    sum = tables.columns.TemplateColumn(template_code=u"""{{ record.sum }}""", orderable=True, verbose_name='Sum of tech criteria')
    class Meta:
        fields =("name",'sum',"category_id")
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        order_by = '-sum'
        template = 'django_tables2/bootstrap.html'
