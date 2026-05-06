from django.contrib.auth.models import User
from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Academic', 'Academic'),
        ('Creative', 'Creative'),
        ('Tech', 'Tech'),
        ('Wellness', 'Wellness'),
        ('Other', 'Other'),
    ]

    CONTACT_CHOICES = [
        ('Email', 'Email'),
        ('Phone', 'Phone'),
        ('DM', 'Direct message'),
    ]

    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Busy', 'Busy'),
        ('Flexible', 'Flexible'),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_free = models.BooleanField(default=False)
    contact_preference = models.CharField(max_length=20, choices=CONTACT_CHOICES)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return f"{self.title} by {self.owner.username}"

    def get_average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(review.rating for review in reviews) / reviews.count(), 1)
        return None

    def get_review_count(self):
        return self.reviews.count()

    def has_completed_booking_with(self, user):
        return self.booking_requests.filter(
            requester=user,
            status='completed',
        ).exists()

    def can_be_reviewed_by(self, user):
        if not user.is_authenticated or user == self.owner:
            return False
        return self.has_completed_booking_with(user)


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('skill', 'reviewer')

    def __str__(self):
        return f"{self.reviewer.username} - {self.rating} stars on {self.skill.title}"


class BookingRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='booking_requests')
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    message = models.TextField(
        max_length=500,
        help_text="Tell the skill provider what you need help with"
    )
    preferred_date = models.DateField(
        null=True,
        blank=True,
        help_text="When would you like the session?"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.requester.username} requested {self.skill.title} ({self.status})"

    def can_be_updated_by(self, user):
        return user == self.requester or user == self.skill.owner
