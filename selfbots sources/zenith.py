import sys
import platform
import os
import io
import urllib
import contextlib
import logging
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QThread
from PySide2.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
from PySide2.QtWidgets import *
from requests import get, post
from zipfile import ZipFile
from shutil import copyfile, rmtree
from base64 import b64decode, b64encode
from UI.splash import Splash_Window
from UI.login import Login_Window
from UI.feedback import Feedback_Window
from classes.bot import Zenith
from cogs.utils.auth import get_HWID, get_device_name
from cogs.utils.endpoints import ZenithAPIEndpoints
from cogs.utils.fileStuff import resource_path
INCORRECT_STYLESHEET = 'background-color: rgb(44, 44, 44);\nborder: 1.5px solid rgb(255, 93, 68);\ncolor: rgb(255, 255, 255);\nborder-radius: 7px;'
CLIENT_INSTANCE = Zenith()
POSTED_FEEDBACK = True
logo = resource_path('logo.svg')
star = resource_path('star.png')
greystar = resource_path('star_grey.png')

class RemoveNoise(logging.Filter):
    __doc__ = 'Basically removes all useless errors'

    def __init__(self):
        super().__init__(name='discord.state')

    def filter(self, record):
        return record.levelname == 'WARNING' and 'referencing an unknown' in record.msg

def _login(key):
    #global POSTED_FEEDBACK
    #try:
    #    response = post(ZenithAPIEndpoints.ACCOUNT_LOGIN, json={'license_key': key, 'HWID': get_HWID(), 'device_name': get_device_name()})
    #    if response.status_code == 200:
    #        body = response.json()
    #        if body['body']['has_sent_feedback'] == False:
    #            POSTED_FEEDBACK = False
    #finally:
    #    pass
    return
@contextlib.contextmanager
def setup_logging():
    'Sets up all my logging stuffs'
    try:
        logging.getLogger('discord').setLevel(logging.INFO)
        logging.getLogger('discord.http').setLevel(logging.WARNING)
        logging.getLogger('discord.state').addFilter(RemoveNoise())
        logging.getLogger('aiohttp.client').setLevel(logging.INFO)
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='zenith.log', encoding='utf-8', mode='w')
        dt_fmt = '%Y-%m-%d %H:%M:%S'
        fmt = logging.Formatter('[{asctime}] [{levelname:<7}] {name}: {message}', dt_fmt, style='{')
        handler.setFormatter(fmt)
        log.addHandler(handler)
        yield None
    finally:
        handlers = log.handlers[:]
        for hdlr in handlers:
            hdlr.close()
            log.removeHandler(hdlr)

class MainwindowMixin(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowIcon(QIcon(logo))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

class FeedbackScreen(MainwindowMixin):

    def __init__(self):
        MainwindowMixin.__init__(self)
        self.ui = Feedback_Window()
        self.ui.setupUi(self)
        self.stars = []
        self.stars_active = True
        self.inputted_stars = 5
        self.ui.tick.hide()
        self.ui.confirmation_text.hide()
        self.ui.minimise_button.installEventFilter(self)
        self.ui.exit_button.installEventFilter(self)
        self.ui.submit_button.installEventFilter(self)
        for i in range(1, 6):
            star = getattr(self.ui, f'star_{i}')
            star.installEventFilter(self)
            self.stars.append(star)
        self.ui.minimise_button.clicked.connect(self.minimise)
        self.ui.exit_button.clicked.connect(self.close_window)
        self.ui.submit_button.clicked.connect(self.submit)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.drop_shadow.setGraphicsEffect(self.shadow)

    def submit(self):
        if len(self.ui.feedback_field.toPlainText().strip()) == 0:
            self.ui.feedback_field.setStyleSheet(INCORRECT_STYLESHEET)
            return
        try:
            response = post(ZenithAPIEndpoints.POST_FEEDBACK, json={'license_key': CLIENT_INSTANCE.license_key, 'feedback': self.ui.feedback_field.toPlainText().strip(), 'stars': self.inputted_stars})
            if response.status_code == 200:
                self.ui.feedback_field.hide()
                self.ui.submit_button.hide()
                self.ui.separator.hide()
                self.ui.main_label.hide()
                self.ui.info_label.hide()
                for star in self.stars:
                    star.hide()
                self.ui.tick.show()
                self.ui.confirmation_text.show()
            else:
                _translate = QCoreApplication.translate
                self.ui.confirmation_text.setText(_translate('MainWindow', '<strong>Failed to post your feedback</strong>'))
                self.ui.confirmation_text.show()
        finally:
            pass

    def minimise(self):
        self.showMinimized()

    def close_window(self):
        self.close()

    def animate_separator(self, state):
        self.anim = QPropertyAnimation(self.ui.separator, b'geometry')
        self.anim.setDuration(150)
        if state:
            self.anim.setStartValue(QRect(225, 325, 0, 2))
            self.anim.setEndValue(QRect(200, 325, 50, 2))
        else:
            self.anim.setStartValue(QRect(200, 325, 50, 2))
            self.anim.setEndValue(QRect(225, 325, 0, 2))
        self.anim.start()

    def animate_button(self, state, source):
        if state:
            source.setStyleSheet('color: rgb(0, 136, 169);\nbackground-color: rgb(24, 24, 24);\nborder: none;')
        else:
            source.setStyleSheet('color: rgb(255, 255, 255);\nbackground-color: rgb(24, 24, 24);\nborder: none;')

    def adjust_stars(self, index):
        for star in self.stars[:index]:
            star.setPixmap(QPixmap(star))
        for star in self.stars[index:]:
            star.setPixmap(QPixmap(greystar))

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if source in self.stars:
                star_index = int(source.objectName()[-1:])
                self.stars_active = False
                self.adjust_stars(star_index)
                self.inputted_stars = star_index
        if event.type() == QEvent.Enter and source in self.stars and self.stars_active:
            star_index = int(source.objectName()[-1:])
            self.adjust_stars(star_index)
        elif event.type() == QEvent.HoverEnter and source in (self.ui.submit_button,):
            self.animate_separator(True)
        elif event.type() == QEvent.HoverLeave and source in (self.ui.submit_button,):
            self.animate_separator(False)
        elif event.type() == QEvent.HoverEnter and source in (self.ui.minimise_button, self.ui.exit_button):
            self.animate_button(True, source)
        elif event.type() == QEvent.HoverLeave and source in (self.ui.minimise_button, self.ui.exit_button):
            self.animate_button(False, source)

class SplashScreen(MainwindowMixin):

    def __init__(self, version):
        MainwindowMixin.__init__(self)
        self.ui = Splash_Window()
        self.ui.setupUi(self)
        self.version = version
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.drop_shadow.setGraphicsEffect(self.shadow)
        _translate = QCoreApplication.translate
        self.ui.version_label.setText(_translate('MainWindow', f'<strong>Zenith</strong> v{CLIENT_INSTANCE.__version__}'))
        self.show()
        self.download_update()

    def download_update(self):
        zip_loc = os.path.abspath(f'./Zenithv{self.version}.zip')
        urllib.request.urlretrieve(ZenithAPIEndpoints.ZENITH_DOWNLOAD, zip_loc, self.handle_progress)
        self.ui.main_label.setText('Finishing up')
        zip_file = ZipFile(zip_loc, mode='r')
        zip_file.extractall(path='../')
        zip_file.close()
        os.remove(zip_loc)
        folder_loc = f'../Zenithv{self.version}/'
        if os.path.isfile('./config.json'):
            copyfile('./config.json', f'{folder_loc}config.json')
        if os.path.isfile('./token.bin'):
            copyfile('./token.bin', f'{folder_loc}token.bin')
        self.ui.main_label.setText('Welcome back')
        os.chdir(folder_loc)
        os.execv(f'{folder_loc}Zenith.exe', (f'{folder_loc}Zenith.exe', os.path.abspath('./')))
        self.close()

    def handle_progress(self, blocknum, blocksize, totalsize):
        readed_data = blocknum*blocksize
        if totalsize > 0:
            download_percentage = readed_data*100/totalsize
            self.ui.progress_bar.setValue(download_percentage)
            QApplication.processEvents()

class LoginScreen(MainwindowMixin):

    def __init__(self):
        MainwindowMixin.__init__(self)
        self.ui = Login_Window()
        self.ui.setupUi(self)
        self.ui.login_button.installEventFilter(self)
        self.ui.token_button.installEventFilter(self)
        self.ui.prefix_button.installEventFilter(self)
        self.ui.password_button.installEventFilter(self)
        self.ui.minimise_button.installEventFilter(self)
        self.ui.exit_button.installEventFilter(self)
        self.ui.login_button.clicked.connect(self.login)
        self.ui.token_button.clicked.connect(self.discord_token)
        self.ui.prefix_button.clicked.connect(self.prefixes)
        self.ui.password_button.clicked.connect(self.password)
        self.ui.minimise_button.clicked.connect(self.minimise)
        self.ui.exit_button.clicked.connect(self.close_window)
        self.ui.optional.hide()
        self.ui.token_field.hide()
        self.ui.prefix_field.hide()
        self.ui.password_field.hide()
        self.ui.token_button.hide()
        self.ui.prefix_button.hide()
        self.ui.password_button.hide()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.drop_shadow.setGraphicsEffect(self.shadow)
        _translate = QCoreApplication.translate
        self.ui.version_label.setText(_translate('MainWindow', f'<strong>Zenith</strong> v{CLIENT_INSTANCE.__version__}'))

    def minimise(self):
        self.showMinimized()

    def close_window(self):
        self.close()

    def animate_separator(self, state):
        self.anim = QtCore.QPropertyAnimation(self.ui.separator, b'geometry')
        self.anim.setDuration(150)
        if state:
            self.anim.setStartValue(QtCore.QRect(225, 290, 0, 2))
            self.anim.setEndValue(QtCore.QRect(200, 290, 50, 2))
        else:
            self.anim.setStartValue(QtCore.QRect(200, 290, 50, 2))
            self.anim.setEndValue(QtCore.QRect(225, 290, 0, 2))
        self.anim.start()

    def animate_button(self, state, source):
        if state:
            source.setStyleSheet('color: rgb(0, 136, 169);\nbackground-color: rgb(24, 24, 24);\nborder: none;')
        else:
            source.setStyleSheet('color: rgb(255, 255, 255);\nbackground-color: rgb(24, 24, 24);\nborder: none;')

    def login(self):
        if len(self.ui.license_key_field.text().strip()) != 36:
            self.ui.license_key_field.setStyleSheet(INCORRECT_STYLESHEET)
            return
        (succ, license_key) = _login(self.ui.license_key_field.text().strip())
        if not succ:
            self.ui.license_key_field.setStyleSheet(INCORRECT_STYLESHEET)
            return
        with open('token.bin', 'wb+') as f:
            f.write(b64encode(license_key.encode('utf-8')))
        self.ui.login_button.hide()
        self.ui.license_key_field.hide()
        if CLIENT_INSTANCE.config['token'] == '':
            self.ui.token_field.show()
            self.ui.token_button.show()
        elif len(CLIENT_INSTANCE.config['prefixes']) == 0:
            self.ui.prefix_button.show()
            self.ui.prefix_field.show()
        elif CLIENT_INSTANCE.config['password'] == '':
            self.ui.password_button.show()
            self.ui.password_field.show()
            self.ui.optional.show()
        else:
            self.close()
            with setup_logging():
                CLIENT_INSTANCE.run()

    def discord_token(self):
        if self.ui.token_field.text() == '':
            self.ui.token_field.setStyleSheet(INCORRECT_STYLESHEET)
            return
        CLIENT_INSTANCE.config['token'] = self.ui.token_field.text().strip()
        self.ui.token_field.hide()
        self.ui.token_button.hide()
        if len(CLIENT_INSTANCE.config['prefixes']) == 0:
            self.ui.prefix_field.show()
            self.ui.prefix_button.show()
        elif CLIENT_INSTANCE.config['password'] == '':
            self.ui.password_field.show()
            self.ui.password_button.show()
            self.ui.optional.show()
        else:
            self.close()
            with setup_logging():
                CLIENT_INSTANCE.run()

    def prefixes(self):
        if self.ui.prefix_field.text().strip() == '':
            self.ui.prefix_field.setStyleSheet(INCORRECT_STYLESHEET)
            return
        prefixes = self.ui.prefix_field.text().strip().split()
        for prefix in prefixes:
            CLIENT_INSTANCE.config['prefixes'].append(prefix.strip())
        if CLIENT_INSTANCE.config['password'] == '':
            self.ui.password_button.show()
            self.ui.password_field.show()
            self.ui.optional.show()
        else:
            self.close()
            with setup_logging():
                CLIENT_INSTANCE.run()

    def password(self):
        if self.ui.password_field.text().strip() != '':
            CLIENT_INSTANCE.config['password'] = self.ui.password_field.text().strip()
        self.close()
        with setup_logging():
            CLIENT_INSTANCE.run()

    def show(self, slide:int=None):
        super().show()
        if slide is None:
            return
        self.ui.login_button.hide()
        self.ui.license_key_field.hide()
        if slide == 2:
            self.ui.token_button.show()
            self.ui.token_field.show()
        elif slide == 3:
            self.ui.prefix_button.show()
            self.ui.prefix_field.show()
        elif slide == 4:
            self.ui.password_button.show()
            self.ui.password_field.show()
            self.ui.optional.show()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.HoverEnter and source in (self.ui.login_button, self.ui.token_button, self.ui.prefix_button, self.ui.password_button):
            self.animate_separator(True)
        elif event.type() == QtCore.QEvent.HoverLeave and source in (self.ui.login_button, self.ui.token_button, self.ui.prefix_button, self.ui.password_button):
            self.animate_separator(False)
        elif event.type() == QtCore.QEvent.HoverEnter and source in (self.ui.minimise_button, self.ui.exit_button):
            self.animate_button(True, source)
        elif event.type() == QtCore.QEvent.HoverLeave and source in (self.ui.minimise_button, self.ui.exit_button):
            self.animate_button(False, source)
        return super().eventFilter(source, event)

def run_bot():
    CLIENT_INSTANCE.kernel32.SetConsoleTitleW(f'Zenith Selfbot v{Zenith.__version__} | Logging in...')
    #req = get(ZenithAPIEndpoints.FETCH_VERSION)
    #if req.status_code != 200:
    #    print('Unable to fetch updates. Please try again later.')
    #    sys.exit(0)
    #    return
    app = QApplication(sys.argv)
    #response = req.text
    #if Zenith.__version__ != response:
    #    window = SplashScreen(response)
    #    sys.exit(app.exec_())
    #    return
    #if os.path.isfile('token.bin'):
       # with open('token.bin', 'rb') as f:
       #     login_token = str(b64decode(f.read()), 'utf-8')
       #     (succ, _) = _login(login_token)
    succ = True
    if not succ:
        main_window = LoginScreen()
        main_window.show()
        sys.exit(app.exec_())
    elif CLIENT_INSTANCE.config['token'] == '':
        main_window = LoginScreen()
        main_window.show(2)
        sys.exit(app.exec_())
    elif len(CLIENT_INSTANCE.config['prefixes']) == 0:
        main_window = LoginScreen()
        main_window.show(3)
        sys.exit(app.exec_())
    elif CLIENT_INSTANCE.config['password'] == '':
        main_window = LoginScreen()
        main_window.show(4)
        sys.exit(app.exec_())
    else:
        with setup_logging():
            CLIENT_INSTANCE.run()
    #else:
    #    main_window = LoginScreen()
    #    main_window.show()
    #    sys.exit(app.exec_())
    if not POSTED_FEEDBACK:
        feedback_window = FeedbackScreen()
        feedback_window.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            try:
                rmtree(sys.argv[1])
            finally:
                pass
        run_bot()
    finally:
        pass
