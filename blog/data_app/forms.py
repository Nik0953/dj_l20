from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from .models import Staff, Procedure, TimeTable

class BookingForm(forms.Form):

    hairdresser = forms.ModelChoiceField(queryset=Staff.objects.exclude(name='default').all(), label='мастер ', required=False)
    service = forms.ModelChoiceField(queryset=Procedure.objects.exclude(name='default').all(), label='услуга ', help_text = '*')
    booking_day = forms.DateField(label='Удобная для Вас дата ', help_text='*', initial='02.01.2023')
    booking_time = forms.TimeField(label='Удобное для Вас время ', help_text='*', initial='15:30')
    remark = forms.CharField(label='Дополнительные пожелания ', required=False)
    customer = forms.CharField(label='Как к Вам обращаться? ', help_text='*')
    contact = forms.CharField(label='Как с Вами связаться (телефон/email)? ', help_text='*')



