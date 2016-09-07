import django_tables2 as tables
from . models import Post, StructuralMeasures

class MeasureTable(tables.Table):
    name = tables.columns.TemplateColumn(template_code=u"""{{ record.name }}""", orderable=True, verbose_name='Name')
    category_id = tables.columns.TemplateColumn(template_code=u"""{{ record.category_id }}""", orderable=True, verbose_name='Main Category')
    sub_id = tables.columns.TemplateColumn(template_code=u"""{{ record.sub_id }}""", orderable=True, verbose_name='Sub Category')
    sum = tables.columns.TemplateColumn(template_code=u"""{{ record.sum }}""", orderable=True, verbose_name='Sum of tech criteria')
    class Meta:
        fields =("name","category_id",'sub_id','sum')
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        order_by = '-sum'
        template = 'django_tables2/bootstrap.html'
