from django.urls import path
from . import views
urlpatterns=[
    path('',views.dice,name='dice'),
    path('possible_combination',views.possible_combination,name='possible_combination'),
    path('possible_distribution',views.possible_distribution,name='possible_distribution'),
    path('possible_probability',views.possible_probability,name='possible_probability'),
    path('doom_dice_challenge',views.doom_dice_challenge,name='doom_dice_challenge')
]