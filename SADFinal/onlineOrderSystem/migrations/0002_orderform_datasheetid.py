# Generated by Django 3.0 on 2020-06-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineOrderSystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderform',
            name='dataSheetID',
            field=models.CharField(default='none', max_length=1000, verbose_name='規格單'),
        ),
    ]