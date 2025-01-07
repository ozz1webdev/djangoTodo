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


class AddTaskForm(forms.Form):
    title = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={
            'placeholder': 'Task Title',
            'class': 'form-control'})
    )

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description',
        'class': 'form-control',
        'rows': 3
    }))

    priority = forms.ChoiceField(
        choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

