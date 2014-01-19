from django import forms
from django.forms.extras.widgets import SelectDateWidget

import account.forms

from django.utils.translation import ugettext_lazy as _

from hackingweek.models import Team

# List of status.
LEVEL_CHOICES = (
    ('Terminale', 'Terminale'),
    ('Bac+1', 'Bac+1'),
    ('Bac+2', 'Bac+2'),
    ('Bac+3', 'Bac+3'),
    ('Bac+4', 'Bac+4'),
    ('Bac+5', 'Bac+5')
    )

class SignupForm(account.forms.SignupForm):
    real_name   = forms.CharField(label=_("Real Name"), max_length=128)
    school      = forms.CharField(label=_("School"), max_length=128)
    study_level = forms.ChoiceField(label=_("Study Level"), choices=LEVEL_CHOICES)

class SettingsForm(account.forms.SettingsForm):
    real_name   = forms.CharField(label=_("Real Name"), max_length=128)
    school      = forms.CharField(label=_("School"), max_length=128)
    study_level = forms.ChoiceField(label=_("Study Level"), choices=LEVEL_CHOICES)
