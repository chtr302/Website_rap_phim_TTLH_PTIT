from django.contrib import admin
from .models import *

# Register your models here.

# Movie API
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'display_genre', 'status')

    search_fields = ['title', 'status']

    list_filter = ('director','genre')
admin.site.register(Movie, MovieAdmin)

admin.site.register(Genre)

class ShowingDateAdmin(admin.ModelAdmin):
    list_display = ('movie', 'branch', 'date')

    search_fields = ['movie', 'branch']

    list_filter = ('movie', 'branch')
admin.site.register(ShowingDate, ShowingDateAdmin)

class ShowingTimeAdmin(admin.ModelAdmin):
    list_display = ('movie', 'branch','date',  'time')

    search_fields = ['movie', 'branch', 'date']

    list_filter = ('movie', 'branch', 'date')
admin.site.register(ShowingTime, ShowingTimeAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status')

    search_fields = ['name', 'status']

    list_filter = ('name', 'status')
admin.site.register(Products, ProductAdmin)
# Booking API

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

    search_fields = ['name', 'address']

    list_filter = ('name', 'address')
admin.site.register(Branch, BranchAdmin)

class CompleteMovie(admin.ModelAdmin):
    list_display = ('user_order', 'movie','seats_quantity', 'total_price')
admin.site.register(CompleteMoviePayment, CompleteMovie)

class CompleteProduct(admin.ModelAdmin):
    list_display = ('user_order', 'product','quantity', 'total_price')
admin.site.register(CompleteProductPayment, CompleteProduct)