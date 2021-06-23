# Medical UI Icons

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

SVG icons dedicated for user interfaces in medical software tools.

![](svg-white/icon-asclepius.svg)
![](svg-white/action-save.svg)
![](svg-white/tool-bezier.svg)
![](svg-white/arrow-up.svg)
![](svg-white/icon-cross.svg)
![](svg-white/organ-lung.svg)

![](svg-dark/icon-asclepius.svg)
![](svg-dark/action-save.svg)
![](svg-dark/tool-bezier.svg)
![](svg-dark/arrow-up.svg)
![](svg-dark/icon-cross.svg)
![](svg-dark/organ-lung.svg)

Directory *svg-dark* contains dark icons for use in light UI themes, whereas
*svg-white* contains white icons for use in dark UI themes.

License: [CC-BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0).
Please give credit to our contributors.

## Usage

Add this repo as a clone (or submodule) to your project:

```bash
git clone https://github.com/ai-health-care/med-ui-icons
```

For Python3 + PySide2 applications, you can use this code snippet to load
individual icon files as SVGs:

```python
import os

from PySide2 import QtGui

def icon(icon):
    base = os.path.dirname(__file__)
    path = os.path.join(base, '..', 'med-ui-icons', 'svg-dark', icon + '.svg')
    return QtGui.QIcon(path)
```

You may want to change the icon path (variable *path*).
Please take a look at *uitest.py* in the *scripts* directory for inspiration.


## Contributing

### Generating PNGs

[Inkscape](https://inkscape.org) needs to be installed to batch-convert
all icons (both white & dark) to PNGs.

```bash
./scripts/generate-png.sh
```

should be sufficient for batch conversion on Unix systems with inkscape
installed.
Please note that PNG files are blacklisted in gitignore and will thus not
appear in the repo.


## Contributors

* Henry Krumb, Medical Computing group, TU Darmstadt
