from django.db import models

# Create your models here.
class company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=200)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(
        ('IT', 'IT'), ('NON IT', 'NON IT')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name+'--'+self.company_location
    

class employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    designation = models.CharField(max_length=50,choices=(
        ('manager','Manager'),('developer','Developer'),('tester','Tester')
    ))
    company = models.ForeignKey(company,on_delete=models.CASCADE)
