"""GETパラメータをpaginationと共存させるため、独自のdjangoタグを定義する"""
from django import template

register = template.Library()  # タグ、フィルターを登録する初期化


@register.simple_tag
def url_replace(request, field, value):
    """GETパラメータを書き換える"""
    url_dict = request.GET.copy()
    url_dict[field] = value
    return url_dict.urlencode()
