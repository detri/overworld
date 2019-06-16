# Generated by Django 2.2.1 on 2019-06-16 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190604_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='backlog',
            field=models.ManyToManyField(related_name='backlog', to='games.Game'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to='games.Game'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='liked',
            field=models.ManyToManyField(related_name='liked', to='games.Game'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='played',
            field=models.ManyToManyField(related_name='played', to='games.Game'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='wishlist',
            field=models.ManyToManyField(related_name='wishlist', to='games.Game'),
        ),
    ]
