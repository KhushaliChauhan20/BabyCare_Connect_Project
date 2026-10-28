from django.db import models
  

# Create your models here.
class parent(models.Model):
    name =models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    address=models.TextField()
    par_mobile=models.IntegerField()
    no_child=models.IntegerField()  
    child_age=models.IntegerField()

    def __str__(self):
        return self.name

class service(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    img=models.ImageField(upload_to='service_images')
    # price=models.IntegerField()

    def __str__(self):
        return self.title

class service_provider(models.Model):
    name=models.CharField(max_length=50)
    pro_password=models.CharField(max_length=50, null=True)
    pro_email=models.CharField(null=True)
    pro_address=models.TextField(null=True)
    experience=models.IntegerField()
    age=models.IntegerField()
    photo=models.ImageField(upload_to='provider_images')
    service=models.ForeignKey(service,on_delete=models.CASCADE)
    pro_price=models.IntegerField()

    def __str__(self):
        return self.name

class book(models.Model):
    parent=models.ForeignKey(parent,on_delete=models.CASCADE)
    book_email=models.EmailField()
    service_provider=models.ForeignKey(service_provider,on_delete=models.CASCADE)
    book_mobile=models.IntegerField()
    book_price=models.IntegerField()
    book_state=models.CharField(max_length=50)
    book_city=models.CharField(max_length=50)
    book_pincode=models.IntegerField()
    book_address=models.TextField()
    transaction=models.CharField(blank=True, null=True)
    datetime=models.DateTimeField()

    def __str__(self):
        return self.parent.name