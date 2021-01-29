from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request,'base.html')
def new_search(request):
    search = request.POST.get('search')
    print(search)
    stuffs={
        'search' : search
    }
    return render(request,'khalil/lamharchi.html',stuffs)
