from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment,Resource, Internship, Fellowship, Program, Gallery
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def articles(request):
    keyword = request.GET.get("keyword")
    recent_articles = Article.objects.filter(published=True).order_by('-created_date')[:5]
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles , "recent_articles":recent_articles})

def index(request):

    return render(request,"index.html")


def post_opportunity(request):
    if request.method == "POST":
        message_name  = request.POST['message-name']
        message_email = request.POST['message']
        message = request.POST['message']

        send_mail(
        message_name,
        message,
        message_email,
        ['jmwai@conncoll.edu', 'mwaijohn244@gmail.com'],

        )

        return render(request, 'post_opportunity.html', {'message_name':message_name})
    else:
        return render(request, "post_opportunity.html", {})
def resources(request):
    resources = Resource.objects.all()
    context = {
        "resources":resources
    }
    return render(request,"resources.html",context)


def internships(request):
    internships = Internship.objects.all()
    return render(request, 'internships.html', {'internships':internships})

def fellowships(request):
    fellowships = Fellowship.objects.all()
    return render(request, 'fellowships.html', {'fellowships':fellowships})

def programs(request):
    programs = Program.objects.all()
    return render(request, 'programs.html', {'programs':programs})

def gallerys(request):
    gallerys = Gallery.objects.all()
    return render(request, 'gallerys.html', {'gallerys':gallerys})

def about(request):
    return render(request,"about.html")

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)
@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.author = request.user
        article.save()

        messages.success(request,"Article Created Successfully")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})
def detail(request,slug):
    #article = Article.objects.filter(id = id).first()
    recent_article = get_object_or_404(Article, slug=slug)
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments, "recent_article":recent_article})
@login_required(login_url = "user:login")
def updateArticle(request, slug):

    article = get_object_or_404(Article, slug=slug)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request,"The article has been updated successfully")
        return redirect("article:dashboard")


    return render(request,"update.html",{"form":form})
@login_required(login_url = "user:login")
def deleteArticle(request,slug):
    article = get_object_or_404(Article,slug=slug)

    article.delete()

    messages.success(request,"Article Successfully Deleted")

    return redirect("article:dashboard")
def addComment(request,slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"slug":slug}))
