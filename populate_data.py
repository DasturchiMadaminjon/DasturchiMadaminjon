import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from adminapp.models import Faculty, Kafedra, Subject, Group, Teacher, Student

# Clear existing data if any
Faculty.objects.all().delete()
Kafedra.objects.all().delete()
Subject.objects.all().delete()
Group.objects.all().delete()
Teacher.objects.all().delete()
Student.objects.all().delete()

# Create Faculties
f1 = Faculty.objects.create(name="Computer Science")
f2 = Faculty.objects.create(name="Economics")
f3 = Faculty.objects.create(name="Humanities")

# Create Kafedras
k1 = Kafedra.objects.create(name="Software Engineering")
k2 = Kafedra.objects.create(name="Artificial Intelligence")
k3 = Kafedra.objects.create(name="Digital Marketing")

# Create Subjects
s1 = Subject.objects.create(name="Python Programming", description="Learn Python from basics to advanced.")
s2 = Subject.objects.create(name="Database Systems", description="SQL and NoSQL database management.")
s3 = Subject.objects.create(name="Macroeconomics", description="Study of economy-wide phenomena.")
s4 = Subject.objects.create(name="Modern History", description="Analysis of world events since 19th century.")

# Create Groups
g1 = Group.objects.create(name="CS-101", faculty=f1)
g2 = Group.objects.create(name="EC-202", faculty=f2)
g3 = Group.objects.create(name="HM-303", faculty=f3)

# Create Teachers
t1 = Teacher.objects.create(first_name="Dr. Alan", last_name="Turing", email="turing@example.com", phone="+123456789")
t1.subjects.add(s1, s2)

t2 = Teacher.objects.create(first_name="Prof. John", last_name="Keynes", email="keynes@example.com", phone="+987654321")
t2.subjects.add(s3)

# Create Students
Student.objects.create(first_name="Alice", last_name="Smith", email="alice@example.com", group=g1)
Student.objects.create(first_name="Bob", last_name="Johnson", email="bob@example.com", group=g1)
Student.objects.create(first_name="Charlie", last_name="Brown", email="charlie@example.com", group=g2)
Student.objects.create(first_name="Diana", last_name="Prince", email="diana@example.com", group=g3)

print("Data populated successfully!")
