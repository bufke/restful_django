from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django import forms
from djangular.forms.angular_model import NgModelFormMixin
from .models import Thing
from django.views.decorators.csrf import csrf_exempt
import json

class ExampleView(TemplateView):
    template_name = "home.html"


class ThingForm(NgModelFormMixin, forms.ModelForm):
    class Meta:
        model = Thing
        
class ThingFormView(TemplateView):
    template_name = 'thing_form.html'

    def get_context_data(self, **kwargs):
        context = super(ThingFormView, self).get_context_data(**kwargs)
        context.update(form=ThingForm(scope_prefix='my_prefix'))
        return context

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(ThingFormView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest('Expected an XMLHttpRequest')
        in_data = json.loads(request.body)
        print in_data
        bound_contact_form = ThingForm(data=in_data['title'])
        obj = bound_contact_form.save()
        print obj.id
