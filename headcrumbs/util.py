# -*- coding: utf-8 -*-

def name_from_pk(model, transform=None):
  '''Gets a text representation for an object from its primary key.

  Returns a function which takes one of its arguments (hopefully the first one)
  lookups an instance of model with this primary key and returns its unicode
  representation.
  Oprionally applies given transformation before returning a value.
  '''
  def _f(*args, **kwargs):
    args = list(args) + kwargs.values()
    pk = args[0]
    text = unicode(model.objects.get(pk=pk))
    return transform(text) if transform else text
  return _f
