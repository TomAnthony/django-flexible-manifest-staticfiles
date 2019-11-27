import os
import re

from collections import OrderedDict

from django.conf import settings
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from django.contrib.staticfiles.utils import matches_patterns
from django.core.files.base import ContentFile

class FlexibleManifestStaticFilesStorage(ManifestStaticFilesStorage):

    whitelisted_patterns = getattr(settings, "STATICFILES_VERSIONED_INCLUDE", ['.*'])
    blacklisted_patterns = getattr(settings, "STATICFILES_VERSIONED_EXCLUDE", [])

    def _post_process(self, paths, adjustable_paths, hashed_files):

        filtered_paths = OrderedDict()

        for name, val in paths.items():
            if any(re.search(wp, name) for wp in self.whitelisted_patterns):
                if not any(re.search(wp, name) for wp in self.blacklisted_patterns):
                    filtered_paths[name] = val
        
        return super()._post_process(filtered_paths, adjustable_paths, hashed_files)