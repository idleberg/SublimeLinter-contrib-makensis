# SublimeLinter-contrib-makensis

[![The MIT License](https://flat.badgen.net/badge/license/MIT/blue)](https://opensource.org/licenses/MIT)
[![Package Control](https://packagecontrol.herokuapp.com/downloads/SublimeLinter-contrib-makensis.svg?style=flat-square)](https://packagecontrol.io/packages/SublimeLinter-contrib-makensis)
[![GitHub](https://flat.badgen.net/github/release/idleberg/SublimeLinter-contrib-makensis)](https://github.com/idleberg/SublimeLinter-contrib-makensis/releases)
[![CircleCI](https://flat.badgen.net/circleci/github/idleberg/generator-atom-package-coffeescript)](https://circleci.com/gh/idleberg/SublimeLinter-contrib-makensis)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [makensis](http://nsis.sourceforge.net/Docs/Chapter3.html). It will be used with NSIS scripts.

## Prerequisites

Before using this plugin, you must ensure that NSIS v3.02.1 (or higher) is installed on your system.

#### Windows

Download the NSIS installer from [SourceForge](https://sourceforge.net/p/nsis) and run setup. Once completed, you need to add the installation folder to your [environmental variable](http://superuser.com/a/284351/195953) manually.

Alternatively, you can install NSIS using the [Scoop](https://github.com/NSIS-Dev/scoop-nsis) package manager:

```sh
$ scoop install nsis/nsis
```

#### Linux

Install NSIS from your distribution's default package manager, for example:

``` bash
# Debian
sudo apt-get -t experimental install nsis

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

## Installation

### Package Control

1. Make sure you have [Package Control](https://packagecontrol.io/) installed
2. Choose *“Install Package”* from the Command Palette (<kbd>Super</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd>)
3. Type *“SublimeLinter-contrib-makensis”* and press <kbd>Enter</kbd>

With the [`auto_upgrade`](https://packagecontrol.io/docs/settings#setting-auto_upgrade) setting enabled, Package Control will keep all installed packages up-to-date!

### Using Git

1. Change to your Sublime Text `Packages` directory
2. Clone repository `git clone https://github.com/idleberg/SublimeLinter-contrib-makensis.git SublimeLinter-contrib-makensis`

## Settings

Please refer to the official documentation in order to tweak the [SublimeLinter settings](http://sublimelinter.readthedocs.org/en/latest/settings.html) or [linter settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

### Plugin Settings

To configure this plugin, bring up the [Command Palette][cmd] and type `Preferences: SublimeLinter Settings`. The following options are available:

Option   | Default | Description
---------|---------|------------
`ppo`    | `true`  | Lints much faster, but ignores warning (equivalent of `-PPO` flag)
`strict` | `false` | Treats warnings as errors (equivalent of `-WX` flag)

**Example:**

```json
{
  "linters": {
    "makensis": {
      "@disable": false,
      "args": [],
      "excludes": [],
      "ppo": true,
      "strict": false
    }
  }
}
```

## License

This work is licensed under the [The MIT License](LICENSE)
