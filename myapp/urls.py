from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('departments/',views.departments,name='departments'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('new_password/',views.new_password,name='new_password'),
    path('change_password/',views.change_password,name='change_password'),
    path('profile/',views.profile,name='profile'),
    path('pcos/',views.pcos,name='pcos'),
    path('pcod/',views.pcod,name='pcod'),
    path('menopause/',views.menopause,name='menopause'),
    path('menstrual_hygiene/',views.menstrual_hygiene,name='menstrual_hygiene'),
    path('doc1/',views.doc1,name="doc1"),
    path('doc2/',views.doc2,name="doc2"),
    path('doc3/',views.doc3,name="doc3"),
    path('faq/',views.faq,name="faq"),
    path('product/',views.product,name="product"),
    path('ajax/validate_email/',views.validate_signup,name='validate_email'),
    
]
