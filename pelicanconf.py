#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from datetime import datetime

AUTHOR = 'Carlos E'
SITENAME = 'CE Blog'
#SITEURL = '/'
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Archive', '/archives'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/escrichov'),
    ('rss', '/feeds/all.atom.xml'),
)

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "pelican-themes/Flex"

STATIC_PATHS = ['images', 'extra']

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True


MENUITEMS = (
    ('Archives', '/archives'),
)

# Plugings
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['post_stats']
