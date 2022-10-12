from pymem import *
from pymem.process import *
import keyboard


health = "F1"
ammo = "r"
jumpReset = "F3"
jumpMedium = "shift"
jumpHigh = "F4"

mem = Pymem("ac_client.exe")
module = module_from_name(mem.process_handle, "ac_client.exe").lpBaseOfDll

offsets = [0x8, 0x98, 0x68, 0x490]
health_offsets = [0x0, 0x408]
jumpValues = [0x8, 0x190, 0x98, 0xB00]
awnValue = [0x8, 0xB74, 0x30, 0x740]


def getPointerAddr(base, offsets):
    addr = mem.read_int(base)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = mem.read_int(addr + offset)
    addr = addr + offsets[-1]
    return addr


def healthHack(base, health_offsets):
    addrh = mem.read_int(base)
    for health_offset in health_offsets:
        if health_offset != health_offsets[-1]:
            addrh = mem.read_int(addrh + health_offset)
    addrh = addrh + health_offsets[-1]
    return addrh


def jumpMethod(base, jumpValues):
    jumpAddress = mem.read_int(base)
    for jumpValue in jumpValues:
        if jumpValue != jumpValues[-1]:
            jumpAddress = mem.read_int(jumpAddress + jumpValue)
    jumpAddress = jumpAddress + jumpValues[-1]
    return jumpAddress


while True:
    if keyboard.is_pressed(ammo):
        mem.write_int(getPointerAddr(module + 0x00183828, offsets), 10000)
        mem.write_int(getPointerAddr(module + 0x00183828, awnValue), 10000)
    elif keyboard.is_pressed(health):
        mem.write_int(healthHack(module + 0x0018B0B8, health_offsets), 9999)
    elif keyboard.is_pressed(jumpMedium):
        mem.write_float(jumpMethod(module + 0x00183828, jumpValues), 9.1)
    elif keyboard.is_pressed(jumpReset):
        reset_value = float(input("Enter the height value : "))
        mem.write_float(jumpMethod(
            module + 0x00183828, jumpValues), reset_value)
    elif keyboard.is_pressed(jumpHigh):
        mem.write_float(jumpMethod(module + 0x00183828, jumpValues), 15.0)
