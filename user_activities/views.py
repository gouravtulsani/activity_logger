from django.http import JsonResponse
from django.views.decorators.http import require_GET
from user_activities.models import User, ActivityPeriod

# Create your views here.

@require_GET
def activities(request):
    users = User.objects.all()
    data = {
        'ok': True,
        'members': []
    }
    for u in users:
        user_info = {
            'id': u.id,
            'real_name': u.real_name,
            'tz': u.timezone,
        }

        activity_periods = ActivityPeriod.objects.filter(user_id = u.id).order_by('-start_time')

        user_info['activity_periods'] = [{
            'start_time': i.start_time,
            'end_time': i.end_time,
        } for i in activity_periods]

        data['members'].append(user_info)

    return JsonResponse(data)

@require_GET
def user_activity(request, user_id):
    data = {
        'ok': True,
    }

    activity_periods = ActivityPeriod.objects.filter(user_id=user_id).order_by('-start_time')

    data['activity_periods'] = [{
        'start_time': i.start_time,
        'end_time': i.end_time,
    } for i in activity_periods]

    return JsonResponse(data)
