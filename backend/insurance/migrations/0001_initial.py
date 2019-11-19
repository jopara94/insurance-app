# Generated by Django 2.2.7 on 2019-11-19 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('phone_number', models.CharField(default='', max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('relationship', models.CharField(default='', max_length=12)),
                ('member', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='dependents', to='insurance.Member')),
            ],
        ),
    ]
