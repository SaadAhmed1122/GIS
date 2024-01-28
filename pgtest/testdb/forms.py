from django import forms  
from testdb.models import RoadData

class RoadForm(forms.ModelForm):  
    class Meta:  
        model = RoadData  
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user.pk
            self.fields['user'].widget.attrs['disabled'] = True
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        image = self.cleaned_data.get('image', None)
        if image:
            print(f'Saving image: {image.name}')
            instance.image_filename = f'road_defect_images/{image.name}'
            instance.image.save(image.name, image, save=True)  # Save the image file
        if commit:
            instance.save()
        return instance