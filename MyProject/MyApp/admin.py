from django.contrib import admin
from .models import Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'published_date', 'price', 'in_stock')

	search_fields = ('title', 'author', 'isbn')

	list_filter = ('in_stock', 'published_date')

	list_editable = ('price', 'in_stock')

	list_display_links = ('title', 'author')
