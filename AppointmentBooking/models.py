from django.db import models

from datetime import datetime

# Create your models here.
class Booking(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length = 100)
	service_type = models.CharField(max_length = 100)
	appointment_time = models.DateTimeField()
	# appointment_date = models.DateTimeField(auto_now_add=False)
      # total_cost = models.FloatField()
	paid = models.BooleanField(default=False)

	def __str__(self):
		return self.name
	
class Customer(models.Model):
	name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	email = models.EmailField()

	def __str__(self):
		return self.name

class Beautician(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField()
	customer = models.ForeignKey(Customer, on_delete = models.CASCADE)

	def __str__(self):
		return self.name

