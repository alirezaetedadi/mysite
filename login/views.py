from django.shortcuts import render
from django.template import RequestContext
from django.http import Http404

def dic(request):
    return {
        'a': 'ali',
        'b': 'reza'
    }
def test(request):
    return render(request,'test.html',{'c':'ETEDADI','a': 'ali','b': '<b>reza</b>'})

