
from django.urls import path
from . import views

app_name = 'indusapp'

urlpatterns =[
    path('',views.create_account,name="create_account"),
    path('view-page/', views.view_page, name='view_page'),
]