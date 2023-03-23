from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    # 우리는 메타 클래스만 바꿔주면 된다
    class Meta(UserCreationForm.Meta):
        # 원래는 Auth.user지만
        # accounts.User를 보게 해주면 된다
        # 클래스를 직접 import해서 가져와도 되지만
        # user는 특별해서 장고에서 지원을 해주니까 저렇게 하자
        # 만약 내가 유저 모델을 세팅가서 바꾼다 하더라도 여기 굳이 다시 바꿔줄 필요X
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')