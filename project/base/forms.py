from django import forms


class createProjectForm(forms.Form):
    projectName = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={
            'placeholder': 'Project Name',
            'class': 'form-control'}))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description',
        'class': 'form-control',
        'rows': 3
    }))
