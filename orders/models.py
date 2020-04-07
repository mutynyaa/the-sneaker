from django.db import models
from products.models import Product
from django.db.models.signals import post_save

class Status(models.Model):
    name=models.CharField('Статус заказа', max_length=24)
    is_active = models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name='Статус заказа'
        verbose_name_plural='Статусы заказа (Admin)'

class Order(models.Model):
    total_amount = models.DecimalField('Общая стоимость', max_digits=10, decimal_places=2, default=0)  # цена на колличество
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    castomer_name=models.CharField('Имя заказчика', max_length=120)
    castomer_email=models.EmailField('Email заказчика', blank=True, null=True, default=None)
    castomer_phone=models.CharField('Телефон заказчика', max_length=48, blank=True, null=True, default=None)
    comments=models.TextField('Комментарии к заказу', blank=True, null=True, default=None)
    created=models.DateTimeField('Дата создания заказа', auto_now_add=True, auto_now=False)
    updated=models.DateTimeField('Дата изменения', auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

class ProductInOrder(models.Model):
    order=models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb=models.IntegerField('Колличество ед.', default=1)
    is_active = models.BooleanField(default=True)
    price_per_item=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price=models.DecimalField(max_digits=10, decimal_places=2, default=0) # цена на колличество
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Товар %s" % self.product.name

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары задействованные в заказах (Admin)'

    def save(self, *args, **kwargs):
        price_per_item=self.product.price
        self.price_per_item = price_per_item
        self.total_price=self.nmb * self.price_per_item
        super(ProductInOrder, self).save(*args, **kwargs)

def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order_total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)

class ProductInBasket(models.Model):
    session_key=models.CharField(max_length=128, blank=True, null=True, default=None)
    order=models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb=models.IntegerField('Колличество ед.', default=1)
    is_active = models.BooleanField(default=True)
    price_per_item=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price=models.DecimalField(max_digits=10, decimal_places=2, default=0) # цена на колличество
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Товар %s" % self.product.name

    class Meta:
        verbose_name='Товар в корзине'
        verbose_name_plural='Товары в корзине'