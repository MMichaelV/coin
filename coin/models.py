from django.db import models


class Coin(models.Model):
    coin = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    datePrice = models.DateTimeField()
    currentPrice = models.FloatField()
    link_to_exch = models.URLField()
    fl_added = models.BooleanField(default=False)

    def __str__(self):
        return self.coin
