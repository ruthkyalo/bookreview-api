from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class Review(models.Model):
    # Each review is linked to a book
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    # Each review belongs to a user (the reviewer)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    # Rating (for example, 1–5 stars)
    rating = models.IntegerField()
    # Optional comment text
    comment = models.TextField(blank=True, null=True)
    # Many-to-many: users can "like" multiple reviews
    likes = models.ManyToManyField(User, related_name="liked_reviews", blank=True)
    # Auto-set timestamp when review is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # When you print a review, show who reviewed which book and the rating
        return f"{self.user.username} - {self.book.title} ({self.rating})"
