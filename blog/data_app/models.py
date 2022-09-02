from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Profession(models.Model):
    """
     профессии
    """
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True)
    actual = models.BooleanField(default=True)

    def __str__(self):
        return self.name

def get_default_profession():
    #в первой строке таблицы profession помещена запись
    # для дефолтного случая (без реальной ссылки)
    return 1


class Staff(models.Model):
    """
    данные о персонале
    """
    name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    mail = models.EmailField(blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    profession = models.ForeignKey(Profession, null=True, on_delete=models.CASCADE)
    actual = models.BooleanField(default=True)

    def __str__(self):
        s = '' + self.name + '_/_' + self.first_name
        return s


class Client(models.Model):
    """
    данные о клиентах
    """
    name = models.CharField(max_length=32, blank=True)
    first_name = models.CharField(max_length=32, blank=True)
    middle_name = models.CharField(max_length=32, blank=True)
    pseudonym = models.CharField(max_length=32, blank=True)
    sex = models.BooleanField(blank=True)
    mail = models.EmailField(blank=True)
    telegram_id = models.CharField(max_length=16, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    description = models.TextField(blank=True)
    actual = models.BooleanField(default=True)

    def __str__(self):
        s = '' + self.name + '_/_' + self.first_name
        return s


class Room(models.Model):
    """
     комнаты
     поле sex - комната для мужчин (=True),
                        для женщин (=False)
                        для всех   (=None)
    """
    name = models.CharField(max_length=32, unique=True)
    sex = models.BooleanField(null=True, default=None)
    description = models.TextField(blank=True)
    in_use = models.BooleanField(null=True, default=True)

    def __str__(self):
        return self.name


class Procedure(models.Model):
    """
     список процедур
    """
    name = models.CharField(max_length=32, unique=True)
    profession = models.ForeignKey(Profession, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    dt = models.DurationField(blank=True, null=True)
    actual = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TimetableStatus(models.Model):
    """
     статус записи в расписании
    """
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class WorkingTime(models.Model):
    """
     таблица рабочего времени с шагом 10 минут
    """
    staff = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    ready = models.BooleanField(default=False)

class TimeTable(models.Model):
    """
    Расписание загруженности мастеров и помещений
    """
    start_time = models.DateTimeField()
    procedure = models.ForeignKey(Procedure, null=True, on_delete=models.CASCADE)
    spec_requirements = models.TextField(blank=True, null=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)      # клиент, сделавший заказ
    client_req_time = models.DateTimeField(blank=True, null=True)                           # время размещения заказ
                                                                                 # сотрудник, подтвердивший заказ
    staff_confirm = models.ForeignKey(Staff, related_name='tt_confirm', null=True, on_delete=models.CASCADE)

    staff_req_time = models.DateTimeField(blank=True, null=True)                            # время подтверждения заказа
                                                                                 # сотрудник, выполняющй заказ
    staff_worker = models.ForeignKey(Staff, related_name='tt_worker', null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey(TimetableStatus, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
