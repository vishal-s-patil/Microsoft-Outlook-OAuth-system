from django.shortcuts import HttpResponse, HttpResponseRedirect
from .models import Users
import base64
import json
from OutlookAuth.helpers.auth_helper import get_sign_in_flow


def initialize_context(request):
    context = {}
    error = request.session.pop('flash_error', None)
    if error is not None:
        context['errors'] = []
    context['errors'].append(error)
    # Check for user in the session
    context['user'] = request.session.get('user', {'is_authenticated': False})
    return context


def home(req):
    if not req.session.has_key('username'):
        return HttpResponseRedirect('/signin')

    return HttpResponse(
        f'Hi, {req.session["username"]} <br/> Thank You for registering')


def callback(req):
    client_info = req.GET.get('client_info')
    if client_info is None or client_info == '':
        return HttpResponseRedirect('/signin')

    print("client_info", req.GET.get('client_info'))
    client_info_padded = client_info + '=' * (-len(client_info) % 4)
    client_info_decoded = base64.b64decode(client_info_padded).decode('utf-8')
    client_info_json = json.loads(client_info_decoded)
    print('json_object', client_info_json)

    users = Users.objects.filter(
        email=client_info_json["preferred_username"]).values()
    if len(users) == 0:
        user = Users(
            user_name=client_info_json["name"],
            email=client_info_json["preferred_username"])
        user.save()

    req.session['username'] = client_info_json["name"]

    return HttpResponse(
        f'Hi, {client_info_json["name"]} <br/> Thank You for registering')


def sign_in(req):
    flow = get_sign_in_flow()
    try:
        req.session['auth_flow'] = flow
    except Exception as e:
        print(e)
    return HttpResponseRedirect(flow['auth_uri'])


def signout(req):
    try:
        del req.session['username']
    except BaseException:
        pass

    return HttpResponse("<strong>You are logged out.</strong>")


def get_all_users(req):
    users = Users.objects.all().values()
    data = json.dumps(list(users))
    return HttpResponse(data, content_type='application/json')
