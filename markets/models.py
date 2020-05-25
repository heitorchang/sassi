from django.db import models


class Market(models.Model):
    cnpj = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['name', 'address']
        
    def __str__(self):
        return "{}, {}".format(self.name, self.address)


class ProductCategory(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=80)
    upc = models.CharField(max_length=32, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Price(models.Model):
    purchase_date = models.DateField()
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.SET_NULL)
    unit = models.CharField(max_length=20)
    # amount = models.FloatField()  # calculate unit price in front-end, store price for 1 unit/1 kg
    price = models.FloatField()  # price per unit/kg
    notes = models.CharField(max_length=200, blank=True)
    
    class Meta:
        ordering = ['-purchase_date', 'product', 'brand', 'market']
        
    def __str__(self):
        return "{} {} {} {} {}".format(self.purchase_date, self.product.name, self.market.name, self.unit, self.price)
