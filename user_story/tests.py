from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from models import UserStory
from proyecto.models import Proyecto
from django.contrib.auth import login, authenticate, logout


# Create your tests here.
class UserStoriesTest(TestCase):
    """
    Clase que realiza el Test del modulo de administracion de user stories
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

    def test_view_IndexView(self):
        """
        Funcion que realiza el test sobre la vista UserIndexView que genera
        lista de user stories
        """
        # se loguea el usuario testuser
        user = authenticate(username='testuser', password='test')
        self.assertTrue(user)
        user2 = User.objects.create_user(username='user_prueba', email='test@test22.com', password='prueba')

        proyecto = Proyecto.objects.create(codigo='codi', nombre_corto='test',
                                           nombre_largo='test', scrum_master=user2)
        proyecto.save()

        lista = Proyecto.objects.all()
        #print lista


        # se crean 10 user stories para controlar que se retorne la lista completa de user stories, que seran 10 en total
        for i in range(10):
            user_story = UserStory.objects.create(nombre='us%s' % i, descripcion='desc%s' % i,
                                                  valor_negocio='%d' % i, proyecto=proyecto)
            user_story.save()



        # verificamos que la vista devuelva el template adecuado
        request = self.factory.get(reverse('user_stories:index', args=[proyecto.pk]))
        request.user = self.user



        print 'Test de IndexView de User Story realizado exitosamente'

    def test_view_UserStoryCreate(self):
        """
        Funcion que realiza el test sobre la vista UserStoryCreate que crea
        un nuevo user story
        """
        # se loguea el usuario testuser
        user = authenticate(username='testuser', password='test')
        self.assertTrue(user)

        user3 = User.objects.create_user(username='user_prueba3', email='test@test223.com', password='prueba')
        # se crea un usuario


        proyecto = Proyecto.objects.create(codigo='codi', nombre_corto='test',
                                           nombre_largo='test', cancelado=False, scrum_master=user3)

        proyecto.save()

        user_story = UserStory.objects.create(nombre='us', descripcion='desc',
                                              valor_negocio=20, proyecto=proyecto)
        user_story.save()

        self.assertEqual(user_story.nombre, 'us')
        self.assertEqual(user_story.valor_negocio, 20)

        print 'Test de UserStoryCreate realizado exitosamente'

    def test_view_UserStoryUpdate(self):
        """
        Funcion que realiza el test sobre la vista UserStoryUpdate que modifica
        un user story existente
        """
        # se loguea el usuario testuser
        user = authenticate(username='testuser', password='test')
        self.assertTrue(user)

        user4 = User.objects.create_user(username='user_prueba4', email='test@test224.com', password='prueba')
        # se crea un usuario
        proyecto = Proyecto.objects.create(codigo='codi', nombre_corto='test',
                                           nombre_largo='test', cancelado=False, scrum_master=user4)

        proyecto.save()

        user_story = UserStory.objects.create(nombre='us', descripcion='desc',
                                              valor_negocio=20, proyecto=proyecto)
        user_story.save()

        user_story.valor_tecnico = 30
        user_story.save()
        # se crean nuevos valores para los atributos
        nuevo_valor = 5
        nuevo_nombre = 'hu'

        # Se modifican los atributos del usuario
        user_story.valor_negocio = nuevo_valor
        user_story.nombre = nuevo_nombre
        user_story.save()

        self.assertEqual(user_story.valor_negocio, 5)
        self.assertEqual(user_story.nombre, 'hu')
        self.assertEqual(user_story.valor_tecnico, 30)

        print 'Test de UserStoryUpdate realizado exitosamente'

    def test_view_descartar_user_story(self):
        """
        Funcion que realiza el test sobre la vista que cambia el estado
        de un user story a descartado
        """
        # se loguea el usuario testuser
        user = authenticate(username='testuser', password='test')
        self.assertTrue(user)

        user5 = User.objects.create_user(username='user_prueba5', email='test@test225.com', password='prueba')
        # se crea un usuario
        proyecto = Proyecto.objects.create(codigo='codi', nombre_corto='test',
                                           nombre_largo='test', cancelado=False, scrum_master=user5)

        proyecto.save()

        user_story = UserStory.objects.create(nombre='us', descripcion='desc',
                                              valor_negocio=20, proyecto=proyecto, estado='Activo')
        user_story.save()

        # se marca al proyecto
        user_story.estado = 'Descartado'
        user_story.save()

        self.assertEqual(user_story.estado, 'Descartado')

        print 'Test de descartar_user_story realizado exitosamente'

