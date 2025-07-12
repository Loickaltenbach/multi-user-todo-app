from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Create test data for the To-Do application'

    def handle(self, *args, **options):
        # Create test users
        users_data = [
            {'username': 'alice', 'email': 'alice@example.com', 'password': 'testpass123'},
            {'username': 'bob', 'email': 'bob@example.com', 'password': 'testpass123'},
        ]

        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                email=user_data['email']
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(f"User {user.username} created")

        # Create test tasks
        alice = User.objects.get(username='alice')
        bob = User.objects.get(username='bob')

        tasks_data = [
            {
                'user': alice,
                'title': 'Complete monthly report',
                'description': 'Finish and send the monthly report to the management team.',
                'priority': 'high',
                'status': 'in_progress',
                'due_date': date.today() + timedelta(days=2)
            },
            {
                'user': alice,
                'title': 'Prepare client presentation',
                'description': 'Create a PowerPoint presentation for Friday\'s client meeting.',
                'priority': 'normal',
                'status': 'todo',
                'due_date': date.today() + timedelta(days=5)
            },
            {
                'user': alice,
                'title': 'Review project code',
                'description': 'Conduct thorough code review before production deployment.',
                'priority': 'high',
                'status': 'todo',
                'due_date': date.today() + timedelta(days=1)
            },
            {
                'user': alice,
                'title': 'Django training',
                'description': 'Complete online Django course and best practices.',
                'priority': 'low',
                'status': 'completed',
                'due_date': None
            },
            {
                'user': bob,
                'title': 'Update documentation',
                'description': 'Review and update all technical project documentation.',
                'priority': 'normal',
                'status': 'in_progress',
                'due_date': date.today() + timedelta(days=7)
            },
            {
                'user': bob,
                'title': 'Unit tests',
                'description': 'Write unit tests for new features.',
                'priority': 'high',
                'status': 'todo',
                'due_date': date.today() + timedelta(days=3)
            },
            {
                'user': bob,
                'title': 'Performance optimization',
                'description': 'Analyze and optimize database queries.',
                'priority': 'normal',
                'status': 'completed',
                'due_date': None
            }
        ]

        for task_data in tasks_data:
            task, created = Task.objects.get_or_create(
                title=task_data['title'],
                user=task_data['user'],
                defaults=task_data
            )
            if created:
                self.stdout.write(f"Task '{task.title}' created for {task.user.username}")

        self.stdout.write(
            self.style.SUCCESS('Test data created successfully!')
        )
