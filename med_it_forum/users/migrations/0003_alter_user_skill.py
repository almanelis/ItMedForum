# Generated by Django 5.0.1 on 2024-01-26 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_middle_name_alter_user_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='skill',
            field=models.ManyToManyField(blank=True, related_name='users', to='users.skill'),
        ),
    ]
