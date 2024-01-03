from django.db import models
from django.db import models
class BaseModel(models.Model):
    created_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    update_add = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True
class Categor(BaseModel):
    title = models.CharField(max_length=100)



class Product(BaseModel):
    image = models.ImageField(upload_to='posts',null=True,blank=False,verbose_name='Фото')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(null=True , blank=True , verbose_name='Описание')
    rate = models.FloatField(default=0 , verbose_name='Рейтинг')

    cat = models.ManyToManyField(Categor,related_name='cat',verbose_name='Категории')
    def __str__(self) -> str:
        return f'{self.title} {self.text} {self.rate} {self.cat}'


    class Meta:
        db_table = 'product'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Category(BaseModel):
    post = models.ForeignKey(
        'blog.Product',
        on_delete=models.CASCADE ,
        verbose_name='пост',
        related_name='category')
    text = models.CharField(max_length=200,verbose_name='Категория',null=True,blank=True,)


    def __str__(self) -> str:
        return f'{self.text}'
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
class Review(BaseModel):
    review = models.ForeignKey(
        'blog.Product',
        on_delete=models.CASCADE,
        verbose_name='отзыв',
        related_name='review'
    )
    text = models.CharField(max_length=400,verbose_name='Отзыа')
    def __str__(self) -> str:
        return f'{self.text}'
    class Meta:
        db_table = 'review'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'