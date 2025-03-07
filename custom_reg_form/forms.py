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

    class Meta(object):
        model = ExtraInfo
        fields = ('market',)
        labels = {'market': u"Select Nearest Aquent Office",}
        help_texts = {'market': u"Please choose the Aquent office nearest to you.",}
