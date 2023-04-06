from django.test import TestCase
from django.urls import reverse
from .models import Pie, Cake


class indexTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class pieTest(TestCase):
    def test_newPie_added(self):
        numPie = Pie.objects.count()
        Pie.objects.create(name='pie2', price_m=34, price_l=59, p_image="someUrl")
        self.assertEqual(Pie.objects.count(), numPie+1)


class cakeTest(TestCase):
    def test_newCake_added(self):
        numCake = Cake.objects.count()
        Cake.objects.create(name='cake2', price_m=34, price_l=59, p_image="someUrl")
        self.assertEqual(Cake.objects.count(), numCake+1)      
