from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.shortcuts import redirect

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
        return redirect('articles:index')
