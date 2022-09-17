"""
Вспомогательные функции
"""

from datetime import datetime

def make_letter_text(form_dict):
    """
    Принимает данные заполненной пользователем формы
    в виде словаря
    формирует текст для запроса админис
    :param form_dict: словарь из формы
    :return: текст для помещения email менеджеру
                                 - запрос на бронирование услуги
    """
    letter_text = 'ЗАПРОС НА УСЛУГУ   время: ' + str(datetime.now()) + '\n'
    letter_text += 'Имя клиента:       ' + form_dict['customer'] + '\n'
    letter_text += 'Запрошена услуга:  ' + str(form_dict['service']) + '\n'
    if form_dict['hairdresser']:
        letter_text += 'Желательно мастер: ' + str(form_dict['hairdresser']) + '\n'
    else:
        letter_text += 'Любой мастер' + '\n'
    letter_text += 'Запрошена дата:    ' + str(form_dict['booking_day']) + ' время: ' + str(form_dict['booking_time']) + '\n'
    letter_text += 'Особые пожелания:  ' + str(form_dict['remark']) + '\n'
    letter_text += 'Контакты клиента:  ' + str(form_dict['contact']) + '\n'
    letter_text += '='*80

    return letter_text