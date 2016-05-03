from django.db import models

class Applicant(models.Model):
    Applicant_Id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length = 30)
    LastName = models.CharField(max_length = 30)
    DateOfBirth = models.DateField()
    City = models.ForeignKey("City")
    Qualification = models.CharField(max_length = 50)
    Job = models.ForeignKey("JobRole")
    #Skills = models.ForeignKey("Skills")
    Experience = models.IntegerField()
    ExpectedSalary = models.IntegerField()
    Languages = models.CharField(max_length = 30)
    Verified_By = models.CharField(max_length = 50)
    
    def __str__(self):
        return str(self.FirstName) + " " +str(self.LastName)

class City(models.Model):
    City_Id = models.AutoField(primary_key=True)
    CityName = models.CharField(max_length = 30)
    State = models.CharField(max_length = 30)

    def __str__(self):
        return str(self.CityName)

class JobRole(models.Model):
    JobRole_Id = models.AutoField(primary_key=True)
    Jobtype = models.CharField(max_length = 30)
    IndustryName = models.CharField(max_length = 30)
    
    def __str__(self):
        return str(self.Jobtype)

class Qualification(models.Model):
    InstitutionName = models.CharField(max_length = 50)
    EducationLevel = models.CharField(max_length = 10)
    StartDate = models.DateField()
    EndDate = models.DateField()
        
    def __str__(self):
        return str(self.InstitutionName)

class Experience(models.Model):
    Applicant_Name = models.ForeignKey("Applicant")
    EmployerName = models.CharField(max_length = 50)
    StartDate = models.DateField()
    EndDate = models.DateField()
    
    def __str__(self):
        return str(self.EmployerName)