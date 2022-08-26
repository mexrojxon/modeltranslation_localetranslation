from django.shortcuts import render
from django.views.generic import TemplateView
from exam.models import ExamModel


class HomePageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self, **kwargs).get_context_data()

        context['blog'] = ExamModel.objects.all()
        return context
