from django.contrib import admin
from.models import  Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['Day', 'Time', 'Customer_number', 'Circuit', 'Category', 'Accessory', 'Case', 'nameimageold', 'nameimagenew', 'pathimage', 'pathoraclecloud', 'show_image']
    list_filter = ['Case']
    search_fields = ['Accessory', 'Case', 'Circuit']




admin.site.register(Image, ImageAdmin)


