from datetime import timedelta, timezone
from django.db import models

# Create your models here.

# Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    is_vandor = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)

# Password History
# used when registring to check if its not in the db for this customer_id
class PasswordHistory(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    passwordHash = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

# login attempt history
# tracking the logins in the platform
class LoginAttemptHistory(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loginSuccessful = models.BooleanField(null=False, default=False)
    attempted_at = models.DateTimeField(auto_now_add=True)

# Product category
class ProductCategory():
    name = models.CharField(max_length=100)
    description = models.TextField()

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    vender_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# The seller of the product
class ProductVendor():
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    description = models.TextField()
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

# The shopping cart Item
class ShoppingCartItem():
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=8, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
 
# Shopping cart actions
class Action():
    action_constant = models.CharField(max_length=100, default='')
    description = models.TextField()

# Shopping carts history
class ShoppingCartHistory():
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    occurried_at = models.DateTimeField(auto_now_add=True)
    # action_id = models.ForeignKey(Action, on_delete=models.CASCADE)
    
# orders
# Order status
class OrderStatusCode():
    status_code = models.CharField(max_length=20)
    description = models.TextField()

# Order
class Order():
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # status_code_id = models.ForeignKey(OrderStatusCode, on_delete=models.CASCADE)
    customer_comment = models.CharField(max_length=250)

# order item
class OrderItem():
    # order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# shipping
# Shippment
class Shippment():
    # order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    to_address = models.CharField(max_length=100)
    from_address = models.CharField(max_length=100)
    tracking_code = models.CharField(max_length=100)
    sent_at = models.DateTimeField(auto_now_add=True)

# Shipment Item
# class ShippmentItem():
    # shippment_id = models.ForeignKey(Shippment)
    # order_item_id = models.ForeignKey(OrderItem, on_delete=models.CASCADE)

# returns
# class OrderItemReturn():
#     order_item_id = models.ForeignKey(OrderItem)
