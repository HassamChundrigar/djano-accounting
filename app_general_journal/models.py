from django.db import models

# Create your models here.


class Head(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title


class SubHead(models.Model):
    title = models.CharField(max_length=50)
    head = models.ForeignKey(Head, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        unique_together = (('head', 'title'),)
        index_together = (('head', 'title'),)

    def __str__(self):
        return self.title


class AccountSubHead(models.Model):
    title = models.CharField(max_length=50)
    subhead = models.ForeignKey(SubHead, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        unique_together = (('subhead', 'title'),)
        index_together = (('subhead', 'title'),)

    def __str__(self):
        return self.title


Entry_Types = (
    ('Debit', "Debit"),
    ('Credit', "Credit"),
)

class Entry(models.Model):
    dated = models.DateField()
    head = models.ForeignKey(Head, on_delete=models.CASCADE)
    subhead = models.ForeignKey(SubHead, on_delete = models.CASCADE)
    account_subhead = models.ForeignKey(AccountSubHead, on_delete=models.CASCADE)
    entry_type = models.CharField(choices=Entry_Types, max_length=15)
    amount = models.DecimalField(decimal_places=2, max_digits=100)
    description = models.CharField(max_length=1000, null=True, blank=True)

    created_on = models. DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)