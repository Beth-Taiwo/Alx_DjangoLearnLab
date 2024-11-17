from django.contrib import admin
from .models import Book, CustomUser, CustomUserManager

# Register your models here.
admin.site.register(Book)
admin.site.register(CustomUser,CustomUserManager)

class BookAdmin(admin.ModelAdmin):
    list_display = ('author','title','publication_year')
    list_filter = ('author', 'title', 'publication_year')
    search_fields = ['author', 'title', 'publication_year']