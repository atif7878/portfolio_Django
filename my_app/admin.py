from django.contrib import admin
from .models import ContactModel

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "comment")


admin.site.register(ContactModel, CompanyAdmin)