from django.contrib import admin
from .models import ImagesCover,Main

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
   readonly_fields = ('created', 'updated')



admin.site.register(ImagesCover,HomeAdmin)
admin.site.register(Main,HomeAdmin)
