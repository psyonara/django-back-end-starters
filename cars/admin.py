from django.contrib import admin

from cars.models import Car, Make


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("make", "model", "year", "color", "mileage", "price")
    search_fields = ("make", "model")
    list_filter = ("make", "year", "color")
