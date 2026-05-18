from django.urls import path
from .import views
# from listings import views as listings_views # add

app_name = 'pages'

urlpatterns = [
    path('',views.index, name='index'),
    path('about', views.about, name='about'),

    # path('listing.html', listings_views.listing, {'listing_id': 1}, name='fix_404_loop'),# add

]