from django.contrib import admin
from .models import Account

#admin.site.register(Account)
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'address', 'data_of_birth']
    search_fields = ['username', 'address']


# Register your models here.
