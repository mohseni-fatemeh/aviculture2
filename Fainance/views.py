from django.shortcuts import render
from django import forms
from django.views import View
from django.http import HttpResponse
from .models import CostModel
from .forms import CostForm


def costListView(request):
    # return HttpResponse("لیست هزینه ها")
    costs= CostModel.objects.all()
    
    context = {
        "costList" : costs,
    }

    return render(request,'fainance/costList.html',context)




def costEditview(request):

    costForm = CostForm()

    context = {

        "costForm" : costForm,

    }

    return render(request,"fainance/costEdit.html", context )


def index(request):
    return render(request,"fainance/index.html")