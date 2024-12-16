from django.urls import path
from .import views


# Rest api version view of our notes
urlpatterns = [
    path("notes/", views.notes, name="notes"),
    path("notes/<slug:slug>/", views.note_detail, name="note-detail"),
    path("notes-search/", views.search_notes, name='notes-search')
]

# our end points
# endpoints:
# get all our notes and create new notes
# GET_ALL_NOTES_and_CREATE_NEW_NOTE = "127.0.0.1:8008/notes/"
# get a specific note, update the note, get a specific note, list a specific note
# GET_SPECIFIC_NOTE = "127.0.0.1:8008/notes/note-slug"
