from django import forms  
from testdb.models import Road,RoadDefectType,RoadData

class RoadForm(forms.ModelForm):
    # class Meta:
    #     model = Road
    #     fields = ['road_name', 'road_type', 'start_measure', 'end_measure', 'geometry']
    #     widgets = {
    #         'road_name': forms.TextInput(attrs={'class': 'form-control'}),
    #         'road_type': forms.Select(choices=RoadDefectType, attrs={'class': 'form-control'}),
    #         'start_measure': forms.NumberInput(attrs={'class': 'form-control'}),
    #         'end_measure': forms.NumberInput(attrs={'class': 'form-control'}),
    #         # 'image': forms.FileInput(attrs={'class': 'form-control'}),
    #     }

    # def clean_geometry(self):
    #     geometry = self.cleaned_data.get('geometry')
    #     if not geometry:
    #         raise forms.ValidationError("Geometry is required.")
    #     return geometry
    # road_type = forms.ChoiceField(choices=[(tag, tag.value) for tag in RoadDefectType], label='Type')
    # description = forms.CharField(label='Description:', widget=forms.Textarea)
    # lat = forms.FloatField(label='Cracks Latitude:')
    # lng = forms.FloatField(label='Cracks Longitude:')

    # TYPE_CHOICES = [
    #     ('road_defect', 'Road Defect'),
    #     ('inspection', 'Inspection'),
    # ]

    etype = forms.CharField(label='Type')

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
            self.fields['etype'].widget = forms.Select(choices=RoadDefectType)

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
    
    # # def save(self, commit=True):
    # #     instance = super().save(commit=False)
    # #     # instance.updated_by_user = self.user
    # #     description = self.cleaned_data.get('description', None)
    # #     if description:
    # #         instance.description = description
    # #     lat = self.cleaned_data.get('lat', None)
    # #     if lat:
    # #         instance.lat = lat
    # #     lng = self.cleaned_data.get('lng', None)
    # #     if lng:
    # #         instance.lng = lng
    # #     if commit:
    # #         instance.save()
    # #     return instance
   