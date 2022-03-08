from django.contrib import admin
from bill.models import Bnda

# Register your models here.
class BndaAdmin(admin.ModelAdmin):
    list_display=('name','bill','paidDate'
    )



admin.site.register(Bnda, BndaAdmin)