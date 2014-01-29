# -*- coding: utf-8 -*-
import doctest
from plone.app.testing import (
    applyProfile,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.app.testing.layers import (
    FunctionalTesting,
    IntegrationTesting,
)
from Products.CMFCore.utils import getToolByName
from zope.configuration import xmlconfig


class GenwebBannersTesting(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # load ZCML
        import genweb.banners
        xmlconfig.file('configure.zcml', genweb.banners,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        # install into the Plone site
        applyProfile(portal, 'genweb.banners:default')


GENWEBEXTRAS_FIXTURE = GenwebBannersTesting()
GENWEBEXTRAS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GENWEBEXTRAS_FIXTURE, ),
    name='GenwebBannersLayer:Integration'
)
GENWEBEXTRAS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GENWEBEXTRAS_FIXTURE, ),
    name='GenwebBannersLayer:Functional'
)

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
