import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbvproject.settings')
import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import *
faker = Faker()

def populate(n):
    for i in range(n):
        feno = faker.random_int(min=1001, max=9999)
        fename = faker.name(),
        fesal = faker.random_int(min=10000, max=20000)
        feaddr  = faker.city()
        emp_record = Employee.objects.get_or_create(
            eno = feno,
            ename = fename,
            esal = fesal,
            eaddr = feaddr)

n = int(input('Enter Employee Records:'))
populate(n)
print(f'{n} records inserted successfully......')
