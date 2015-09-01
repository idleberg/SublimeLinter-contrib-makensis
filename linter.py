#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jan T. Sott
# Copyright (c) 2015 Jan T. Sott
#
# https://github.com/idleberg/SublimeLinter-contrib-makensis
#
# License: MIT
#

"""This module exports the Makensis plugin class."""

from SublimeLinter.lint import Linter, util
from sys import platform as _platform

class Makensis(Linter):

    """Provides an interface to makensis."""

    if _platform == "win32":
        syntax = 'nsis'
        cmd = ('makensis', '@', '-X!error END_OF_LINTING')
        version_args = '-VERSION'
        version_re = r'(?P<version>\d+\.\d+)'
        version_requirement = '>= 2.46'
    elif _platform == "darwin":
        syntax = 'nsis'
        cmd = ('makensis', '@', '-X!error END_OF_LINTING')
        version_args = '-VERSION'
        # version_re = r'(?P<version>\d+\.\d+)'
        # version_re = 'v12-Mar-2015.cvs~'
        # version_requirement = '>= 2.46'

    regex = (

        r'^(Error in script\:? \"(.+?)\" on line (?P<line>\d+) -- aborting creating process)'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
