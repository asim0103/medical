# Generated by Django 3.2.3 on 2023-05-04 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uptadet_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Başliq')),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uptadet_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Başliq')),
                ('images', models.FileField(null=True, upload_to='uploads/%Y/%m/%d/')),
                ('video', models.URLField(null=True)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctorscategory')),
            ],
            options={
                'verbose_name': 'Doctors',
                'verbose_name_plural': 'Doctorss',
            },
        ),
    ]
