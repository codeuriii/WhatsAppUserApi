import requests

class WhatsAppUserApi():

    def __init__(self, phone_number: str) -> None:
        self.phone = phone_number
        