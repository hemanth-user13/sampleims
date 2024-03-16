from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_dashboard, name='main_dashboard'),
    path('student/login/', views.Student_Login, name='Student_Login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/register/', views.student_register, name='student_register'),
    path('faculty/login/', views.faculty_login, name='faculty_login'),
    path('hod/login/', views.hod_login, name='hod_login'),
    # path('upload/', views.upload_files, name='upload_files_page_url'),
    path('hod/dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('generate_mapping_excel/', views.generate_mapping_excel, name='generate_mapping_excel'),
    path('download_mapped_excel/', views.download_mapped_excel, name='download_mapped_excel'),
    path('mapping_list/', views.mapping_list, name='mapping_list'),
    path('student_files/', views.student_files, name='student_files'),
    path('faculty_dashboard/', views.faculty_dashboard, name='faculty_dashboard'),

    # Add the URL pattern for downloading files by passing the file_id as a parameter
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('faculty_files/', views.faculty_files_view, name='faculty_files_view'),
    path('faculty/activities/<str:roll_number>/', views.faculty_activities, name='faculty_activities'),
    path('hod/activities/<str:roll_number>/', views.hod_activities, name='hod_activities'),
    path('faculty/files/<str:roll_number>/', views.faculty_files_view, name='faculty_files_view_with_roll_number'),
    path('update_marks/<int:file_id>/', views.update_marks, name='update_marks'),
    path('student/marks/', views.student_marks_view, name='student_marks_view'),
    path('download_student_marks/', views.download_student_marks_excel, name='download_student_marks'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('hodmarks/',views.hod_marks_view,name='hod_marks_view'),
    path('student_private_files/<str:email>/', views.student_private_files, name='student_private_files'),

    #path('view_all_files/',views.view_all_files, name='view_all_files'),
    # path('view_file/<int:file_id>/',views.view_file, name='view_file'),
    path('download_file/<int:file_id>/',views.download_file, name='download_file'),
    path('admin_dashboard/',views.upload_file, name='upload_file'),
    path('internship_opportunities/',views.internship_opportunities, name='internship_opportunities'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('resume_builder/', views.resume_builder, name='resume_builder'),
    path('voicechat/',views.speech_recognition_and_execution, name='voice_assistant'),
    path('resource_center/',views.resource_center, name='resource_center'),
    path('hod_circular/',views.circular,name='circular'),
    path('student-circulars/', views.display_circulars, name='display_circulars'),
    path('student_performance/',views.student_performance, name='student_performance'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)