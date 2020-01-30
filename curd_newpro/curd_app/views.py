from django.shortcuts import render,redirect
from curd_app.models import emp
from curd_app import forms

# Create your views here.

def curd_view(request):
    form=emp.objects.all()
    return render(request,'curd.html',{'form':form})

def insert_view(request):
    form=forms.empform()
    if request.method=='POST':
        form = forms.empform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'insert.html',{'form':form})