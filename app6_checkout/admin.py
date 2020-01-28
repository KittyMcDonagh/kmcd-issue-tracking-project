#NOTE: These were originally copied from the ecommerce project and adjusted

from django.contrib import admin

from .models import Order, OrderLineItem

# OrderLineAdmin inherits from the TabularInline within admin.
# TabularInline subclass defines the template used to render the Order in the
# admin interface.

class OrderLineAdminInline(admin.TabularInline):
    
    # And it uses the OrderLineItem as a model
    
    model = OrderLineItem

# OrderAdmin, which inherits from the ModelAdmin of the admin Django. 
# That just takes inlines, which is the OrderLineAdmin inline that was
# created above. 

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)
    
    
