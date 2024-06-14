from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import *
from pages.urls import *
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate,login
from .forms import CustomUserCreationForm


def Home_page(request):
    return render(request, "pages/Home_page.html", {"name": "Home_page"})



def SignUp_page(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('Login')  # Use the name of the URL pattern
    else:
        form = CustomUserCreationForm()
    return render(request, "pages/Sign_up.html", {"form": form, "name": "Sign_up"})



def Login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'profile'):
                acc_type = user.profile.accType
                if acc_type == 'Admin':
                    return AdminHome_page(request)
                elif acc_type == 'User':
                    return UserHome_page(request)
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "pages/Log_in.html", {"name": "Log_in"})


 
def AdminHome_page(request):
    return render(request, "pages/Admin_home_page.html", {"name": "AdminHome"})

 
def UserHome_page(request):
    return render(request, "pages/User_home_page.html", {"name": "UserHome"})

 
def AdminList_page(request):
    return render(request, "books/View_list_admin.html", {"books": Book.objects.all()})

 
def BookDetails_Admin(request):
    book_id = request.GET.get("id")
    book = get_object_or_404(Book, id=book_id)
    return render(request, "books/view.html", {"books": book})

 
def UserList_page(request):
    return render(request, "books/View_list_user.html", {"books": Book.objects.all()})

 
def BookDetails_User(request):
    book_id = request.GET.get("id")
    book = get_object_or_404(Book, id=book_id)
    return render(request, "books/BookDetailsUser.html", {"book": book})


def add_book(request):
    if request.method == "POST":
        Id = request.POST.get("book_id")
        Name = request.POST.get("book_name")
        Author = request.POST.get("author")
        Category = request.POST.get("category")
        Description = request.POST.get("description")
        PublishDate = request.POST.get("publish_date")
        CoverImage = request.FILES.get("book_image")
        if Id:
            data = Book(
                bId=Id,
                bName=Name,
                bAuthor=Author,
                bCategory=Category,
                bDescription=Description,
                bPublishDate=PublishDate,
                bCoverImage=CoverImage,
            )
            data.save()
            return AdminList_page(request)
        else:
            return Addbook_page(request)
    else:
        return AdminHome_page(request)


def Addbook_page(request):
    return render(request, "books/Add_books.html", {"name": "AddBook"})


@csrf_exempt
def delete_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")

        try:
            book_to_delete = Book.objects.get(pk=book_id)
            book_to_delete.delete()
            return JsonResponse({"message": "Book deleted successfully"}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)



def update_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        new_author = request.POST.get('new_author')
        new_genre = request.POST.get('new_genre')
        new_description = request.POST.get('new_description')

        # Retrieve the book instance
        book = get_object_or_404(Book, pk=book_id)

        # Update book attributes
        book.bAuthor = new_author
        book.bCategory = new_genre
        book.bDescription = new_description

        try:
            book.save()
            return JsonResponse({'message': 'Book details updated successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def search_books(request):
    query = request.GET.get('query', '')
    if query:
        books = Book.objects.filter(bName__icontains=query) | Book.objects.filter(bAuthor__icontains=query)
        suggestions = [{'id': book.id, 'title': book.bName, 'author': book.bAuthor, 'cover_image_url': book.bCoverImage.url} for book in books]
    else:
        suggestions = []
    return JsonResponse({'suggestions': suggestions})

def search_page(request):
    return render(request, 'search_page.html')



def filter_books(request):
    category = request.GET.get('category', 'All')
    if category == 'All':
        books = Book.objects.all()
    else:
        books = Book.objects.filter(bCategory=category)

    serialized_books = [{'id': book.id, 'title': book.bName, 'author': book.bAuthor, 'cover_image_url': book.bCoverImage.url, 'category': book.bCategory, 'publish_date': book.bPublishDate} for book in books]
    return JsonResponse({'books': serialized_books})


def BorrowedBooks(request):
    borrowed_books = BorrowRecord.objects.filter(user=request.user)
    return render(request, "books/Borrowed_list.html", {"borrowed_books": borrowed_books})

from datetime import timedelta

def borrow_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('id')
        borrow_date = request.POST.get('BDate')
        return_date = request.POST.get('RDate')
        duration = request.POST.get('Duration')

        book = get_object_or_404(Book, id=book_id)

        if book.is_borrowed:
            return HttpResponse("This book is already borrowed.")

        borrow_datetime = timezone.datetime.strptime(borrow_date, "%Y-%m-%d")
        return_datetime = timezone.datetime.strptime(return_date, "%Y-%m-%d")

        # Calculate duration in days
        duration = (return_datetime - borrow_datetime).days
        
        # Calculate price based on duration
        price = duration * 5

        borrow_record = BorrowRecord(
            user=request.user,
            book=book,
            borrow_date=borrow_datetime,
            return_date = return_datetime,
            duration=duration,
            price=price,
        )
        borrow_record.save()

        book.is_borrowed = True
        book.save()

        # Add the borrowed book to the user's list of borrowed books
        request.user.borrowed_books.add(book)

        return HttpResponse("Book borrowed successfully!")
    return HttpResponse("Invalid request method.")
