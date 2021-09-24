from django.contrib import admin

# Register your models here.
from user_login.models import UserDetails

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['vchr_name', 'dat_dob','bint_phone']
    list_filter = ['vchr_name', 'dat_dob','bint_phone']
    search_fields = ['vchr_name', 'dat_dob','bint_phone', 'first_name', 'last_name', 'username']
    def full_name(self,obj):
        return obj.first_name+' '+obj.last_name
admin.site.register(UserDetails, UserDetailsAdmin)
