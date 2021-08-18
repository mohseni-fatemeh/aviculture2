from django.contrib import admin

from period.models import PeriodModel,DailyperformanceModel,JojeModel


admin.site.register(PeriodModel)
admin.site.register(DailyperformanceModel)
admin.site.register(JojeModel)