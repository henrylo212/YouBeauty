from customers.models import Customer

def global_variable(request):
    is_authenticated_customer = False

    current_user = request.user
    if current_user.is_authenticated:
        customer_exists = Customer.objects.filter(user=current_user).exists()
        is_authenticated_customer = True


    return {
        "is_authenticated_customer": is_authenticated_customer
    }