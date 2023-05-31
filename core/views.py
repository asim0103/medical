from audioop import reverse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView

from core.models import *
from core.models import News
from core.forms import *
# Create your views here.

def home(request):
    return render(request, 'index.html')


# def service(request):
#     return render(request, 'services.html')

def home2(request):
    return render(request, 'index-02.html')
   
def about(request):
    abouts = About.objects.all()
    context = {
        'abouts' : abouts
            }
    return render(request, 'about.html', context)


def services(request):
    
    services = Service.objects.all()[:1]
    servicecategory = ServiceCategory.objects.all()
    count = 1

    if "servicecategory" in request.GET.keys():
        services = Service.objects.filter(
            servicecategory_id__title=request.GET["servicecategory"]) 
        

        
    if request.method == 'POST':
        more = int(request.POST['more-services'])
        services = Service.objects.all()[:more+1]  
        count = len(services)
        



    context={
        'services' : services,
        'servicecategory': servicecategory,
        'count': count,
        
    }
        
    return render (request, 'services.html', context)


def service_details(request, slug):
    context = {
        'services': Service.objects.get(slug=slug)
    }
    return render(request, 'service-details.html', context)



# def doctor_details_2(request):
#     return render (request, 'doctor-details-2.html')


# def doctor_details(request):
#     return render (request, 'doctor-details.html')


# def blog_single_standart(request):
#     return render (request, 'blog_single_standart.html')




def blog_classic(request):
    
    blogs=Blog.objects.all()
    
    context={
        'blog' : blogs
    }
        
    return render (request, 'blog-classic.html', context)



def blog_single(request, id):
     
    blogs=Blog.objects.get(id=id)
    
    context={
        
        'blog' : blogs
    }
        
    return render (request, 'blog-single.html', context)


# class DoctorsListView(ListView):
#     model = News
#     template_name = 'doctors-grid.html'
#     context_object_name = 'doctors'
#     paginate_by = 2

def blog_grid(request):
    
    blogs = Blog.objects.all()[:3]

    count = 3

    if request.method == 'POST':
        more = int(request.POST['more-blog'])
        blogs = Blog.objects.all()[:more+3]  
        count = len(blogs)
    
    context={
        'blogs' : blogs,
        'count': count
    }
        
    return render (request, 'blog-grid.html', context)


def blog_list(request):
    return render (request, 'blog-list.html')


def blog_single_2(request):
    return render (request, 'blog-single.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form=ContactForm
    context = {
        'test' : form
    
        
    }
    return render(request, 'contact-us.html', context)


# class NewsListView(ListView):
#     model = News
#     template_name = 'news.html'
#     context_object_name = 'news'
#     paginate_by = 1
    
#     def get_queryset(self) :
#         return News.objects.filter(is_published=True).order_by('updated_at')
    
#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context ['title'] = 'News'
#         context ['count'] = News.objects.filter(is_published=True).count('updated_at')
#         query = self.request.GET.get('blog')
#         if query:
#             context['blog'] = Blog.objects.filter(title__icontains=query)
#         context['title'] = 'Blog'
#         return context
     
    

# general search for all models

class DoctorsDetailView(DetailView):
    model = Doctors
    template_name = 'doctor-details.html'
    context_object_name = 'detail_doctors'

class DoctorsListView(ListView):
    model = Doctors
    template_name = 'doctors-grid.html'
    context_object_name = 'doctors'
    paginate_by = 1

    def get_queryset(self):
        return Doctors.objects.all().order_by('-created_at')


    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        context['count'] = Doctors.objects.filter().count()

        # context['news'] = News.objects.all().order_by('-updated_at')
        context['title'] = 'Doctors'
        query = self.request.GET.get('doctors')
        if query:
            context['doctors'] = Doctors.objects.filter(title__icontains=query)
        context['title'] = 'Doctors'
        return context
      

      
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)



def search(request):
    print("request get: ", request.GET)
    query = request.GET.get('query')
    if query:
        doctors = Doctors.objects.filter(title__icontains=query)
        # course = Course.objects.filter(title__icontains=query)
        context = {
            'title': 'Search',
            'query': query,
            'doctors': doctors,
            # 'course': course,
        }
        return render(request, 'search.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))
    

def faq(request):
    faqs = FAQ.objects.all()
    context = {
        
        'faqs' : faqs
    
        
    }

    return render(request, 'faq.html', context )

def testimonials(request):
    

    return render(request, 'testimonials.html' )

