SublimeLinter-contrib-makensis
================================

[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![Package Control](https://packagecontrol.herokuapp.com/downloads/SublimeLinter-contrib-makensis.svg?style=flat-square)](https://packagecontrol.io/packages/SublimeLinter-contrib-makensis)
[![GitHub](https://img.shields.io/github/release/idleberg/SublimeLinter-contrib-makensis.svg?style=flat-square)](https://github.com/idleberg/SublimeLinter-contrib-makensis/releases)
[![Travis CI](https://img.shields.io/travis/idleberg/SublimeLinter-contrib-makensis/master.svg?style=flat-square)](https://travis-ci.org/idleberg/SublimeLinter-contrib-makensis)

This linter plugin for [SublimeLinter][docs] provides an interface to [makensis](http://nsis.sourceforge.net/Docs/Chapter3.html). It will be used with NSIS scripts.

![Screenshot](https://raw.githubusercontent.com/idleberg/SublimeLinter-contrib-makensis/master/screenshot.png)

*Linter in action (using [Hopscotch](https://github.com/idleberg/Hopscotch) color scheme)*

## Installation

SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that NSIS v3.02.1 (or higher) is installed on your system. To install it, do the following:

#### Windows

Download the NSIS installer from [SourceForge](https://sourceforge.net/p/nsis) and run setup. Make sure `makensis` is in your [PATH environmental variable][path].

Alternatively, you can install NSIS through [Chocolatey](https://chocolatey.org/packages/nsis):

``` bash
choco install nsis
```

#### Linux

Install NSIS from your distribution's default package manager, for example:

``` bash
# Debian
sudo apt-get install nsis

# Red Hat
sudo dnf install nsis
```

#### macOS

Install NSIS using [Homebrew](http://brew.sh/) or [MacPorts](https://www.macports.org/):

``` bash
# Homebrew
brew install nsis

# MacPorts
port install nsis
```

**Note:** As of v3.02.1, the macOS builds should use the correct version string rather than build date

### Linter Configuration

In order for `makensis` to be executed by SublimeLinter, you must [ensure that its path is available][path] to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `makensis`, you can proceed to install the SublimeLinter-contrib-makensis plugin if it is not yet installed.

### Plugin Installation

Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `makensis`. Among the entries you should see `SublimeLinter-contrib-makensis`. If that entry is not highlighted, use the keyboard or mouse to select it.

### Plugin Configuration

To configure this plugin, bring up the [Command Palette][cmd] and type `Preferences: SublimeLinter Settings`. The following options are available:

Option   | Default | Description 
---------|---------|------------
`ppo`    | `true`  | Lints much faster, but ignores warning (equivalent of `-PPO` flag)
`strict` | `false` | Treats warnings as errors (equivalent of `-WX` flag)

**Example:**

```json
"user": {
    "linters": {
        "makensis": {
            "ppo_mode": true,
            "safe_mode": false
        }
    }
}
```

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
[path]: http://superuser.com/a/284351/195953
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
