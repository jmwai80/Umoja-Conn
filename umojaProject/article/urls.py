from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler500
from . import views
app_name = "article"

urlpatterns = [
    # path('dashboard/',views.dashboard,name = "dashboard"),
    path('resources/',views.resources,name = "resources"),
    path('internships/',views.internships,name = "internships"),
    path('programs/',views.programs,name = "programs"),
    # path('recent_articles/',views.recent_articles,name = "recent_articles"),
    # path('addarticle/',views.addArticle,name = "addarticle"),
    path('fellowships/',views.fellowships,name = "fellowships"),
    path('gallerys/',views.gallerys,name = "gallerys"),
    path('post_opportunity/', views.post_opportunity, name = "post_opportunity"),
    path('addInternship/',views.addInternship,name = "addInternship"),
    path('article/<slug:slug>/',views.detail,name = "detail"),
    path('addFellowship/',views.addFellowship,name = "addFellowship"),
    path('addImage/',views.addImage,name = "addImage"),
    path('addProgram/',views.addProgram,name = "addProgram"),
    path('addResource/',views.addResource,name = "addResource"),
    path('addArticle/',views.addArticle,name = "addArticle"),
    path('addProfile/',views.addProfile,name = "addProfile"),



    # path('update/<slug:slug>',views.updateArticle,name = "update"),
    # path('delete/<slug:slug>',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"),
    path('comment/<slug:slug>',views.addComment,name = "comment"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
