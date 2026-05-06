import random
from datetime import timedelta
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from marketplace.models import BookingRequest, Review, Skill


class Command(BaseCommand):
    help = "Seed the database with reusable demo data."

    def handle(self, *args, **options):
        random.seed(42)

        demo_users = [
            {
                "username": "demo_alex",
                "email": "alex@example.com",
                "first_name": "Alex",
                "last_name": "Chen",
            },
            {
                "username": "demo_jordan",
                "email": "jordan@example.com",
                "first_name": "Jordan",
                "last_name": "Patel",
            },
            {
                "username": "demo_maya",
                "email": "maya@example.com",
                "first_name": "Maya",
                "last_name": "Lopez",
            },
            {
                "username": "demo_sam",
                "email": "sam@example.com",
                "first_name": "Sam",
                "last_name": "Brooks",
            },
            {
                "username": "demo_riley",
                "email": "riley@example.com",
                "first_name": "Riley",
                "last_name": "Nguyen",
            },
        ]

        skill_blueprints = [
            {
                "owner": "demo_alex",
                "title": "Calculus Study Sessions",
                "description": "One-on-one help with derivatives, integrals, and exam prep for intro calculus classes.",
                "category": "Academic",
                "price": Decimal("20.00"),
                "is_free": False,
                "contact_preference": "Email",
                "availability": "Flexible",
            },
            {
                "owner": "demo_alex",
                "title": "Python Debugging Help",
                "description": "Bring your assignment or side project and we can work through errors together step by step.",
                "category": "Tech",
                "price": Decimal("0.00"),
                "is_free": True,
                "contact_preference": "DM",
                "availability": "Available",
            },
            {
                "owner": "demo_jordan",
                "title": "Portfolio Photography",
                "description": "Outdoor portrait and headshot sessions for student orgs, resumes, and social profiles.",
                "category": "Creative",
                "price": Decimal("35.00"),
                "is_free": False,
                "contact_preference": "Phone",
                "availability": "Busy",
            },
            {
                "owner": "demo_jordan",
                "title": "Poster Design Critiques",
                "description": "Fast feedback on typography, layout, and visual hierarchy for campus flyers and posters.",
                "category": "Creative",
                "price": Decimal("12.00"),
                "is_free": False,
                "contact_preference": "Email",
                "availability": "Flexible",
            },
            {
                "owner": "demo_maya",
                "title": "Yoga for Beginners",
                "description": "Gentle guided sessions focused on mobility, breathing, and stress relief between classes.",
                "category": "Wellness",
                "price": Decimal("15.00"),
                "is_free": False,
                "contact_preference": "DM",
                "availability": "Available",
            },
            {
                "owner": "demo_maya",
                "title": "Biology Lab Study Group",
                "description": "Review lab reports, memorization strategies, and quiz prep for first-year biology.",
                "category": "Academic",
                "price": Decimal("0.00"),
                "is_free": True,
                "contact_preference": "Email",
                "availability": "Flexible",
            },
            {
                "owner": "demo_sam",
                "title": "Resume Review for Internships",
                "description": "Detailed resume edits with stronger bullet points tailored for internships and campus jobs.",
                "category": "Other",
                "price": Decimal("10.00"),
                "is_free": False,
                "contact_preference": "Email",
                "availability": "Available",
            },
            {
                "owner": "demo_riley",
                "title": "Web Design Basics",
                "description": "Learn HTML, CSS, and how to make a small landing page feel polished and intentional.",
                "category": "Tech",
                "price": Decimal("25.00"),
                "is_free": False,
                "contact_preference": "DM",
                "availability": "Flexible",
            },
        ]

        review_blueprints = [
            ("Python Debugging Help", "demo_maya", 5, "Super patient and explained each bug in a way that finally clicked."),
            ("Calculus Study Sessions", "demo_riley", 4, "Very clear explanations and the practice problems were helpful."),
            ("Portfolio Photography", "demo_sam", 5, "Photos turned out great and the session felt really relaxed."),
            ("Yoga for Beginners", "demo_alex", 5, "Great pacing for beginners and I left feeling much less stressed."),
            ("Web Design Basics", "demo_jordan", 4, "Helped me understand layout and spacing without overcomplicating it."),
            ("Resume Review for Internships", "demo_maya", 5, "My resume reads much stronger now and I got interview callbacks."),
        ]

        booking_blueprints = [
            ("Calculus Study Sessions", "demo_sam", "I need help reviewing for next week's midterm.", 3, "pending"),
            ("Python Debugging Help", "demo_riley", "Can you help me fix a Django template issue?", 2, "accepted"),
            ("Portfolio Photography", "demo_alex", "Looking for two outdoor headshots for LinkedIn.", 5, "completed"),
            ("Yoga for Beginners", "demo_jordan", "Interested in a low-stress evening session this weekend.", 4, "pending"),
            ("Web Design Basics", "demo_maya", "I'd love help polishing a club landing page.", 6, "declined"),
        ]

        with transaction.atomic():
            # Remove previously seeded demo users and all related sample data.
            User.objects.filter(username__startswith="demo_").delete()

            users = {}
            for user_data in demo_users:
                user = User.objects.create_user(
                    username=user_data["username"],
                    email=user_data["email"],
                    password="password123",
                    first_name=user_data["first_name"],
                    last_name=user_data["last_name"],
                )
                users[user.username] = user

            skills = {}
            for blueprint in skill_blueprints:
                skill = Skill.objects.create(
                    owner=users[blueprint["owner"]],
                    title=blueprint["title"],
                    description=blueprint["description"],
                    category=blueprint["category"],
                    price=blueprint["price"],
                    is_free=blueprint["is_free"],
                    contact_preference=blueprint["contact_preference"],
                    availability=blueprint["availability"],
                )
                skills[skill.title] = skill

            for skill_title, reviewer_username, rating, comment in review_blueprints:
                Review.objects.create(
                    skill=skills[skill_title],
                    reviewer=users[reviewer_username],
                    rating=rating,
                    comment=comment,
                )

            today = timezone.localdate()
            for skill_title, requester_username, message, days_out, status in booking_blueprints:
                BookingRequest.objects.create(
                    skill=skills[skill_title],
                    requester=users[requester_username],
                    message=message,
                    preferred_date=today + timedelta(days=days_out),
                    status=status,
                )

        self.stdout.write(self.style.SUCCESS("Dummy data created successfully."))
        self.stdout.write("Demo login password for all sample users: password123")
        self.stdout.write("Sample users: " + ", ".join(user["username"] for user in demo_users))
