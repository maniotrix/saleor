from django.contrib import admin
from .order.models import DeliveryGroup, OrderLine, OrderNote, Order, OrderLine, OrderLineChild, OrderLineChildImage
from .product.models import Product, ProductImage
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(OrderLineChild)
admin.site.register(OrderLineChildImage)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(OrderNote)
admin.site.register(DeliveryGroup)
