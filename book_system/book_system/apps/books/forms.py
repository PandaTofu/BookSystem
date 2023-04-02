from django import forms
from .models import Book, BookReview, ReadingPlan, PreferenceBooks


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', '']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['text', 'price', 'brief_introduction', 'b_type']

class PlanForm(forms.ModelForm):
    class Meta:
        model = ReadingPlan
        fields = ['book_name', 'period']

class PBForm(forms.ModelForm):
    class Meta:
        model = PreferenceBooks