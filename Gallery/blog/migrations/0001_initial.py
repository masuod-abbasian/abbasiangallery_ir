# Generated by Django 3.2.12 on 2022-02-07 22:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='آدرس')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='تصویر')),
                ('description', models.TextField(verbose_name='شرح')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=1, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'نوشته',
                'verbose_name_plural': 'نوشته ها',
            },
        ),
    ]
