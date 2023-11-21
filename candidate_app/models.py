from django.db import models


class EventDetails(models.Model):
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    event_location = models.CharField(max_length=255)

    def __str__(self):
        return self.event_name

    class Meta:
        db_table = "event"


class JobRequisition(models.Model):
    JOB_POSITION = [
        ('ONLINE', 'ONLINE'),
        ('OFFLINE', 'OFFLINE')
    ]
    job_position = models.CharField(max_length=20, choices=JOB_POSITION)

    def __str__(self):
        return self.job_position
    
    class Meta:
        db_table = "job_position"

class Persona(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "persona"

class ScreeningMode(models.Model):
    SCREENING_MODE = [
        ('ONLINE', 'ONLINE'),
        ('OFFLINE', 'OFFLINE')
    ]
    screening_mode = models.CharField(max_length=20, choices=SCREENING_MODE)
    
    def __str__(self):
        return self.screening_mode
    
    class Meta:
        db_table = "screening_mode"

class Gender(models.Model):
    CHOICES = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('Others', 'Others')
    ]
    gender = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return self.gender
    
    class Meta:
        db_table = "gender"

class MaritalStatus(models.Model):
    MARITAL_STATUS = [
        ('Married', 'Married'),
        ('Single', 'Single'),
        ('Prefer Not To Sa', 'Prefer Not To Say')
    ]
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS)
    
    def __str__(self):
        return self.marital_status
    
    class Meta:
        db_table = "marital_status"

class EmployeeDirectory(models.Model):
    employee_dir = models.CharField(max_length=255)

    def __str__(self):
        return self.employee_dir
    
    class Meta:
        db_table = "referred_by"

class City(models.Model):
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return self.city_name
    
    class Meta:
        db_table = "city"
    

class ExperienceLevel(models.Model):
    EXPERIENCE_LEVEL = [
        ('FRESHER', 'FRESHER'),
        ('JUNIOR', 'JUNIOR'),
        ('SENIOR', 'SENIOR')
    ]
    exp_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL)
    
    def __str__(self):
        return self.exp_level
    
    class Meta:
        db_table = "experience_level"

class EducationLevel(models.Model):
    EDU_LEVEL = [
        ('UNDER GRADUATE', 'UNDER GRADUATE'),
        ('POST GRADUATE', 'POST GRADUATE'),
        ('DOCTORAL', 'DOCTORAL'),
    ]
    edu_level = models.CharField(max_length=20, choices=EDU_LEVEL)
    
    def __str__(self):
        return self.edu_level
    
    class Meta:
        db_table = "education_level"

class EducationQualification(models.Model):
    EDU_QUALIFICATION = [
        ('BACHELORS', 'BACHELORS'),
        ('MASTERS', 'MASTERS'),
        ('PHD', 'PHD'),
    ]
    qualification = models.CharField(max_length=20, choices=EDU_QUALIFICATION)
    
    def __str__(self):
        return self.qualification
    
    class Meta:
        db_table = "education_qualification"

class EducationSpecialization(models.Model):
    specialization = models.CharField(max_length=255)
    
    def __str__(self):
        return self.specialization
    
    class Meta:
        db_table = "education_specialization"

class EducationSource(models.Model):
    institution_name = models.CharField(max_length=255)

    def __str__(self):
        return self.institution_name

    class Meta:
        db_table = "education_institution"

class SourceType(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type

    class Meta:
        db_table = "source_type"

class Source(models.Model):
    source_name = models.CharField(max_length=255)
    source_type = models.ForeignKey(SourceType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.source_name

    class Meta:
        db_table = "source"


class ReasonForChange(models.Model):
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.reason

    class Meta:
        db_table = "reason_for_change"



class Candidatedirectory(models.Model):
    event = models.ForeignKey("Eventdetails", models.DO_NOTHING, db_column="event", blank=True,null=True)
    job_position = models.ForeignKey("Jobrequisition",models.DO_NOTHING,db_column="job_position",blank=True,null=True,)
    recruiter_alert = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    persona = models.ForeignKey("Persona",models.DO_NOTHING,db_column="persona",blank=True,null=True,default=1,)
    role = models.IntegerField(blank=True, null=True)
    screening_mode = models.ForeignKey("Screeningmode",models.DO_NOTHING,db_column="screening_mode",blank=True,null=True,)
    dob = models.DateField(blank=True, null=True)
    gender = models.ForeignKey("Gender", models.DO_NOTHING, db_column="gender", blank=True, null=True)
    marital_status = models.ForeignKey("Maritalstatus",models.DO_NOTHING,db_column="marital_status",blank=True,null=True,)
    contact_no_primary = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    contact_no_alternate = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    referred_by = models.ForeignKey("Employeedirectory",models.DO_NOTHING,db_column="referred_by",blank=True,null=True,)
    referred_by_other = models.CharField(max_length=250, blank=True, null=True)
    address_line = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey("City", models.DO_NOTHING, db_column="city", blank=True, null=True)
    pincode = models.DecimalField(max_digits=6, decimal_places=0, blank=True,null=True)
    experience_level = models.ForeignKey("Experiencelevel",models.DO_NOTHING,db_column="experience_level",blank=True,null=True,)
    education_level = models.ForeignKey("Educationlevel",models.DO_NOTHING,db_column="education_level",blank=True,null=True,)
    education_qualification = models.ForeignKey("Educationqualification",models.DO_NOTHING,db_column="education_qualification",blank=True,null=True,)
    education_specialization = models.ForeignKey("Educationspecialization",models.DO_NOTHING,db_column="education_specialization",blank=True,null=True,)
    education_specialization_other = models.TextField(blank=True, null=True) # This field type is a guess.
    education_institution = models.ForeignKey("Source",models.DO_NOTHING,db_column="education_institution",blank=True,null=True,)
    education_institution_other = models.TextField(blank=True, null=True) # This field type is a guess.
    source = models.ForeignKey("Source",models.DO_NOTHING,db_column="source",blank=True,null=True,related_name="source_for_candidate_details",)
    source_type = models.ForeignKey("Sourcetype", models.DO_NOTHING, db_column="source_type", blank=True,null=True)
    years_of_experience = models.DecimalField(
    max_digits=4, decimal_places=2, blank=True, null=True)
    current_employer = models.CharField(max_length=100, blank=True, null=True)
    current_designation = models.TextField(blank=True, null=True) # This field type is a guess.
    current_monthly_salary = models.IntegerField(blank=True, null=True)
    expected_monthly_salary = models.IntegerField(blank=True, null=True)
    notice_period = models.CharField(max_length=50, blank=True, null=True)
    reason_for_change = models.ForeignKey("Reasonforchange",models.DO_NOTHING,db_column="reason_for_change",blank=True,null=True,)
    photo_path = models.TextField(blank=True, null=True) # This field type is a guess.
    resume_path = models.TextField(blank=True, null=True) # This field type is a guess.
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    geo_location = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = "CandidateDirectory"
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='full_nam')
        ]