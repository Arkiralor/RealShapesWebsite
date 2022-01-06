# Generated by Django 3.0.8 on 2020-08-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servname', models.CharField(max_length=16)),
                ('custname', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='serv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servname', models.CharField(max_length=16)),
                ('servdesc', models.TextField()),
                ('servpic', models.ImageField(upload_to='assets/images/productimg')),
                ('servishigh', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='trans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servname', models.CharField(max_length=16)),
                ('custname', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrfname', models.CharField(max_length=16)),
                ('usrlname', models.CharField(max_length=16)),
                ('usremail', models.CharField(max_length=32)),
                ('usrphn', models.CharField(max_length=12)),
                ('usrpwd', models.CharField(max_length=16)),
                ('usradd1', models.CharField(max_length=64)),
                ('usradd2', models.CharField(max_length=64)),
                ('usrcity', models.CharField(max_length=16)),
                ('usrdist', models.CharField(max_length=16)),
                ('usrstate', models.CharField(max_length=16)),
                ('usrpincode', models.CharField(max_length=7)),
            ],
        ),
    ]
