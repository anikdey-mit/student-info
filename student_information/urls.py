from django.urls import path
from . import views

app_name = "student_information"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('student_form/', views.form, name='form'),
    path('student_details/<int:student_id>/', views.details, name='details'),
    path('student_update/<int:student_id>/', views.update, name='update'),
    path('student_delete/<int:student_id>/', views.delete, name='delete'),
]

