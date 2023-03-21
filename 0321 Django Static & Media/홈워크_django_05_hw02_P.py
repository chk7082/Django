class Reservation(models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField()