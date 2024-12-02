from abc import ABC, abstractclassmethod

class MakeCall(ABC):

    def make_call(self):
        pass

class SendSMS(ABC):
    def send_sms(self):
        pass

class GetInternet(ABC):
    def get_internet(self):
        pass

class MobilePhone(MakeCall, SendSMS, GetInternet):

    def make_call(self):
        print("Calling to abonent...")

    def send_sms(self):
        print("Sending a sms to abonent")

    def get_internet(self):
        print("Get connect to internet")

class StacionarPhone(MakeCall):

    def make_call(self):
        print("Hello! What are you doing?")

mobile_phone = MobilePhone()
mobile_phone.send_sms()
mobile_phone.make_call()
mobile_phone.get_internet()

stacionar_phone = StacionarPhone()
stacionar_phone.make_call()

