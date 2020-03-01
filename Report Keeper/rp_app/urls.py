from django.urls import path
from . import views

app_name = 'rp_app'

urlpatterns = [
    path('', views.TableListView.as_view(), name='table-list'),
    # path('home', views.HomeView.as_view(), name='home'),
    path('new-record/', views.NewRecordView.as_view(), name='new-record'),
    path('single-record/<int:pk>/', views.SingleRecordView.as_view(), name='single-record'),
    path('single-record/<int:pk>/edit/', views.UpdateRecord.as_view(), name='single-record-edit'),
    path('single-record/<int:pk>/delete/', views.RecordDelete.as_view(), name='single-record-delete'),
    path('search/', views.searchposts, name='search'),    
]