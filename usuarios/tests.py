from django.test import TestCase


from .models import Usuario
class DetailModelTest(TestCase):
    def test_detalhe(self):
        usuario = Usuario(nome="Meu nome")

        self.assertEqual(str(usuario), usuario.nome)




