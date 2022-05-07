from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm#BookForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
import requests, json, pprint
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

def home(request):
	return render(request,'home.html')

def contact(request):
	return render(request,'contact.html')


def register(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'Register Successfull')
			return redirect('register')
	context = {'form':form} #dictionary
	return render(request,'register.html', context)


def login(request):
	if request.method == "POST": #for form submit
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username = username, password = password)
		if user is not None:
			auth_login(request, user)
			return redirect('home')
		else:
			messages.info(request,f'Username or Password is incorrect')
	return render(request,'login.html')

def user_logout(request):
	logout(request)
	return redirect('home')

def booking(request):

	if not request.user.is_authenticated:
		messages.error(request, 'Please Login or Register first!')
		return redirect('login')

	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		service_type = request.POST['service_type']
		appointment_time = request.POST['appointment_time']
		appointment_date = request.POST['appointment_date']
		dd = datetime.strptime(appointment_date+'/'+appointment_time, '%m/%d/%Y/%I:%M%p')
		paid = False
		if 'paid' in request.COOKIES:
			paid = request.COOKIES.get('paid') #To see the payment
		
		# print(dd)
		reserved = Booking.objects.filter(appointment_time=dd)
		if reserved:#To see whether the booking is booked or not
			messages.error(request,'Sorry, provided schedule is reserved.')
			return redirect('booking')
		else:
			new_booking = Booking.objects.create(# create booking
				name = name,
				email = email,
				service_type = service_type,
				appointment_time = dd,
				paid = paid
			)
			new_booking.save()
			messages.success(request, 'Your appointment is successfully saved.')
			return redirect('home')

	return render(request,'Appointmentbooking.html')
#Khalti App
@csrf_exempt 
def verify_payment(request):
   print('Khalti')
   data = request.POST
   product_id = data['product_identity']
   token = data['token']
   amount = data['amount']

   url = "https://khalti.com/api/v2/payment/verify/"
   payload = {
   "token": token,
   "amount": amount
   }
   headers = {
   "Authorization": "Key test_secret_key_d0b5ad6269bf4830a94db46724c93962"
   }
   

   response = requests.post(url, payload, headers = headers)
   
   response_data = json.loads(response.text)
   status_code = str(response.status_code)

   if status_code == '400':
      response = JsonResponse({'status':'false','message':response_data['detail']}, status=500)
      return response

   pp = pprint.PrettyPrinter(indent=4)
   pp.pprint(response_data)
   
   response = JsonResponse(f"Payment Done !!",safe=False)
   response.set_cookie('paid', True, max_age=30) # cookie save data
   return response

def services(request):
	return render(request, 'services.html')

def test_chat(request):
	return HttpResponse("Done dona done")

# def upload_book(request):
# 	form = BookForm()
# 	if request.method == "POST":
# 		form = BookForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request,f'Book upload Successfull')
# 			return redirect('book_upload')
# 	context = {'form':form}
# 	return render(request,'book/upload.html', context)


# def update_book(request, id = None):
# 	instance = get_object_or_404(Book, id = id)
# 	form = BookForm()
# 	if request.method == "POST":
# 		form = BookForm(request.POST, request.FILES, instance = instance)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request,f'Update Book Successfull')
# 			return redirect('book_upload')
# 	context = {'form':form,'instance':instance}
# 	return render(request,'book/upload.html', context)

# def delete_book(request, id):
# 	book = Book.objects.all()
# 	book.delete()
# 	return redirect('home')


# def list_book(request):
# 	book = Book.objects.all()
# 	if request.GET:
# 		query = request.GET['q']
# 		book = get_queryset_data(str(query))
# 	context = {'book':book}
# 	return render(request,'book/list_book.html',context)


# def customer_list(request):
# 	customer = Customer.objects.all()
# 	context = {'customer':customer}
# 	return render(request,'customer_list.html', context)

# def beautician_list(request):
# 	beautician = Beautician.objects.all()
# 	context = {'beautician': beautician}
# 	return render(request,'beautician_list.html', context)

# def delete_customer(request, id):
# 	customer = Customer.objects.get(id = id)
# 	customer.delete()
# 	return redirect('list_customer')