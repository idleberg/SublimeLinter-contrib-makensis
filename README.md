SublimeLinter-contrib-makensis
================================

[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![Travis CI](https://img.shields.io/travis/idleberg/SublimeLinter-contrib-makensis/master.svg?style=flat-square)](https://travis-ci.org/idleberg/SublimeLinter-contrib-makensis)

This linter plugin for [SublimeLinter][docs] provides an interface to [makensis](http://nsis.sourceforge.net/Docs/Chapter3.html). It will be used with NSIS scripts.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `makensis` is installed on your system. To install `makensis`, do the following:

#### Windows

Download NSIS 2.46 (or later) from [SourceForge](https://sourceforge.net/p/nsis) and run setup

#### Linux

Install `makensis` from your distribution's default package manager, for example:

   ``` bash
   # Debian
   sudo apt-get install nsis

   # Red Hat
   sudo yum install nsis
   ```

#### Mac OS X

Install `makensis` through [Homebrew](http://brew.sh/) or [MacPorts](https://www.macports.org/)

   ``` bash
   # Homebrew
   brew install makensis

   # MacPorts
   ports install nsis
   ```

**Note:** This plugin requires `makensis` 2.46 or later.

### Linter configuration
In order for `makensis` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `makensis`, you can proceed to install the SublimeLinter-contrib-makensis plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `makensis`. Among the entries you should see `SublimeLinter-contrib-makensis`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
