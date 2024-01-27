from django import forms  
from testdb.models import Employee

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"
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