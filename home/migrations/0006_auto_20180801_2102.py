# Generated by Django 2.0.7 on 2018-08-01 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180730_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='skill1_percentage',
            field=models.IntegerField(blank=True, help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skill2_percentage',
            field=models.IntegerField(blank=True, help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skill3_percentage',
            field=models.IntegerField(blank=True, help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skill4_percentage',
            field=models.IntegerField(blank=True, help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skill5_percentage',
            field=models.IntegerField(blank=True, help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.', max_length=100, null=True),
        ),
    ]
