from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Product)
# admin.site.register(Price)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'user_id', 'storage', 'partner', 'count', 'price', 'active')
    list_filter = ('storage', 'partner', 'active')


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Storage)
admin.site.register(Partner)



