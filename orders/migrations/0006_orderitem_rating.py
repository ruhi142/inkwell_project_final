from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0005_order_delivered_at_order_out_for_delivery_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="rating",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]