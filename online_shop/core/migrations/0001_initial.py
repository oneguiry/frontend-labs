# Generated by Django 4.1.2 on 2022-10-24 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DictProduct',
            fields=[
                ('type', models.IntegerField(choices=[(0, 'Бытовая техника'), (1, 'Промышленное оборудование'), (2, 'Инструменты'), (3, 'Дом, декор и кухня'), (4, 'Строительство')], primary_key=True, serialize=False, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='Описание товара')),
                ('type_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dictproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('path', models.ImageField(upload_to='media')),
                ('date_upload', models.DateTimeField(auto_now=True, verbose_name='Дата загрузки')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='core.product')),
            ],
        ),
    ]
