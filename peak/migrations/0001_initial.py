# Generated by Django 3.0.3 on 2020-02-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.IntegerField(default=1)),
                ('lon', models.IntegerField(default=1)),
                ('altitude', models.IntegerField(default=1)),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
