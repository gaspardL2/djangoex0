from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views import View

from .forms import CountryForm
# Create your views here.

class CountryFormView(FormView):
    template_name = 'country_form.html'
    form_class = CountryForm # see this class in "forms.py"
    success_url = '/nations/country_success' # want to display search results here

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Search done!")



