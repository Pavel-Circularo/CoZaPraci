from django.forms import ModelForm

from .models import Job

class JobForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Job
        fields = "__all__"
        