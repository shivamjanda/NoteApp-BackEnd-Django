from django.shortcuts import render
from noteapp.models import Note
from noteapp.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q


# Create your views here.


# CRUD operations

# Search fuctionalilty 
@api_view(['GET'])
def search_notes(request):
    query = request.query_params.get("search")
    notes = Note.objects.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(category__icontains=query))
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Getting all the notes (listing note) and also creating new note
@api_view(["GET", "POST"])
def notes(request):
    if request.method == "GET":
        # Serializing what we have in our database to make it come out in JSON form
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # De serialize the object to save into the database
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 # View specific note, update specific note and delete specific note   
@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, slug):
    try:
        note = Note.objects.get(slug=slug)
    except Note.DoesNotExist: # if the note is not found from the slug return the error response
        return Response(status-status.HTTP_404_NOT_FOUND) 

    # Get note request (serializer is to make it into json format to read)
    if request.method == 'GET': 
        serializer = NoteSerializer(note)
        return Response(serializer.data)

       # Update note request  
    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_TP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete note reqest
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)