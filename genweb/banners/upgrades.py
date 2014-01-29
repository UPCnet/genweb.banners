# -*- coding: utf-8 -*-
import logging

from Products.CMFCore.utils import getToolByName


PROFILE_ID = 'profile-genweb.banners:default'
LOGGER = 'genweb.banners'


def update_rolemap_tool(context, logger=None):
    if logger is None:
        logger = logging.getLogger(LOGGER)
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'rolemap')
