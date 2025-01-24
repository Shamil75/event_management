from django.urls import path
from tasks.views import dashboard, create_event,update_event, delete_event, create_category, update_category, delete_category, create_participant, update_participant, delete_participant

urlpatterns = [
    path('dashboard/', dashboard , name='dashboard'),
    path('create_event/', create_event, name='create_event'),
    path('update_event/<int:id>/', update_event, name='update_event'),
    path('delete_event/<int:id>/', delete_event, name='delete_event'),

    path('create_category/', create_category, name='create_category'),
    path('update_category/<int:id>/', update_category, name='update_category'),
    path('delete_category/<int:id>/', delete_category, name='delete_category'),

    path('create_participant/', create_participant, name='create_participant'),
    path('update_participant/<int:id>/', update_participant, name='update_participant'),
    path('delete_participant/<int:id>/', delete_participant, name='delete_participant')
]
