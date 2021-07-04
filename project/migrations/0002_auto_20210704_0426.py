# Generated by Django 3.2.4 on 2021-07-04 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer1', models.IntegerField(default=0, verbose_name='How many planets does the solar sytem have?')),
                ('answer2', models.IntegerField(default=0, verbose_name='How far away is the sun from the earth? (In kms)')),
                ('answer3', models.BooleanField(default=False, verbose_name='Does Saturn have ring system?')),
                ('answer4', models.BooleanField(default=False, verbose_name='The name of Mercury is based off of greek mythology.')),
                ('answer5', models.IntegerField(default=0, verbose_name='How many moons does Mars have?')),
                ('answer6', models.BooleanField(default=False, verbose_name='Does a planet have to orbit a star?')),
                ('answer7', models.IntegerField(default=0, verbose_name='How many moons does the Earth have?')),
                ('answer8', models.BooleanField(default=False, verbose_name='Does the name Venus have greek inspirations?')),
                ('answer9', models.BooleanField(default=False, verbose_name='Is Mars often referred as the Blue Planet?')),
                ('answer10', models.CharField(default='Satellite', max_length=20, verbose_name='What is the name of the satellite orbiting the Earth?')),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='groupName',
            field=models.CharField(max_length=30, verbose_name='Group Name'),
        ),
        migrations.AlterField(
            model_name='group',
            name='numberMembers',
            field=models.IntegerField(default=0, verbose_name='Number of Members'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=40, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(max_length=40, verbose_name='User Name'),
        ),
    ]
