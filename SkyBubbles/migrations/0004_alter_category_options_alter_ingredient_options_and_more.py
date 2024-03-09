# Generated by Django 4.2.10 on 2024-03-09 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SkyBubbles', '0003_category_ingredient_partner_storage_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ингридиент', 'verbose_name_plural': 'Ингридиенты'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Поставщик', 'verbose_name_plural': 'Поставщики'},
        ),
        migrations.AlterModelOptions(
            name='storage',
            options={'verbose_name': 'Склад', 'verbose_name_plural': 'Склады'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'Приход', 'verbose_name_plural': 'Приходы'},
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user_id',
        ),
        migrations.AddField(
            model_name='category',
            name='createFd_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='createFd_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partner',
            name='createFd_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='partner',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partner',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='partner',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='createFd_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='price',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='storage',
            name='createFd_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='storage',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storage',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='storage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='createFd_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
