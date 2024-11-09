from django.contrib import admin

# Register your models here.

from relationship_app.models import Author,Book,Library,Librarian

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

