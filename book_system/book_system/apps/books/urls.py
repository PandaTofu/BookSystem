from django.urls import path
from .views import index, post_review


urlpatterns = [
    path('', index),
    path('add-book/', add_book, name='add book'),
    path('preference-books', choose_preference_books, name='preference books'),
    path('post-review/<int:book_id>/', post_review, name='post_review'),
]
