from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='start'),
    #  path('bugs/', views.bug_list, name='bugs'),
    #  path('features/', views.feature_list, name='features'),
    #  path('bugs/<int:bug_id>/', views.bug_detail, name='bugs_id'),
    #  path('features/<int:feature_id>/', views.feature_id_detail, name='features_id'),

    # path('', views.IndexView.as_view(), name='start'),
    # path('bugs/', views.BugListView.as_view(), name='bugs'),
    # path('features/', views.FeatureListView.as_view(), name='features'),
    path('bugs/', views.bug_list, name='bugs'),
    path('features/', views.feature_list, name='features'),

    path('bugs/new/', views.BugCreateView.as_view(), name='add_bug'),
    path('features/new/', views.FeatureCreateView.as_view(), name='add_feature'),
    # path('bugs/new/', views.add_bug, name='add_bug'),
    # path('features/new/', views.add_feature, name='add_feature'),

    path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug'),
    path('features/<int:features_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),
    # path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    # path('features/<int:features_id>/delete/', views.delete_feature, name='delete_feature'),

    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bugs_id'),
    path('features/<int:features_id>/', views.FeatureDetailView.as_view(), name='features_id'),
    # path('bugs/<int:bug_id>/', views.BugReportView.as_view(), name='bugs_id'),
    # path('features/<int:features_id>/', views.FeatureReportView.as_view(), name='features_id'),

    path('bugs/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='update_bug'),
    path('features/<int:features_id>/update/', views.FeagureUpdateView.as_view(), name='update_features'),
    # path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    # path('features/<int:features_id>/update/', views.update_feature, name='update_features'),
]