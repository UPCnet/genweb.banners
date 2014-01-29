# -*- coding: utf-8 -*-
import logging


# define here the methods needed to be run at install time


def importVarious(context):
    if context.readDataFile('genweb.banners_various.txt') is None:
        return
    logger = logging.getLogger('genweb.banners')

    # add here your custom methods that need to be run when
    # genweb.banners is installed
