from django.db import models


class BaseModel(models.Model):
    """Базовая модель, дата создания"""
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")


class UsersModel(BaseModel):
    """Модель пользователей"""
    first_name = models.CharField(max_length=32, verbose_name="Имя")
    last_name = models.CharField(max_length=32, verbose_name="Фамилия")

    def __str__(self):
        return str(" ".join([self.first_name, self.last_name]))

    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"


class ProductsModel(BaseModel):
    """Модель продукта"""
    product_name = models.CharField(max_length=32, verbose_name="Название продукта")
    owner = models.ForeignKey(UsersModel, on_delete=models.CASCADE, verbose_name="Владелец продукта")

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = "Продукты"
        verbose_name = "Продукт"


class LessonsModel(BaseModel):
    """Модель уроков"""
    lesson_name = models.CharField(max_length=32, verbose_name="Название урока")
    owner = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, verbose_name="Продукт урока")
    url_video = models.URLField(max_length=256, verbose_name="Ссылка на видео")
    duration_view = models.IntegerField(verbose_name="Длительность видео")
    how_many_viewed = models.IntegerField(verbose_name="Сколько просмотренно видео")
    status_view = models.BooleanField(default=False, verbose_name="Статус просмотра видео")

    """Метод определения статуса просмотра видео"""
    def save(self, *args, **kwargs):
        percentage_video = self.duration_view * 0.8
        if percentage_video <= self.how_many_viewed:
            self.status_view = True
        else:
            self.status_view = False
        super(LessonsModel, self).save(*args, **kwargs)

        return self

    def __str__(self):
        return str(self.lesson_name)

    class Meta:
        verbose_name_plural = "Уроки"
        verbose_name = "Урок"


class Access(models.Model):
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
