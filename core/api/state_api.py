# core/api/state_api.py

from core.client.state_machine import ClientStateMachine


class ClientStateAPI:
    def __init__(self):
        self.sm = ClientStateMachine()

    def pad_loaded(self):
        self.sm.on_pad_loaded()

    def ready(self):
        self.sm.on_ready()

    def send(self):
        self.sm.on_send()

    def receive(self):
        self.sm.on_receive()

    def exhausted(self):
        self.sm.on_exhausted()

    def error(self):
        self.sm.on_error()

    def get_state(self):
        return self.sm.state