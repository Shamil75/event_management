from django import forms
from tasks.models import Event, Category, Participant


class StyledFormMisin:

    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder': f"Enter {field.label.lower()}",
                    'rows': 5,
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': "border-2 border-gray-300 p-2 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': "space-y-2"
                })


class EventModelForm(StyledFormMisin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'location','status', 'category' ]
        widgets = {
            'date': forms.SelectDateWidget,
            'category': forms.Select,
            'status': forms.Select,
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

class CategoryModelForm(StyledFormMisin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

class ParticipantModelForm(StyledFormMisin, forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'event']
        widgets = {
            'email': forms.EmailInput,
            'event': forms.CheckboxSelectMultiple
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
