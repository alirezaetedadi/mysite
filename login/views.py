from django.shortcuts import render
from signin.models import sign_in
from login.forms import login_form
import hashlib

def login(request):
    ok = False
    ein = False
    if request.method == 'POST':
        form=login_form(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            if sign_in.objects.filter(username=f['user'], password=hashlib.md5(f['pas'].encode()).hexdigest()):
                ok= True
                return render(request,'personal.html', {'ok': ok})
            else:
                return render(request,'login/login.html', {'error': False, 'ein':not ein, 'form': form})
        else:
            return render(request,'login/login.html',{'error': True,'form': form, 'ein': ein})
    else:
        form= login_form()
        return render(request,'login/login.html',{'error': False,'form': form,'ein': ein})
