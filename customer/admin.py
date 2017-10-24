from django.contrib import admin

from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('c_name', 'c_user_name', 'phone_no')

    def c_user_name(self, obj):
        return obj.user.username

    def c_name(self, obj):
        return "{0} {1}".format(obj.user.first_name, obj.user.last_name)
