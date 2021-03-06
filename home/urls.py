from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),

    url(r'^student/board_result/$', views.student_board_result, name='student_board_result'),

    url(r'^student/$', views.student, name='student'),
    url(r'^student/profile/$', views.student_profile, name='student_profile'),
    url(r'^student/study-material/$', views.student_material, name='student_material'),
    url(r'^student/scholarship/$', views.student_scholarship, name='student_scholarship'),
    url(r'^student/scholarship/apply/$', views.student_scholarship_apply, name='student_scholarship_apply'),
    url(r'^student/result/$', views.student_result, name='student_result'),

    url(r'^admission/$', views.admission, name='admission'),
    url(r'^admission/(?P<type>\w+)/$', views.admission, name='admission'),

    url(r'^faculty/$', views.faculty, name='faculty'),
    url(r'^moderator/$', views.moderator, name='moderator'),
    url(r'^disclaimer/$', views.disclaimer, name='disclaimer'),

    url(r'^send_email/$', views.send_email, name='send_email'),
]
