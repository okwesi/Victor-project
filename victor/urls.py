from django.contrib import admin
from django.urls import path
from .views import create_person, person_list, person_list_csv, success_page, person_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', create_person),
    path('success', success_page, name='success_page'),  # Add the success page URL path
    path('list', person_list),
    path('csv/', person_list_csv, name='person_list_csv'),
    path('person/delete/<int:pk>/', person_delete, name='person_delete'),

]
