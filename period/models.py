from django.db import models

class PeriodModel(models.Model):
    class Meta:
        verbose_name = "اطلاعات دوره  "
        verbose_name_plural = "اطلاعات دوره "

    prd_number = models.IntegerField(verbose_name= "شماره دوره ")
    prd_fasl = models.IntegerField(verbose_name= "فصل دوره")
    prd_startdate = models.IntegerField(verbose_name= "تاریخ شروع دوره ")
    prd_finishdate = models.IntegerField(verbose_name= "تاریخ پایان دوره")
    prd_modat = models.IntegerField(verbose_name= "مدت دوره")
    prd_tedadjoje = models.IntegerField(verbose_name= "تعداد جوجه ")
    
    def __str__(self):
        return self.prd_number, self.prd_startdate,self.prd_modat

    

class JojeModel(models.Model):
    class Meta:
        verbose_name = "ثبت اطلاعات جوجه  "
        verbose_name_plural = "ثبت اطلاعات جوجه "
    joj_sen =  models.IntegerField(verbose_name= "شماره دوره ")
    joj_talafat =  models.IntegerField(verbose_name= "شماره دوره ")
    joj_hazfi =  models.IntegerField(verbose_name= "شماره دوره ")
    joj_jamekol =  models.IntegerField(verbose_name= "شماره دوره ")
    joj_vazn =  models.IntegerField(verbose_name= "شماره دوره ")
    joj_tozihat =  models.IntegerField(verbose_name= "شماره دوره ")
    joj_nehad =  models.IntegerField(verbose_name= "شماره دوره ")
    joj_namemadar =  models.IntegerField(verbose_name= "شماره دوره ")
    joj_senmadar =  models.IntegerField(verbose_name= "شماره دوره ")




class DailyperformanceModel(models.Model):
    class Meta:
        verbose_name = "عملکرد روزانه  "
        verbose_name_plural = "عملکرد روزانه "

    dlp_date = models.IntegerField(verbose_name= " تاریح  روز")
    dlp_sen = models.IntegerField(verbose_name= "سن گله ")
    dlp_talafat = models.IntegerField(verbose_name= "تعداد تلفات ")
    dlp_hazfi = models.IntegerField(verbose_name= "تعداد حذفی ")
    dlp_talafatkol = models.IntegerField(verbose_name= " تلفات کل ")
    dlp_danmasrafi = models.IntegerField(verbose_name= "مقدار دان مصرفی ")
    dlp_dankol = models.IntegerField(verbose_name= "دان مصرفی کل ")
    dlp_saranedan = models.IntegerField(verbose_name= "سرانه مصرفی دان ")
    dlp_vazn = models.IntegerField(verbose_name= "میانگین وزن ")
    dlp_afzayeshvaznroozane = models.IntegerField(verbose_name= "افزایش وزن روزانه ")
    dlp_dama = models.IntegerField(verbose_name= "میانگین دما ")
    dlp_abmasrafi = models.IntegerField(verbose_name= "مقدار اب مصرفی ")
    dlp_etefaghat = models.IntegerField(verbose_name= "اتفاقات مهم ")
    dlp_daroo = models.IntegerField(verbose_name= "دارو مصرفی ")
    dlp_vaksan = models.IntegerField(verbose_name= "واکسن مصرفی  ")
    dlp_tozih = models.IntegerField(verbose_name= "توضیحات  ")
