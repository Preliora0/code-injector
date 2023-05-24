from pymem.process import *
from pymem import *

appName = ""

app = pymem.Pymem(appName)
module = module_from_name(app.process_handle, appName).lpBaseOfDll
addingAddr = 0x00325A70

def getPointerAddr(base, offsets):
    addr = app.read_int(base)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = app.read_int(addr + offset)
    addr = addr + offsets[-1]
    return addr


#This is to change values: app.write_int(getPointerAddr(module + addingAddr, [0x7D0, 0xF8, 0x318, 0x390, 0x7F8]), 123)

