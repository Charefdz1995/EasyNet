from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    ctx = {}
    return render(request,'base.html',context=ctx)


def drawTopology(request):
    ctx = {}
    return render(request,'draw.html',context = ctx)
    
