from django.contrib import admin
from .models import Collection, Product, Customer, Order

# FIXED: Changed admin.site.ModelAdmin to admin.ModelAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page = 10

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

# FIXED: Changed admin.site.ModelAdmin to admin.ModelAdmin
@admin.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    # We use methods (defined below) to get the names from the linked User model
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    # We use double underscore __ to tell Django to sort by the linked User's fields
    ordering = ['user__first_name', 'user__last_name']

    # Helper method to get First Name
    @admin.display(ordering='user__first_name')
    def first_name(self, customer):
        return customer.user.first_name

    # Helper method to get Last Name
    @admin.display(ordering='user__last_name')
    def last_name(self, customer):
        return customer.user.last_name