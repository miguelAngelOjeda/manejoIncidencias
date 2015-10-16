from django.test.client import RequestFactory
from django.test import TestCase
from django.contrib.auth.models import User
from usuario.views import usuarios, nuevo_usuario
from models import Usuario

class UsuariosTest(TestCase):
    """
    Clase que realiza el Test del modulo de administracion de usuarios
    """
    def setUp(self):
        """
        Funcion que inicializa el RequestFactory y un usuario de prueba para
        realizar los test
        """
        # Se crea el Request factory pars simular peticiones
        self.factory = RequestFactory()
        # Se crea el User que realiza las peticiones
        self.user = User.objects.create_user(username='testuser', email='test@test.com', password='test')



    def test_view_nuevo_usuario(self):
        """
        Funcion que realiza el test sobre la vista UserCreate que crea
        un nuevo usuario
        """
        # se loguea el usuario testuser


        # se crea un usuario
        user = User.objects.create_user(username='user_prueba', email='test@test2.com', password='prueba')
        Usuario.objects.create(user=user, telefono='222', direccion='Avenida', documento='12345')

        self.assertEqual(Usuario.objects.get(user=user).user.username, 'user_prueba')
        self.assertEqual(Usuario.objects.get(user=user).user.email, 'test@test2.com')
        self.assertEqual(Usuario.objects.get(user=user).telefono, '222')
        self.assertEqual(Usuario.objects.get(user=user).documento, '12345')


        print 'Test de nuevo_usuario realizado exitosamente'


    def test_view_desactivar_usuario(self):
        """
        Funcion que realiza el test sobre la vista inactivar_usuario que cambia el estado
        de un usuario a inactivo
        """
        # se loguea el usuario testuser
        user = self.client.login(username='testuser', password='test')
        self.assertTrue(user)
        # se crea un usuario
        user = User.objects.create_user(username='user_prueba', email='test@test4.com', password='prueba')
        usuario_prueba = Usuario.objects.create(user=user, telefono='222', direccion='Avenida', documento='12345')
        # se marca al usuario como inactivo
        usuario_prueba.user.is_active = False
        usuario_prueba.save()

        self.assertEqual(usuario_prueba.user.is_active, False)

        print 'Test de desactivar_usuario realizado exitosamente'

    def test_view_activar_usuario(self):
        """
        Funcion que realiza el test sobre la vista activar_usuario que cambia el estado
        de un usuario a activo
        """
        # se loguea el usuario testuser
        user = self.client.login(username='testuser', password='test')
        self.assertTrue(user)
        # se crea un usuario
        user = User.objects.create_user(username='user_prueba', email='test@test5.com', password='prueba')
        usuario_prueba = Usuario.objects.create(user=user, telefono='222', direccion='Avenida', documento='12345')
        # se marca al usuario como inactivo
        usuario_prueba.user.is_active = False
        usuario_prueba.save()
        self.assertEqual(usuario_prueba.user.is_active, False)
        # se marca al usuario como activo
        usuario_prueba.user.is_active = True
        usuario_prueba.save()

        self.assertEqual(usuario_prueba.user.is_active, True)

        print 'Test de activar_usuario realizado exitosamente'

