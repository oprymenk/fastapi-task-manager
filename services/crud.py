from models.models import Task


def get_tasks(db):
    return db.query(Task).all()


def get_task_by_id(db, task_id):
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db, title, status, priority, deadline):
    task = Task(
        title=title,
        status=status,
        priority=priority,
        deadline=deadline
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(db, task_id, title, status, priority, deadline):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        task.title = title
        task.status = status
        task.priority = priority
        task.deadline = deadline

        db.commit()
        db.refresh(task)

    return task


def delete_task(db, task_id):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()