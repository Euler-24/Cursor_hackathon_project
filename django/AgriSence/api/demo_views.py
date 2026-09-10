from django.views.generic import TemplateView


class AccueilDemoView(TemplateView):
    template_name = "demo.html"
