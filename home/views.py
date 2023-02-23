from django.shortcuts import render
from django.views.generic import ListView, TemplateView


def index_page(request):
    return render(request, "index.html", context={})
