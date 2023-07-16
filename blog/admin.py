from django.contrib import admin
from .models import Post
from .models import Booking
from .import models
from .models import Employee
from .models import Employee_signups
from.models import admin_signup
from .models import client_signup

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'price']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(models.Category)
admin.site.register(Booking)
admin.site.register(Employee)
admin.site.register(admin_signup)
admin.site.register(client_signup)
admin.site.register(Employee_signups)


