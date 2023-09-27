from django.urls import path
from . import views

urlpatterns = [
    path('',views.run_migrations,name='run_migrations'),
    path('see_data/',views.view_data,name='view_data'),
]
