from django.test import TestCase, Client
from django.urls import reverse
from user.models import UserCourse, Users, UserMentor
from teacher.models import Kelas
from owner.models import Kategori, Level
import json
from django.contrib.auth.models import User  # Import the User model

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('user:index')
        self.kelas = reverse("user:kelas")
        self.koridor = reverse("user:koridor", args=['1'])

        # Create a user and log them in
        self.user = User.objects.create_user(username='testuser', email='testuser@gmail.com', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.userModel = Users.objects.create(user=self.user)
        
        self.kategori1 = Kategori.objects.create(name="Speaking", keterangan="ini keterangan")
        self.level1 = Level.objects.create(name="Beginner", keterangan="ini keterangan")

        self.kelas1 = Kelas.objects.create(kelas="TOEFL", kategori=self.kategori1, level=self.level1, urutan=1)


    def test_index_nomentor(self):
        response = self.client.get(self.index)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/index.html')

    def test_kelas_index(self):
        response = self.client.get(self.kelas)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/kelas/index.html')

    def test_kelas_koridor_not_enroll(self):
        response = self.client.get(self.koridor)
        self.assertEquals(response.status_code, 302)


    def test_kelas_koridor_enroll(self):
        response = self.client.get(self.koridor)
        UserCourse.objects.create(user=self.user, kelas=self.kelas1)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/kelas/index.html')
