import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','curd_newpro.settings')
import django
django.setup()

from curd_app.models import *
from faker import Faker
from random import *
fake=Faker()
def populate(n):
    for i in range(n):
        feno=randint(100,999)
        fname=fake.name()
        feaadres=fake.city()
        emp_record=emp.objects.get_or_create(eno=feno,ename=fname,eaddres=feaadres)

populate(20)
