from customers.models import Customer
from salons.models import SalonOwner

def global_variable(request):
    is_authenticated_customer = False
    is_authenticated_salon_owner = False

    current_user = request.user
    if current_user.is_authenticated:
        customer_exists = Customer.objects.filter(user=current_user).exists()

        #check if customer
        matching_customer_set = Customer.objects.filter(user=current_user)
        num_customer_matches = 0
        last_customer_match = None
        for match in matching_customer_set:
            print(match)
            num_customer_matches += 1
            last_customer_match = match

        if num_customer_matches == 0:
            print("No customer matches")
        elif num_customer_matches > 1:
            print(f"Multiple customer matches (has {num_customer_matches} matches)")
            is_authenticated_customer = True
        else:
            print(f"One customer match! {last_customer_match}")
            is_authenticated_customer = True

        
        print(f"{current_user} is authenticated customer: {is_authenticated_customer}")

        # check if salon owner
        matching_salon_owner_set = SalonOwner.objects.filter(user=current_user)
        num_salon_owner_matches = 0
        last_salon_owner_match = None
        for match in matching_salon_owner_set:
            print(match)
            num_salon_owner_matches += 1
            last_salon_owner_match = match

        if num_salon_owner_matches == 0:
            print("No salon_owner matches")
        elif num_salon_owner_matches > 1:
            print(f"Multiple salon_ownermatches (has {num_salon_owner_matches} matches)")
            is_authenticated_salon_owner = True
        else:
            print(f"One salon_owner match! {last_salon_owner_match}")
            is_authenticated_salon_owner = True

    print(f"{current_user} is authenticated salon_owner: {is_authenticated_salon_owner}")


    return {
        "is_authenticated_customer": is_authenticated_customer,
        "is_authenticated_salon_owner": is_authenticated_salon_owner,
    }