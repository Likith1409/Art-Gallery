# Generated by Django 5.0.3 on 2024-03-30 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=100)),
                ('cimage', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'db_table': 'cust',
            },
        ),
    ]
