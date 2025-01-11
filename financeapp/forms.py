from django import forms
from .models import Transaction,Category,Income,SavingsGoal

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date','amount', 'category', 'description','item']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = [ 'date','salary', ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Date picker widget
        }

class SavingsGoalForm(forms.ModelForm):
    class Meta:
        model = SavingsGoal
        fields = ['goal_name', 'target_amount', 'target_date']
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'}),  # Date picker widget
        }