from django.db import models

class ProductCategory(models.Model):
    name=models.CharField(max_length=64,blank=True, null=True, default=None)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.id, self.name)

    class Meta:
        verbose_name='Категория товара'
        verbose_name_plural='Категория товаров'

class Product(models.Model):
    name=models.CharField('Наименование товара', max_length=120)
    short_description = models.TextField('Описание товара', blank=True, null=True, default=None)
    discount=models.IntegerField(default=0)
    category=models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    description=models.TextField('Описание товара', blank=True, null=True, default=None)
    is_active = models.BooleanField('В наличии',default=True)
    price = models.DecimalField('Цена товара', max_digits=10, decimal_places=2, default=0)
    created=models.DateTimeField('Дата создания товара', auto_now_add=True, auto_now=False)
    updated=models.DateTimeField('Последние изменения', auto_now_add=True, auto_now=False)

    def __str__(self):
        return "№ товара:  (%s) Наименование товара:  //%s// Цена:*%s*" % (self.id,self.name, self.price)

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'

class ProductImage(models.Model):
    product=models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product_images/')
    is_active=models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "(%s) %s" % (self.id, self.product)

    class Meta:
        verbose_name='Фотография'
        verbose_name_plural='Фотографии к товарам (admin)'