
from django.test import TestCase
from .models import Patrimonio
class DetailModelTest(TestCase):
    def test_detalhe(self):
        patrimonio = Patrimonio(nome="Nome do patrimonio")
        self.assertEqual(str(patrimonio), patrimonio.nome)





