from django.contrib import admin

# Register your models here.
from basic.models import User
from basic.models import Todos

admin.site.register(User)
admin.site.register(Todos)
