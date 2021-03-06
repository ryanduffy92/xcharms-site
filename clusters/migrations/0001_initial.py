# Generated by Django 3.1.3 on 2020-11-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root', models.CharField(max_length=50)),
                ('z', models.DecimalField(decimal_places=4, max_digits=8)),
                ('ra', models.DecimalField(decimal_places=4, max_digits=10)),
                ('dec', models.DecimalField(decimal_places=4, max_digits=10)),
                ('goodtime', models.DecimalField(decimal_places=2, max_digits=20)),
                ('catalogue', models.CharField(max_length=20)),
            ],
        ),
    ]
