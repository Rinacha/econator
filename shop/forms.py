from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=100)
    sender = forms.EmailField(label='Email', help_text='※ご確認の上、正しく入力してください。')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
#    myself = forms.BooleanField(label='同じ内容を受け取る', required=False)
#  def clean_subject(self)
    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if(subject.find('<') != -1 or subject.find('>') != -1):
            raise forms.ValidationError("Tags are not allowed.")
        return subject
    def clean_message(self):
        message = self.cleaned_data['message']
        if(message.find('<') != -1 or message.find('>') != -1):
            raise forms.ValidationError("Tags are not allowed.")
        return message
