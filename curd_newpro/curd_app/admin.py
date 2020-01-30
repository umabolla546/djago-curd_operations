from django.contrib import admin
from curd_app.models import emp
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','eaddres']
admin.site.register(emp,EmpAdmin)