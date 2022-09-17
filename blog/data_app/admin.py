from django.contrib import admin

from .models import Profession, Staff, Client, Room, Procedure, TimetableStatus, WorkingTime, TimeTable, News

admin.site.register(Profession)
admin.site.register(Staff)
admin.site.register(Client)
admin.site.register(Room)
admin.site.register(TimetableStatus)
admin.site.register(WorkingTime)
admin.site.register(TimeTable)
admin.site.register(Procedure)
admin.site.register(News)


