from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title':'HomePage'
    }
    return render(request,'index.html',data)


def aboutus(request):
    return HttpResponse('1')

def news_details(request):
  return render(request,'news&details.html')

def best_hotel(request):
    return render(request,'besthotel.html')

def world_tourist_spot(request):
    return render(request,'worldtouristspot.html')

def event_management(request):
    return render(request,'eventmanagement.html')

def customer_service(request):
    return render(request,'customerservice.html')

def terms_conditions(request):
    return render(request,'terms&conditions.html')

def facilities(request):
    return render(request,'facilities.html')

def contact(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'aboutus.html')

def customer_view(request):
    return render(request,'customerview.html')

def customer_register(request):
    return render(request,'customerregister.html')