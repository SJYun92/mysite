# Generated by Django 4.1.7 on 2023-03-09 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0004_mydesignitem_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydesignitem',
            name='img',
            field=models.TextField(default='https://izapislewska.weebly.com/uploads/4/9/8/6/49862713/custom-design_orig.png'),
        ),
    ]