from django.contrib import admin
from .models import*



# Register your models here.

#admin.site.register(AbstractBaseModel)
admin.site.register(Settings)
admin.site.register(Category)
admin.site.register(About)
admin.site.register(FAQ)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Doctors)
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(DoctorsCategory)


@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    list_display=('title', 'category', 'is_published', 'created_at')
    list_filter=('category', 'is_published')
    search_fields=('title',)
    list_editable=('is_published',)
    list_per_page=2
    
# @admin.register(Settings)
# class SettingsAdmin(admin.ModelAdmin):
    
    
#     def has_add_permission(self, request):
#         return False
    
#     def has_delete_permission(self, request,):
#         return False


    
 