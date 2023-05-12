from django.contrib import admin
from organizations.models import Organization
# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ['name','tickets_sold','organization_user','created_at']
    list_filter = ['name','creator__email']
    search_fields = ['name','creator__email',]
    
    @admin.display()
    def organization_user(self, obj):
        return obj.creator.email

admin.site.register(Organization, OrganizationAdmin)