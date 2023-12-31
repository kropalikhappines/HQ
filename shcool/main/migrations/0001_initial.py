# Generated by Django 4.2.5 on 2023-09-27 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.basemodel')),
                ('first_name', models.CharField(max_length=32, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=32, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            bases=('main.basemodel',),
        ),
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.basemodel')),
                ('product_name', models.CharField(max_length=32, verbose_name='Название продукта')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usersmodel', verbose_name='Владелец продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
            bases=('main.basemodel',),
        ),
        migrations.CreateModel(
            name='LessonsModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.basemodel')),
                ('lesson_name', models.CharField(max_length=32, verbose_name='Название урока')),
                ('url_video', models.URLField(max_length=256, verbose_name='Ссылка на видео')),
                ('duration_view', models.IntegerField(max_length=20, verbose_name='Длительность видео')),
                ('how_many_viewed', models.IntegerField(max_length=20, verbose_name='Сколько просмотренно видео')),
                ('status_view', models.BooleanField(default=False, verbose_name='Статус просмотра видео')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productsmodel', verbose_name='Продукт урока')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
            bases=('main.basemodel',),
        ),
    ]
