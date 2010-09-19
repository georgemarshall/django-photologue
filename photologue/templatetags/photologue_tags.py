from django import template

from photologue.models import Photo

register = template.Library()

@register.inclusion_tag('photologue/tags/next_in_gallery.html')
def next_in_gallery(photo, gallery):
    return {'photo': photo.get_next_in_gallery(gallery)}

@register.inclusion_tag('photologue/tags/prev_in_gallery.html')
def previous_in_gallery(photo, gallery):
    return {'photo': photo.get_previous_in_gallery(gallery)}

@register.inclusion_tag('photologue/tags/gallery_photo.html')
def random_photos(number=0, is_public=True):
    """
    Return a specified number of random photos from all galleries
    """
    return {'object_list': Photo.objects.sample(number, is_public)}