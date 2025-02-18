from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['market'].error_messages = {
            "required": u"Please select the Aquent office nearest to you.",
            "invalid": u"Please select a valid Aquent office.",
        }
        self.fields['market'].required = True
        self.fields['receive_job_offers'].required = True

    class Meta(object):
        model = ExtraInfo
        fields = ('market','receive_job_offers')
        labels = {'market': u"Select Nearest Aquent Office", 'receive_job_offers': u"Do you wish to receive emails for job opportunities?" }
        help_texts = {'market': u"Please choose the Aquent office nearest to  you.", 'receive_job_offers': u"Please choose." }
