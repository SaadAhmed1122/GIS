from django import forms  
from testdb.models import RoadData

class RoadForm(forms.ModelForm):
    TYPE_CHOICES = [
        ('road_defect', 'Road Defect'),
        ('inspection', 'Inspection'),
    ]

    etype = forms.ChoiceField(choices=TYPE_CHOICES, label='Type')  
    class Meta:  
        model = RoadData  
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user
            self.fields['user'].required = False
            self.fields['user'].widget = forms.HiddenInput()

            # Set the initial value to the current user
            # self.fields['user'].widget.attrs['disabled'] = True
        print(user)
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        # instance.user = self.user
        image = self.cleaned_data.get('image', None)
        if image:
            print(f'Saving image: {image.name}')
            instance.image_filename = f'road_defect_images/{image.name}'
            instance.image.save(image.name, image, save=True)  # Save the image file
        if commit:
            instance.save()
        return instance