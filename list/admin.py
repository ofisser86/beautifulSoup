from django.contrib import admin
from list.models import Company, CompanyOwner


# Register your models here.
class CompanyOwnerInline(admin.TabularInline):
    model = CompanyOwner
    extra = 0

class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]
    # phone = Phone.objects.filter()
    # print(phone)
    # list_display = ('first_name', 'last_name', 'phone')
    inlines = [CompanyOwnerInline]

    class Meta(object):
        model = Company


class CompanyOwnerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CompanyOwner._meta.fields]

    # phone = Phone.objects.filter()
    # print(phone)
    # list_display = ('first_name', 'last_name', 'phone')



    class Meta(object):
        model = CompanyOwner

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyOwner, CompanyOwnerAdmin)