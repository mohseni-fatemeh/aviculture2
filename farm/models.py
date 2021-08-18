from django.db import models

class FarmModel(models.Model):
    class Meta:
        verbose_name = "مدیریت فارم "
        verbose_name_plural = "مدیریت فارم "

    frm_name = models.CharField(max_length=30, verbose_name= "نام فارم")
    frm_zarfiat = models.IntegerField(verbose_name= "ظرفیت فارم")
    frm_tedad_salon = models.IntegerField(verbose_name= "تعداد سالن")

    def __str__(self):
        return self.frm_name


class SalonModel(models.Model):
    class Meta:
        verbose_name = "مدیریت سالن  "
        verbose_name_plural = "مدیریت سالن "

    sln_name = models.CharField(max_length=30, verbose_name= "نام سالن")
    sln_tedad = models.IntegerField(verbose_name= "تعداد سالن")
    sln_zarfiat = models.IntegerField(verbose_name= "ظرفیت سالن")
    sln_frm_name = models.ForeignKey(FarmModel, on_delete = models.CASCADE)

    def __str__(self):
        return self.sln_name

