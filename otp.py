import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import createOTP
import sendMail
import createCertificate


class inputdialogdemo(QWidget):
    secret = "MCZGFJ"

    def __init__(self, parent=None):
        super(inputdialogdemo, self).__init__(parent)

        layout = QFormLayout()

        self.label1 = QLabel("Nom")
        self.firstName = QLineEdit()
        layout.addRow(self.label1, self.firstName)

        self.label2 = QLabel("Prenom")
        self.lastName = QLineEdit()
        layout.addRow(self.label2, self.lastName)

        self.label3 = QLabel("Email")
        self.email = QLineEdit()
        layout.addRow(self.label3, self.email)

        self.label4 = QLabel("CAName")
        self.caname = QLineEdit()
        layout.addRow(self.label4, self.caname)

        self.submit = QPushButton("Soumettre")
        layout.addRow(self.submit)
        self.submit.clicked.connect(self.submitForm)
        self.setLayout(layout)
        self.setWindowTitle("Generateur OTP")

    def submitForm(self):
        firstName = self.firstName.text()
        lastName = self.lastName.text()
        email = self.email.text()
        caname = self.caname.text()
        # TODO create OTP and send email

        otp = 123456  # Temporary value
        otp = createOTP.get_hotp_token(self.secret)
        print(otp)
        # OTP = createOtp(secret) TODO define the secret string (hash of time * name ?)
        # sendMail(OTP)
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter The password send by email:')
        print(text)
        print(ok)
        if ok:
            print("ok")
            if int(text) == int(otp):
                print("otp OK")
                createCertificate.downloadRessources()
                # checks whetehr the generated OTP is equal to the provided OTP
                # TODO Process certificate request
                #self.le1.setText(str(text))



def main():
    app = QApplication(sys.argv)
    ex = inputdialogdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
