from django.db import models
from django.conf import settings



class Post(models.Model):
    title = models.CharField('Заголовок поста',max_length=200)
    text = models.TextField('Текст под постом',)
    image = models.ImageField('Картинка поста',upload_to='product_images/',blank=True, null=True, default=None)
    price=models.DecimalField('Цена товара', max_digits=10, decimal_places=2, default=0)


    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Пост на главной'
        verbose_name_plural='Посты на главной'