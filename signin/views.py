from django.shortcuts import render
from signin.forms import signin_form
from signin.models import sign_in

def signin(request):
    if request.method == 'POST':
        form = signin_form(request.POST)
        if form.is_valid():
            f=form.cleaned_data
            if sign_in.objects.filter(username=f['user']):
                return render(request,'signin/signin.html',{'form':form,'username_e':True})
            else:
                database_user = sign_in(username=f['user'],password=f['pas'],email=f['email'])
                database_user.save()
    else:
        form = signin_form()
    return render(request,'signin/signin.html', {'form': form,'username_e':False})
