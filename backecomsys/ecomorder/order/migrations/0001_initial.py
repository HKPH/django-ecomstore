# Generated by Django 4.0.1 on 2024-05-09 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_id', models.PositiveIntegerField()),
                ('order_datetime', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('product_type', models.CharField(max_length=100)),
                ('product_id', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
            ],
        ),
    ]
