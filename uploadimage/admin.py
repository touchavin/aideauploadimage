from django.contrib import admin
from.models import  Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['job_id', 'job_name', 'job_data', 'job_time', 'job_officerid', 'job_picture', 'vol_name', 'eq_name', 'subeq_name', 'abnor_name','abnor_other', 'nameimageold', 'nameimagenew', 'pathimage', 'show_image']
    list_filter = ['job_name']
    search_fields = ['job_name', 'vol_name', 'abnor_name']


           


admin.site.register(Image, ImageAdmin)


