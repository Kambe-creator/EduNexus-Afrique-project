from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def edu_konnect(request):
    return render(request, 'website/edu_konnect.html')

def mtaa_legit(request):
    return render(request, 'website/mtaa_legit.html')

from django.shortcuts import render
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'website/blog_list.html', {'posts': posts})

from django.shortcuts import get_object_or_404

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'website/blog_detail.html', {'post': post})

def blog_list(request):
    category = request.GET.get('category', '')
    if category:
        posts = BlogPost.objects.filter(categories__icontains=category).order_by('-created_at')
    else:
        posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'website/blog_list.html', {'posts': posts, 'category': category})

from .models import Comment

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        Comment.objects.create(post=post, name=name, email=email, content=content)
    comments = post.comments.all()
    return render(request, 'website/blog_detail.html', {'post': post, 'comments': comments})

from django.shortcuts import render

def contact_us(request):
    return render(request, 'website/contact_us.html')

from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Combine the message with the sender's details
        full_message = f"Message from {name} ({email}):\n\n{message}"

        try:
            # Send the email
            send_mail(
                subject=subject,
                message=full_message,
                from_email='your_email@example.com',  # Replace with your email
                recipient_list=['recipient_email@example.com'],  # Replace with the recipient email
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

    return render(request, 'website/contact_us.html')

from django.shortcuts import render

def about_us(request):
    return render(request, 'website/about_us.html')
