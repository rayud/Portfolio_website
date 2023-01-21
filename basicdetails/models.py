


from django.db import models
from django.contrib.auth.models import User

class skills(models.Model) :
    name = models.CharField(max_length=30) 
    icon = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class About(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=13)
    description = models.TextField()
    linkedin_url = models.URLField()
    github_url = models.URLField()
    twitter_url = models.URLField()
    facebook_url = models.URLField()
    skillset = models.ManyToManyField(skills)

    def __str__(self):
        return self.user.username
    

class Experience(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_position = models.CharField(max_length=30, null=False, blank=False)
    organization = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField()
    presently_working = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) : 
        return self.organization
    class Meta : 
        ordering = ['-start_date']

    


class Education(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=30, null=False, blank=False)
    specilization = models.CharField(max_length=30, null=False, blank=False)
    percentage_cgpa = models.FloatField()
    presently_studying = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    class Meta : 
        ordering = ['-start_date']
    
    def __str__(self):
        return self.user.username +" "+self.course 


class workflow(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workflow = models.TextField()

    class Meta: 
        ordering = ['workflow']

    def __str__(self) : 
        return self.workflow + " " + self.user.username

class interests(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()

class awards_certifications(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.user.username +" "+self.name
    