from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView
# Create your views here.
from django.views import View
from www.models import Link


class Welcome(View):
    def get(self, request):
        return render(request, 'www/index.html')


class LinkListView(ListView):
    model = Link
    template_name = 'www/index.html'


class Redirect(View):
    def get(self, request, path):
        link = Link.objects.get(path=path)
        return HttpResponseRedirect(link.href)
