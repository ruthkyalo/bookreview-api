from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # Only authenticated users can create, and only owners can update/delete
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Automatically link the logged-in user as the review author
        serializer.save(user=self.request.user)
