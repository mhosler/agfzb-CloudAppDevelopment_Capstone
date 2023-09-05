from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for about view
    path('about/', views.about, name='about'),

    # path for contact us view
    path('contact/', views.contact, name='contact'),

    # path for registration
    # Uncomment below when you've defined registration_request view
    # path('register/', views.registration_request, name='register'),

    # path for login
    # Uncomment below when you've defined login_request view
    # path('login/', views.login_request, name='login'),

    # path for logout
    # Uncomment below when you've defined logout_request view
    # path('logout/', views.logout_request, name='logout'),

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view
    # Uncomment below when you've defined get_dealer_details view
    # path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_reviews'),

    # path for add a review view
    # Uncomment below when you've defined add_review view
    # path('dealer/<int:dealer_id>/add_review/', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
