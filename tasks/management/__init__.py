from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Créer des données de test pour l\'application To-Do'

    def handle(self, *args, **options):
        # Créer des utilisateurs de test
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
                self.stdout.write(f"Utilisateur {user.username} créé")

        # Créer des tâches de test
        alice = User.objects.get(username='alice')
        bob = User.objects.get(username='bob')

        tasks_data = [
            {
                'user': alice,
                'titre': 'Finir le rapport mensuel',
                'description': 'Compléter et envoyer le rapport mensuel à l\'équipe de direction.',
                'priorite': 'haute',
                'statut': 'en_cours',
                'date_echeance': date.today() + timedelta(days=2)
            },
            {
                'user': alice,
                'titre': 'Préparer la présentation client',
                'description': 'Créer une présentation PowerPoint pour le meeting client de vendredi.',
                'priorite': 'normale',
                'statut': 'a_faire',
                'date_echeance': date.today() + timedelta(days=5)
            },
            {
                'user': alice,
                'titre': 'Réviser le code du projet',
                'description': 'Faire une revue de code approfondie avant la mise en production.',
                'priorite': 'haute',
                'statut': 'a_faire',
                'date_echeance': date.today() + timedelta(days=1)
            },
            {
                'user': alice,
                'titre': 'Formation Django',
                'description': 'Suivre le cours en ligne sur Django et les bonnes pratiques.',
                'priorite': 'basse',
                'statut': 'termine',
                'date_echeance': None
            },
            {
                'user': bob,
                'titre': 'Mettre à jour la documentation',
                'description': 'Réviser et mettre à jour toute la documentation technique du projet.',
                'priorite': 'normale',
                'statut': 'en_cours',
                'date_echeance': date.today() + timedelta(days=7)
            },
            {
                'user': bob,
                'titre': 'Tests unitaires',
                'description': 'Écrire les tests unitaires pour les nouvelles fonctionnalités.',
                'priorite': 'haute',
                'statut': 'a_faire',
                'date_echeance': date.today() + timedelta(days=3)
            },
            {
                'user': bob,
                'titre': 'Optimiser les performances',
                'description': 'Analyser et optimiser les requêtes de base de données.',
                'priorite': 'normale',
                'statut': 'termine',
                'date_echeance': None
            }
        ]

        for task_data in tasks_data:
            task, created = Task.objects.get_or_create(
                titre=task_data['titre'],
                user=task_data['user'],
                defaults=task_data
            )
            if created:
                self.stdout.write(f"Tâche '{task.titre}' créée pour {task.user.username}")

        self.stdout.write(
            self.style.SUCCESS('Données de test créées avec succès!')
        )
