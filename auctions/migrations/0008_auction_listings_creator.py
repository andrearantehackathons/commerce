# Generated by Django 4.0.3 on 2022-03-20 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auction_listings_closed_auction_listings_watchlisted'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listings',
            name='creator',
            field=models.CharField(default=None, max_length=64),
        ),
    ]