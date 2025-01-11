from .models import Transaction,Income,Category,SavingsGoal
from datetime import datetime
from django.db.models import Sum

def generate_report_data_month(user, year=None, month=None):
    today = datetime.today()
    year = year or today.year
    month = month or today.month

    transactions = Transaction.objects.filter(user=user, date__year=year, date__month=month)
    income = Income.objects.filter(user=user, date__year=year, date__month=month)

    total_income_month = income.aggregate(Sum('salary'))['salary__sum'] or 0
    total_expenses_month = transactions.aggregate(Sum('amount'))['amount__sum'] or 0
    total_savings_month = total_income_month - total_expenses_month

    category_data_month = (
        transactions.values('category__name')
        .annotate(total_amount=Sum('amount'))
        .order_by('-total_amount')
    )

    categories_month = [item['category__name'] for item in category_data_month]
    amounts_month = [item['total_amount'] for item in category_data_month]

    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]

    no_data_month = not categories_month and not amounts_month


    return {
        'total_income_month': total_income_month,
        'total_expenses_month': total_expenses_month,
        'total_savings_month': total_savings_month,
        'categories_month': categories_month,
        'amounts_month': amounts_month,
        'months': months,  
        'selected_month': month,
        'no_data_month': no_data_month,  
    }






def generate_report_data_year(request):
    current_year = datetime.now().year
    selected_year = int(request.GET.get('year', current_year))  
    years = [year for year in range(2020, current_year + 1)]  

    expenses_year = Transaction.objects.filter(user=request.user,date__year=selected_year)
    incomes_year = Income.objects.filter(user=request.user,date__year=selected_year)

    total_expenses_year = sum(expense.amount for expense in expenses_year)
    total_income_year = sum(income.salary for income in incomes_year)
    total_savings_year = total_income_year - total_expenses_year

    category_data_year = (
        expenses_year.values('category__name')
        .annotate(total_amount=Sum('amount'))
        .order_by('-total_amount')
    )

    categories_year = [item['category__name'] for item in category_data_year]
    amounts_year = [item['total_amount'] for item in category_data_year]

    no_data_year = not categories_year and not amounts_year

    return {
         'selected_year': selected_year,
        'years': years,
        'categories_year': categories_year,
        'amounts_year': amounts_year,
        'total_expenses_year': total_expenses_year,
        'total_income_year': total_income_year,
        'total_savings_year': total_savings_year,
        'no_data_year': no_data_year,

    }
   

    



