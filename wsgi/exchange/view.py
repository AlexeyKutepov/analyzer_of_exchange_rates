__author__ = 'kutepoval'

from django.shortcuts import render_to_response

def chart(request):
    return render_to_response('chart_currency.html', {'title':'Котировки', 'quotes':'Курсы валют'})