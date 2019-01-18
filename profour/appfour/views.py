from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basics/index.html')

def form_name_view(request):
    form = forms.FormName()

    if form.is_valid():
        #Do something LANGUAGE_CODE
        print("validation success")
        print("NAME: "+form.cleaned_data['name'])
        print("EMAIL: "+form.cleaned_data['email'])
        print("TEXT:"+form.cleaned_data['text'])


    return render(request,'basics/basic_forms.html',{'form':form})
