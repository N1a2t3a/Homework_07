from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Student, Group, Teacher, Subject, Grade
import random
from datetime import date, timedelta

# Підключення до бази даних
engine = create_engine('postgresql://postgres:natalia_2007@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()

# Ініціалізація генератора випадкових даних
fake = Faker()

# Функція для генерації даних студента
def generate_student():
    first_name = fake.first_name()
    last_name = fake.last_name()
    return Student(first_name=first_name, last_name=last_name)

# Генерація студентів
students = [generate_student() for _ in range(50)]
session.add_all(students)
session.commit()

# Додавання груп
groups = [Group(group_name=f'Group {i+1}') for i in range(3)]
session.add_all(groups)
session.commit()

# Генерація даних викладачів
teachers = [Teacher(first_name=fake.first_name(), last_name=fake.last_name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

# Генерація даних предметів та призначення їх викладачам
subjects = []
for _ in range(8):
    teacher = random.choice(teachers)
    subject = Subject(subject_name=fake.word(), teacher=teacher)
    subjects.append(subject)
session.add_all(subjects)
session.commit()

# Генерація оцінок для студентів із предметів
for student in students:
    for subject in subjects:
        grade = round(random.uniform(3, 5), 2)
        exam_date = fake.date_between(start_date='-1y', end_date='today')
        session.add(Grade(student=student, subject=subject, grade=grade, exam_date=exam_date))
session.commit()

# Закриття сесії
session.close()
