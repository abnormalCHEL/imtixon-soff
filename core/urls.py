from django.contrib import admin
from django.urls import path
from app.views import BlogListView,BlogDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog-details/',BlogDetailView.as_view()),
    # path('categories/', CategoryListView.as_view()),
    path('blog-list/',BlogListView.as_view()),
    
    
]
