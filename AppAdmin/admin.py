from django.contrib import admin
from .models import *
from datetime import datetime


class ProductSupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

    search_fields = ['name', 'address']

    list_filter = ('name', 'address')
admin.site.register(ProductSupplier, ProductSupplierAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier')

    search_fields = ['name', 'supplier']

    list_filter = ('name', 'supplier')
admin.site.register(Product, ProductAdmin)

class CinemaBranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

    search_fields = ['name']
admin.site.register(CinemaBranch, CinemaBranchAdmin)

class CinemaRoomAdmin(admin.ModelAdmin):
    list_display = ('branch', 'name', 'seat')

    search_fields = ['branch', 'name']

    list_filter = ('branch', 'name')
admin.site.register(CinemaRoom, CinemaRoomAdmin)

class CinemaSeatAdmin(admin.ModelAdmin):
    list_display = ('branch', 'room', 'number_of_seats', 'status')

    search_fields = ['branch', 'room']

    list_filter = ('branch', 'room')
admin.site.register(CinemaSeat, CinemaSeatAdmin)

class CinemaWarehouseAdmin(admin.ModelAdmin):
    list_display = ('cinemabranch', 'product', 'quantity', 'status')

    search_fields = ['cinemabranch', 'product']

    list_filter = ('cinemabranch', 'product')
admin.site.register(CinemaWarehouse, CinemaWarehouseAdmin)

class CinemaStaffAdmin(admin.ModelAdmin):
    list_display = ('branch', 'name', 'day_of_work', 'status')

    search_fields = ['branch', 'name', 'status', 'day_of_work']

    list_filter = ('branch', 'name', 'status', 'day_of_work')
admin.site.register(CinemaStaff, CinemaStaffAdmin)

def caculate_totals_movies(modeladmin, request, queryset):
    for branch in queryset:
        caculate_total_movie(branch.branch, datetime.today().date())
caculate_totals_movies.short_description = "Caculate Movies"

def caculate_totals_products(modeladmin, request, queryset):
    for branch in queryset:
        caculate_total_product(branch.branch, datetime.today().date())
caculate_totals_products.short_description = "Caculate Products"

class CinemaBillMovieAdmin(admin.ModelAdmin):

    list_display = ('branch', 'movie', 'movie_seat', 'payment_date')

    search_fields = ['branch', 'movie', 'payment_date']

    list_filter = ('branch', 'payment_date')

    actions = [caculate_totals_movies]
admin.site.register(CinemaBillMovie, CinemaBillMovieAdmin)

class CinemaBillProductAdmin(admin.ModelAdmin):
    
        list_display = ('branch', 'product', 'product_quantity', 'payment_date')
    
        search_fields = ['branch', 'product', 'payment_date']
    
        list_filter = ('branch', 'payment_date')
    
        actions = [caculate_totals_products]
admin.site.register(CinemaBillProduct, CinemaBillProductAdmin)

class ImportDetailAdmin(admin.ModelAdmin):
    list_display = ('branch', 'product', 'quantity','staff', 'date_import')

    search_fields = ['branch', 'product','staff', 'date_import']

    list_filter = ('branch', 'product','staff', 'date_import')
admin.site.register(ImportDetail, ImportDetailAdmin)

class ExportDetailAdmin(admin.ModelAdmin):
    list_display = ('branch', 'product', 'quantity','staff', 'date_export')

    search_fields = ['branch', 'product','staff', 'date_export']

    list_filter = ('branch', 'product','staff', 'date_export')
admin.site.register(ExportDetail, ExportDetailAdmin)

class MovieStitatical(admin.ModelAdmin):
    list_display = ('branch', 'movie')

    search_fields = ['branch', 'movie']

    list_filter = ('branch', 'movie')
admin.site.register(CinemaStatisticalMovie, MovieStitatical)

class ProductStitatical(admin.ModelAdmin):
    list_display = ('branch', 'product')

    search_fields = ['branch', 'product']

    list_filter = ('branch', 'product')
admin.site.register(CinemaStatisticalProduct, ProductStitatical)

def export_selected_to_excel(modeladmin, request, queryset):
    CinemaReport.export_to_excel(queryset)
export_selected_to_excel.short_description = "Export To Excel"

class CinemaReportAdmin(admin.ModelAdmin):
    list_display = ('branch', 'difference')
    actions = [export_selected_to_excel]

    search_fields = ['branch', 'difference']

    list_filter = ('branch', 'difference')
admin.site.register(CinemaReport, CinemaReportAdmin)