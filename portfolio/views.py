from django.shortcuts import redirect, render, get_object_or_404
from .models import Home, About, Portfolio, Category, Profile, Blog, Contact
from django.contrib import messages



# Create your views here.
def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    # Blog
    blogs = Blog.objects.all().order_by('-id')
    total_obj = Blog.objects.count()
    

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios, 
        'blogs': blogs,
        'total_obj': total_obj
    }

    return render(request, 'index.html', context)

def detail_blog_view(request, slug):

    context = {}

    blog_post = get_object_or_404(Blog, slug=slug)
    context['blog_post'] = blog_post
    return render(request, 'blog_detail.html', context)

def contact(request):
    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    # Blog
    blogs = Blog.objects.all().order_by('-id')
    total_obj = Blog.objects.count()
    

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios, 
        'blogs': blogs,
        'total_obj': total_obj
    }
    
    if request.method == "POST":
        contact = Contact(name= request.POST.get('name'), email= request.POST.get('email'), subject = request.POST.get('subject'), message = request.POST.get('message'))
        contact.save()

        messages.success(request, "Your message has been sent successfully")
        return redirect('/', context)
    
