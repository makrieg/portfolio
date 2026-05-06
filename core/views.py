from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse, FileResponse
from django.views.decorators.http import require_http_methods
from .models import Project, Skill, Contact
from .forms import ContactForm
import os


class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(featured=True)[:3]
        context['skills'] = Skill.objects.all()[:6]
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ProjectListView(ListView):
    model = Project
    template_name = 'core/projects.html'
    context_object_name = 'projects'
    paginate_by = 6


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'core/project_detail.html'
    context_object_name = 'project'


class SkillsView(TemplateView):
    template_name = 'core/skills.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.order_by('category', 'order', 'name')
        context['categories'] = Skill.objects.values_list('category', flat=True).distinct()
        return context


class ResumeView(TemplateView):
    template_name = 'core/resume.html'


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})


def resume_download(request):
    """Download the resume PDF if it exists"""
    resume_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'resume.pdf')
    
    if os.path.exists(resume_path):
        return FileResponse(open(resume_path, 'rb'), as_attachment=True, filename='resume.pdf')
    else:
        messages.warning(request, 'Resume not available for download.')
        return redirect('resume')
