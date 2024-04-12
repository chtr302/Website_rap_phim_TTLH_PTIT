from django.db import models
from App import models as AppModels
import pandas as pd
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from datetime import datetime


# Supplier
class ProductSupplier(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.ForeignKey(AppModels.Products, on_delete=models.CASCADE)
    supplier = models.ForeignKey(ProductSupplier, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
# Cinema
class CinemaBranch(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class CinemaRoom(models.Model):
    branch = models.ForeignKey(CinemaBranch, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    seat = models.IntegerField()

    def __str__(self):
        return self.name

class CinemaSeat(models.Model):
    branch = models.ForeignKey(CinemaBranch, on_delete=models.CASCADE)
    room = models.ForeignKey(CinemaRoom, on_delete=models.CASCADE)
    number_of_seats = models.IntegerField()
    LOAN_STATUS = (
        ('St', 'Standard Seat'),
        ('Pr', 'Premium Seat'),
        ('Sw', 'Sweetbox Seat'),
    )
    status = models.CharField(
        max_length=2,
        choices=LOAN_STATUS,
        blank=True,
        default='St',
    )

    def __str__(self):
        return str(self.number_of_seats)

class CinemaWarehouse(models.Model):
    cinemabranch = models.ForeignKey(CinemaBranch, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    LOAN_STATUS = (
        ('S', 'Stocking'),
        ('O', 'Out of stock')
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='S',
    )
    def __str__(self):
        return str(self.quantity)
    
class CinemaStaff(models.Model):
    branch = models.ForeignKey(CinemaBranch, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    day_of_work = models.DateField()
    LOAN_STATUS = (
        ('M', 'CinemaManager'),
        ('P', 'ProductManager'),
        ('S', 'Staff'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='S',
    )
    def __str__(self):
        return self.name
    
class CinemaBillMovie(models.Model):
    branch = models.ForeignKey(AppModels.Branch, on_delete=models.CASCADE)
    movie = models.ForeignKey(AppModels.Movie, on_delete=models.CASCADE)
    date = models.ForeignKey(AppModels.ShowingDate, on_delete=models.CASCADE)
    time = models.ForeignKey(AppModels.ShowingTime, on_delete=models.CASCADE)
    movie_seat = models.IntegerField()
    total = models.IntegerField()
    payment_date = models.DateField(null = True)

    def __str__(self):
        return str(self.total)
    
def caculate_total_movie(branch, date):
    
    bills = CinemaBillMovie.objects.filter(branch=branch, payment_date=date)

    movie_totals = bills.values('movie').annotate(total=Sum('movie_seat'))

    for movie_total in movie_totals:
        CinemaStatisticalMovie.objects.update_or_create(
            branch = branch,
            date = date,
            movie = AppModels.Movie.objects.get(id=movie_total['movie']),
            movie_virual = movie_total['total']
        )

@receiver(post_save, sender=AppModels.CompleteMoviePayment)
def create_cinema_bill_movie(sender, instance, created, **kwargs):
    if created:
        CinemaBillMovie.objects.create(
            branch = instance.branch,
            movie = instance.movie,
            date = instance.date,
            time = instance.time,
            movie_seat = instance.seats_quantity,
            total = instance.total_price,
            payment_date = instance.payment_date
        )

class CinemaBillProduct(models.Model):
    branch = models.ForeignKey(AppModels.Branch, on_delete=models.CASCADE)
    product = models.ForeignKey(AppModels.Products, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    total = models.IntegerField()
    payment_date = models.DateField(null = True)

    def __str__(self):
        return str(self.total)
    
@receiver(post_save, sender=AppModels.CompleteProductPayment)
def create_cinema_bill_product(sender, instance, created, **kwargs):
    if created and instance.branch is not None and instance.product is not None:
        CinemaBillProduct.objects.create(
            branch = instance.branch,
            product = instance.product,
            product_quantity = instance.quantity,
            total = instance.total_price,
            payment_date = instance.payment_date
        )

def caculate_total_product(branch, date):

    bills = CinemaBillProduct.objects.filter(branch=branch, payment_date=date)

    product_totals = bills.values('product').annotate(total=Sum('product_quantity'))

    for product_total in product_totals:
        CinemaStatisticalProduct.objects.update_or_create(
            branch = branch,
            date = date,
            product = AppModels.Products.objects.get(id=product_total['product']),
            product_virual = product_total['total']
        )

class ImportDetail(models.Model):
    branch = models.ForeignKey(CinemaBranch, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    staff = models.CharField(max_length=50)
    date_import = models.DateField()

    def __str__(self):
        return self.branch.name

class ExportDetail(models.Model):
    branch = models.ForeignKey(CinemaBranch, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    staff = models.CharField(max_length=50)
    date_export = models.DateField()

    def __str__(self):
        return self.branch.name

class CinemaStatisticalMovie(models.Model):
    branch = models.ForeignKey(AppModels.Branch, on_delete=models.CASCADE)
    date = models.DateField()
    movie = models.ForeignKey(AppModels.Movie, on_delete=models.CASCADE)
    movie_virual = models.IntegerField()

    def __str__(self):
        return self.branch.name
    
class CinemaStatisticalProduct(models.Model):
    branch = models.ForeignKey(AppModels.Branch, on_delete=models.CASCADE)
    date = models.DateField()
    product = models.CharField(max_length=50)
    product_virual = models.IntegerField()

    def __str__(self):
        return self.branch.name

class CinemaReport(models.Model):
    branch = models.ForeignKey(CinemaBranch, on_delete=models.CASCADE)
    date = models.DateField()
    phantom = models.IntegerField()
    actual = models.IntegerField()
    difference = models.IntegerField()

    def __str__(self):
        return self.branch.name
    def get_total(self):
        if self.phantom > self.actual:
            return self.difference == (self.phantom - self.actual)
        else:
            return self.difference == (self.actual - self.phantom)
    @staticmethod
    def export_to_excel(queryset):
        data = queryset.values('branch__name', 'date', 'phantom', 'actual', 'difference')
        df = pd.DataFrame.from_records(data)
        df.columns = ['Branch', 'Date', 'Phantom', 'Actual', 'Difference']
        df.to_excel('CinemaReport.xlsx', sheet_name='TTLHReport', index=False, header=True)
