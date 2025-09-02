from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import *
from .serializers import *


# generics.CreateAPIView -- Post only
# generics.ListAPIView --- Get all
# generics.RetrieveAPIView --- Get single
# generics.UpdateAPIView --- Update
# generics.DestroyAPIView --- Delete
# generics.ListCreateAPIView --- Get all & Post
# generics.RetrieveDestroyAPIView --- Get single & Delete
# generics.RetrieveUpdateAPIView --- Get single & Update
# generics.RetrieveUpdateDestroyAPIView --- Get single & Update & Delete

class BookView(ModelViewSet):

    queryset = Book.objects.all()

    serializer_class = Book_Serializer

class LaptopView(generics.ListCreateAPIView):

    def get_queryset(self):
        return Laptop.objects.filter(brand='Dell')

    def perform_create(self, serializer):

        #print(self.request.data)

        serializer.save(user_type="high performance")

    queryset = Laptop.objects.all()
    serializer_class = Laptop_Serializer

class LaptopViewById(generics.RetrieveUpdateDestroyAPIView):

    def perform_update(self, serializer):

        #print(self.request.data)

        serializer.save(user_type="low performance")



    queryset = Laptop.objects.all()
    serializer_class = Laptop_Serializer