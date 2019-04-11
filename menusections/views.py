from rest_framework import generics
from .models import MenuSections
from .serializers import MenuSectionsSerializer


class MenuView(generics.ListCreateAPIView):
    """
    GET menusection/
    POST menusection/add/

    Add menu section by inputting name and clicking POST
    """

    queryset = MenuSections.objects.all()
    serializer_class = MenuSectionsSerializer

    def perform_create(self, serializer):
        """Save post data when creating new menusection"""
        serializer.save()


class SectionView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET menusection/id
    PUT menusection/id/edit/
    DELETE menusection/id/delete/

    Edit menu sections by inputting name and clicking PUT
    Delete menu sections by clicking DELETE
    """

    queryset = MenuSections.objects.all()
    serializer_class = MenuSectionsSerializer
