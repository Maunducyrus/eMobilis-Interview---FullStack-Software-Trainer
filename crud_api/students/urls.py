from django.urls import path
from .views import     student_list, student_detail, student_ui_list, add_student_ui, update_student_ui,  delete_student_ui

urlpatterns = [
    path('students/', student_list),
    path('students/<int:id>/', student_detail),

    # Interface routing
    path('ui/', student_ui_list, name='student_ui_list'),
    path('ui/add/', add_student_ui),
    path('ui/update/<int:id>/', update_student_ui),
    path('ui/delete/<int:id>/', delete_student_ui),
]
