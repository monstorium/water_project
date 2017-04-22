#watersourcereport/urls.py

from django.conf.urls import url
from watersourcereport.views import WaterSourceReportPage

app_name = 'watersourcereport'

urlpatterns = [
    url(r'^watersourcereport/', WaterSourceReportPage.as_view()),
]
