from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('about', views.about_page_view, name='about'),
    path('contactsAdd', views.contactsAdd_page_view, name='contactsAdd'),
    path('contactsView', views.contactsView_page_view, name='contactsView'),
    path('contactsEdit/<int:user_id>', views.contactsEdit_page_view, name='contactsEdit'),
    path('contactsDelete/<int:user_id>', views.contactsDelete_page_view, name='contactsDelete'),
    path('quizAdd', views.quizAdd_page_view, name='quizAdd'),
    path('quizView', views.quizView_page_view, name='quizView'),
    path('answerCheck/<int:answer_id>', views.answerCheck_page_view, name='answerCheck'),
    path('quizAnswer/<int:answer_id>', views.quizAnswer_page_view, name='quizAnswer'),
    path('commentsView', views.commentsView_page_view, name='commentsView'),
    path('commentsAdd', views.commentsAdd_page_view, name='commentsAdd'),
    path('planets/earth', views.earth_page_view, name='earth'),
    path('planets/jupiter', views.jupiter_page_view, name='jupiter'),
    path('planets/mars', views.mars_page_view, name='mars'),
    path('planets/mercury', views.mercury_page_view, name='mercury'),
    path('planets/neptune', views.neptune_page_view, name='neptune'),
    path('planets/saturn', views.saturn_page_view, name='saturn'),
    path('planets/sun', views.sun_page_view, name='sun'),
    path('planets/uranus', views.uranus_page_view, name='uranus'),
    path('planets/venus', views.venus_page_view, name='venus'),
]