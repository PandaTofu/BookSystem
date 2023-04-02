# Generated by Django 4.1.5 on 2023-03-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.CharField(
                blank=True,
                help_text="avatar",
                max_length=255,
                null=True,
                verbose_name="avatar",
            ),
        ),
    ]
