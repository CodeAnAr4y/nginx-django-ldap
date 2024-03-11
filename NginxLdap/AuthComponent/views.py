from django.shortcuts import render
import ldap
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


def index(request):
    return render(request, 'auth/index.html')


@require_http_methods(["POST"])
def connect_to_ldap(request):
    try:
        server_url = request.POST.get('server_url')
        server_port = request.POST.get('server_port')
        uid = request.POST.get('uid')
        ou = request.POST.get('ou')
        dc1 = request.POST.get('dc1')
        dc2 = request.POST.get('dc2')
        password = request.POST.get('pass')
        # Формируется DN (Distinguished Name)
        dn = f"uid={uid},ou={ou},dc={dc1},dc={dc2}"
        # Подключение к LDAP серверу
        try:
            con = ldap.initialize(f"ldap://{server_url}:{server_port}")
            con.simple_bind_s(dn, password)
            # Если аутентификация прошла успешно
            return JsonResponse({'success': True})
        except ldap.LDAPError as e:
            # Если аутентификация не удалась
            return JsonResponse({'success': False, 'error': str(e)})
    except Exception as e:
        # Если произошла другая ошибка
        return JsonResponse({'error': str(e)}, status=400)
