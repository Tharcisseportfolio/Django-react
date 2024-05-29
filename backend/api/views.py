from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):#get function with the notes of the current user

        user = self.request.user
        return Note.objects.filter(author=user) #return the notes of the current user

    def perform_create(self, serializer): #save the author of the note
        if serializer.is_valid():
            user = self.request.user
            serializer.save(author=user) #save the author of the note
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView): #delete a note
    queryset = Note.objects.all() #get all the notes
    serializer_class = NoteSerializer # use the serializer
    permission_classes = [IsAuthenticated] #only authenticated users can delete a note


    def get_queryset(self): #get the notes of the current user
        user = self.request.user #get the current user
        return Note.objects.filter(author=user) #return the notes of the current user




