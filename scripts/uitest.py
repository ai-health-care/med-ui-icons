#!/usr/bin/env python3
import os
import sys


from PySide2 import QtGui, QtWidgets
try:
    from qt_material import apply_stylesheet
except ImportError:
    try:
        from pyside_material import apply_stylesheet
    except ImportError:
        def apply_stylesheet(app, theme):
            print('Could not apply stylesheet')

def icon(icon):
    base = os.path.dirname(__file__)
    path = os.path.join(base, '..', 'svg-white', icon + '.svg')
    return QtGui.QIcon(path)



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
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
            action = QtWidgets.QAction(icon(ico), ico.title(), self)
            toolbar.addAction(action)
        self.addToolBar(toolbar)


def main():
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
