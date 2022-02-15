from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        f'api/v1/puppies/<int:pk>/',
        views.get_update_delete_puppy,
        name='get_delete_update_puppy'
    ),
    url(
        f'api/v1/puppies/',
        views.get_post_puppies,
        name='get_post_puppies'
    )
]