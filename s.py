from ctypes import *

msvcrt = cdll.msvcrt
message_string = b"How Do U Do"
msvcrt.printf(b"%s", message_string)