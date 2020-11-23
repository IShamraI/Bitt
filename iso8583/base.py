from .config import DictConfig
from .logger import Logger


class ISO8583(object):
    BitmapFieldID = 1

    def __init__(self, config) -> None:
        self.cfg = DictConfig(config)
        self.log = Logger()

    @staticmethod
    def ordp(c: bytes) -> str:
        output = []
        for i in c:
            if (i < 32) or (i >= 127):
                output.append('.')
            else:
                output.append(chr(i))
        return ''.join(output)

    def hexdump(self, p: bytes) -> str:
        output = []
        l = len(p)
        i = 0
        while i < l:
            output.append('{:04d}   '.format(i))
            for j in range(16):
                if (i + j) < l:
                    byte = p[i + j]
                    output.append('{:02X} '.format(byte))
                else:
                    output.append('   ')
                if (j % 16) == 7:
                    output.append(' ')
            output.append('  ')
            output.append(self.ordp(p[i:i + 16]))
            output.append('\n')
            i += 16
        return ''.join(output).rstrip('\n')
