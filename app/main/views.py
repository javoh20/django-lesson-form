from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

# Create your views here.
def MainView(request):
    return render(request, 'index.html')

def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.py')
    else:
        form = ContactForm()

    context = {
        'form' : form,
    }

    return render(request, 'contact.html', context)

