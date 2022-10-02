from django.urls import path

from .views import CountryFormView, FormSuccessView

urlpatterns = [path('country_views/', CountryFormView.as_view(), name='country_form'),
    path('form_success/', FormSuccessView.as_view(), name='form_success')


]