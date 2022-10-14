from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def primes(a,b):
    primes = []
    for i in range(a,b):
        if i > 1:
            for j in range(2,i):
                if (i % j) == 0:
                    break
            else:
                primes.append(i)
    return primes

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context
    
