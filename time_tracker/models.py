from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class TimeEntry(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Time Entry for {self.project.name}"

    def save(self, *args, **kwargs):
        self.duration_minutes = (self.end_time - self.start_time).total_seconds() / 60
        super().save(*args, **kwargs)


class LineItem(models.Model):
    time_entry = models.ForeignKey(TimeEntry, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_charged = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Line Item for {self.time_entry.project.name}"

    def save(self, *args, **kwargs):
        if not self.hourly_rate:
            self.hourly_rate = self.time_entry.project.hourly_rate
        super().save(*args, **kwargs)


class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    line_items = models.ManyToManyField(LineItem)
    invoice_date = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    paid_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Invoice for {self.client.name} - {self.invoice_date}"
