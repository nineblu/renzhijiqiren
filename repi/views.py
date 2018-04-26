from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import connection
from . import models
from . import run
import datetime

# Create your views here.
def che(request):
    if request.method=='POST':
        address=request.POST.get('address',None)
        print(str(address))
        ads=run.runner(str(address))
        return render(request, 'repi/index.html',{'ads':ads})
    return render(request,'repi/index.html')



