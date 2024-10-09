from customers.models import Customer

def global_variable(request):
    is_authenticated_customer = False

    current_user = request.user
    if current_user.is_authenticated:
        customer_exists = Customer.objects.filter(user=current_user).exists()

        matching_customer_set = Customer.objects.filter(user=current_user)
        num_matches = 0
        last_customer_ma