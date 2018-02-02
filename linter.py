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


class Makensis(Linter):

    """Provides an interface to the makensis executable."""

    cmd = None
    version_args = '-VERSION'
    version_re = r'(?P<version>\d+\.\d+(\.\d+)?)'
    version_requirement = '>= 3.02.1'

    syntax = 'nsis'
    regex = (
        r'((?P<warning>warning): (?P<warnMessage>.*) \(.*:(?P<warnLine>\d+)\)'
        r'|(?P<message>[^\r?\n]+)\r?\n(?P<error>Error) in script "[^"]+" on line (?P<line>\d+) -- aborting creation process)'
    )
    multiline = True
    error_stream = util.STREAM_BOTH
    line_col_base = (1, 1)

    def cmd(self):
        """Create the command"""
        settings = Linter.get_view_settings(self)

        # Default arguments
        cmd = ['makensis', '-V2']

        # Is strict mode?
        if settings.get('strict_mode') is True:
            cmd.append('-WX')

        # Is PPO mode?
        if settings.get('ppo_mode') in [True, None]:
            cmd.append('-PPO')
            cmd.append('@')
        else:
            cmd.append('@')
            cmd.append('-X!error "Abort linting"')

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
        if settings.get('strict_mode') is True:
            error = warning

        warnMessage = str(match.groupdict()["warnMessage"])
        warnLine = match.groupdict()["warnLine"]

        if warnMessage and warnLine:
            message = warnMessage
            line = int(warnLine) - 1

        return match, line, col, error, warning, message, near
