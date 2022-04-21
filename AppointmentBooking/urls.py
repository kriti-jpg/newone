from django.urls import path
from .import views

urlpatterns = [
	path('', views.home, name='home'),
	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('contact/', views.contact, name='contact'),
	path('booking/', views.booking, name='booking'),
	path('services/', views.services, name='services'),
	path('chat/',views.test_chat),
	path('api/verify_payment',views.verify_payment,name='verify_payment')
	# path('book_upload/', views.upload_book, name='book_upload'),
	# path('book_update/<int:id>/', views.update_book, name='book_update'),
	# path('book_delete/<int:id>/', views.delete_book, name='book_delete'),
	# path('book_list/', views.list_book, name='book_list'),
	# path('list_customer/', views.customer_list, name='list_customer'),
	#  path('list_beautician/', views.beautician_list, name='list_beautician'),
	# path('customer_delete/<int:id>/', views.delete_customer, name='customer_delete')

]