# Generated by Django 5.0.7 on 2024-08-02 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(to='product.color'),
        ),
    ]
