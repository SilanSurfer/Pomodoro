from PyQt5 import QtWidgets
import stepfinished_dialog_design

class StepFinishedDialog(QtWidgets.QDialog, stepfinished_dialog_design.Ui_StepFinishedDialog):
    def __init__(self, accept_callback, reject_callback):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(lambda: self.handle_accept(accept_callback))
        self.buttonBox.rejected.connect(lambda: self.handle_reject(reject_callback))

    def handle_accept(self, accept_callback):
        accept_callback()
        self.accept

    def handle_reject(self, reject_callback):
        reject_callback()
        self.reject

    def set_information(self, text_to_display):
        self.notificationLabel.setText(text_to_display)