from django.contrib import admin

# Register your models here.
from .models import Book   # import your model

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'created_at')   # show these fields in admin list
    search_fields = ('title',)                                # enable search by name
    list_filter = ('title',)                            # add filter sidebar
    ordering = ('-created_at',)   
    
admin.site.register(Book)