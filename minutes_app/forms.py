from django import forms
from models import Meeting

# Meeting form
class MeetingForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=250, widget=forms.widgets.TextInput(attrs={'stat': 'normal'}))
#     email = forms.EmailField(required=True, max_length=75, widget=forms.widgets.TextInput(attrs={'stat': 'normal'}))

    items_discussed = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={'id': 'items_discussed_input', 'class': 'input-content'}))
    decisions_made = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={'id': 'decisions_made_input','class': 'input-content'}))
    action_items = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={'id': 'action_items_input','class': 'input-content'}))

    occurred = forms.DateTimeField(required=False)

    class Meta:
        model = Meeting
        exclude = ('url_ref',)