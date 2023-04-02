from django.db import models
from django.urls import reverse
# from tinymce.models import HTMLField  # 使用富文本编辑框要在settings文件中安装
from datetime import datetime

from apps.user.models import User


# Create your models here.
class BookType(models.Model):
    # book type
    isDelete = models.BooleanField(default=False)
    book_type = models.CharField(max_length=20, verbose_name="type")

    class Meta:
        verbose_name = "book type"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_type


class Books(models.Model):
    # book
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    book_name = models.CharField(max_length=20, verbose_name="book name", unique=True)
    book_pic = models.ImageField(verbose_name='image', upload_to='books/image/%Y/%m', null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="price")  # 书籍价格小数位为两位，整数位为3位
    brief_introduction = models.CharField(max_length=200, verbose_name="brief introduction")
    # information = HTMLField(max_length=200, verbose_name="information")
    #b_type = models.ForeignKey(BookType, verbose_name="type")  # BookType
    b_type = models.CharField(max_length=20, verbose_name="type")

    class Meta:
        verbose_name = "book"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('books:book_detail', arg=[self.id])

class BookReview(models.Model):
    # book review
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    text = momdels.TextField()
    date_publish = models.DateTimeField(verbose_name="published date", default=datetime.now)
    #avatar = models.CharField(verbose_name='avatar', max_length=200, default=None)
    # review = HTMLField(max_length=200, verbose_name="用户评论")
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="reviews", 
        verbose_name="user")
    book = models.ForeignKey(
        Books, 
        on_delete=models.CASCADE,
        related_name="reviews",  
        verbose_name="book")

    class Meta:
        verbose_name = "book review"
        verbose_name_plural = verbose_name
        ordering = ('date_publish', )

    def __str__(self):
        return self.text[:20]

class ReadingPlan(models.Model):
    book_name = models.CharField(max_length=20, verbose_name="book name", unique=True)
    period = models.IntegerField(verbose_name="reading period") #define how many days to finish the reading plan
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="plans", 
        verbose_name="user")

    class Meta:
        verbose_name = "reading plan"
        verbose_name_plural = verbose_name

class PreferenceBooks(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="reviews", 
        verbose_name="user")
    book = models.ForeignKey(
        Books, 
        on_delete=models.CASCADE,
        related_name="reviews",  
        verbose_name="book")
    created = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "preferences of books"
        verbose_name_plural = verbose_name