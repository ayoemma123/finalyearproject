# Generated by Django 5.0.4 on 2024-06-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=85)),
                ('trestbps', models.CharField(max_length=85)),
                ('chol', models.CharField(max_length=85)),
                ('thalach', models.CharField(max_length=85)),
                ('oldpeak', models.CharField(max_length=85)),
            ],
        ),
    ]