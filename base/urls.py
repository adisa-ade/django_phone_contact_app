from django.urls import path
from .views import (HomeView,
    HomeDetailView,
    CreateContact,
    UpdateContact,
    DeleteContact,
    RegisterPage,
    CustomLoginView,
    CustomLogoutView)
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('contact-detail/<int:pk>', HomeDetailView.as_view(), name='contact-detail'),
    path('create-contact', CreateContact.as_view(), name='create-contact'),
    path('<int:pk>/update-contact/', UpdateContact.as_view(), name='update-contact'),
    path('<int:pk>/delete-contact/', DeleteContact.as_view(), name='delete-contact'),
    path('register/', RegisterPage.as_view(), name='register'),
]
