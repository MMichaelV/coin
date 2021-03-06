# Generated by Django 2.0.1 on 2018-01-10 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('coin', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('datePrice', models.DateTimeField()),
                ('currentPrice', models.FloatField()),
                ('link_to_exch', models.URLField()),
                ('fl_added', models.BooleanField(default=False)),
            ],
        ),
    ]
