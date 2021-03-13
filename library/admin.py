from django.contrib import admin
from .models import Author, Book, InstanceBook


class InstanceBookModelAdmin(admin.ModelAdmin):
    list_display = ["book", "took_book", "is_available"]
    list_filter = ["is_available"]


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(InstanceBook, InstanceBookModelAdmin)
