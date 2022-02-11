# Generated by Django 3.2.12 on 2022-02-08 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان دسته\u200cبندی')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='آدرس دسته\u200cبندی')),
                ('status', models.BooleanField(default=True, verbose_name='آیا این دسته\u200cبندی نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی\u200cها',
                'ordering': ['position'],
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش\u200cنویس'), ('p', 'منتشرشده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
