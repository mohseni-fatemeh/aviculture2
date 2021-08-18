from django.db import models



class CostModel(models.Model):
    class Meta:
        verbose_name = "هزینه ها "
        verbose_name_plural = "هزینه ها"
    ct_onvan = models.CharField(max_length=30, verbose_name= "شرح هزینه")
    ct_date = models.DateField(verbose_name= "تاریخ ")
    ct_mablagh = models.IntegerField(verbose_name= "مبلغ هزینه")
    ct_desc = models.CharField(max_length=300,verbose_name= "توضیحات هزینه")

    def __str__(self):
        return self.ct_onvan

