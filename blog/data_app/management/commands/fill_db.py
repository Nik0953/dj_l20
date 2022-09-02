from django.core.management.base import BaseCommand
from data_app.models import Profession, Staff, Client, Room, Procedure, TimetableStatus, WorkingTime, TimeTable

class Command(BaseCommand):

    def handle(self, *args, **options):

        # Выбираем ВСЕ категории
        profs = Profession.objects.all()
        print(profs)
        print('type:', type(profs))
        print('=======================')
        for item in profs:
            print(item)
            print(item.name)
            print(type(item))

        print('End')

        # # Выбрать ОДНУ категорию
        # category = Category.objects.get(name='Игрушки')
        # print(category)
        # print(type(category))
        #
        # # Несколько
        # category = Category.objects.filter(name='Игрушки')
        # print(category)
        # print(type(category))
        #
        # # Первый пост
        # post = Post.objects.first()
        #
        # print(post)
        #
        # # Связанные поля
        # # ForeignKey
        # print(post.category)
        # print(type(post.category))
        # print(post.category.name)
        # # ManyToMany
        # print(post.tags.all())
        # print(post.tags.first())
        # print(post.tags.first().name)
        # print(type(post.tags.first()))
        # print(post.tags.filter(name='Один'))
        #
        # # print(Tag.objects.first().posts.all())
        # # Создание
        # Category.objects.create(name='Новая', description='Что то')
        #
        # # Изменение
        # category = Category.objects.get(name='Новая')
        # category.name = 'Измененная'
        # category.save()
        #
        # # Удаление
        # # Можно одну,
        # category.delete()
        # # можно несколько
        # # Category.objects.all().delete()
        #
        # print(category.has_image())