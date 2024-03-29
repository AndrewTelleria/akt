# Generated by Django 2.0.7 on 2018-08-01 21:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180801_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='skill1',
            new_name='skill_1',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='skill2',
            new_name='skill_2',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='skill3',
            new_name='skill_3',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='skill4',
            new_name='skill_4',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='skill5',
            new_name='skill_5',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='skill1_percentage',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='skill2_percentage',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='skill3_percentage',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='skill4_percentage',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='skill5_percentage',
        ),
        migrations.AddField(
            model_name='homepage',
            name='skill_1_percentage',
            field=models.IntegerField(blank=True, help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skill_2_percentage',
            field=models.IntegerField(blank=True, help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skill_3_percentage',
            field=models.IntegerField(blank=True, help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skill_4_percentage',
            field=models.IntegerField(blank=True, help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skill_5_percentage',
            field=models.IntegerField(blank=True, help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.', null=True),
        ),
    ]
