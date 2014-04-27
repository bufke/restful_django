from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django import forms
from djangular.forms.angular_model import NgModelFormMixin
from .models import Thing

class ExampleView(TemplateView):
    template_name = "home.html"


class ThingForm(NgModelFormMixin, forms.Form):
    class Meta:
        model = Thing
        
class ThingFormView(TemplateView):
    template_name = 'thing_form.html'

    def get_context_data(self, **kwargs):
        context = super(ThingFormView, self).get_context_data(**kwargs)
        context.update(form=ThingForm())
        return context
