# REQUIRED LIBRARIES
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

# MAIN WINDOW CLASS


class MainWindow(QMainWindow):

    # CONSTRUCTOR
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # QWEBENGINEVIEW BEING CREATED
        self.browser = QWebEngineView()

        # DEFAULT SEARCH ENGINE GOOGLE
        self.browser.setUrl(QUrl("http://google.com"))

        # ACTION FOR URL CHANGE
        self.browser.urlChanged.connect(self.update_urlbar)

        # URL FINISHED LOADING
        self.browser.loadFinished.connect(self.update_title)

        # CENTRAL WIDGET & MAIN WINDOW
        self.setCentralWidget(self.browser)

        # STATUS BAR
        self.status = QStatusBar()

        # STATUS BAR TO MAIN WINDOW
        self.setStatusBar(self.status)

        # QTOOLBAR FOR NAVIGATION
        navtb = QToolBar("Navigation")

        # TOOL BAR TO MAIN WINDOW
        self.addToolBar(navtb)

        # ACTIONS ON TOOLBAR
        # ACTION FOR BACK
        back_btn = QAction("Back", self)

        # STATUS SETTING
        back_btn.setStatusTip("Back to previous page")

        # ACTION FOR BACK BUTTON
        # BROWSER GOES BACK
        back_btn.triggered.connect(self.browser.back)

        # ACTION ADDED TO TOOLBAR
        navtb.addAction(back_btn)

        # FOR FORWARD ACTION
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")

        # ACTION FOR NEXT BUTTON
        # BROWSER GOES FORWARD
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        # FOR RELOAD ACTION
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")

        # ACTION FOR RELOAD BUTTON
        # BROWSER RELOADS
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        # FOR HOME ACTION
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        # SEPARATOR FOR TOOLBAR
        navtb.addSeparator()

        # LINE EDIT FOR URL
        self.urlbar = QLineEdit()

        # ACTION FOR RETURN KEY
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # ADDING TO TOOLBAR
        navtb.addWidget(self.urlbar)

        # STOP ACTION TO TOOLBAR
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")

        # ACTION FOR STOP BUTTON
        # BROWSER STOPS
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # ALL COMPONENTS
        self.show()

    # UPDATE TITLE OF WINDOW
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - TRON BROWSER" % title)

    # METHOD BY HOME ACTION
    def navigate_home(self):

        # GOOGLE
        self.browser.setUrl(QUrl("http://www.google.com"))

    # LINE EDIT METHOD BY RETURN KEY
    def navigate_to_url(self):

        # URL IS CONVERTED TO QURL OBJECT
        q = QUrl(self.urlbar.text())

        # URL SCHEME BLANK
        if q.scheme() == "":
            # URL SCHEME TO HTML
            q.setScheme("http")

        # URL IS SET TO BROWSER
        self.browser.setUrl(q)

    # UPDATING URL
    # QWEBENGINEVIEW CALLS THE METHOD
    def update_urlbar(self, q):

        # TEXT FOR URL BAR
        self.urlbar.setText(q.toString())

        # CURSOR POSITION FOR URL BAR
        self.urlbar.setCursorPosition(0)


# PYQT5 APPLICATION
app = QApplication(sys.argv)

# APPLICATION NAME
app.setApplicationName("TRON BROWSER")

# MAIN WINDOW OBJECT
window = MainWindow()

# LOOP
app.exec_()
