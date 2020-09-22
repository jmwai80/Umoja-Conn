from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler500
from . import views
app_name = "article"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('resources/',views.resources,name = "resources"),
    path('internships/',views.internships,name = "internships"),
    path('programs/',views.programs,name = "programs"),
    path('fellowships/',views.fellowships,name = "fellowships"),
    path('gallerys/',views.gallerys,name = "gallerys"),
    path('post_opportunity/', views.post_opportunity, name = "post_opportunity"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('article/<slug:slug>/',views.detail,name = "detail"),
    path('update/<slug:slug>',views.updateArticle,name = "update"),
    path('delete/<slug:slug>',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"),
    path('comment/<slug:slug>',views.addComment,name = "comment"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
