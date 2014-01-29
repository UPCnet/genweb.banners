from zope.component.hooks import getSite
from zope.interface import implements

from plone.dexterity.content import Item
from Products.CMFCore.utils import getToolByName

from genweb.banners.content.banner import IBanner


class Banner(Item):
    implements(IBanner)


