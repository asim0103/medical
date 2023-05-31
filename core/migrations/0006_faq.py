# Generated by Django 4.1.7 on 2023-05-27 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_category_service_servicecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uptadet_at', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=300, verbose_name='Sual')),
                ('answer', models.CharField(max_length=1000, verbose_name='Cavab')),
                ('order', models.IntegerField(default=0, verbose_name='Sıra')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
