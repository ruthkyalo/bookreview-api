from rest_framework import viewsets, filters, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer
from books.permissions import IsOwnerOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations for Books.
    - Anyone can list and search books (read-only).
    - Only logged-in users can create books.
    - Only the book owner can update or delete their book.
    """

    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer

    # Permissions:
    # Anyone can read (GET)
    # Logged-in users can create (POST)
    #  Only the owner can update/delete (PUT/PATCH/DELETE)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        Automatically assign the logged-in user as the book owner
        when a new book is created.
        """
        serializer.save(user=self.request.user)

    # Search & ordering functionality
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']  # Search by title or author
    ordering_fields = ['rating', 'created_at']  # Allow sorting by rating or creation date
