from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Add_new_worker_shift)
admin.site.register(ProfileUserModel)


