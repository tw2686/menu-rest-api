from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import MenuSections
from .serializers import MenuSectionsSerializer
import json


class ModelTestCase(APITestCase):
    """This class tests for the model"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.name = "Lunch Specials"
        self.menusection = MenuSections(name=self.name)

    def test_model_can_create_menusection(self):
        """Tests the model can create menusection"""
        old_count = MenuSections.objects.count()
        self.menusection.save()
        new_count = MenuSections.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        """Tests model returns readable string as representation"""
        self.assertEqual(str(self.menusection), self.name)


class BaseViewTest(APITestCase):
    """This class tests for views"""
    client = APIClient()

    def postRequest(self, data):
        """Helper method for post requests"""
        return self.client.post(
            reverse("add"),
            data=json.dumps(data),
            content_type='application/json'
        )

    def putRequest(self, data, id):
        """Helper method for put requests"""
        return self.client.put(
            reverse('edit', kwargs={'pk': id}),
            data=json.dumps(data),
            content_type='application/json'
        )

    def getSingle(self, pk=0):
        """Helper method for get requests for single"""
        return self.client.get(
            reverse('single', kwargs={'pk': pk})
        )

    def deleteSingle(self, pk=0):
        """Helper method for delete requests single"""
        return self.client.delete(
            reverse('delete', kwargs={'pk': pk})
        )

    def setUp(self):
        """Set up test variables"""
        MenuSections.objects.create(name="section1")
        MenuSections.objects.create(name="section2")
        MenuSections.objects.create(name="section3")
        self.valid_id = 1
        self.valid_data = {"id": self.valid_id, "name": "test menu section"}


class GetASingleMenuSectionsTest(BaseViewTest):
    """This class tests to get a single menusections"""

    def test_get_a_menusection(self):
        """Test that a single menusection of a given id is returned"""
        response = self.getSingle(self.valid_id)
        expected = MenuSections.objects.get(pk=self.valid_id)
        serialized = MenuSectionsSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllMenuSectionsTest(BaseViewTest):
    """This class tests to get all menusections"""

    def test_get_all_menusections(self):
        """Test that all songs added in setUp method exists with GET request"""
        response = self.client.get(
            reverse("all")
        )
        expected = MenuSections.objects.all()
        serialized = MenuSectionsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AddMenuSectionsTest(BaseViewTest):
    """This class tests adding menusections"""

    def test_add_menusection(self):
        """Tests that a menusection can be added"""
        response = self.postRequest(self.valid_data)
        self.assertEqual(response.data['name'], self.valid_data['name'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class EditMenuSectionsTest(BaseViewTest):
    """This class tests editing menusections"""

    def test_edit_menusection(self):
        """Tests that a menusection can be edited"""
        response = self.putRequest(self.valid_data, self.valid_id)
        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteMenuSectionsTest(BaseViewTest):
    """This class tests updating menusections"""

    def test_delete_menusection(self):
        """Tests that a menusection can be deleted"""
        response = self.deleteSingle(1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
