from django import forms  
from FirstApp.models import login
from FirstApp.models import registration

class login(forms.ModelForm):  
    class Meta:  
        model = login 
        fields = "__all__"  
        
class registration(forms.ModelForm):
	class Meta:
		model=registration
		fields="__all__"

class contact(forms.ModelForm):
	class Meta:
		model=contact
		fields="__all__"