# all the imports to make the whole site work
import time as delay
from datetime import datetime, date, time
from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from .models import Settings_fieldnames, Settings_lightnames, Selecting_fields, LightButton
field_names = Settings_fieldnames
light_names = Settings_lightnames.objects.all()
light_button = LightButton

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
                return render(request, 'Login.html', data)
        else:
            data = {
                'page': 'Login.html',
                'error': 'Incorrect password and/or username. Note that both fields may be case-sensitive.',
            }
            return render(request, 'Login.html', data)

    data = {
        'page': 'Login.html',
        'error': '',
    }

    return render(request, 'Login.html', data)

def logoutview(request):
    logout(request)
    return redirect("/login")

# with line 49 to line 82, you can make your own account to view the site, however, you dont get permission to change anything.
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

# line 98 to line 125 are to make sure that you are logged in before you can view the site, but also to display the changes that are made in the Settings page.
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

# line 128 to line 155 are to make sure that you are logged in before you can view the site, but also to display the changes that are made in the Settings page.
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

# line 158 to 167 makes sure that you are logged in before you can view the site
def settingsview(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    data = {
            'page': 'Settings.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
        }

    return render(request, 'Index.html', data )

# line 170 to line 197 are to make sure that you are logged in before you can view the site, but also to display the changes that are made in the Settings page.
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

# line 200 to line 228 are to make sure that you are logged in before you can view the site, but also to display the changes that are made in the Settings page.
def veld4view(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    data = {
            'page': 'Veld4.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),          
        }

    return render(request, 'Index.html', data)

# line 199 to line 281, are there to make sure that all the lights will turn off at a specific time.
# def homeview(request):
    
#     now = datetime.now()

#     time_range_start = "23:00"
#     time_range_end = "06:00"

#     lamp001_bool = True
#     lamp002_bool = True
#     lamp003_bool = True
#     lamp004_bool = True

#     current_time = now.strftime("%H:%M")

#     if current_time == time_range_start:
#         lamp001_bool = False
#         lamp002_bool = False
#         lamp003_bool = False
#         lamp004_bool = False
#     elif current_time == time_range_end:
#         lamp001_bool = True
#         lamp002_bool = True
#         lamp003_bool = True
#         lamp004_bool = True

#     data = {
#             'page': 'Home.html',
#             'error': '',
#             'field': Settings_fieldnames.objects.last(),
#             'lamp001_bool': lamp001_bool,
#             'lamp002_bool': lamp002_bool,
#             'lamp003_bool': lamp003_bool,
#             'lamp004_bool': lamp004_bool,
#         }

#     return render(request, 'Index.html', data)

def homeview(request):
    
    now = datetime.now()

    time_range_start = "23:00"
    time_range_end = "06:00"

    if 'Lamp1' in request.POST:
        request.session['lamp001_bool'] = not request.session.get('lamp001_bool', True)
    if 'Lamp2' in request.POST:
        request.session['lamp002_bool'] = not request.session.get('lamp002_bool', True)
    if 'Lamp3' in request.POST:
        request.session['lamp003_bool'] = not request.session.get('lamp003_bool', True)
    if 'Lamp4' in request.POST:
        request.session['lamp004_bool'] = not request.session.get('lamp004_bool', True)

    current_time = now.strftime("%H:%M")

    lamp001_bool = request.session.get('lamp001_bool', True)
    lamp002_bool = request.session.get('lamp002_bool', True)
    lamp003_bool = request.session.get('lamp003_bool', True)
    lamp004_bool = request.session.get('lamp004_bool', True)

    if current_time == time_range_start:
        lamp001_bool = False
        lamp002_bool = False
        lamp003_bool = False
        lamp004_bool = False
    elif current_time == time_range_end:
        lamp001_bool = True
        lamp002_bool = True
        lamp003_bool = True
        lamp004_bool = True

    data = {
            'page': 'Home.html',
            'error': '',
            'field': Settings_fieldnames.objects.last(),
            'lamp001_bool': lamp001_bool,
            'lamp002_bool': lamp002_bool,
            'lamp003_bool': lamp003_bool,
            'lamp004_bool': lamp004_bool,
        }

    return render(request, 'Index.html', data)

# lines 284 to 482 makes sure that you can sellect the correct light option and makes the fields on the home page change color when its activated. There are 4 the same codes, but for a different page
def homeview(request):
    light_button = LightButton.objects.last()
    active_lamps = [lamp for lamp in ['Lamp001_bool', 'Lamp002_bool', 'Lamp003_bool', 'Lamp004_bool'] if getattr(light_button, lamp)]
    enabled_lamps = bool(active_lamps)

    field_settings = Selecting_fields.objects.last()
    active_fields = [field for field in ['field1_active', 'field2_active', 'field3_active', 'field4_active', 'field5_active', 'field6_active'] if getattr(field_settings, field)]
    enabled_fields = bool(active_fields)

    if request.method == 'POST':
        for lamp in ['Lamp001_bool', 'Lamp002_bool', 'Lamp003_bool', 'Lamp004_bool']:
            if lamp in request.POST:
                setattr(light_button, lamp, lamp not in active_lamps)
                light_button.save()
                active_lamps = [lamp] if lamp not in active_lamps else []
                enabled_lamps = bool(active_lamps)
                for other_lamp in ['Lamp001_bool', 'Lamp002_bool', 'Lamp003_bool', 'Lamp004_bool']:
                    if other_lamp != lamp:
                        setattr(light_button, other_lamp, False)
                        light_button.save()

        for field in ['field1_active', 'field2_active', 'field3_active', 'field4_active', 'field5_active', 'field6_active']:
            if field in request.POST:
                setattr(field_settings, field, field not in active_fields)
                field_settings.save()
                active_fields = [field] if field not in active_fields else []
                enabled_fields = bool(active_fields)
                for other_field in ['field1_active', 'field2_active', 'field3_active', 'field4_active', 'field5_active', 'field6_active']:
                    if other_field != field:
                        setattr(field_settings, other_field, False)
                        field_settings.save()

    lamp_data = {}
    for field_name in ['Lamp001_bool', 'Lamp002_bool', 'Lamp003_bool', 'Lamp004_bool']:
        lamp_data[field_name.lower()] = getattr(light_button, field_name)

    field_data = {f: getattr(field_settings, f) for f in ['field1_active', 'field2_active', 'field3_active', 'field4_active', 'field5_active', 'field6_active']}

    data = {
        'page': 'Home.html',
        'light': lamp_data,
        'field': Settings_fieldnames.objects.last(),
        'enabled_lamps': enabled_lamps,
        'active_lamps': active_lamps,
        'field_data': field_data,
        'enabled_fields': enabled_fields,
        'active_fields': active_fields,
    }
    return render(request, 'Index.html', data)

def veld1view(request):
    light_button = LightButton.objects.last()
    active_lamps = [lamp for lamp in ['Lamp005_bool', 'Lamp006_bool', 'Lamp007_bool', 'Lamp008_bool'] if getattr(light_button, lamp)]
    enabled_lamps = bool(active_lamps)

    field_settings = Selecting_fields.objects.last()
    active_fields = [field for field in ['field7_active', 'field8_active', 'field9_active', 'field10_active', 'field11_active', 'field12_active'] if getattr(field_settings, field)]
    enabled_fields = bool(active_fields)

    if request.method == 'POST':
        for lamp in ['Lamp005_bool', 'Lamp006_bool', 'Lamp007_bool', 'Lamp008_bool']:
            if lamp in request.POST:
                setattr(light_button, lamp, lamp not in active_lamps)
                light_button.save()
                active_lamps = [lamp] if lamp not in active_lamps else []
                enabled_lamps = bool(active_lamps)
                for other_lamp in ['Lamp005_bool', 'Lamp006_bool', 'Lamp007_bool', 'Lamp008_bool']:
                    if other_lamp != lamp:
                        setattr(light_button, other_lamp, False)
                        light_button.save()

        for field in ['field7_active', 'field8_active', 'field9_active', 'field10_active', 'field11_active', 'field12_active']:
            if field in request.POST:
                setattr(field_settings, field, field not in active_fields)
                field_settings.save()
                active_fields = [field] if field not in active_fields else []
                enabled_fields = bool(active_fields)
                for other_field in ['field7_active', 'field8_active', 'field9_active', 'field10_active', 'field11_active', 'field12_active']:
                    if other_field != field:
                        setattr(field_settings, other_field, False)
                        field_settings.save()

    lamp_data = {}
    for field_name in ['Lamp005_bool', 'Lamp006_bool', 'Lamp007_bool', 'Lamp008_bool']:
        lamp_data[field_name.lower()] = getattr(light_button, field_name)

    field_data = {f: getattr(field_settings, f) for f in ['field7_active', 'field8_active', 'field9_active', 'field10_active', 'field11_active', 'field12_active']}

    data = {
        'page': 'Veld1.html',
        'light': lamp_data,
        'field': Settings_fieldnames.objects.last(),
        'enabled_lamps': enabled_lamps,
        'active_lamps': active_lamps,
        'field_data': field_data,
        'enabled_fields': enabled_fields,
        'active_fields': active_fields,
    }
    return render(request, 'Index.html', data)

def veld2view(request):
    light_button = LightButton.objects.last()
    active_lamps = [lamp for lamp in ['Lamp009_bool', 'Lamp0010_bool', 'Lamp0011_bool', 'Lamp0012_bool'] if getattr(light_button, lamp)]
    enabled_lamps = bool(active_lamps)

    field_settings = Selecting_fields.objects.last()
    active_fields = [field for field in ['field13_active', 'field14_active', 'field15_active', 'field16_active', 'field17_active', 'field18_active'] if getattr(field_settings, field)]
    enabled_fields = bool(active_fields)

    if request.method == 'POST':
        for lamp in ['Lamp009_bool', 'Lamp0010_bool', 'Lamp0011_bool', 'Lamp0012_bool']:
            if lamp in request.POST:
                setattr(light_button, lamp, lamp not in active_lamps)
                light_button.save()
                active_lamps = [lamp] if lamp not in active_lamps else []
                enabled_lamps = bool(active_lamps)
                for other_lamp in ['Lamp009_bool', 'Lamp0010_bool', 'Lamp0011_bool', 'Lamp0012_bool']:
                    if other_lamp != lamp:
                        setattr(light_button, other_lamp, False)
                        light_button.save()

        for field in ['field13_active', 'field14_active', 'field15_active', 'field16_active', 'field17_active', 'field18_active']:
            if field in request.POST:
                setattr(field_settings, field, field not in active_fields)
                field_settings.save()
                active_fields = [field] if field not in active_fields else []
                enabled_fields = bool(active_fields)
                for other_field in ['field13_active', 'field14_active', 'field15_active', 'field16_active', 'field17_active', 'field18_active']:
                    if other_field != field:
                        setattr(field_settings, other_field, False)
                        field_settings.save()

    lamp_data = {}
    for field_name in ['Lamp009_bool', 'Lamp0010_bool', 'Lamp0011_bool', 'Lamp0012_bool']:
        lamp_data[field_name.lower()] = getattr(light_button, field_name)

    field_data = {f: getattr(field_settings, f) for f in ['field13_active', 'field14_active', 'field15_active', 'field16_active', 'field17_active', 'field18_active']}

    data = {
        'page': 'Veld2.html',
        'light': lamp_data,
        'field': Settings_fieldnames.objects.last(),
        'enabled_lamps': enabled_lamps,
        'active_lamps': active_lamps,
        'field_data': field_data,
        'enabled_fields': enabled_fields,
        'active_fields': active_fields,
    }
    return render(request, 'Index.html', data)

def veld3view(request):
    light_button = LightButton.objects.last()
    active_lamps = [lamp for lamp in ['Lamp0013_bool', 'Lamp0014_bool', 'Lamp0015_bool', 'Lamp0016_bool'] if getattr(light_button, lamp)]
    enabled_lamps = bool(active_lamps)

    field_settings = Selecting_fields.objects.last()
    active_fields = [field for field in ['field19_active', 'field20_active', 'field21_active', 'field22_active', 'field23_active', 'field24_active'] if getattr(field_settings, field)]
    enabled_fields = bool(active_fields)

    if request.method == 'POST':
        for lamp in ['Lamp0013_bool', 'Lamp0014_bool', 'Lamp0015_bool', 'Lamp0016_bool']:
            if lamp in request.POST:
                setattr(light_button, lamp, lamp not in active_lamps)
                light_button.save()
                active_lamps = [lamp] if lamp not in active_lamps else []
                enabled_lamps = bool(active_lamps)
                for other_lamp in ['Lamp0013_bool', 'Lamp0014_bool', 'Lamp0015_bool', 'Lamp0016_bool']:
                    if other_lamp != lamp:
                        setattr(light_button, other_lamp, False)
                        light_button.save()

        for field in ['field19_active', 'field20_active', 'field21_active', 'field22_active', 'field23_active', 'field24_active']:
            if field in request.POST:
                setattr(field_settings, field, field not in active_fields)
                field_settings.save()
                active_fields = [field] if field not in active_fields else []
                enabled_fields = bool(active_fields)
                for other_field in ['field19_active', 'field20_active', 'field21_active', 'field22_active', 'field23_active', 'field24_active']:
                    if other_field != field:
                        setattr(field_settings, other_field, False)
                        field_settings.save()

    lamp_data = {}
    for field_name in ['Lamp0013_bool', 'Lamp0014_bool', 'Lamp0015_bool', 'Lamp0016_bool']:
        lamp_data[field_name.lower()] = getattr(light_button, field_name)

    field_data = {f: getattr(field_settings, f) for f in ['field19_active', 'field20_active', 'field21_active', 'field22_active', 'field23_active', 'field24_active']}

    data = {
        'page': 'Veld3.html',
        'light': lamp_data,
        'field': Settings_fieldnames.objects.last(),
        'enabled_lamps': enabled_lamps,
        'active_lamps': active_lamps,
        'field_data': field_data,
        'enabled_fields': enabled_fields,
        'active_fields': active_fields,
    }
    return render(request, 'Index.html', data)

# line 485 to 497 makes sure that if you've got the 'Guest' role, that you cant change anything on the site.
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

# line 500 to 534 changes the name in the nav-bar. It also changes the name of the lights displayed on a certain kind of page
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
    return render(request, 'Index.html', data)

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
