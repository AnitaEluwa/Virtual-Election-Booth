# Generated by Django 3.1.1 on 2020-09-30 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_count', models.IntegerField()),
                ('result_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.vote')),
            ],
        ),
    ]