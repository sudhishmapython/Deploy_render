from . import views
from django.urls import path

urlpatterns = [
    path('demo',views.fun1,name='functn1'),
    path('abc',views.add_form,name='add'),
    path('p_read', views.read_form, name='read'),
    path('p_edit/<int:id>/', views.update_form, name='edit'),
    path('add',views.stud_add,name='s_add'),
    path('', views.emp_add, name='e_add'),
    path('emp_read',views.emp_read,name='e_read'),
    path('emp_edit/<int:id>/',views.emp_update,name='emp_edit'),
    path('qwe',views.demo_html,name='demo'),
    path('c_add',views.college_add,name='cadd'),

]
