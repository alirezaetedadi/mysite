from django import forms

class login_form(forms.Form):
    user = forms.CharField(max_length=50,label='نام کاربری')
    pas = forms.CharField(max_length=8,label='رمز عبور')
