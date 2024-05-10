from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
import requests
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Rate
from .serializers import RateSerializer
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, Http404

# Create your views here.

# path("conversion/<str:currency1>/<str:currency2>/<str:amount_of_currency1>/",
from rest_framework import generics

"""
This class is responsible for getting queryset from Rate model and implements the logic of get api
responsible in currency conversion.
"""
class CurrencyConverter(generics.ListCreateAPIView):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()

    def get(self, request, *args, **kwargs):
        currency1 = self.kwargs['currency1']
        currency2 = self.kwargs['currency2']
        amount_of_currency1 = float(self.kwargs['amount_of_currency1'])

        try:
            # This query filters the currency given and gives the rate related to it.
            rate = float(Rate.objects.get(currency1=currency1, currency2=currency2).rate)
        except Rate.DoesNotExist:
            return Response({'error': 'One or both currencies not supported'}, status=status.HTTP_400_BAD_REQUEST)

        #converts the amount received by multiplying by rate queried from model
        converted_amount = round(amount_of_currency1 * rate, 4)
        data = {'rate': rate, 'converted_amount': converted_amount}
        return Response(data)


"""
This view function can only be accessed by logged in user.
This function is responsible for calling the get api in this page which gives the converted amount and rate 
if currency are given, by default base currency is gbp here.
# This is an extra functionality implemented by me.
"""
@login_required(login_url='login')
def currency_converter_page(request):
    if request.method == 'GET':
        currency1 = request.GET.get('currency1', default="gbp")
        currency2 = request.GET.get('currency2', default="gbp")
        amount_of_currency1 = request.GET.get('amount_of_currency1',default=1000)

        api_url = f"http://localhost:8000/conversion/{currency1}/{currency2}/{amount_of_currency1}/"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            rate = data['rate']
            converted_amount = data['converted_amount']
            context = {
                'currency1': currency1,
                'amount_of_currency1': amount_of_currency1,
                'rate': rate,
                'currency2': currency2,
                'converted_amount': converted_amount,
            }
            return render(request, "convert_currency_api/currency_converter.html", context)
        else:
            error_message = response.text
            context = {'error_message': error_message}
            return render(request, "convert_currency_api/currency_converter.html", context)