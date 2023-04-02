from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from .models import Books, BookReview
from .forms import BookForm, ReviewForm, PlanForm, PBForm


def index(request):
    return HttpResponse('BOOKS')

def add_book(request):
    book_form = BookForm(request.POST)
    if book_form.is_valid():
        new_book = book_form.save(commit=True)

def add_reading_plan(request):
    plan_form = PlanForm(request.POST)
    if plan_form.is_valid():
        new_plan = plan_form.save(commit=False)
        new_plan.user = request.username
        new_plan.save()

def choose_preference_books(request, id=book_id):
    book = get_object_or_404(Books, id=book_id)
    pb_form = PBForm(request.POST)
    new_pb = pb_form.save(commit=False)
    new_pb.user = user

def book_detail(request, book_id):
    book = get_object_or_404(Books, id=book_id)

    # Get all reviews for this book
    reviews = book.reviews.all()

    # Context for the book
    context = {'book': book, 'reviews': reviews}

def post_review(request, book_id):
    # Check if it's valid book
    book = get_object_or_404(Books, id=book_id)

    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        new_review = review_form.save(commit=False)
        new_review.book = book
        new_review.user = request.user
        new_review.save()
        # Redirect to the page of showing book details
        return redirect(book)

    else:
        return HttpResponse("Invalid review, please re-post.")