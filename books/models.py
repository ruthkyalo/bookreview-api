from django.db import models

class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=255)

    # Author name (simple text field for now)
    author = models.CharField(max_length=255)

    # Short description or summary
    description = models.TextField()

    # Average rating (we’ll use this for "top-rated")
    rating = models.FloatField(default=0.0)

    # When the book was created (auto set)
    created_at = models.DateTimeField(auto_now_add=True)

    # When the book was last updated (auto set)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
