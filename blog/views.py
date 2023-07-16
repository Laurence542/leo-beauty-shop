from django.views import generic
from .models import Post
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category
from .models import Booking
from .models import Employee
from .models import client_signup
from .models import Employee_signups
from .models import admin_signup
from django.shortcuts import get_object_or_404, redirect
from django.utils.text import slugify
from django.contrib import messages

def action_bookings(request):
    views = Booking.objects.all()
    return render(request, 'client/actionbooking.html', {'views' : views})

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('action_booking')

def assign_case(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    case_category = request.POST.get('case_category')
    booking.assigned_person = case_category
    booking.save()
    
    messages.success(request, 'Client assigned successfully', {'sucess_message':'Account created sucessfully'})  # Add success message
    
    return redirect('booking')



def create_admin_signups(request):
    if request.method == 'POST':
        name_admin_signup = request.POST.get('admin_name')
        email_admin_signup = request.POST.get('admin_email')
        password_admin_signup = request.POST.get('admin_password')

        admin_new = admin_signup.objects.create(admin_name=name_admin_signup, admin_email=email_admin_signup, admin_password=password_admin_signup)
        if admin_new:
            return redirect('booking')
        else:
            return render(request, 'admin/signup_admin.html', {'success_message': 'wrong email or password.Please try again'})

    return render(request, 'admin/signup_admin.html')

def create_admin_logins(request):
    if request.method == 'POST':
        email_admin_login = request.POST['admin_email']
        password_admin_login = request.POST['admin_password']

        admin_login_users = admin_signup.objects.filter(admin_email=email_admin_login, admin_password=password_admin_login)
        if admin_login_users:
            return redirect('booking')

        else:
            return render(request, 'admin/login_admin.html', {'sucess_message': 'wrong email or password.Please try again'})
        
    return render(request, 'admin/login_admin.html')



def employeesignup(request):
    if request.method == 'POST':
        emplooye_name = request.POST.get('employee_full_names')
        emplooye_email = request.POST.get('employee_emails')
        emplooye_password = request.POST.get('employee_passwords')

        employeos_new = Employee_signups.objects.create(employee_full_names=emplooye_name, employee_emails=emplooye_email, employee_passwords=emplooye_password)
        if employeos_new:
             return render(request, 'employee/signup_employe.html',{'sucess_message':'Account created sucessfully'})
        
        else:
             return render(request, 'employee/signup_employe.html',{'sucess_message':'wrong email or password.Please try againr'})
        
    return render(request, 'employee/signup_employe.html')

def clients_signup(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_full_name')
        client_email = request.POST.get('client_email')
        client_password = request.POST.get('client_password')

        client_new = client_signup.objects.create(client_full_name=client_name, client_email=client_email, client_password=client_password)
        if client_new:
          
          return redirect('client_view')
           
        else:

            return render(request, 'client/signup_client.html', {'sucess_message':'wrong email or password.Please try again'}) 

    
    return render(request, 'client/signup_client.html')


def clientslogin(request):
    if request.method == 'POST':
        name_login_clients = request.POST['client_email']
        password_login_clients = request.POST['client_password']

        clients_logins = client_signup.objects.filter(client_email=name_login_clients, client_password=password_login_clients)
        
        if clients_logins:

            return redirect('client_view')

        else:

            return render(request, 'client/login_client.html', {'sucess_message':'wrong email or password.Please try again'})
    
    return render(request, 'client/login_client.html')


def view_employe(request):
    view_employee = Booking.objects.all()
    return render(request, 'employee/view_employee.html', {'view_employee': view_employee})

def client_views(request):
    views = Booking.objects.all()
    return render(request, 'client/view_client.html', {'views' : views})

def employelogins(request):
    if request.method == 'POST':
        employee_login_email = request.POST['employee_email']
        employee_login_password = request.POST['employee_password']

        new_empoyee_loginns = Employee.objects.filter(employee_email=employee_login_email,employee_password=employee_login_password)
        if new_empoyee_loginns:

            return redirect('view_employee')
        
        else:
             return render(request, 'employee/login_employe.html', {'sucess_message': 'wrong email or password.Please try again'})
        
    return render(request, 'employee/login_employe.html')

def create_employees(request):
    if request.method == 'POST':
        name_employes = request.POST.get('employee_full_name')
        email_employes = request.POST.get('employee_email')
        password_employes = request.POST.get('employee_password')

        Employee.objects.create(employee_full_name=name_employes, employee_email=email_employes, employee_password=password_employes)
        
        sucess_employee = {'success_message': 'Account created sucessfully'}
        
        return render(request, 'admin/create_employee.html', sucess_employee)
    
    else:
        fail_employee = {'sucess_message': 'Failed please try agin later'}

    return render(request, 'admin/create_employee.html',fail_employee)


def booking_views(request):
    bookingviewss = Post.objects.all()
    return render(request, 'booking_view.html', {'bookingviewss': bookingviewss})

def contact_us(request):
    return render(request, 'contactus.html')

def ourservices(request):
    return render(request, 'services.html')

def booking_view(request):
    view_username = Employee.objects.all()
    view_bookings = Booking.objects.all()
    return render(request, 'admin/bookings.html', {'view_bookings': view_bookings,'view_username':view_username})


def sucess_message(request):
    return render(request, 'success_message.html')

def credit_card(request):
    return render(request, 'creditcard.html')

def payment_methods(request):
    return render(request, 'payment_methods.html')

def booking_appointment(request):
    if request.method == 'POST':
        customer_name = request.POST.get('name')
        customer_email = request.POST.get('email')
        customer_phone = request.POST.get('phone')
        customer_servces = request.POST.get('service')
        customer_date = request.POST.get('date')
        customer_time = request.POST.get('time')
      
        Booking.objects.create(name= customer_name, email=customer_email, phone=customer_phone, service=customer_servces, date=customer_date, time=customer_time)
        
        context = {'success_message': 'Booking is successful. Please proceed to payment'}

        return render(request, 'payment_methods.html', context)
    
    return render(request, 'booking.html')


def admin_homepage (request):
    return render(request, 'admin/main_admin.html')


def hotel_view(request):
    services = Post.objects.all()
    return render(request, 'admin/hotel_view.html', {'services' : services})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('hotel_views')



def addservices(request):
    if request.method == 'POST':
        title_post = request.POST.get('title')
        slug_post = slugify(title_post)  # Generate the slug from the title using Django's slugify function
        body_post = request.POST.get('body')
        price_post = request.POST.get('price')
        image_post = request.FILES.get('image')

        addservicess = Post.objects.filter(title=title_post, slug=slug_post)
        if addservicess:
            return render(request, 'admin/add_services.html', {'success_message':'Services already exists Do not refresh'})
            
        else:
            Post.objects.create(title=title_post, slug=slug_post, body=body_post, price=price_post, image=image_post)
            return render(request, 'admin/add_services.html', {'success_message':'Service sucessfully added'})
         
    return render(request, 'admin/add_services.html')

  


# admin end

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

def about(request):
    return render(request, "about.html")   

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def home(request):
    return render(request, 'base.html')    

class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='1')
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context
    
def about(request):
    return render(request, 'about.html')    

def feature(request):
    return render(request, 'feature.html')     


