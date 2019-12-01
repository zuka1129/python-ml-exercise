import abc

class Computer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        print('computer method')
class Usb(Computer):
    def run_u(self):
        print('usb run')
    def run(self):
        pass
u = Usb()
u.run_u()