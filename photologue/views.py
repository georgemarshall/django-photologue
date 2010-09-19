from django import forms
from django.http import HttpResponse
from django.views.generic.date_based import archive_index
from django.utils import simplejson as json

from forms import AjaxRequestForm
from models import Photo
from urls import photo_args

def ajax_view(request):
    """
    Handle any async JS server function request
    """
    def JsonResponse(data):
        """
        Wraper to allow an easy method to return json data
        """
        return HttpResponse(json.dumps(data), mimetype='application/json')

    ajax_request = AjaxRequestForm(data=request.GET)
    if ajax_request.is_valid():
        request_type = ajax_request.cleaned_data['type']

        # sample()
        if request_type == 'sample':
            # Excluded is_public for obvious security reasons
            ajax_request.fields['count'] = forms.IntegerField(min_value=0, max_value=100, required=False)
            ajax_request.full_clean()
            if ajax_request.is_valid():
                photo_list = []
                photos = Photo.objects.sample(ajax_request.cleaned_data['count'])
                for photo in photos:
                    photo_list.append({
                        'thumbnail': photo.get_thumbnail_url(),
                        'title': photo.title,
                        'url': photo.get_absolute_url()
                    })
                return JsonResponse(photo_list)

def photo_index(request):
    if request.is_ajax():
        return ajax_view(request)
    return archive_index(request, **photo_args)
