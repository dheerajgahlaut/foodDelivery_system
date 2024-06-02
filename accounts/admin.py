from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# ----in django admin user password is editable so we want to make it read only---

class CustomUserAdmin(UserAdmin):
    list_display = ('email','first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',) #---when we have 1 item in tuple use , in last---
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    
    
admin.site.register(User,CustomUserAdmin)
admin.site.register(UserProfile)  #regisstered user profile for admin
