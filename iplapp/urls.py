from django.urls import path
from iplapp.views import (
    landing_page1,
    landing_page2,
    stats_dashboard,
)

urlpatterns = [
    path('', landing_page1, name='landing_page1'),
    path('advanced/', landing_page2, name='landing_page2'),
    path('dashboard/', stats_dashboard, name='stats-dashboard'),
]