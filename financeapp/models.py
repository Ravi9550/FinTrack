from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    description = models.TextField()
    item = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        amount = f"{self.amount:.2f}"
        return f"{self.category} - {amount} on {self.date}"

class Income(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    salary = models.DecimalField(max_digits=10, decimal_places=2)  
    date = models.DateField() 
   
    def __str__(self):
        salary = f"{self.salary:.2f}"
        return f"{salary} on {self.date}"

    
class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    goal_name = models.CharField(max_length=100)  
    target_amount = models.DecimalField(max_digits=10, decimal_places=2) 
    target_date = models.DateField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        target_amount = f"{self.target_amount:.2f}"
        return f"{self.goal_name} - {target_amount}"
