from django.contrib import admin
from .models import ContactInfo

# Register your models here.
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'subject']
    search_fields = ['name', 'email', 'phone']

admin.site.register(ContactInfo, ContactInfoAdmin)