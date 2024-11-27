from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edu-konnect/', views.edu_konnect, name='edu_konnect'),
    path('mtaa-legit/', views.mtaa_legit, name='mtaa_legit'),
    path('blog/', views.blog_list, name='blog_list'),
]

urlpatterns = [
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('about-us/', views.about_us, name='about_us'),
]
