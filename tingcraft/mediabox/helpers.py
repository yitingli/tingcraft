import hashlib
from datetime import datetime
from os import path
from random import randint

from django.conf import settings
from django.utils.encoding import smart_str


def tokey(*args):
    """
    Computes a (hopefully) unique key from arguments given.
    Copied from sorl.thumbnail.helpers
    """
    salt = '||'.join([smart_str(arg) for arg in args])
    hash_ = hashlib.md5(salt)
    return hash_.hexdigest()


"""
def _get_thumbnail_filename(self, source, geometry_string, options):
        key = tokey(source.key, geometry_string, serialize(options))
        # make some subdirs
        path = '%s/%s/%s' % (key[:2], key[2:4], key)
        return '%s%s.%s' % (settings.THUMBNAIL_PREFIX, path,
                            EXTENSIONS[options['format']])
"""


def upload_filename(instance, filename):

    SECRET_KEY = 'Or3An6ge'
    _, extension = path.splitext(filename)
    fmt = "%Y%m%d%H%M%S%f"
    utc_now = datetime.utcnow().strftime(fmt)
    randnum = randint(10000, 99999)
    key = tokey(instance.owner.username, filename, utc_now, SECRET_KEY, str(randnum))
    return '%s/%s/%s/%s/%s%s' % (settings.IMAGE_PATH_PREFIX, key[:2], key[2:4], key[4:6], key, extension)
