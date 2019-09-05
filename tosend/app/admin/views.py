# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required


from . import admin
from forms import TaskForm,RegistrationForm

from .. import db
from ..models import Task,Employee


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Department Views


@admin.route('/task/add', methods=['GET', 'POST'])
@login_required
def add_task():
    """
    Add a department to the database
    """
    check_admin()

    add_task = True

    form = TaskForm()
    if form.validate_on_submit():
        task = Task(name=form.name.data,
                                description=form.description.data,status=form.status.data,importance=form.importance.data,towhom=form.towhom.data)
        try:
            # add department to the database
            db.session.add(task)
            db.session.commit()
            flash('You have successfully added a new Task.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_task'))

    # load department template
    return render_template('admin/task/task.html', action="Add",
                           add_task=add_task, form=form,
                           title="Add Task")


@admin.route('/task/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    """
    Edit a department
    """
    check_admin()

    add_task = False

    task = Task.query.get_or_404(id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.name = form.name.data
        task.description = form.description.data
        task.status = form.status.data
        task.importance = form.importance.data
        task.towhom = form.towhom.data
        db.session.commit()
        flash('You have successfully edited the department.')

        # redirect to the departments page
        return redirect(url_for('admin.list_task'))

    form.description.data = task.description
    form.name.data = task.name
    form.status.data = task.status
    form.importance.data = task.importance
    form.towhom.data = task.towhom
    return render_template('admin/task/task.html', action="Edit",
                           add_task=add_task, form=form,
                                task=task, title="Edit Task")


@admin.route('/task/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_task(id):
    """
    Delete a department from the database
    """
    check_admin()
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('admin.list_task'))

@admin.route('/task/showall', methods=['GET','POST'])
@login_required
def list_task():

    check_admin()
    tasks = Task.query.all()
    return render_template('admin/task/task_showall.html',
                           tasks=tasks, title="Tasks")




@admin.route('/employee/add', methods=['GET', 'POST'])
@login_required
def add_employee():
    """
    Add a department to the database
    """
    check_admin()

    add_employee = True

    form = RegistrationForm()
    if form.validate_on_submit():
        employees = Employee(email=form.email.data,
                                username=form.username.data,
                                password=form.password.data)


        try:
            # add department to the database
            db.session.add(employees)
            db.session.commit()
            flash('You have successfully added a new Employee.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_employee'))

    # load department template
    return render_template('admin/employee/employee.html', action="Add",
                           add_employee=add_employee, form=form,
                           title="Add Task")

@admin.route('/employee/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_employee(id):
    """
    Edit a department
    """
    check_admin()

    add_employee = False

    employee = Employee.query.get_or_404(id)
    form = RegistrationForm(obj=employee)
    if form.validate_on_submit():
        employee.email = form.email.data
        employee.username = form.username.data
        db.session.commit()
        flash('You have successfully edited the Employee.')

        # redirect to the departments page
        return redirect(url_for('admin.list_employee'))

    form.email.data = employee.email
    form.username.data = employee.username


    return render_template('admin/employee/employee.html', action="Edit",
                           add_employee=add_employee, form=form,
                                employee=employee, title="Edit Employee")


@admin.route('/employee/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_employee(id):
    """
    Delete a department from the database
    """
    check_admin()
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    flash('You have successfully deleted the Employee.')

    # redirect to the departments page
    return redirect(url_for('admin.list_employee'))


@admin.route('/employee/showall', methods=['GET','POST'])
@login_required
def list_employee():

    check_admin()
    employee = Employee.query.all()
    return render_template('admin/employee/employee_showall.html',
                           employee=employee, title="Employees")



