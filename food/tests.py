from django.test import TestCase
from django.urls import reverse
from .models import Pie, Cake, Donut, Order


class indexTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class pieTest(TestCase):
    def test_newPie_added(self):
        numPie = Pie.objects.count()
        Pie.objects.create(name='pie2', price_m=34, price_l=59, p_image="someUrl")
        self.assertEqual(Pie.objects.count(), numPie+1)


class donutTest(TestCase):
    def test_newDonut_added(self):
        numDonut = Donut.objects.count()
        Donut.objects.create(name='donut2', price_m=3, price_l=5, p_image="someUrl")
        self.assertEqual(Donut.objects.count(), numDonut+1)


class cakeTest(TestCase):
    def test_newCake_added(self):
        numCake = Cake.objects.count()
        Cake.objects.create(name='cake2', price_m=34, price_l=59, p_image="someUrl")
        self.assertEqual(Cake.objects.count(), numCake+1)      


class orderTest(TestCase):
    def test_newOrder_added(self):
        numOrder = Order.objects.count()
        self.assertEqual(Order.objects.count(), numOrder+0) 
