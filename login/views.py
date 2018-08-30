import simplejson as simplejson
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from pip._vendor.requests import Response

from signin.models import sign_in
from login.forms import login_form
import hashlib
import json


@csrf_exempt
def login(request):

    data = {'a': 'doroste'}
    if request.method == 'POST':
        form=login_form(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            if sign_in.objects.filter(username=f['user'], password=hashlib.md5(f['pas'].encode()).hexdigest()):
                return JsonResponse(data)
            else:
                return JsonResponse({'data': 'True'})
        else:
            return JsonResponse({'data': 'True'})
    else:
        form= login_form()
        return render(request,'login/login.html',{'form':form})
