from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('author','title','publication_year')
    list_filter = ('author', 'title', 'publication_year')
    search_fields = ['author', 'title', 'publication_year']
    

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo')
    list_filter = ('date_of_birth',)
    search_fields = ['username', 'email']
    fieldsets = (
        ('Personal Info', {
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2')
        }),
    )
    ordering = ('username',)
    filter_horizontal = ()
    readonly_fields = ('date_of_birth',)
    form = CustomUserAdminForm
    add_form = CustomUserAddForm
    change_form = CustomUserChangeForm
    inlines = [BookInline]
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(form.cleaned_data['password1'])
        super().save_model(request, obj, form, change)
        
admin.site.register(CustomUser,CustomUserAdmin)
