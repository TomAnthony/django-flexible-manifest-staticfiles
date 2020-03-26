import os
import re

from collections import OrderedDict
from urllib.parse import unquote, urlsplit, urlunsplit

from django.conf import settings
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from django.contrib.staticfiles.utils import matches_patterns
from django.core.files.base import ContentFile

class FlexibleManifestStaticFilesStorage(ManifestStaticFilesStorage):

    whitelisted_patterns = getattr(settings, "STATICFILES_VERSIONED_INCLUDE", ['.*'])
    blacklisted_patterns = getattr(settings, "STATICFILES_VERSIONED_EXCLUDE", [])

    def hashed_name(self, name, content=None, filename=None):

        if any(re.search(wp, name) for wp in self.whitelisted_patterns):
            if not any(re.search(bp, name) for bp in self.blacklisted_patterns):

                return super().hashed_name(name, content, filename)

        return name

