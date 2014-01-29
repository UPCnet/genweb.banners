# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.directives import form
from plone.namedfile.field import NamedImage
from webupcnet.core import _
from zope import schema


class IBanner(form.Schema):
    """ A company's service
    """

    title = schema.TextLine(
        title=_(u'label_title', default=u'Title'),
        required=True
    )

    picture = NamedImage(
        title=_(u"Picture"),
        description=_(u"Please upload an image"),
        required=False,
    )

    description = RichText(
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

# @indexer(ICommunity)
# def imageFilename(context):
#     """Create a catalogue indexer, registered as an adapter, which can
#     populate the ``context.filename`` value and index it.
#     """
#     return context.image.filename
# grok.global_adapter(imageFilename, name='image_filename')



