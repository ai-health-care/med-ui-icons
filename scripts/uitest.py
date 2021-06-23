#!/usr/bin/env python3
import os
import sys

import click

from PySide2 import QtGui, QtWidgets
try:
    from qt_material import apply_stylesheet
except ImportError:
    try:
        from pyside_material import apply_stylesheet
    except ImportError:
        def apply_stylesheet(app, theme):
            print('Could not apply stylesheet')

def icon(icon, theme):
    base = os.path.dirname(__file__)
    path = os.path.join(base, '..', theme, icon + '.svg')
    return QtGui.QIcon(path)



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, theme):
        super().__init__()
        toolbar = QtWidgets.QToolBar()
        
        icons = [
            'icon-asclepius',
            'action-save',
            'tool-bezier',
            'arrow-up',
            'icon-cross'
        ]
        for ico in icons:
            action = QtWidgets.QAction(icon(ico, theme), ico.title(), self)
            toolbar.addAction(action)
        self.addToolBar(toolbar)


@click.command()
@click.option('--dark', '-d', is_flag=True)
def main(dark):
    app = QtWidgets.QApplication(sys.argv)
    if dark:
        apply_stylesheet(app, theme='dark_teal.xml')
        theme = 'svg-white'
    else:
        apply_stylesheet(app, theme='teal.xml')
        theme = 'svg-dark'

    window = MainWindow(theme)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
