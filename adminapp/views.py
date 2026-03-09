from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Subject, Group, Teacher, Student, Faculty, Kafedra
from .forms import SubjectForm, GroupForm, TeacherForm, StudentForm, FacultyForm, KafedraForm

def login_required_decorator(func):
    return login_required(func, login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")

def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")
    return render(request, 'login.html')

@login_required_decorator
def home_page(request):
    ctx = {
        'subjects_count': Subject.objects.count(),
        'groups_count': Group.objects.count(),
        'teachers_count': Teacher.objects.count(),
        'students_count': Student.objects.count(),
        'faculties_count': Faculty.objects.count(),
        'kafedras_count': Kafedra.objects.count(),
    }
    return render(request, 'dashboard.html', ctx)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_page")
    template_name = "signup.html"

# Generic CRUD helper
@login_required_decorator
def crud_view(request, model_class, form_class, redirect_url, obj_id=None):
    obj = get_object_or_404(model_class, id=obj_id) if obj_id else None
    if request.method == 'POST':
        form = form_class(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=obj)
    return render(request, 'generic_form.html', {'form': form, 'obj': obj})

# Faculty
@login_required_decorator
def faculty_list(request):
    objects = Faculty.objects.all()
    return render(request, 'faculty_list.html', {'objects': objects})

@login_required_decorator
def faculty_create(request):
    return crud_view(request, Faculty, FacultyForm, 'faculty_list')

@login_required_decorator
def faculty_update(request, pk):
    return crud_view(request, Faculty, FacultyForm, 'faculty_list', obj_id=pk)

@login_required_decorator
def faculty_delete(request, pk):
    obj = get_object_or_404(Faculty, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('faculty_list')
    return render(request, 'delete_confirm.html', {'obj': obj})

# Kafedra
@login_required_decorator
def kafedra_list(request):
    objects = Kafedra.objects.all()
    return render(request, 'kafedra_list.html', {'objects': objects})

@login_required_decorator
def kafedra_create(request):
    return crud_view(request, Kafedra, KafedraForm, 'kafedra_list')

@login_required_decorator
def kafedra_update(request, pk):
    return crud_view(request, Kafedra, KafedraForm, 'kafedra_list', obj_id=pk)

@login_required_decorator
def kafedra_delete(request, pk):
    obj = get_object_or_404(Kafedra, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('kafedra_list')
    return render(request, 'delete_confirm.html', {'obj': obj})

# Subjects
@login_required_decorator
def subject_list(request):
    objects = Subject.objects.all()
    return render(request, 'subject_list.html', {'objects': objects})

@login_required_decorator
def subject_create(request):
    return crud_view(request, Subject, SubjectForm, 'subject_list')

@login_required_decorator
def subject_update(request, pk):
    return crud_view(request, Subject, SubjectForm, 'subject_list', obj_id=pk)

@login_required_decorator
def subject_delete(request, pk):
    obj = get_object_or_404(Subject, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('subject_list')
    return render(request, 'delete_confirm.html', {'obj': obj})

# Groups
@login_required_decorator
def group_list(request):
    objects = Group.objects.all()
    return render(request, 'group_list.html', {'objects': objects})

@login_required_decorator
def group_create(request):
    return crud_view(request, Group, GroupForm, 'group_list')

@login_required_decorator
def group_update(request, pk):
    return crud_view(request, Group, GroupForm, 'group_list', obj_id=pk)

@login_required_decorator
def group_delete(request, pk):
    obj = get_object_or_404(Group, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('group_list')
    return render(request, 'delete_confirm.html', {'obj': obj})

# Teachers
@login_required_decorator
def teacher_list(request):
    objects = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'objects': objects})

@login_required_decorator
def teacher_create(request):
    return crud_view(request, Teacher, TeacherForm, 'teacher_list')

@login_required_decorator
def teacher_update(request, pk):
    return crud_view(request, Teacher, TeacherForm, 'teacher_list', obj_id=pk)

@login_required_decorator
def teacher_delete(request, pk):
    obj = get_object_or_404(Teacher, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('teacher_list')
    return render(request, 'delete_confirm.html', {'obj': obj})

# Students
@login_required_decorator
def student_list(request):
    objects = Student.objects.all()
    return render(request, 'student_list.html', {'objects': objects})

@login_required_decorator
def student_create(request):
    return crud_view(request, Student, StudentForm, 'student_list')

@login_required_decorator
def student_update(request, pk):
    return crud_view(request, Student, StudentForm, 'student_list', obj_id=pk)

@login_required_decorator
def student_delete(request, pk):
    obj = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('student_list')
    return render(request, 'delete_confirm.html', {'obj': obj})
