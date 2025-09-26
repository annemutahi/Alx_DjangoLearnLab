from django.contrib import admin

# Register your models here.
from .models import Book   # import your model

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'created_at')  
    search_fields = ('title',)                               
    list_filter = ('title',)                           
    ordering = ('-created_at',)   
    
admin.site.register(Book)