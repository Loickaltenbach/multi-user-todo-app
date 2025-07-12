# Multi-User To-Do App

A Django multi-user task management application with authentication system.

## Features

### Task Model

- **user**: ForeignKey to User (task owner)
- **title**: CharField (max_length=255)
- **description**: TextField (optional)
- **priority**: Choices (low, normal, high)
- **due_date**: DateField (optional)
- **status**: Choices (to do, in progress, completed)
- **created_date**: DateTimeField (auto)
- **modified_date**: DateTimeField (auto)

### Class-based Views

- **TaskListView**: ListView filtered by logged-in user with pagination
- **TaskDetailView**: DetailView to view a task
- **TaskCreateView**: CreateView to add a task
- **TaskUpdateView**: UpdateView to modify a task
- **TaskDeleteView**: DeleteView to delete a task
- **CustomLoginView**: Custom login view
- **CustomLogoutView**: Custom logout view

### Security

- All views use `LoginRequiredMixin`
- Automatic filtering by logged-in user
- Only owners can view/modify/delete their tasks

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd multi-user-todo-app
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Configure the database

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

4. Create a superuser

```bash
python3 manage.py createsuperuser
```

5. Start the development server

```bash
python3 manage.py runserver
```

## Static Files (for Production)

To collect static files for production deployment:

```bash
python3 manage.py collectstatic --noinput
```

This will collect all static files into the `staticfiles/` directory.

## Usage

### Test account created

- **Username**: admin
- **Password**: admin123

### Main URLs

- `/`: Task list (automatic redirect to login if not authenticated)
- `/login/`: Login page
- `/logout/`: Logout
- `/task/new/`: Create a new task
- `/task/<id>/`: View a task
- `/task/<id>/edit/`: Edit a task
- `/task/<id>/delete/`: Delete a task
- `/admin/`: Admin interface

### User Interface

- Modern interface with Bootstrap 5
- Font Awesome icons
- Message system (success, error, warning)
- Automatic pagination
- Visual indicators for priority and status
- Responsive design

### Advanced Features

- Task statistics (total, pending, completed)
- Automatic filtering by user
- Alerts for overdue tasks
- Custom admin interface
- Form validation
- Confirmation messages

## Project Structure

```
multi-user-todo-app/
├── manage.py
├── requirements.txt
├── README.md
├── todoproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   └── tests.py
└── templates/
    ├── base.html
    ├── registration/
    │   └── login.html
    └── tasks/
        ├── task_list.html
        ├── task_detail.html
        ├── task_form.html
        └── task_confirm_delete.html
```

## Technologies Used

- Django 4.2+
- Bootstrap 5
- Font Awesome 6
- SQLite (default database)
- HTML/CSS/JavaScript

## Development

To contribute to the project:

1. Fork the repository
2. Create a branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
