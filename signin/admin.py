from django.contrib import admin
from signin.models import sign_in

class sign(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email')

admin.site.register(sign_in,sign)

