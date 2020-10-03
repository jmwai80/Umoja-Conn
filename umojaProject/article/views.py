from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm, InternshipForm, ImageForm, FellowshipForm, ProgramForm, ProfileForm
from .models import Article,Comment,Resource, Internship, Fellowship, Program, Gallery, Profile, FeaturedStudent
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

def recent_articles(request):
    recent_articles = Article.objects.filter(published=True).order_by('-created_date')[:8]
    return render(request,"index.html",{"recent_articles":recent_articles})

def about(request):
    profiles = Profile.objects.all()
    return render(request, "about.html", {'profiles': profiles})

def index(request):
    featuredStudents = FeaturedStudent.objects.filter(published=True).order_by('-created_date')[:5]
    return render(request,"index.html", {"featuredStudents":featuredStudents})


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
    resources = Resource.objects.filter(admin_approved=True)
    context = {
        "resources":resources
    }
    return render(request,"resources.html",context)


def internships(request):
    internships = Internship.objects.filter(admin_approved=True)
    return render(request, 'internships.html', {'internships':internships})

def fellowships(request):
    fellowships = Fellowship.objects.filter(admin_approved=True)
    return render(request, 'fellowships.html', {'fellowships':fellowships})

def programs(request):
    programs = Program.objects.filter(admin_approved=True)
    return render(request, 'programs.html', {'programs':programs})

def gallerys(request):
    gallerys = Gallery.objects.filter(admin_approved=True)
    return render(request, 'gallerys.html', {'gallerys':gallerys})

# def about(request):
#     return render(request,"about.html")

def addInternship(request):
    form = InternshipForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        internships = form.save(commit=False)
        internships.save()

        messages.success(request,"Internship Created Successfully")
        return redirect("article:internships")
    return render(request,"addInternship.html",{"form":form})

def addResource(request):
    form = InternshipForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        internships = form.save(commit=False)
        internships.save()

        messages.success(request,"Resource Created Successfully")
        return redirect("article:internships")
    return render(request,"addInternship.html",{"form":form})

def addProgram(request):
    form = ProgramForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        programs = form.save(commit=False)
        programs.save()

        messages.success(request,"Program Created Successfully")
        return redirect("article:programs")
    return render(request,"addProgram.html",{"form":form})

def addFellowship(request):
    form = FellowshipForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        fellowships = form.save(commit=False)
        fellowships.save()

        messages.success(request,"Fellowship Created Successfully")
        return redirect("article:fellowships")
    return render(request,"addFellowship.html",{"form":form})

def addImage(request):
    form = ImageForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        gallerys = form.save(commit=False)
        gallerys.save()

        messages.success(request,"Image Added Successfully")
        return redirect("article:gallerys")
    return render(request,"addImage.html",{"form":form})

def addProfile(request):
    form = ProfileForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        about = form.save(commit=False)
        about.save()

        messages.success(request,"Profile Added Successfully")
        return redirect("about")
    return render(request,"addProfile.html",{"form":form})
# def addAchievement(request):
#     form = ArticleForm(request.POST or None,request.FILES or None)
#
#     if form.is_valid():
#         article = form.save(commit=False)
#         article.save()
#
#         messages.success(request,"Article Created Successfully")
#         return redirect("article:articles")
#     return render(request,"addAchievement.html",{"form":form})

def detail(request,slug):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article, "comments":comments })

def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.save()

        messages.success(request,"Article Created Successfully")
        return redirect("article:articles")
    return render(request,"addarticle.html",{"form":form})


def addComment(request,slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"slug":slug}))
