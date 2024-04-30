from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
   # path('', views.index, name='start'),
  #  path('bugs/', views.bug_list, name='bugs'),
  #  path('features/', views.feature_list, name='features'),
  #  path('bugs/<int:bug_id>/', views.bug_detail, name='bugs_id'),
  #  path('features/<int:feature_id>/', views.feature_id_detail, name='features_id'),

    path('', views.IndexView.as_view(), name='start'),
    path('bugs/', views.bug_list, name='bugs'),
    path('features/', views.feature_list, name='features'),
    path('bugs/<int:bug_id>/', views.BugReportView.as_view(), name='bugs_id'),
    path('features/<int:features_id>/', views.FeatureReportView.as_view(), name='features_id'),
]