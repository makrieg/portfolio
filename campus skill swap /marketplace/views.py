from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SkillForm, UserRegisterForm, ReviewForm, BookingRequestForm
from .models import Skill, Review, BookingRequest


def home(request):
    """Show all public skill posts on the homepage with search functionality."""
    skills = Skill.objects.order_by('-created_at')
    query = request.GET.get('q', '')
    selected_category = request.GET.get('category', '')
    categories = [choice[0] for choice in Skill.CATEGORY_CHOICES]

    if query:
        skills = skills.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        )

    if selected_category:
        skills = skills.filter(category=selected_category)

    return render(request, 'marketplace/home.html', {
        'skills': skills,
        'query': query,
        'categories': categories,
        'selected_category': selected_category,
    })


def register(request):
    """Register a new user account."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome! Your account is ready.')
            return redirect('marketplace:dashboard')
    else:
        form = UserRegisterForm()

    return render(request, 'marketplace/register.html', {'form': form})


@login_required
def logout_view(request):
    """Log out the user and redirect to home."""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('marketplace:home')


@login_required
def dashboard(request):
    """Show the logged-in user's own skill posts."""
    skills = Skill.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'marketplace/dashboard.html', {'skills': skills})


def skill_detail(request, pk):
    """Display one skill post in detail with reviews."""
    skill = get_object_or_404(Skill, pk=pk)
    reviews = Review.objects.filter(skill=skill).order_by('-created_at')
    can_review = request.user.is_authenticated and skill.can_be_reviewed_by(request.user)

    form = ReviewForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to leave a review.')
            return redirect('marketplace:login')

        if skill.owner == request.user:
            messages.error(request, 'You cannot review your own skill.')
            return redirect('marketplace:skill_detail', pk=skill.pk)

        if not skill.can_be_reviewed_by(request.user):
            messages.error(request, 'You can only review a skill after completing a booking for it.')
            return redirect('marketplace:skill_detail', pk=skill.pk)

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.skill = skill
            review.reviewer = request.user

            try:
                review.save()
                messages.success(request, 'Your review has been posted.')
                return redirect('marketplace:skill_detail', pk=skill.pk)
            except IntegrityError:
                messages.error(request, 'You have already reviewed this skill.')

    return render(request, 'marketplace/skill_detail.html', {
        'skill': skill,
        'reviews': reviews,
        'form': form,
        'can_review': can_review,
    })


@login_required
def skill_create(request):
    """Create a new skill listing."""
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user
            skill.save()
            messages.success(request, 'Skill posted successfully.')
            return redirect('marketplace:skill_detail', pk=skill.pk)
    else:
        form = SkillForm()

    return render(request, 'marketplace/skill_form.html', {
        'form': form,
        'title': 'Post a Skill',
    })


@login_required
def skill_update(request, pk):
    """Edit an existing skill post owned by the user."""
    skill = get_object_or_404(Skill, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully.')
            return redirect('marketplace:skill_detail', pk=skill.pk)
    else:
        form = SkillForm(instance=skill)

    return render(request, 'marketplace/skill_form.html', {
        'form': form,
        'title': 'Edit Skill',
    })


@login_required
def skill_delete(request, pk):
    """Delete a skill post if the current user owns it."""
    skill = get_object_or_404(Skill, pk=pk, owner=request.user)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted.')
        return redirect('marketplace:dashboard')

    return render(request, 'marketplace/skill_confirm_delete.html', {'skill': skill})


@login_required
def booking_request_create(request, skill_pk):
    """Create a new booking request for a skill."""
    skill = get_object_or_404(Skill, pk=skill_pk)

    if skill.owner == request.user:
        messages.error(request, 'You cannot request a session for your own skill.')
        return redirect('marketplace:skill_detail', pk=skill.pk)

    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.skill = skill
            booking.requester = request.user
            booking.save()
            messages.success(request, 'Your booking request has been sent!')
            return redirect('marketplace:booking_requests_sent')
    else:
        form = BookingRequestForm()

    return render(request, 'marketplace/booking_request_form.html', {
        'form': form,
        'skill': skill,
        'title': f'Request Session: {skill.title}',
    })


@login_required
def booking_requests_received(request):
    """Show booking requests received for user's skills."""
    requests = BookingRequest.objects.filter(
        skill__owner=request.user
    ).order_by('-created_at')

    return render(request, 'marketplace/booking_requests_received.html', {
        'requests': requests,
    })


@login_required
def booking_requests_sent(request):
    """Show booking requests sent by the user."""
    requests = BookingRequest.objects.filter(
        requester=request.user
    ).order_by('-created_at')

    return render(request, 'marketplace/booking_requests_sent.html', {
        'requests': requests,
    })


@login_required
def booking_request_update_status(request, pk, status):
    """Update the status of a booking request."""
    booking = get_object_or_404(BookingRequest, pk=pk)

    if not booking.can_be_updated_by(request.user):
        messages.error(request, 'You do not have permission to update this request.')
        return redirect('marketplace:booking_requests_received')

    valid_statuses = ['accepted', 'declined', 'completed', 'cancelled']
    if status not in valid_statuses:
        messages.error(request, 'Invalid status.')
        return redirect('marketplace:booking_requests_received')

    booking.status = status
    booking.save()

    status_messages = {
        'accepted': 'Booking request accepted!',
        'declined': 'Booking request declined.',
        'completed': 'Booking marked as completed!',
        'cancelled': 'Booking request cancelled.',
    }

    messages.success(request, status_messages.get(status, 'Status updated.'))

    if request.user == booking.skill.owner:
        return redirect('marketplace:booking_requests_received')
    return redirect('marketplace:booking_requests_sent')
