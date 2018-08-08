# Generated by Django 2.0.6 on 2018-08-07 17:46

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', help_text="user's gender, only can select 'male' or 'female' ", max_length=6, verbose_name='gender')),
                ('mobile', models.CharField(blank=True, help_text="mobile number, usually contain 11 number, like '15033517890'", max_length=100, null=True, verbose_name='mobile')),
                ('email', models.EmailField(blank=True, help_text="email address, like 'neuq@neuq.edu.cn'", max_length=100, null=True, verbose_name='email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': ('user_profile',),
                'verbose_name_plural': ('user_profile',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='verify code, contain 4 numbers. in development env, the value is 1234', max_length=10, verbose_name='verify_code')),
                ('mobile', models.CharField(help_text="mobile number, usually contain 11 number, like '15033517890'", max_length=11, verbose_name='mobile')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='add item time', verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'SMS_verify',
                'verbose_name_plural': 'SMS_verify',
            },
        ),
    ]
