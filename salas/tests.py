from django.test import TestCase


from .models import Sala
    class DetailModelTest(TestCase):
        def test_detalhe(self):
            sala = Sala(nome="Minha sala")
            self.assertEqual(str(sala), sala.nome)





