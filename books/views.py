from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations for Books.
    - Anyone can list and search books (read-only).
    - Only logged-in users can create, update, or delete books.
    """

    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # secure create/update/delete

    # search functionality (by title or author)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']  # users can search by title or author
    ordering_fields = ['rating', 'created_at']  # allow sorting by rating or created date
