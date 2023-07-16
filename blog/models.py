from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class admin_signup(models.Model):
    admin_name = models.CharField(max_length=255)
    admin_email = models.EmailField(max_length=255)
    admin_password = models.CharField(max_length=255)

    def __str__(self):
        return self.admin_name


class client_signup(models.Model):
    client_full_name = models.CharField(max_length=255)
    client_email = models.EmailField(max_length=255)
    client_password = models.CharField(max_length=255)

    def __str__(self):
        return self.client_full_name


class Employee(models.Model):
    employee_full_name = models.CharField(max_length=255)
    employee_email = models.EmailField(max_length=255)
    employee_password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.employee_full_name

class Employee_signups(models.Model):
    employee_full_names = models.CharField(max_length=255)
    employee_emails = models.EmailField(max_length=255)
    employee_passwords = models.CharField(max_length=255)

    def __str__(self):
        return self.employee_full_names


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    body = models.TextField(null=True, blank = True)
    price = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    image = models.ImageField(null=True, blank = True,upload_to='picture')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    service = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    assigned_person = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name  
