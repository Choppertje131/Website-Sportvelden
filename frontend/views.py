import time
from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from .models import Settings_fieldnames
from .models import Settings_lightnames
from .models import Selecting_fields
from datetime import datetime
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

    reversed_list = list(reversed(list(light_names.values())))
    for item in reversed_list:
        if item["field_id"] == "VID-B":
            lamp1 = item["Lamp1"]
            lamp2 = item["Lamp2"]
            lamp3 = item["Lamp3"]
            lamp4 = item["Lamp4"]
            lamp5 = item["Lamp5"]
            lamp6 = item["Lamp6"]
            break

    data = {
            'page': 'veld2.html',
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

    reversed_list = list(reversed(list(light_names.values())))
    for item in reversed_list:
        if item["field_id"] == "VID-C":
            lamp1 = item["Lamp1"]
            lamp2 = item["Lamp2"]
            lamp3 = item["Lamp3"]
            lamp4 = item["Lamp4"]
            lamp5 = item["Lamp5"]
            lamp6 = item["Lamp6"]
            break

    data = {
            'page': 'veld3.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
            'lamp1': lamp1,
            'lamp2': lamp2,
            'lamp3': lamp3,
            'lamp4': lamp4,
            'lamp5': lamp5,
            'lamp6': lamp6,
        }

    return render(request, 'Index.html', data)

def veld4view(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    reversed_list = list(reversed(list(light_names.values())))
    for item in reversed_list:
        if item["field_id"] == "VID-D":
            lamp1 = item["Lamp1"]
            lamp2 = item["Lamp2"]
            lamp3 = item["Lamp3"]
            lamp4 = item["Lamp4"]
            lamp5 = item["Lamp5"]
            lamp6 = item["Lamp6"]
            break

    data = {
            'page': 'veld4.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
            'lamp1': lamp1,
            'lamp2': lamp2,
            'lamp3': lamp3,
            'lamp4': lamp4,
            'lamp5': lamp5,
            'lamp6': lamp6,
            
        }

    return render(request, 'Index.html', data)

def toggle_boolean_field(request, field_name):
    if not Selecting_fields.objects.exists():
        Selecting_fields.objects.create(field1_active=False, field2_active=False, field3_active=False, field4_active=False, field5_active=False, field6_active=False)

    current_value = getattr(Selecting_fields.objects.last(), field_name)
    updated_value = not current_value

    setattr(Selecting_fields.objects.last(), field_name, updated_value)
    Selecting_fields.objects.last().save()
    
    return updated_value

def homeview(request):
    data = {
        'field1_active': Selecting_fields.objects.values('field1_active').last()['field1_active'],
        'field2_active': Selecting_fields.objects.values('field2_active').last()['field2_active'],
        'field3_active': Selecting_fields.objects.values('field3_active').last()['field3_active'],
        'field4_active': Selecting_fields.objects.values('field4_active').last()['field4_active'],
        'field5_active': Selecting_fields.objects.values('field5_active').last()['field5_active'],
        'field6_active': Selecting_fields.objects.values('field6_active').last()['field6_active'],
        'page': 'Home.html',
        'field': Selecting_fields(),
        'field': Settings_fieldnames.objects.last(),
    }

    return render(request, 'Index.html', data)

def turn_on_setup(field_name):
    table = Selecting_fields()

    for key, val in Selecting_fields.objects.values().last():
        if key == field_name:
            table.key = True
        else:
            table.key = False

    table.save()

field1_active = False

# def homeview(request):
#     global field1_active
#     if field1_active:
#         field1_active = False
#     else:
#         field1_active = True

#     data = {
#         'field1_active': field1_active,
#         'page': 'Home.html',
#         'field': Selecting_fields(),
#         'field': Settings_fieldnames.objects.last(),
#     }

#     return render(request, 'Index.html', data)

# field2_active = False

# def homeview(request):
#     global field2_active
#     if field2_active:
#         field2_active = False
#     else:
#         field2_active = True

#     data = {
#         'field2_active': field2_active,
#         'page': 'Home.html',
#         'field': Selecting_fields(),
#         'field': Settings_fieldnames.objects.last(),
        
#     }

#     return render(request, 'Index.html', data)

# field3_active = False

# def homeview(request):
#     global field1_active
#     if field3_active:
#         field3_active = False
#     else:
#         field3_active = True

#     data = {
#         'field3_active': field3_active,
#         'page': 'Home.html',
#         'field': Selecting_fields(),
#         'field': Settings_fieldnames.objects.last(),
#     }

#     return render(request, 'Index.html', data)

# field4_active = False

# def homeview(request):
#     global field4_active
#     if field4_active:
#         field4_active = False
#     else:
#         field4_active = True

#     data = {
#         'field4_active': field4_active,
#         'page': 'Home.html',
#         'field': Selecting_fields(),
#         'field': Settings_fieldnames.objects.last(),
#     }

#     return render(request, 'Index.html', data)

# field5_active = False

# def homeview(request):
#     global field5_active
#     if field5_active:
#         field5_active = False
#     else:
#         field5_active = True

#     data = {
#         'field5_active': field5_active,
#         'page': 'Home.html',
#         'field': Selecting_fields(),
#         'field': Settings_fieldnames.objects.last(),
#     }

#     return render(request, 'Index.html', data)

# field6_active = False

# def homeview(request):
#     global field6_active
#     if field6_active:
#         field6_active = False
#     else:
#         field6_active = True

#     data = {
#         'field6_active': field6_active,
#         'page': 'Home.html',
#         'field': Selecting_fields(),
#         'field': Settings_fieldnames.objects.last(),
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

# naam navigatiebalk veranderen
def settingssview(request):
    if request.method == "POST" and "nav" in request.POST:
        boxes = {'Box1': 'Veld1', 'Box2': 'Veld2', 'Box3': 'Veld3', 'Box4': 'Veld4'}
        table = Settings_fieldnames()

        for box, field in boxes.items():
            requested_box = request.POST.get(box)
            if requested_box != "" and len(requested_box) > 0:
                setattr(table, field, requested_box)
            else:
                setattr(table, field, Settings_fieldnames.objects.values(field).last()[field])

        table.save()

    
    if request.method == "POST" and "lights" in request.POST:
        boxes = {'l1': 'Lamp1', 'l2': 'Lamp2', 'l3': 'Lamp3', 'l4': 'Lamp4'}
        table = Settings_lightnames()

        for box, lamp in boxes.items():
            requested_box = request.POST.get(box)
            if requested_box != "" and len(requested_box) > 1:
                setattr(table, lamp, requested_box)
            else:
                setattr(table, lamp, Settings_lightnames.objects.values(lamp).last()[lamp])
        table.field_id = request.POST.get('field_id')
        
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
