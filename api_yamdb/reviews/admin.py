from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'role',
    )
    search_fields = (
        'username',
        'email',
        'role',
    )
    list_filter = ('role',)


admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(User, UserAdmin)
