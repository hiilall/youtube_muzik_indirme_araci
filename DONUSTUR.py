import os

try:
    os.system("python -m PyQt5.uic.pyuic -x thresholdV2.ui -o ui_thresholdV2.py")
    #☻os.system("pyrcc5 icons.qrc -o icons_rc.py")
except Exception as e:
    print(e)
    pass