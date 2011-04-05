from datetime import datetime
from opendata.models import *
from django.contrib import admin

class UrlImageInline(admin.TabularInline):
    model = UrlImage
    extra = 1
    
class UrlInline(admin.TabularInline):
    model = Url
    extra = 1
    verbose_name = 'Resource Url'
    verbose_name_plural = 'Resource Urls'

class ResourceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':[('name', 'is_published'), 'description', 'short_description', 'usage', 
            ('organization', 'division'), ('contact_phone', 'contact_email', 'contact_url')], 'classes':['wide']}),
        ('Metadata Fields ', {'fields':['release_date', ('time_period', 'update_frequency'), 
            'updates',
            ('data_formats', 'area_of_interest'), 'proj_coord_sys', 
            ('created_by', 'created'), ('last_updated_by', 'last_updated'),
            'metadata_contact','metadata_notes', 'data_types', 'coord_sys', 'tags', ], 'classes':['wide']})
    ]
    readonly_fields = ['created_by', 'created', 'last_updated_by', 'last_updated']
    inlines = [UrlInline,]
    
    list_display = ('name', 'organization', 'release_date', 'is_published')
    search_fields = ['name', 'description', 'organization']
    list_filter = ['tags', 'url__url_type', 'is_published']
    date_heirarchy = 'release_date'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created = datetime.now()
        
        obj.last_updated_by = request.user
        obj.save()

class UrlImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ['image', 'title', 'description']
    
class UrlAdmin(admin.ModelAdmin):
    list_display = ('url_label', 'url_type', 'url')
    inlines = [UrlImageInline,]
    list_filter = ['url_type',]
    
class CoordSystemAdmin(admin.ModelAdmin):
    list_display = ('EPSG_code', 'name')
    search_fields = ['name', 'EPSG_code', 'description']
    
admin.site.register(Tag)
admin.site.register(UpdateFrequency)
admin.site.register(UrlType)
admin.site.register(CoordSystem, CoordSystemAdmin)
admin.site.register(DataType)
admin.site.register(Url, UrlAdmin)
admin.site.register(UrlImage, UrlImageAdmin)
admin.site.register(Resource, ResourceAdmin)