from django.shortcuts import render,HttpResponse
from datetime import datetime
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from payapp.models import Contact
from django.contrib import messages

# Create your views here.

"""
This view function renders the index page to user.
"""
def index(request):
    return render(request, "payapp/index.html")

"""
This view function renders the about page to user.
"""
def about(request):
    return render(request, "payapp/about.html")

"""
This function is responsible for getting POST request and handles all the data given by user and saves in 
Contact model.
"""
def contact(request):
    if request.method == "POST":
        print(request.path)
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        return render(request, "payapp/index.html")
    return render(request, "payapp/contact.html")

# Serialize Django model to Thrift
def django_to_thrift(django_model):
    thrift_event = django_model.to_thrift()
    transport_out = TTransport.TMemoryBuffer()
    protocol_out = TBinaryProtocol.TBinaryProtocol(transport_out)
    thrift_event.write(protocol_out)
    return transport_out.getvalue()
