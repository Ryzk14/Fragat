from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'client_registration/home.html'

class AboutPageView(TemplateView):
    template_name = 'client_registration/about.html'