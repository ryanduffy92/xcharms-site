# Generated by Django 3.1.3 on 2020-12-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0003_auto_20201230_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obs',
            name='expgoodtime',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Expected length (ks)'),
        ),
    ]
