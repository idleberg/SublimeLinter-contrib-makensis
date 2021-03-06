#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jan T. Sott
# Copyright (c) 2016-2018 Jan T. Sott
#
# https://github.com/idleberg/SublimeLinter-contrib-makensis
#
# License: MIT
#


"""This module exports the Makensis plugin class."""

from SublimeLinter.lint import Linter, util
from sys import platform


class Makensis(Linter):

    """Provides an interface to the makensis executable."""

    cmd = None
    executable = 'makensis'
    defaults = {
        'selector': 'source.nsis'
    }
    version_args = '-VERSION'
    version_re = r'(?P<version>\d+\.\d+(\.\d+)?)'
    version_requirement = '>= 3.02.1'
    regex = (
        r'((?P<warning>warning): (?P<warnMessage>.*) \(.*:(?P<warnLine>\d+)\)'
        r'|(?P<message>[^\r?\n]+)\r?\n(?P<error>Error) in script "[^"]+" on line (?P<line>\d+) -- aborting creation process)'
    )
    multiline = True
    error_stream = util.STREAM_BOTH
    line_col_base = (1, 1)

    def cmd(self):
        """Create the command."""
        settings = Linter.get_view_settings(self)

        # Default arguments
        cmd = ['makensis']

        linter_args = settings.get('args') or []
        strict = settings.get('strict') or False
        preprocess_mode = settings.get('preprocess_mode')
        preprocess_mode = "-{}".format(preprocess_mode) if str(preprocess_mode).upper() in ('PPO', 'SAFEPPO') else False

        cmd = cmd + linter_args

        # Set verbosity
        verbose_flags = ['-V0', '-V1', '-V2', '-V4', '-V4', '/V0', '/V1', '/V2', '/V4', '/V4']
        if not any(x in cmd for x in verbose_flags):
            cmd.append('-V2')

        # Is strict mode?
        strict_flags = ['-WX', '/WX']
        if strict and not any(x in cmd for x in strict_flags):
            cmd.append('-WX')

        # Is PPO mode?
        ppo_flags = ['-PPO', '-SAFEPPO', '/PPO', '/SAFEPPO']
        if preprocess_mode and any(x in preprocess_mode for x in ppo_flags):
            cmd.append(preprocess_mode)
            cmd.append("${file}")
        else:
            cmd.append("${file}")

            # Don't write installer
            if platform == 'win32':
                out_file = 'OutFile NUL'
            else:
                out_file = 'OutFile /dev/null/'

            cmd.append('-X' + out_file)

        return cmd

    def split_match(self, match):
        """Extract and return values from match."""
        match, line, col, error, warning, message, near = (
            super().split_match(match)
        )

        if message:
            return match, line, col, error, warning, message, near

        # Is strict mode?
        settings = Linter.get_view_settings(self)
        if settings.get('strict') is True:
            error = warning

        warnMessage = str(match.groupdict()["warnMessage"])
        warnLine = match.groupdict()["warnLine"]

        if warnMessage and warnLine:
            message = warnMessage
            line = int(warnLine) - 1

        return match, line, col, error, warning, message, near
