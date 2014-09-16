# -*- coding: utf-8 -*-
from plone.app.textfield import RichText as RichTextField
from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from genweb.banners import _
from zope import schema


class IBanner(form.Schema):
    """ A site banner.
    """

    picture = NamedBlobImage(
        title=_(u"Picture"),
        description=_(u"Please upload an image"),
        required=False,
    )

    description = RichTextField(
        title=_(u"Description"),
        description=_(u"Rich Text to use along with the banner"),
        required=False
    )

    url = schema.TextLine(
        title=_(u"url"),
        description=_(u"URL to open"),
        required=False,
    )

    new_window = schema.Bool(
        title=_(u"Open in new window"),
        description=_(u"Check it to open link in a new window"),
        default=True,
        required=False,
    )
