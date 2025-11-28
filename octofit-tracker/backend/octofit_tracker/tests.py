from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        user1 = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        user2 = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=user1, type='Running', duration=30)
        Activity.objects.create(user=user2, type='Swimming', duration=45)
        workout = Workout.objects.create(name='Hero Training', description='Intense workout for heroes')
        workout.suggested_for.add(user1, user2)
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=80)

    def test_user_email_unique(self):
        marvel = Team.objects.get(name='Marvel')
        with self.assertRaises(Exception):
            User.objects.create(name='Duplicate', email='ironman@marvel.com', team=marvel)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 2)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 2)

    def test_workout_suggestion(self):
        workout = Workout.objects.get(name='Hero Training')
        self.assertEqual(workout.suggested_for.count(), 2)
