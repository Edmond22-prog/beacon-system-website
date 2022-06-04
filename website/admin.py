from django.contrib import admin
from .models import ContactInfo, Testimonial


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone", "subject"]
    search_fields = ["name", "email", "phone"]


admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Testimonial)