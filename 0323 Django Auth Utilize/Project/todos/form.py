from django import forms
from .models import Todo

'''
Django Form VS ModelForm
Form : html 랜더링, 유효성 검사 <= 귀찮다. django야 대신해줘
ModelForm : 어차피 form 객체 DB와 같이 쓸건데, 필드도 model 기반으로 만들어줘
            왜? 귀찮으니까

'''

class TodoForms(forms.ModelForm):
    class Meta:
        model = Todo # 이 모델 기반으로 Form을 만들어줘
        fields = ('task',) # 모든 필드를 다 받을거야
        # exclude와 fields 둘 중 하나만 사용하자