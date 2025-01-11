from django.urls import path
from . import views

urlpatterns = [
    
    #  Authentication Urls
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),


    # Transactions Urls
    path('add/', views.add_transaction, name='add_transaction'),
    path('view/', views.view_transactions, name='view_transaction'),
    path('update/<int:transaction_id>/', views.update_transaction, name='update_transaction'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('category-summary/', views.transaction_summary, name='transaction_summary'),


    # Catgory Urls
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),

  
    # Income Urls
    path('add-income/', views.add_income, name='add_income'),
    path('income-list/', views.income_list, name='income_list'),
    path('income/<int:income_id>/update/', views.update_income, name='update_income'),
    path('income/<int:income_id>/delete/', views.delete_income, name='delete_income'),

     # Savings Goal Urls
    path('add_savings_goal/', views.add_saving_goal, name='add_saving_goal'),
    path('savings_goal_list/', views.saving_goal_list, name='saving_goal_list'),
     
    # Reports Urls
    path('monthly_report/', views.monthly_report, name='monthly_report'),
    path('yearly-report/', views.yearly_report, name='yearly_report'),


  


   
    
]
