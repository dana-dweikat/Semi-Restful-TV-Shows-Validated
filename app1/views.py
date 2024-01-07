from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages

from .models import *
from .forms import ShowForm


def main(request):
    return redirect('app1:shows')

def shows(request):
    all_shows = Show.objects.all()
    
    context={
        'all_shows' : all_shows
    }
    
    return render(request, 'index.html', context)






def show(request, pk):
    show = Show.objects.get(id=pk)
    
    context={
        'show' : show
    }
    
    return render(request, 'display_show.html', context)


def add(request):
    form = ShowForm(request.POST or None)

    if request.method == "POST":
        errors = Show.objects.validate_input(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                
            context = {
                "form": form
                }
            return render(request, 'add_show.html', context)
            
        
    if form.is_valid():
        new_show = form.save()
        pk = new_show.id
        url = reverse('app1:show', args=[pk])
        return redirect(url)
    
    context = {
        "form": form
    }
    
    return render(request, 'add_show.html', context)

def edit_show(request, pk):
    show = Show.objects.get(id=pk)
    form = ShowForm(request.POST or None, instance=show)
    
    context = {
        "form": form,
        "show": show
    }
    

    if request.method == "POST":
        errors = Show.objects.validate_input(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        
            return render(request, 'edit_show.html', context)

    
        if form.is_valid():
            new_show = form.save()
            pk = new_show.id
            url = reverse('app1:show', args=[pk])
            return redirect(url)
    
    return render(request, 'edit_show.html', context)


def delete_show(request, pk):
    show = Show.objects.get(id=pk)
    show.delete()
    return redirect('app1:shows')

