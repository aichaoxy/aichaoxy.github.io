AUTHOR = 'aichaoxy'
SITENAME = "aichaoxy's blog"
SITEURL = "https://aichaoxy.github.io"
SITETITLE = "aichaoxy's blog"
SITESUBTITLE = "Software Development"
SITEDESCRIPTION = "aichaoxy's Thoughts and Writings"
SITELOGO = SITEURL + "/theme/img/profile.png"
FAVICON = SITEURL + "/theme/img/favicon.ico"

BROWSER_COLOR = "#333"
ROBOTS = "index, follow"

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}

COPYRIGHT_YEAR = 2024

STATIC_PATHS = ["extra/custom.css"]

EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
}

CUSTOM_CSS = "static/custom.css"

MAIN_MENU = True
USE_FOLDER_AS_CATEGORY = False
HOME_HIDE_TAGS = True

# ADD_THIS_ID = "ra-77hh6723hhjd"
DISQUS_SITENAME = "aichaoxys-blog"
GOOGLE_ANALYTICS = "G-JBY072ENWC"
GOOGLE_TAG_MANAGER = "GTM-P9HV32H"

# Enable i18n plugin.
# PLUGINS = ["i18n_subsites"]
PLUGIN_PATHS = ["plugins"]
PLUGINS = []

# Enable Jinja2 i18n extension used to parse translations.
# JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# Translate to German.
DEFAULT_LANG = "zh"
OG_LOCALE = "zh_CN"
LOCALE = "zh_CN"

# Default theme language.
I18N_TEMPLATES_LANG = "en"

# Pelican-search Configuration
STORK_INPUT_OPTIONS = {"stemming": "Chinese", "url_prefix": SITEURL}

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
)

# Social widget
SOCIAL = (
    ("github", "https://github.com/aichaoxy"),
    ("rss", "/feeds/all.atom.xml"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/Flex"