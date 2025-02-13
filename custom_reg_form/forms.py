from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['market'].error_messages = {
            "invalid": u"Please select the Aquent office nearest you.",
        }
        self.fields['market'].required = False

    class Meta(object):
        model = ExtraInfo
        fields = ('market',)
