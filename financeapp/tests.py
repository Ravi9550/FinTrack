from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Transaction,SavingsGoal,Income

class TransactionTests(TestCase):

    def setUp(self):
        """Create sample data for tests"""
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Food', user=self.user)
        self.transaction = Transaction.objects.create(
            user=self.user,
            amount=100.00,
            date='2025-01-11',
            category=self.category,
            description='Grocery shopping',
            item='Groceries'
        )

    def test_transaction_creation(self):
        """Test that transaction is created correctly"""
        self.assertEqual(self.transaction.amount, 100.00)
        self.assertEqual(self.transaction.category.name, 'Food')
        self.assertEqual(self.transaction.description, 'Grocery shopping')

    def test_transaction_str_method(self):
        """Test the string representation of a transaction"""
        self.assertEqual(str(self.transaction), "Food - 100.00 on 2025-01-11")


class IncomeTests(TestCase):

    def setUp(self):
        """Create sample data for tests"""
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.income = Income.objects.create(
            user=self.user,
            salary=5000.00,
            date='2025-01-01'
        )

    def test_income_creation(self):
        """Test that income is created correctly"""
        self.assertEqual(self.income.salary, 5000.00)

    def test_income_str_method(self):
        """Test the string representation of income"""
        self.assertEqual(str(self.income), "5000.00 on 2025-01-01")

class SavingsGoalTests(TestCase):

    def setUp(self):
        """Create sample data for tests"""
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.savings_goal = SavingsGoal.objects.create(
            user=self.user,
            goal_name='Vacation',
            target_amount=2000.00,
            target_date='2025-12-31'
        )

    def test_savings_goal_creation(self):
        """Test that savings goal is created correctly"""
        self.assertEqual(self.savings_goal.goal_name, 'Vacation')
        self.assertEqual(self.savings_goal.target_amount, 2000.00)

    def test_savings_goal_str_method(self):
        """Test the string representation of savings goal"""
        self.assertEqual(str(self.savings_goal), 'Vacation - 2000.00')
