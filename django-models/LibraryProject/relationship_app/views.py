from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.
def BookListView(request):
    books = Book.objects.all()
    output = []
    for book in books:
        output.append(f"{book.title} by {book.author.name}")
    return render(request, "<br>".join(output))


class LibrarydetailView(DetailView):
    model = Library 
    template_name = "library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context
