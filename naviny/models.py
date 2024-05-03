from django.db import models

class Articles(models.Model):
    title = models.CharField('Тип животного', max_length=50)
    anons = models.CharField('Порода животного', max_length=250)
    full_text = models.TextField('Вид работ')
    price = models.FloatField('Стоимость')
    date = models.DateTimeField('Дата записи')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/naviny/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

