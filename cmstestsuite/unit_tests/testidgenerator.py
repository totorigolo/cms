#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Contest Management System - http://cms-dev.github.io/
# Copyright © 2015-2016 Stefano Maggiolo <s.maggiolo@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Utilities to generate "unique" test ids."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future.builtins.disabled import *
from future.builtins import *

import hashlib
import random

from cmscommon.binary import bin_to_hex


def unique_long_id():
    """Return a unique id of type long."""
    if not hasattr(unique_long_id, "id"):
        unique_long_id.id = random.randint(0, 1000000000)
    unique_long_id.id += 1
    return unique_long_id.id


def unique_unicode_id():
    """Return a unique id of type unicode."""
    return str(unique_long_id())


def unique_digest():
    """Return a unique digest-like string."""
    hasher = hashlib.sha1()
    hasher.update(str(unique_long_id()).encode('ascii'))
    return bin_to_hex(hasher.digest())
