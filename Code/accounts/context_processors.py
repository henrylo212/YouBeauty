from customers.models import Customer

def global_variable(request):
    is_authenticated_customer = False

    current_user = request.user
    if current_user.is_authenticated:
        customer_exists = Customer.objects.filter(user=current_user).exists()

        matching_customer_set = Customer.objects.filter(user=current_user)
        num_matches = 0
        last_customer_match = None
        for match in matching_customer_set:
            print(match)
            num_matches += 1

        if num_matches == 0:
            print("No matches")
        elif num_matches > 1:
            print(f"Multiple matches (has {num_matches} matches)")
            is_authenticated_customer = True
        else:
            print("One match! {last_customer_match}")
            is_authenticated_customer = True

    print(f"{current_user} is authenticated customer: {is_authenticated_customer}")


    return {
        "is_authenticated_customer": is_authenticated_customer,
    }