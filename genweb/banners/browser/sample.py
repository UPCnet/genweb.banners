# -*- coding: utf-8 -*-
from five import grok
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import IPloneSiteRoot

from genweb.banners import DOMAIN


#class View(grok.View):
#    grok.context(IPloneSiteRoot)
#    grok.require('zope2.View')
#    grok.name('sample-view')
#
#    def get_types(self):
#        catalog_tool = getToolByName(self.context, 'portal_catalog')
#        types_tool = getToolByName(self.context, 'portal_types')
#
#        results = []
#
#        content_types = types_tool.listContentTypes()
#        # filter out Archetypes content types
#        content_types = [t for t in content_types if not t.startswith('AT')]
#
#        for ct in content_types:
#            qtt = len(catalog_tool(portal_type=ct))
#            if qtt > 0:
#                results.append({'type': ct, 'qtt': qtt, })
#
#        return results
