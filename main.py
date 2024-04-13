import window as w
import loginpage as l
import firstLogin as f
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedLayout

if _name_ == '_main_':
    app = QApplication(sys.argv)
    main_window = w.MyWindow()
    main_window.show()
    login = l.create_login_page()
    main_window.switch_to_page(login)
    main_window.remove_current_page()
    first = f.create_page()
    main_window.switch_to_page(first)
    sys.exit(app.exec_())
