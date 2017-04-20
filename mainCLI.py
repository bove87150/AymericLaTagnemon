import sys
import createOTP
import sendMail
import createCertificate
import creationattes

class getInputs():
    def __init__(self, parent=None):
        self.firstName = raw_input("prenom : ")
        self.lastName = raw_input("nom : ")
        self.email = raw_input("email : ")
        self.caname = raw_input("intule certificat : ")
        # TODO create OTP and send email
        creationattes.ecriture(self.firstName,self.lastName)
        otp = 123456  # Temporary value
        otp = createOTP.get_totp_token("BASE32SECRET3232") #Final value
        sendMail.sendOtp(otp, self.email)
        print("Le mot de passe unique vous a ete envoye par email")
        otp_check = input("Code recu par email : ")

        if int(otp_check) == int(otp):
            print("otp OK")
            createCertificate.downloadRessources()
            # checks whetehr the generated OTP is equal to the provided OTP
            # TODO Process certificate request
            # self.le1.setText(str(text))

def main():
    getInputs()


if __name__ == '__main__':
    main()
