from django.contrib import admin
from app.models import company,employee
# Register your models here.
class companyadmin(admin.ModelAdmin):
    list_display = ('company_name','company_location','type')
    search_fields = ('company_name',)


class employeeadmin(admin.ModelAdmin):
    list_display = ('name','phone','company')
    list_filter = ('name',)


admin.site.register(company,companyadmin)
admin.site.register(employee,employeeadmin)