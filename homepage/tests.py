from django.test import TestCase
from django.shortcuts import render
from ipware.ip import get_ip
from homepage.models import visit

def test(request):
    user_ip=get_ip(request)
    f = visit.objects.latest('id')
    ip=visit(user_ip=user_ip,count=f.count+1)
    ip.save()
    return render(request,'test2.html', {'num': f})

