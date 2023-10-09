from django.contrib import admin

# Register your models here.
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name','phone')

admin.site.register(Realtor,RealtorAdmin)