from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from .models import Settings_fieldnames
from .models import Settings_lightnames
field_names = Settings_fieldnames
light_names = Settings_lightnames.objects.all()


def loginview(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                data = {
                    'page': 'Login.html', 
                    'error': 'User account not activated',
                }
                return render(request, 'Index.html', data)
        else:
            data = {
                'page': 'Login.html',
                'error': 'Incorrect password and/or username. Note that both fields may be case-sensitive.',
            }
            return render(request, 'Index.html', data)

    data = {
        'page': 'Login.html',
        'error': '',
    }

    return render(request, 'Index.html', data)

def logoutview(request):
    logout(request)
    return redirect("/login")

def registerview(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirmPassword')

        if password1 == password2:
            user = User.objects.create_user(username=username, email='', password=password1)

            if user is not None:
                return redirect('/login')

            else:
                data = {
                    'page': 'Register.html',
                    'error': 'Form incomplete'
                }

                return render(request, 'Index.html', data)
        
        else:
            data = {
                'page': 'Register.html',
                'error': 'Passwords are not the same'
            }
            return render(request, 'Index.html', data)

    data = {
            'page': 'Register.html',
            'error': '',
        }

    return render(request, 'Index.html', data )

def homeview(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    data = {
            'page': 'Home.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
        }

    return render(request, 'Index.html',data)

def veld1view(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    reversed_list = list(reversed(list(light_names.values())))
    for item in reversed_list:
        if item["field_id"] == "VID-A":
            lamp1 = item["Lamp1"]
            lamp2 = item["Lamp2"]
            lamp3 = item["Lamp3"]
            lamp4 = item["Lamp4"]
            lamp5 = item["Lamp5"]
            lamp6 = item["Lamp6"]
            break

    data = {
            'page': 'veld1.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
            'lamp1': lamp1,
            'lamp2': lamp2,
            'lamp3': lamp3,
            'lamp4': lamp4,
            'lamp5': lamp5,
            'lamp6': lamp6,
        }

    return render(request, 'Index.html', data )

def veld2view(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    data = {
            'page': 'Veld2.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
        }

    return render(request, 'Index.html', data )

def settingsview(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    data = {
            'page': 'Settings.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
        }

    return render(request, 'Index.html', data )

def veld3view(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    data = {
            'page': 'Veld3.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
        }   
    return render(request, 'Index.html', data)

def veld4view(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    data = {
            'page': 'Veld4.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
        }   
    return render(request, 'Index.html', data)

# def settingssview(request):
#     if not request.user.is_authenticated:
#         return redirect('/login')
#     data = {
#             'page': 'Settingss.html',
#             'error': '',
#             'field': Settings_fieldnames.objects.last(),
#         }   
#     return render(request, 'Index.html', data)

# def homeview(request):
#     Lamp001_bool = False

#     data = {
#         'Lamp001_bool': Lamp001_bool,
#         'page': 'Home.html',
#     }
#     return render(request, 'Index.html', data)

def settingsview(request):
    if request.user.is_authenticated:
        if request.user.has_perm('Guest','Guest'):
            return redirect('/settingss')
    else:
        return redirect('/')
    
    data = {
            'page': 'Settings.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
        }   
    return render(request, 'Index.html', data)

# def settingsview(request):
#     if request.user.is_authenticated:
#         if request.user.has_perm('Admin','Admin'):
#             return redirect('/settings')

# naam navigatiebalk veranderen
def settingssview(request):
    if request.method == "POST":
        boxes = {'Box1': 'Veld1', 'Box2': 'Veld2', 'Box3': 'Veld3', 'Box4': 'Veld4'}
        table = Settings_fieldnames()

        for box, field in boxes.items():
            requested_box = request.POST.get(box)
            if requested_box != "" and len(requested_box) > 1:
                setattr(table, field, requested_box)
            else:
                setattr(table, field, Settings_fieldnames.objects.values(field).last()[field])

        table.save()
    
    data = {
                'page': 'Settingss.html',
                'error': '',
                'field': Settings_fieldnames.objects.last(),
            }   
    return render(request, 'index.html', data)

# Naam lampen veranderen
# def settingssview(request):
#     if request.method == "POST":
#         boxes = {'Box5': 'Lamp1', 'Box6': 'Lamp2', 'Box7': 'Lamp3', 'Box8': 'Lamp4'}
#         table = Settings_lightnames()

#         for box, light in boxes.items():
#             requested_box = request.POST.get(box)
#             if requested_box is not None and requested_box != "" and len(requested_box) > 1:
#                 setattr(table, light, requested_box)
#             else:
#                 setattr(table, light, Settings_lightnames.objects.values(light).last()[light])

#         table.save()
    
#     data = {
#         'page': 'Settingss.html',
#         'error': '',
#         'field': Settings_lightnames.objects.last(),
#     }   
#     return render(request, 'index.html', data)

     