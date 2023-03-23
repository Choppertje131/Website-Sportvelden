# Django framework packages
from datetime import datetime, date, time
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Permission
from .models import Settings_fieldnames, Settings_lightnames, Selecting_fields

# Own packages
from .site_functions import get_field_button_states, select_field_state

# Global variables
field_names = Settings_fieldnames
light_names = Settings_lightnames.objects.all()


# line 15 to line 47 makes sure that you cant enter the website without having an account.
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

# with line 50 to line 83, you can make your own account to view the site, however, you dont get permission to change anything.
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













# --------------------- CODE SEBAS ----------------------------------
def homeview(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    if request.method == 'POST':
        fields = Selecting_fields.objects.all().values().last()
        field_names = [key for key in fields if key != 'id']
        
        for idx, key in enumerate(["0", "1", "2", "3", "4", "5"]):
            if key in request.POST:
                field = field_names[idx]
                select_field_state(field)

    field_bools = get_field_button_states()

    data = {
            'page': 'Home.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
            'field1_active': field_bools[0],
            'field2_active': field_bools[1],
            'field3_active': field_bools[2],
            'field4_active': field_bools[3],
            'field5_active': field_bools[4],
            'field6_active': field_bools[5],
        }

    return render(request, 'Index.html',data)

# --------------------- CODE SEBAS ----------------------------------


















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

# line 129 to line 156 are to make sure that you are logged in before you can view the site, but also to display the changes that are made in the Settings page.
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

# line 159 to 168 makes sure that you are logged in before you can view the site
def settingsview(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    data = {
            'page': 'Settings.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
        }

    return render(request, 'Index.html', data )

# line 171 to line 198 are to make sure that you are logged in before you can view the site, but also to display the changes that are made in the Settings page.
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

# line 201 to line 229 are to make sure that you are logged in before you can view the site, but also to display the changes that are made in the Settings page.
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


def turn_on_setup(field_name):
    table = Selecting_fields()

    for key, val in Selecting_fields.objects.values().last():
        if key == field_name:
            table.key = True
        else:
            table.key = False

    table.save()


# line 393 to 405 makes sure that if you've got the 'Guest' role, that you cant change anything on the site.
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

# line 408 to 442 changes the name in the nav-bar. It also changes the name of the lights displayed on a certain kind of page
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
        boxes = {'l1': 'Lamp1', 'l2': 'Lamp2', 'l3': 'Lamp3', 'l4': 'Lamp4', 'l5': 'Lamp5', 'l6': 'Lamp6'}
        table = Settings_lightnames()

        for box, lamp in boxes.items():
            requested_box = request.POST.get(box)
            if requested_box != "" and len(requested_box) > 1:
                setattr(table, lamp, requested_box)
            else:
                setattr(table, lamp, Settings_lightnames.objects.values(lamp).last()[lamp])
        table.field_id = request.POST.get('field_id')
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

     
