# -*- coding: utf-8 -*-

def crumb(text, parent=None, parent_args=[], parent_kwargs={}):
  '''Marks view as crumbed (add information for vreadcrumbs construction.

  parent, parent_args and parent_kwargs will be given directly to
  django.core.urlresolvers.reverse so see documentation for restrictions
  (e.g. do not mix args and kwargs within single call).

  text can be a string or a callback which will be called with exactly
  the same arguments as its correspnding view (except for request).
  The same applies to parent_args and parent_kwargs which can be
  list and dict respectively or callbacks.
  '''
  def _crumbed(view):
    view.crumb_text = text
    view.crumb_parent = parent
    view.crumb_p_args = parent_args
    view.crumb_p_kwargs = parent_kwargs
    return view
  return _crumbed
