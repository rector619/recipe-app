# Generated by Django 4.1 on 2022-08-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipes/'),
        ),
    ]