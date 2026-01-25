# core/client/state_machine.py

class ClientStateMachine:
    """
    S0: No pad
    S1: Pad loaded
    S2: Ready to send
    S3: Waiting for message
    S4: Pad exhausted
    S5: Error
    """

    def __init__(self):
        self.state = "S0"

    def on_pad_loaded(self):
        if self.state != "S0":
            raise ValueError("Invalid transition")
        self.state = "S1"

    def on_ready(self):
        if self.state != "S1":
            raise ValueError("Invalid transition")
        self.state = "S2"

    def on_send(self):
        if self.state != "S2":
            raise ValueError("Invalid transition")
        self.state = "S3"

    def on_receive(self):
        if self.state != "S3":
            raise ValueError("Invalid transition")
        self.state = "S2"

    def on_exhausted(self):
        self.state = "S4"

    def on_error(self):
        self.state = "S5"