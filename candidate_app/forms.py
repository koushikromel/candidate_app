from django.forms import ModelForm
from .models import *


class CandidateForm(ModelForm):
    class Meta:
        model = Candidatedirectory
        fields = '__all__'


class EventDetailsForm(ModelForm):
    class Meta:
        model = EventDetails
        fields = '__all__'

class JobRequisitionForm(ModelForm):
    class Meta:
        model = JobRequisition
        fields = '__all__'

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class ScreeningModeForm(ModelForm):
    class Meta:
        model = ScreeningMode
        fields = '__all__'

class GenderForm(ModelForm):
    class Meta:
        model = Gender
        fields = '__all__'

class MaritalStatusForm(ModelForm):
    class Meta:
        model = MaritalStatus
        fields = '__all__'

class EmployeeDirectoryForm(ModelForm):
    class Meta:
        model = EmployeeDirectory
        fields = '__all__'

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class ExperienceLevelForm(ModelForm):
    class Meta:
        model = ExperienceLevel
        fields = '__all__'

class EducationLevelForm(ModelForm):
    class Meta:
        model = EducationLevel
        fields = '__all__'

class EducationQualificationForm(ModelForm):
    class Meta:
        model = EducationQualification
        fields = '__all__'

class EducationSpecializationForm(ModelForm):
    class Meta:
        model = EducationSpecialization
        fields = '__all__'

class EducationSourceForm(ModelForm):
    class Meta:
        model = EducationSource
        fields = '__all__'

class SourceTypeForm(ModelForm):
    class Meta:
        model = SourceType
        fields = '__all__'

class SourceForm(ModelForm):
    class Meta:
        model = Source
        fields = '__all__'

class ReasonForChangeForm(ModelForm):
    class Meta:
        model = ReasonForChange
        fields = '__all__'