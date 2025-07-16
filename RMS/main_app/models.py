from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.id}: {self.name}"

class UserInformation(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/',null=True,blank=True)
    username = models.CharField(unique=True,max_length=20)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    otp = models.CharField(max_length=6)
    otp_created_at = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.id}: {self.username}"


class Skills(models.Model):
    name = models.CharField(max_length=20)

class JobPost(models.Model):
    # id = models.IntegerField()
    status_choices = [
        ('open','Open'),
        ('closed','Closed'),
        ('onhold','Onhold')
    ]
    job_mode = [
        ('online','Online'),
        ('offline','Offline')
    ]
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=50)
    mode = models.CharField(max_length=50,choices=job_mode)
    experience_year = models.IntegerField()
    experience_month = models.IntegerField()
    status = models.CharField(max_length=50,choices=status_choices)
    skills = models.ForeignKey(Skills,on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserInformation,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class JobDesignation(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class AppliedJobs(models.Model):
    user = models.ForeignKey(UserInformation,on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class InterviewScheduling(models.Model):
    
    results = [
        ('pending','Pending'),
        ('selected','Selected'),
        ('resected','Resected'),
        ('onhold','Onhold')
    ]
    
    job_mode = [
        ('online','Online'),
        ('offline','Offline')
    ]
    # id = models.IntegerField()
    date_of_interview = models.DateTimeField()
    mode = models.CharField(max_length=50,choices=job_mode)
    feedback = models.TextField(max_length=150)
    job_designation = models.ForeignKey(JobDesignation,on_delete=models.CASCADE,related_name='job_designation')
    job_post = models.ForeignKey(JobPost,on_delete=models.CASCADE,related_name='job_post')
    createdby = models.ForeignKey(UserInformation,on_delete=models.CASCADE,related_name='interviews_created')
    schedule_for = models.ForeignKey(UserInformation,on_delete=models.CASCADE,related_name='interviews_recieved',null=True,blank=True)
    result = models.CharField(max_length=50,choices=results)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CandidateStatus(models.Model):
    # id = models.IntegerField()
    user = models.ForeignKey(UserInformation,on_delete=models.CASCADE)
    resume = models.FileField(upload_to='CandidateStatus/', max_length=255)
    skills = models.ForeignKey(Skills,on_delete=models.CASCADE)
    experience = models.FloatField()
    education = models.CharField(max_length=50)
    
        # def __str__(self):
        #     return f"{self.name}"



# Create your models here.
