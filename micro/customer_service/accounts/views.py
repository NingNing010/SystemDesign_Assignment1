from django.http import JsonResponse
from .models import Customer

def get_customers(request):
    customers = Customer.objects.all()
    data = list(customers.values('id', 'username', 'email'))
    return JsonResponse({'customers': data})