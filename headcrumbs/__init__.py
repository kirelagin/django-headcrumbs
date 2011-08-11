# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse, resolve, get_callable

def is_crumbed(view):
  return hasattr(get_callable(view), 'crumb_text')


class CrumbedView(object):
  def __init__(self, view, url, args, kwargs):
    view = get_callable(view)
    if (not is_crumbed(view)):
      raise ValueError("The view is not crumbed")
    self._view = view
    self._url = url
    # Theese are exactly those args expected by view, not by url pattern
    self._args = args
    self._kwargs = kwargs

  @property
  def text(self):
    val = self._view.crumb_text
    if isinstance(val, basestring):
      return val
    else:
      try:
        return self._helper_call(val)
      except TypeError:
        raise TypeError('String or callable expected but got: {0}'.format(val))

  @property
  def _parent_args(self):
    val = self._view.crumb_p_args
    if isinstance(val, list):
      return val
    else:
      try:
        return self._helper_call(val)
      except TypeError as e:
        raise TypeError('List or callable expected but got: {0}'.format(val))

  @property
  def _parent_kwargs(self):
    val = self._view.crumb_p_kwargs
    if isinstance(val, dict):
      return val
    else:
      try:
        return self._helper_call(val)
      except TypeError:
        raise TypeError('Dictionary or callable expected but got: {0}'.format(val))

  @property
  def parent(self):
    p = getattr(self._view, 'crumb_parent', None)
    if p is None:
      return None
    else:
      v = CrumbedView.get_view_info(p, self._parent_args, self._parent_kwargs)
      return CrumbedView(p, *v)

  @property
  def url(self):
    return self._url


  def as_dict(self):
    return {'text': self.text, 'url': self.url}

  def _helper_call(self, val):
    if callable(val):
      try:
        return val(*self._args, **self._kwargs)
      except TypeError as e:
        raise ValueError(e)
    else:
      raise TypeError("Callable expected")


  @staticmethod
  def get_view_info(view, pattern_args=[], pattern_kwargs={}):
    '''Resolves pattern args to view args.

    This trick is needed because the view (and provided function) doesn't necessary _expect to get_
    the same arguments as given to url pattern.
    '''
    url = reverse(view, args=pattern_args, kwargs=pattern_kwargs)
    match = resolve(url)
    return (url, match.args, match.kwargs)
