from credentials.apps.records.rest_api.v1 import views
from django.urls import re_path

urlpatterns = [re_path(r"^program_records/$", views.ProgramRecords.as_view(), name="program_records")]
