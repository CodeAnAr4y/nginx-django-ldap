from django.shortcuts import render
import ldap
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login, logout

def index(request):
    return HttpResponse("Home")



def logout_view(request):
    logout(request)
    return HttpResponse("Logged Out!")



def authorize_view(request):
    
    if request.user.is_authenticated:
        return HttpResponse("<h1>Authenticated</h1>")
    else:
        return HttpResponseBadRequest("failed", status=401)



def login_view(request):
    if request.method == "POST":
        user = authenticate(request=request,
                            username = request.POST['uid'],
                            password = request.POST['pass'],
                            )
        if user is not None:
            login(request, user)
            return HttpResponse(f"<h1>Logged In</h1>")
        else:
            return render(request, 'auth/index.html')
    else:
        return render(request, 'auth/index.html')
            




        # Формируется DN (Distinguished Name)
        # dn = f"uid={uid},ou=People,dc=sme-soft,dc=by"
    #     try:
    #         # if user is not None:
    #             login(request, user)
    #             connection = ldap.initialize(f"ldap://comelfo.com:389")
    #             connection.simple_bind_s(dn, password)
    #             request.session['username'] = uid
    #             request.session.save()
    #             return HttpResponse("Success")
    #         # else:
    #             # return HttpResponseBadRequest("Authentication failed1", status=401)
    #     except ldap.LDAPError as e:
    #         # Если аутентификация не удалась
    #         return HttpResponseBadRequest("Authentication failed2", status=401)
    # else:
    #     return render(request, 'auth/index.html')


# @require_http_methods(["POST"])
# def connect_to_ldap(request):
#     try:
#         uid = request.POST.get('uid')
#         password = request.POST.get('pass')
#         # Формируется DN (Distinguished Name)
#         dn = f"uid={uid},ou=People,dc=sme-soft,dc=by"
#         # Подключение к LDAP серверу
#         try:
#             con = ldap.initialize(f"ldap://comelfo.com:389")
#             con.simple_bind_s(dn, password)
#             return HttpResponse(f"<h1>Referer is: {request.headers['Referer']}</h1>", status=200)
#         except ldap.LDAPError as e:
#             # Если аутентификация не удалась
#             return HttpResponseBadRequest(f'<h1>${e}</h1>', status=400)
#     except Exception as e:
#         # Если произошла другая ошибка
#         return JsonResponse({'error': str(e)})