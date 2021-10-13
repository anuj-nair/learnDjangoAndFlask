from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes


# Class Based View (CreateView)
class NotesCreateView(CreateView):
    model = Notes
#    fields = ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Class Based View (UpdateView)
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

# Class Based View (DeleteView)


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

# Class Based View (ListView)


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

# Class Based View (DetailView)


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'


# Function Based Views
# def list(requests):
#    all_notes = Notes.objects.all()
#    return render(requests, 'notes/notes_list.html',{'notes':all_notes})

# def detail(request, pk):
#    try:
#        note = Notes.objects.get(pk=pk)
#    except Notes.DoesNotExist:
#        raise Http404("Note doesn't Exist")
#    return render(request,'notes/notes_detail.html',{'note':note})
