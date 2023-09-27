from sqlalchemy import func, text
from sqlalchemy.orm import Session
from models import Student, Grade, Group, Teacher, Subject

def select_1(session: Session):
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    subquery = session.query(
        Student.student_id,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade).group_by(Student.student_id).subquery()

    query = session.query(
        Student.first_name,
        Student.last_name,
        subquery.c.avg_grade
    ).join(subquery, Student.student_id == subquery.c.student_id).\
        order_by(subquery.c.avg_grade.desc()).limit(5)

    result = query.all()
    return result

def select_2(session: Session, subject_name: str):
    """Знайти студента із найвищим середнім балом з певного предмета."""
    subquery = session.query(
        Student.student_id,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade).join(Subject).\
        filter(Subject.subject_name == subject_name).group_by(Student.student_id).subquery()

    query = session.query(
        Student.first_name,
        Student.last_name,
        subquery.c.avg_grade
    ).join(subquery, Student.student_id == subquery.c.student_id).\
        order_by(subquery.c.avg_grade.desc()).limit(1)

    result = query.first()
    return result

def select_3(session: Session, subject_name: str):
    """Знайти середній бал у групах з певного предмета."""
    query = session.query(
        Group.group_name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Student).join(Grade).join(Subject).\
        filter(Subject.subject_name == subject_name).group_by(Group.group_name)

    result = query.all()
    return result

def select_4(session: Session):
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    query = session.query(
        func.avg(Grade.grade).label('avg_grade')
    )

    result = query.first()
    return result

def select_5(session: Session, teacher_id: int):
    """Знайти які курси читає певний викладач."""
    query = session.query(
        Subject.subject_name
    ).filter(Subject.teacher_id == teacher_id)

    result = query.all()
    return result

def select_6(session: Session, group_name: str):
    """Знайти список студентів у певній групі."""
    query = session.query(
        Student.first_name,
        Student.last_name
    ).join(Group).filter(Group.group_name == group_name)

    result = query.all()
    return result

def select_7(session: Session, group_name: str, subject_name: str):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    query = session.query(
        Student.first_name,
        Student.last_name,
        Grade.grade
    ).join(Group).join(Grade).join(Subject).filter(
        Group.group_name == group_name,
        Subject.subject_name == subject_name
    )

    result = query.all()
    return result

def select_8(session: Session, teacher_id: int):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    query = session.query(
        Subject.subject_name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade).filter(Subject.teacher_id == teacher_id).group_by(Subject.subject_name)

    result = query.all()
    return result

def select_9(session: Session, student_id: int):
    """Знайти список курсів, які відвідує певний студент."""
    query = session.query(
        Subject.subject_name
    ).join(Grade).filter(Grade.student_id == student_id)

    result = query.all()
    return result

def select_10(session: Session, student_id: int, teacher_id: int):
    """Список курсів, які певному студенту читає певний викладач."""
    query = session.query(
        Subject.subject_name
    ).join(Grade).filter(
        Grade.student_id == student_id,
        Subject.teacher_id == teacher_id
    )

    result = query.all()
    return result
