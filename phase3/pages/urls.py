from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_page, name = 'Home_page'),
    path('Sign_up.html', views.SignUp_page, name = 'SignUp'),
    path('Log_in.html', views.Login_page, name = 'Login'),
    path('Admin_home_page.html', views.AdminHome_page, name = 'AdminHome'),
    path('User_home_page.html', views.UserHome_page, name = 'UserHome'),
    path('View_list_admin.html', views.AdminList_page, name = 'AdminList'),
    path('view.html', views.BookDetails_Admin, name='BookDetails'),
    path('View_list_user.html', views.UserList_page, name = 'UserList'),
    path('BookDetailsUser.html', views.BookDetails_User, name = 'BookDUser'),
    path('Add_books.html', views.Addbook_page, name = 'AddBook'),
    path('View_List_admin.html', views.add_book, name = 'added'),
    path("View_list_admin.html", views.delete_book, name="adminpage"),
    path('update_book/', views.update_book, name='update_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
    path('search/', views.search_page, name='search_page'),
    path('search-books/', views.search_books, name='search_books'),
    path('filter-books/', views.filter_books, name='filter_books'),
    path('Borrowed-Books/', views.BorrowedBooks, name='BorrowedBooks'),
    path('borrow_book/', views.borrow_book, name='borrow_book'),


]