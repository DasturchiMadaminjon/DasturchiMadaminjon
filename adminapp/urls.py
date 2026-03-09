from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('signup/', SignUpView.as_view(), name='signup'),
    
    # Faculty
    path('faculties/', faculty_list, name='faculty_list'),
    path('faculties/create/', faculty_create, name='faculty_create'),
    path('faculties/<int:pk>/update/', faculty_update, name='faculty_update'),
    path('faculties/<int:pk>/delete/', faculty_delete, name='faculty_delete'),

    # Kafedra
    path('kafedras/', kafedra_list, name='kafedra_list'),
    path('kafedras/create/', kafedra_create, name='kafedra_create'),
    path('kafedras/<int:pk>/update/', kafedra_update, name='kafedra_update'),
    path('kafedras/<int:pk>/delete/', kafedra_delete, name='kafedra_delete'),

    # Subject
    path('subjects/', subject_list, name='subject_list'),
    path('subjects/create/', subject_create, name='subject_create'),
    path('subjects/<int:pk>/update/', subject_update, name='subject_update'),
    path('subjects/<int:pk>/delete/', subject_delete, name='subject_delete'),
    
    # Group
    path('groups/', group_list, name='group_list'),
    path('groups/create/', group_create, name='group_create'),
    path('groups/<int:pk>/update/', group_update, name='group_update'),
    path('groups/<int:pk>/delete/', group_delete, name='group_delete'),
    
    # Teacher
    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/create/', teacher_create, name='teacher_create'),
    path('teachers/<int:pk>/update/', teacher_update, name='teacher_update'),
    path('teachers/<int:pk>/delete/', teacher_delete, name='teacher_delete'),
    
    # Student
    path('students/', student_list, name='student_list'),
    path('students/create/', student_create, name='student_create'),
    path('students/<int:pk>/update/', student_update, name='student_update'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),
]