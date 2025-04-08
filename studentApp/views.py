from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def addStudent(request):    
    if request.method == 'POST':
        form = forms.ModelForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Student added successfully!')
            return redirect('showStudent')
    else:
        form = forms.ModelForms()
    return render(request, 'createStudent.html', {'form': form})

def showStudent(request):
    students = models.Form.objects.all()
    return render(request, 'showStudent.html', {'students': students})

@login_required(login_url='login_view')
def update(request,id):
    formdata = models.Form.objects.get(id=id)
    form = forms.ModelForms(instance=formdata)
    if request.method == 'POST':
        form = forms.ModelForms(request.POST, request.FILES, instance=formdata)
        if form.is_valid():
            form.save()
            return redirect('showStudent')
    return render(request, 'update.html', {'form': form, 'edit': True})

@login_required(login_url='login_view')
def delete(request,id):
    formdata = models.Form.objects.get(id=id)
    formdata.delete()
    messages.success(request,'Form deleted successfully!')
    return redirect('showStudent')