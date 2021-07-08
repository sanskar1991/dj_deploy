from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import NetworkList, AddSubList, NewExposure
from .forms import NetListForm, AddSubListForm, NewExpForm


# Create your views here.
def index(request):
    """Home page"""
    return HttpResponse("<h1>Hi! You are at the Home page.</h1>")

def add_sub_list(request):
    """AddSubnetList"""
    add_sub_list = AddSubList.objects.all()
    context = {'add_sub_list':add_sub_list}
    return render(request, 'add_sub_list.html', context)

def network_list(request):
    """AddSubnetList"""
    network_list = NetworkList.objects.all()
    context = {'network_list':network_list}
    return render(request, 'network_list.html', context)

def new_exposure(request):
    """NewExposure"""
    if request.method == 'GET':
        new_expo = NewExposure.objects.all()
        context = {'new_expo':new_expo}
        return render(request, 'new_expo.html', context)
    elif request.method == 'POST':
        print('ddddd')
        is_present = True
        data = request.POST.get('button1')
        expo = NewExposure.objects.get(new_sub_name=data)
        network_list = NetworkList.objects.filter(subnet_name=data).first()
        if not network_list:
            add_sub_list = AddSubList.objects.filter(acc_subnet_name=data).first()
            if not add_sub_list:
                is_present = False
            else:
                expo.new_sub_value = add_sub_list.acc_subnet_value
        else:
            expo.new_sub_value = network_list.subnet_value
        expo.save()
        new_expo = NewExposure.objects.all()
        
        context = {"is_present":is_present, 'new_expo':new_expo, 'data':data}
        return render(request, 'new_expo.html', context)
        
        
def check_values(request):
    
    form = NewExpForm(request.POST or None)
    if request.method == 'GET':
        if form.is_valid():
            expo = form.save()
            return render(request, 'add_values.html', {'expo': expo})
        context = {
            "form": form,
        }
        return render(request, 'add_values.html', context)



def addition(request):
    """Check"""
    print("111")
    return 'Hello'
    if request.GET.get('mybtn2'):
        return HttpResponse("Hello WOrld")
    print("shaj")
    # print(data)