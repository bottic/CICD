
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from django_project.permissions import IsOwner
from .srializers import PostSerializer, CommentSerializers, AdvSerializers, MassageSerializer
from main.models import Post, Car, Person, Order, Comment, Adv, Message
import random
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated

def test_view(request):
    return render(request, 'base.html')


def posts(request):
    posts_list = Post.objects.all()
    return render(request, 'posts.html', context={'posts': posts_list})


def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_details.html', context={'post': post})


def hello(request):
    name = request.GET.get('name', '111')
    age = int(request.GET.get('age', 11))
    print(age)
    return HttpResponse(f'hello, {name}')


def sum(request, a, b):
    context = {
        'a': a,
        'b': b,
        'result': int(a) + int(b)
    }
    return render(request, 'sum.html', context)


CONTEND = [str(i) for i in range(1000)]


def pagi(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTEND, 20)
    page = paginator.get_page(page_number)
    return render(request, 'pagi.html', context={'page': page})


def create_car(request):
    car = Car(brand=random.choice(['b1', 'b2', 'b3']),
              model=random.choice(['m1', 'm2', 'm3']),
              color=random.choice(['c1', 'c2', 'c3']))
    car.save()
    return HttpResponse(f'OK, new car -- {car.brand}, {car.model}')


def list_car(request):
    car_obj = Car.objects.filter(brand__startswith='b')
    cars = [f' {c.id}::{c.brand}, {c.model}:{c.color} | {c.owners.count()}' for c in car_obj]
    return HttpResponse('<br>'.join(cars))


def create_person(request):
    car_obj = Car.objects.all()
    for car in car_obj:
        Person(name='demo1', car=car).save()
    return HttpResponse('OK')


def list_person(request):
    person_obj = Person.objects.all()
    people = [f'{p.name}: {p.car}' for p in person_obj]
    # person = [f'{p.id}:: {p.name} car -- {p.car}' for p in person_obj]
    return HttpResponse('<br>'.join(people))


def list_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', context={'orders': orders})


@api_view(['GET', 'POST'])
def demo(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        ser = PostSerializer(posts, many=True)
        return Response(ser.data)
    else:
        ...


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user']
    search_fields = ['text', ]
    ordering_fields = ['id', 'user', 'text', 'created_at']


class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializers
    permission_classes = [IsAuthenticated, IsOwner]
    throttle_classes = [AnonRateThrottle]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MassageSerializer