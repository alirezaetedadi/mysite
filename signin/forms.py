from django import forms

class signin_form( forms.Form ):
    user = forms.CharField(max_length=50, min_length=5, label='نام کاربری')
    pas = forms.CharField(min_length=8, label='کلمه عبور')
    email = forms.EmailField(required=False, label='پست الکترونیکی')
