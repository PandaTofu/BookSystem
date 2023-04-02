from django.contrib import admin
from .models import Books, BookType, BookReview


class BookTypeAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'book_type']
    search_fields = ['book_type']
    list_display_links = ['book_type']


class BooksAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'book_name', 'book_pic', 'price', 'brief_introduction', 'b_type']
    search_fields = ['book_name', 'b_type']
    list_display_links = ['book_name']


class BookReviewAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'b_name', 'username', 'avatar', 'date_publish']
    search_fields = ['b_name', 'username', 'date_publish']
    list_display_links = ['b_name']


admin.site.register(BookType, BookTypeAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(BookReview, BookReviewAdmin)
