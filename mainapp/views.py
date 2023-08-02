from django.shortcuts import render
from item.models import Catagory, Item

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[:9]
    categories = Catagory.objects.all() 
    return render(request,'mainapp/index.html',{'items':items,'categories':categories})
def contact(request):
    return render(request,'mainapp/contact.html')