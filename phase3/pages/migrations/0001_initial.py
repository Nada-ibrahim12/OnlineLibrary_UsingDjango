# Generated by Django 5.0.5 on 2024-05-22 04:28

import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=25)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bId', models.IntegerField(unique=True)),
                ('bName', models.CharField(max_length=255)),
                ('bAuthor', models.CharField(max_length=100)),
                ('bCategory', models.CharField(choices=[('romance', 'Romance'), ('horror', 'Horror'), ('fantasy', 'Fantasy'), ('science_fiction', 'Science Fiction'), ('history', 'History')], max_length=100)),
                ('bDescription', models.TextField(max_length=1000)),
                ('bPublishDate', models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2024, 5, 22))])),
                ('bCoverImage', models.ImageField(blank=True, default='images/13.jpg', upload_to='book_covers/')),
                ('is_borrowed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(default='', max_length=25)),
                ('LastName', models.CharField(default='', max_length=25)),
                ('usernamee', models.CharField(default='', max_length=50, unique=True)),
                ('Email', models.EmailField(default='', max_length=100, unique=True)),
                ('Password', models.CharField(default='', max_length=50, validators=[django.core.validators.MinLengthValidator(8)])),
                ('AccType', models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserAcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=25)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('duration', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
