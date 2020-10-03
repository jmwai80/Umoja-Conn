from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import
from .models import GalleryImage, Gallery
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.db.models import Count



def gallerys(request):
    gallerys = Gallery.objects.filter(admin_approved=True)
    return render(request, 'gallerys.html', {'gallerys':gallerys}))

def addFolder(request):
    form = ImageForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        gallerys = form.save(commit=False)
        gallerys.save()

        messages.success(request,"Image Added Successfully")
        return redirect("article:gallerys")
    return render(request,"addImage.html",{"form":form})

def detail(request,slug):
    #article = Article.objects.filter(id = id).first()
    image = get_object_or_404(Gallery)
    images = image.images.all()
    return render(request,"images.html",{"image":image, "images":images })

def addImages(request,slug):
    image = get_object_or_404(Gallery)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"slug":slug}))
