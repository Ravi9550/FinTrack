from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Transaction,Category,SavingsGoal,Income
from .forms import TransactionForm,CategoryForm,IncomeForm,SavingsGoalForm
from django.db.models import Sum
from django.db.models.functions import Lower  
from datetime import datetime
from .report import generate_report_data_month,generate_report_data_year



def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')



@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user}) 

@login_required
def monthly_report(request):
    user = request.user
    selected_month = int(request.GET.get('month', datetime.today().month))  
    report_data = generate_report_data_month(user, month=selected_month)
    return render(request, 'monthly_report.html', report_data)

@login_required
def yearly_report(request):
    user = request.user  
    current_year = datetime.now().year
    selected_year = int(request.GET.get('year', current_year))

    report_data = generate_report_data_year(request)
    return render(request, 'yearly_report.html', report_data)

@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    expenses = Transaction.objects.filter(user=request.user).order_by('-date')
    summary = {}
    for expense in expenses:
        summary[expense.category] = summary.get(expense.category.name, 0) + float(expense.amount)

    selected_month = int(request.GET.get('month', datetime.today().month))
    selected_year = datetime.today().year

    current_year = datetime.now().year
    selected_year = int(request.GET.get('year', current_year))

    report_data_month = generate_report_data_month(request.user, year=selected_year, month=selected_month)
    report_data_year = generate_report_data_year(request)


    context = {
        'user': request.user,
        'expenses': expenses,
        'summary': summary,

        # For Monthly Reports
        'months': report_data_month['months'],
        'selected_month': selected_month,
        'total_income_month': report_data_month['total_income_month'],
        'total_expenses_month': report_data_month['total_expenses_month'],
        'total_savings_month': report_data_month['total_savings_month'],
        'categories_month': report_data_month['categories_month'],
        'amounts_month': report_data_month['amounts_month'],
        'no_data_month': report_data_month['no_data_month'],

        # For Yearly Reports
        'years': report_data_year['years'],
        'selected_year': selected_year,
        'total_income_year': report_data_year['total_income_year'],
        'total_expenses_year': report_data_year['total_expenses_year'],
        'total_savings_year': report_data_year['total_savings_year'],
        'categories_year': report_data_year['categories_year'],
        'amounts_year': report_data_year['amounts_year'],
        'no_data_year': report_data_year['no_data_year'],
       


        


    }

    return render(request, 'dashboard.html', context)
    





@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST) 
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  
            transaction.save()
            messages.success(request, 'Transaction added successfully!')
            return redirect('view_transaction')  
    else:
        form = TransactionForm()  

    return render(request, 'add_transaction.html', {'form': form})


@login_required
def view_transactions(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'view_transaction.html', {'transactions': transactions})


@login_required
def update_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transaction updated successfully!')
            return redirect('view_transaction')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'update_transaction.html', {'form': form})


@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    transaction.delete()
    messages.success(request, 'Transaction deleted successfully!')
    return redirect('view_transaction')

@login_required
def transaction_summary(request):
    summary_type = request.GET.get('type', 'category')  

    # Filter transactions for the current user
    transactions = Transaction.objects.filter(user=request.user)
    total_expense_all = transactions.aggregate(total_expense=Sum('amount'))['total_expense'] or 0

    if summary_type == 'category':
        summary_data = transactions.annotate(category_lower=Lower('category__name')) \
                                .values('category_lower') \
                                .annotate(total_expense=Sum('amount')) \
                                .order_by('category_lower')

    elif summary_type == 'item':
        summary_data = transactions.annotate(item_lower=Lower('item')) \
                                .values('item_lower') \
                                .annotate(total_expense=Sum('amount')) \
                                .order_by('item_lower')

    elif summary_type == 'date':
        summary_data = transactions.values('date') \
                                .annotate(total_expense=Sum('amount')) \
                                .order_by('date')

    return render(request, 'transaction_summary.html', {
        'summary_data': summary_data,
        'summary_type': summary_type,
        'total_expense_all': total_expense_all,
    })

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user  # Ensure the category is added to the current user
            category.save()
            return redirect('category_list')  # Redirect to category list after adding
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)  # Fetch categories for the logged-in user
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def edit_category(request, category_id):
    category = Category.objects.get(id=category_id, user=request.user)  # Fetch the category for the logged-in user
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form})


from django.shortcuts import get_object_or_404

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)
    category.delete()
    return redirect('category_list')


@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user  
            income.save()
            return redirect('income_list')  
    else:
        form = IncomeForm()

    return render(request, 'add_income.html', {'form': form})

@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)  
    return render(request, 'income_list.html', {'incomes': incomes})



@login_required
def update_income(request, income_id):
    income = get_object_or_404(Income, id=income_id, user=request.user)  
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save() 
            return redirect('income_list')  
    else:
        form = IncomeForm(instance=income)

    return render(request, 'update_income.html', {'form': form, 'income': income})


@login_required
def delete_income(request, income_id):
    income = get_object_or_404(Income, id=income_id, user=request.user)  
    income.delete()  
    return redirect('income_list')  

@login_required
def add_saving_goal(request):
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST)
        if form.is_valid():
            savings_goal = form.save(commit=False)
            savings_goal.user = request.user  
            savings_goal.save()
            return redirect('saving_goal_list')  
    else:
        form = SavingsGoalForm()

    return render(request, 'add_saving_goal.html', {'form': form})

@login_required
def saving_goal_list(request):
    # Fetch goals for the current user
    goals = SavingsGoal.objects.filter(user=request.user)
    
    for goal in goals:
        
        target_date_reached = datetime.today().date() >= goal.target_date
        
        total_income = Income.objects.filter(user=request.user, date__lte=datetime.today()).aggregate(Sum('salary'))['salary__sum'] or 0
        total_spent = Transaction.objects.filter(user=request.user, date__lte=goal.target_date).aggregate(Sum('amount'))['amount__sum'] or 0
        
        saved_amount_till_now = total_income - total_spent

        today = datetime.today().date()
        total_time = (goal.target_date - goal.created_at.date()).days
        elapsed_time = (today - goal.created_at.date()).days

        goal.progress_time = (elapsed_time / total_time) * 100 if total_time > 0 else 0
        goal.progress_time = min(100, goal.progress_time)  # Cap at 100%

        if target_date_reached:
            if saved_amount_till_now >= goal.target_amount:
                goal.progress_money = 100
                goal.remaining = 0
                goal.status = 'Goal Achieved'
            else:
                goal.progress_money = (saved_amount_till_now / goal.target_amount) * 100 if goal.target_amount > 0 else 0
                goal.remaining = goal.target_amount - saved_amount_till_now
                goal.status = 'Goal Missed'
        else:
            if saved_amount_till_now >= goal.target_amount:
                goal.progress_money = 100
                goal.remaining = 0
                goal.status = 'On Track'
            else:
                goal.progress_money = (saved_amount_till_now / goal.target_amount) * 100 if goal.target_amount > 0 else 0
                goal.remaining = max(0, goal.target_amount - saved_amount_till_now)
                goal.status = 'Off Track' if goal.progress_money < goal.progress_time else 'On Track'

        goal.progress_money = min(100, goal.progress_money)

    return render(request, 'saving_goal_list.html', {'goals': goals})



