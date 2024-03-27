from django.contrib import admin
from .models import room, booking, ReviewRating

# Register your models here.
admin.site.register(room)
admin.site.register(booking)
admin.site.register(ReviewRating)

class Reviewadmin(admin.ModelAdmin):
    list_display=['user','room','rating','created_at']
    readonly_fields=['created_at','updated_at']