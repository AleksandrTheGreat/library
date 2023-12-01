from django.shortcuts import render
from .forms import *

def main(request):
    poisk = search()
    data = {'poisk':poisk}
    return render(request,'main.html', context=data)