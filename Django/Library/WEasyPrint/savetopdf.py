from django.conf import settings
from django.views.generic import DetailView

from django_weasyprint import CONTENT_TYPE_PNG, WeasyTemplateResponseMixin


class MyModelView(DetailView):
    # vanilla Django DetailView
    model = MyModel
    template_name = 'mymodel.html'


class MyModelPrintView(WeasyTemplateResponseMixin, MyModelView):
    # output of DetailView rendered as PDF
    pdf_stylesheets = [
        settings.STATIC_ROOT + 'css/app.css',
    ]


class MyModelImageView(WeasyTemplateResponseMixin, MyModelView):
    # generate a PNG image instead
    content_type = CONTENT_TYPE_PNG