from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm

def contact(request):
    if request.method=='POST':
        if form.is_valid():
            cleaned_data=form.cleaned_data
            print(cleaned_data)
            form=MyForm()
            return HttpResponse("Yay! You are a human")
        else:
            return HttpResponse("Oops! Bot Suspected")
    else:
        form=MyForm()
    return render(request,'index.html',{'form':form})
        
    