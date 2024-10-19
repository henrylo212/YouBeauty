# from django.test import TestCase, RequestFactory
# from django.contrib.auth.models import User
# from customers.models import Customer
# from accounts.context_processors import global_variable  # Adjust to your correct import path

# class GlobalVariableTestCase(TestCase):
    
#     def setUp(self):
#         # Set up RequestFactory and create some users and customer records
#         self.factory = RequestFactory()

#         # Create an unauthenticated user
#         self.unauthenticated_user = User.objects.create_user(username='anon_user', password='test')

#         # Create an authenticated user without any Customer record
#         self.auth_user_no_customer = User.objects.create_user(username='auth_user_no_customer', password='test')

#         # Create an authenticated user with one Customer record
#         self.auth_user_one_customer = User.objects.create_user(username='auth_user_one_customer', password='test')
#         Customer.objects.create(user=self.auth_user_one_customer)

#         # Create an authenticated user with multiple Customer records
#         self.auth_user_multi_customer = User.objects.create_user(username='auth_user_multi_customer', password='test')
#         Customer.objects.create(user=self.auth_user_multi_customer)
#         Customer.objects.create(user=self.auth_user_multi_customer)
    
#     def test_unauthenticated_user(self):
#         # Simulate a request for an unauthenticated user
#         request = self.factory.get('/')
#         request.user = self.unauthenticated_user
#         request.user.is_authenticated = False  # Set as unauthenticated
        
#         result = global_variable(request)
#         self.assertFalse(result['is_authenticated_customer'], "Unauthenticated user should not be an authenticated customer.")
    
#     def test_authenticated_user_no_customer(self):
#         # Simulate a request for an authenticated user without any matching Customer records
#         request = self.factory.get('/')
#         request.user = self.auth_user_no_customer
#         request.user.is_authenticated = True
        
#         result = global_variable(request)
#         self.assertFalse(result['is_authenticated_customer'], "Authenticated user with no customer record should not be authenticated customer.")
    
#     def test_authenticated_user_one_customer(self):
#         # Simulate a request for an authenticated user with one matching Customer record
#         request = self.factory.get('/')
#         request.user = self.auth_user_one_customer
#         request.user.is_authenticated = True
        
#         result = global_variable(request)
#         self.assertTrue(result['is_authenticated_customer'], "Authenticated user with one customer record should be an authenticated customer.")
    
#     def test_authenticated_user_multiple_customers(self):
#         # Simulate a request for an authenticated user with multiple matching Customer records
#         request = self.factory.get('/')
#         request.user = self.auth_user_multi_customer
#         request.user.is_authenticated = True
        
#         result = global_variable(request)
#         self.assertTrue(result['is_authenticated_customer'], "Authenticated user with multiple customer records should be an authenticated customer.")
