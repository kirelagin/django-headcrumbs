django-headcrumbs
==================

[Breadcrumbs][1] for [Django][2] that are not going to eat your brains!

What's that?
-------------

Breadcrumbs let users visiting your website see where exactly they are now
and how to get back. That's something like “Back” button but
even more powerfull. Anyway, I suppose you came here because you are
looking for breadcrumbs and you know why you need it.

Why did I start a new project? Well the answer is rather obvious:
I needed breadcrumbs and couldn't find a good enough solution
(see bottom of this file).

How to use
-----------

### Installation ###
1. `git clone git://github.com/kirelagin/django-headcrumbs.git`.
2. Copy (or, even better, symlink) `headcrumbs` directory to your Django project.
3. Add `'headcrumbs.middleware.CrumbsMiddleware'` to `MIDDLEWARE_CLASSES`
   in your `settings.py`.
4. _(Optional)_ Add `'headcrumbs'` to `INSTALLED_APPS` variable in your
  `settings.py`. It will be handy if you are going to use included template
  (see “Crumbs output” below).

### Defining crumbs ###
I'm one of those strange people who believe that for each _view_ you can say
which one came before it. Imagine you are on a website and you are somewhere
in `Stuff > Managers > John > more`. Well, thanks to the trail left by
the developer, you know that you are reading detailed bio of a manager
whose name is John. It means that `detailed` view structurally comes after
`person` view, which in turn comes after `division` view and so on.

You'll be using `headcrumbs.decorators.crumb` decorator to describe this kind
of relations between views.

**views.py**:

```python
from headcrumbs.decorators import crumb
from headcrumbs.util import name_from_pk

@crumb('Stuff') # This is the root crumb -- it doesn't have a parent
def index(request):
    # In our example you'll fetch the list of divisions (from a database)
    # and output it.

@crumb(name_from_pk(Category), parent=index)
def division(request, slug):
    # Here you find all employees from the given division
    # and list them.
```

The second node in our example path is “Managers” which is the name
of a division. It is something dynamic and can be determined only from
the path we followed (e.g. from the employee whose profile we are viewing).
That's why you see a helper function `headcrumbs.util.name_from_pk` there.

Now when, I hope, you got _The General Idea_ you'll want to look at the
[Full example](http://github.com/kirelagin/django-headcrumbs/wiki/Full-example).
I advise you also to read docstrings, as they are
really useful (at least I tried to make them useful).

### Crumbs output ###
You have defined your website structure. Time to output
that navigation bar with breadcrumbs! It's going to be easy.
Thanks to our cool middleware you get `crumbs` variable in your templates.
It's a list of dictionaries with `'text'` and `'url'` records each. Just
iterate over it and you get your path! For your convenience there is a
`crumbs.html` template included. It will output something like this:

```html
<ul class="nav">
    <li><a href="/">Stuff</a></li>
    <li><a href="/divisions/managers/">Managers</a></li>
    <li><a href="/people/3/">John</a></li>
</ul>
```

Just style it properly and you get a pretty breadcrumbs bar. For example:

```css
ul.nav {
    display: inline;
    padding-left: 0px;
}

ul.nav li {
    list-style-type: none;
    display: inline;
}

ul.nav li:before {
    content: "> ";
}

ul.nav li:first-child:before {
    content: none;
}
```

And you get something like this:

![Resulting breadcrumbs example](http://kirelagin.ru/~kirrun/headcrumbs/bar.png)


Appendix A. About the name
---------------------------

Ok, I admit, I'm not very good at thinking up  names for projects.  
But it seems to me that *headcrumbs* sounds at least funny =).

Appendix B. Other options
--------------------------

*   [`django-crumbs`][3] defines crumbs in templates which seems weird to me.
    Because, you know, templates are **templates**. They are used for different
    kind of things.
*   [`django-breadcrumbs`][4] is strange. Its `request.breadcrumbs` object does lots of things,
    but doesn't do anything to help you in dealing with breadcrumbs. Maybe I just didn't get
    something.
*   [`django-simplecrumbs`][5] is nearly perfect. Really. But in my opinion it's a bit… hm…
    messy. Both in its interface and in source code.

[1]: http://en.wikipedia.org/wiki/Breadcrumb_%28navigation%29
[2]: http://www.djangoproject.com/
[3]: http://code.google.com/p/django-crumbs/
[4]: http://github.com/chronossc/django-breadcrumbs/
[5]: http://bitbucket.org/anti_social/django-simplecrumbs
