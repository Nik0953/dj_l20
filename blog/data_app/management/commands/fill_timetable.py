from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from data_app.models import Room, TimetableStatus, TimeTable

class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        заполняем таблицу TimeTable
        """
        # заполним таблицу
        # записями для всех комнат, так что в каждой комнате
        # можно будет записать только одного клиента
        # с 8 утра 9 января 2023 г. с шагом 10 минут до 20 часов.

        h0 = 8
        d0 = 9
        m0 = 1
        y0 = 2023
        t0 = datetime(y0, m0, d0, h0)
        dt = timedelta(minutes=10)
        # количество интервалов времени 12ч*6 = 72 в день
        t_intervals = 72

        # список комнат, для которых создается расписание
        rooms = Room.objects.exclude(name='default')

        status0 = TimetableStatus.objects.get(name='not assigned')

        for rm in rooms:
            t = t0
            for t_count in range(t_intervals):
                TimeTable.objects.create(start_time=t,
                                         room=rm,
                                         status=status0
                                         )
                t += dt
