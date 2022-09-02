from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from data_app.models import Staff, WorkingTime

class Command(BaseCommand):

    def handle(self, *args, **options):

        """
        заполняем строки таблицы WorkingTime
        """
        # пока для примера заполним таблицу
        # записями для всех сотрудников
        # от 8 утра 9 января 2023 г. с шагом 10 минут

        h0 = 8
        d0 = 9
        m0 = 1
        y0 = 2023
        t0 = datetime(y0, m0, d0, h0)
        dt = timedelta(minutes=10)
        # количество интервалов времени 12ч*6 = 72 в день
        t_intervals = 72

        # список сотрудников
        workers = Staff.objects.exclude(name='default')

        for wrk in workers:
            t = t0
            for t_count in range(t_intervals):
                WorkingTime.objects.create(staff=wrk, start_time=t, ready=True)
                t += dt
