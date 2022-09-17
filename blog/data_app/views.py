from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from .models import News, Procedure, Staff
from .forms import BookingForm
from .support_func import make_letter_text

# Create your views here.

def main_view(request):
    last_news = 2
    posts = News.objects.order_by('-day')[:last_news]
    return render(request, 'data_app/index.html', context={'posts': posts})

def post(request, id):
    post = get_object_or_404(News, id=id)
    return render(request, 'data_app/post.html', context={'post': post})

def service(request):
    posts = Procedure.objects.exclude(name='default').all()
    return render(request, 'data_app/service.html', context={'posts': posts})

def hairdresser(request):
    staff = Staff.objects.exclude(name='default').all()
    return render(request, 'data_app/hairdresser.html', context={'posts': staff})

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_order = {}
            booking_order['hairdresser'] = form.cleaned_data['hairdresser']
            booking_order['service'] = form.cleaned_data['service']
            booking_order['booking_day'] = form.cleaned_data['booking_day']
            booking_order['booking_time'] = form.cleaned_data['booking_time']
            booking_order['remark'] = form.cleaned_data['remark']
            booking_order['customer'] = form.cleaned_data['customer']
            booking_order['contact'] = form.cleaned_data['contact']

            send_mail('Новый заказ',make_letter_text(booking_order),
                      '7900953@gmail.com', ['nik_agafonov@icloud.com'],
                      fail_silently=False)



            return HttpResponseRedirect(reverse('salon:index'))

        else:
            return render(request, 'data_app/booking.html', context={'form': form})
    else:
        form = BookingForm()
        return render(request, 'data_app/booking.html', context={'form': form})

def contacts(request):
    pass
    return render(request, 'data_app/contacts.html')
