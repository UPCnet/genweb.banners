# -*- coding: utf-8 -*-
from zope.i18nmessageid import MessageFactory

import random

from zope.interface import implements
from zope.component import getUtility
from zope.component import getMultiAdapter
from zope.component import getAdapter

from Products.CMFCore.utils import getToolByName

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema

from plone.memoize.instance import memoize

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.i18n.normalizer.interfaces import IIDNormalizer

from plone.portlet.collection import PloneMessageFactory as _

from plone.formwidget.querystring.widget import QueryStringFieldWidget

from z3c.form import field

from plone.app.portlets.browser import z3cformhelper

from plone.app.querystring.querybuilder import QueryBuilder
from genweb.banners.renderers.interfaces import IPortletItemRenderer
import sys
from Acquisition import aq_parent, aq_inner
from plone.app.collection.interfaces import ICollection


DOMAIN = u'genweb.banners'
_ = MessageFactory(DOMAIN)


class IBanners(IPortletDataProvider):
    """A portlet which renders the results of a collection object.
    """

    header = schema.TextLine(
        title=_(u"Portlet header"),
        description=_(u"Title of the rendered portlet"),
        required=True)

    query = schema.List(
        title=_(u'label_query', default=u'Search terms'),
        description=_(u"""Define the search terms for the items you want to
            list by choosing what to match on.
            The list of results will be dynamically updated"""),
        value_type=schema.Dict(value_type=schema.Field(),
                               key_type=schema.TextLine()),
        required=False
    )

    sort_on = schema.TextLine(
        title=_(u'label_sort_on', default=u'Sort on'),
        description=_(u"Sort the collection on this index"),
        required=False,
    )

    sort_reversed = schema.Bool(
        title=_(u'label_sort_reversed', default=u'Reversed order'),
        description=_(u'Sort the results in reversed order'),
        required=False,
    )

    limit = schema.Int(
        title=_(u"Limit"),
        description=_(u"Specify the maximum number of items to show in the "
                      u"portlet. Leave this blank to show all items."),
        required=False)

    random = schema.Bool(
        title=_(u"Select random items"),
        description=_(u"If enabled, items will be selected randomly from the "
                      u"collection, rather than based on its sort order."),
        required=True,
        default=False)

    more = schema.TextLine(
        title=_(u"Show more link"),
        description=_(u"Link to display in the footer, leave empty to hide it"),
        required=True)


class Assignment(base.Assignment):
    """
    Portlet assignment.
    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IBanners)

    header = u""
    query = None
    limit = None
    random = False

    def __init__(self, header=u"", sort_on="effective", sort_reversed="False", query=None, limit=None, random=False, more=u""):
        self.header = header
        self.sort_on = sort_on
        self.sort_reversed = sort_reversed
        self.limit = limit
        self.query = query
        self.random = random
        self.more = u""

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen. Here, we use the title that the user gave.
        """
        return self.header


class Renderer(base.Renderer):

    _template = ViewPageTemplateFile('templates/banners.pt')
    render = _template

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        self.plone_view = getMultiAdapter((self.context, self.request), name='plone')
        self.ptypes = getToolByName(self.context, 'portal_types')

    @property
    def available(self):
        return True
        return len(self.results())

    def css_class(self):
        header = self.data.header
        normalizer = getUtility(IIDNormalizer)
        return "portlet-smart-%s" % normalizer.normalize(header)

    def results(self):
        if self.data.random:
            return self._random_results()
        else:
            return self._standard_results()

    def renderItem(self, item):
        args = dict(
            item=item,
            toLocalizedTime=self.plone_view.toLocalizedTime,
            cropText=self.plone_view.cropText)
        fti = self.ptypes.getTypeInfo(item.PortalType())
        module = fti.klass[:fti.klass.rfind('.')]
        klass = fti.klass[fti.klass.rfind('.') + 1:]
        dummy = getattr(sys.modules[module], klass)
        renderer = getAdapter(dummy(object), IPortletItemRenderer)
        return renderer(self, **args)

    def queryCatalog(self, limit):
        """
        """
        querybuilder = QueryBuilder(self, self.request)
        if not hasattr(self.data, 'sort_on'):
            self.data.sort_on = 'effective'
        if not hasattr(self.data, 'sort_reversed'):
            self.data.sort_reversed = False

        sort_order = 'descending' if self.data.sort_reversed else 'ascending'
        sort_on = self.data.sort_on

        query = list(self.data.query)

        if ICollection.providedBy(self.context):
            query += self.context.query and self.context.query or []
            parent = aq_parent(aq_inner(self.context))
            if ICollection.providedBy(parent):
                query += parent.query and parent.query or []
        return querybuilder(query=query,
                            sort_on=sort_on,
                            sort_order=sort_order,
                            limit=limit)

    def _standard_results(self):
        results = []
        limit = self.data.limit
        if self.data.query:
            results = self.queryCatalog(limit=limit)
            if limit and limit > 0:
                results = results[:limit]
        return results

    def _random_results(self):
        # intentionally non-memoized
        results = []
        if self.data.query:
            results = self.queryCatalog()
            results = random.sample(results, self.data.limit)
        return results


class AddForm(z3cformhelper.AddForm):

    fields = field.Fields(IBanners)
    fields['query'].widgetFactory = QueryStringFieldWidget

    label = _(u"Add Query Portlet")
    description = _(u"This portlet displays a listing of items from a "
                    u"Collection.")

    def create(self, data):
        return Assignment(**data)


class EditForm(z3cformhelper.EditForm):

    fields = field.Fields(IBanners)
    fields['query'].widgetFactory = QueryStringFieldWidget

    label = _(u"Edit Collection Portlet")
    description = _(u"This portlet displays a listing of items from a "
                    u"Collection.")
