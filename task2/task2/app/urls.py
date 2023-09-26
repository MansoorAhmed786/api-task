from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView, TaskListCreateView, TaskDetailView, TaskAssignView, DocumentListCreateView, DocumentDetailView, CommentListCreateView, CommentDetailView,  PostCreateView, user_login, user_logout, project_deadlines

urlpatterns = [
    path('register/', PostCreateView.as_view(), name='register-user'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/assign/', TaskAssignView.as_view(), name='task-assign'),
    path('documents/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'), 
    path('project-deadlines/', project_deadlines, name='project-deadlines'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
]
