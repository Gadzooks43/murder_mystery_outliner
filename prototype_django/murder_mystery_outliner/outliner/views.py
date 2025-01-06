from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'projects_list_create')  # default to 'home' if no next param
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
    
    # If GET request, or user is not authenticated, just show the login page
    return render(request, 'auth/login.html')

@login_required
def projects_list_create(request):
    # Only try to create a project if 'name' is in the POST data
    if request.method == 'POST' and 'name' in request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects_list_create')
        # if not valid, fall through to re-render with errors
    else:
        form = ProjectForm()

    projects = Project.objects.all().order_by('-date_created')
    return render(request, 'projects/projects.html', {
        'form': form,
        'projects': projects,
    })

@login_required
def delete_project(request, pk):
    """
    Deletes the specified project by primary key, then redirects.
    """
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('projects_list_create')

@login_required
def project_detail(request, project_name):
    """
    Detail view for a single project, looked up by its 'name'.
    Note: This assumes names are unique enough or won't cause collisions.
    """
    project = get_object_or_404(Project, name=project_name)
    # For now, just render some simple detail
    return render(request, 'projects/project_detail.html', {
        'project': project
    })