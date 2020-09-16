# Generated by Django 2.2.5 on 2020-09-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200914_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_methode',
            field=models.CharField(choices=[('email', 'Email'), ('github', 'Github'), ('kakao', 'Kakao')], default='email', max_length=50),
        ),
    ]
