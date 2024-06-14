from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User
# from .views import validate_password_strength

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accType = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('User', 'User')])

    def __str__(self):
        return self.user.username


class Book(models.Model):
    BOOK_CATEGORY = [
        ('romance', 'Romance'),
        ('horror', 'Horror'),
        ('fantasy', 'Fantasy'),
        ('science_fiction', 'Science Fiction'),
        ('history', 'History')
    ]
    bId = models.IntegerField(null=False, unique=True)
    bName = models.CharField(max_length=255, null=False)
    bAuthor = models.CharField(max_length=100, null=False)
    bCategory = models.CharField( max_length=100, choices=BOOK_CATEGORY, null=False)
    bDescription = models.TextField(max_length=1000)
    bPublishDate = models.DateField(validators=[MaxValueValidator(timezone.now().date())]) 
    bCoverImage = models.ImageField(upload_to='book_covers/',null=False, blank=True, default="images/13.jpg")
    is_borrowed = models.BooleanField(default=False)


class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=False, blank=True, default="")
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
