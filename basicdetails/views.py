


from django.shortcuts import render
from basicdetails import models 
# Create your views here.

def index(request) : 
    skills_details = models.skills.objects.all()
    about = models.About.objects.all()
    for i in about : 
        about = i 
        break
    experiences = models.Experience.objects.all()
    educations = models.Education.objects.all()
    
    work_flow_details = models.workflow.objects.all()
    interests_details = models.interests.objects.all()
    awards_certifications_details = models.awards_certifications.objects.all()
    skill_details = about.skillset.all()
    return render(request, "index.html", {'about':about, 
                                         'experiences':experiences, 
                                         'educations' : educations,
                                         'work_flow_details':work_flow_details, 
                                         'interests_details':interests_details, 
                                         'skill_details':skill_details,
                                         'awards_certifications_details' : awards_certifications_details})

