from django.shortcuts import render
from .models import Tiny
from .forms import TinyForm

def tinys_home(request):
    return render(request, 'tinys/tinys_home.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TinyForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = form.errors

    form = TinyForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'tinys/create.html', data)
