#!/usr/bin/env python
# encoding:utf8;
"""
    * Author:ChenJun
    * Time:2020/12/24
    * description:
"""
from PyCRC import *


class CRC:

    @classmethod
    def CRC(cls, check_hex, model=None):
        global bytes
        check_hex = check_hex.replace(' ', '')
        try:
            bytes = [int(check_hex[i:i + 2], 16) for i in range(0, len(check_hex), 2)]
        except Exception:
            raise
        if model == CRC_4_ITU:
            return cls()._crc_4_itu(bytes)
        elif model == CRC_5_EPC:
            return cls()._crc_5_epc(bytes)
        elif model == CRC_5_ITU:
            return cls()._crc_5_itu(bytes)
        elif model == CRC_5_USB:
            return cls()._crc_5_usb(bytes)
        elif model == CRC_6_ITU:
            return cls()._crc_6_itu(bytes)
        elif model == CRC_7_MMC:
            return cls()._crc_7_mmc(bytes)
        elif model == CRC_8:
            return cls()._crc_8(bytes)
        elif model == CRC_8_ITU:
            return cls()._crc_8_itu(bytes)
        elif model == CRC_8_ROHC:
            return cls()._crc_8_rohc(bytes)
        elif model == CRC_8_MAXIM:
            return cls()._crc_8_maxim(bytes)
        elif model == CRC_16_IBM:
            return cls()._crc_16_ibm(bytes)
        elif model == CRC_16_MAXIM:
            return cls()._crc_16_maxim(bytes)
        elif model == CRC_16_USB:
            return cls()._crc_16_usb(bytes)
        elif model == CRC_16_MODBUS:
            return cls()._crc_16_modbus(bytes)
        elif model == CRC_16_CCITT:
            return cls()._crc_16_ccitt(bytes)
        elif model == CRC_16_CCITT_FALSE:
            return cls()._crc_16_ccitt_false(bytes)
        elif model == CRC_16_X25:
            return cls()._crc_16_x25(bytes)
        elif model == CRC_16_XMODEM:
            return cls()._crc_16_xmodem(bytes)
        elif model == CRC_16_DNP:
            return cls()._crc_16_dnp(bytes)
        elif model == CRC_32:
            return cls()._crc_32(bytes)
        elif model == CRC_32_MPEG_2:
            return cls()._crc_32_mpeg_2(bytes)
        else:
            return None

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-4/ITU	x4 + x + 1
    # *Width: 4
    # *Poly: 0x03
    # *Init: 0x00
    # *Xorout: 0x00
    # *Refin: True
    # *Refout: True  False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_4_itu(self, bytes):
        Width, Poly, Init, Refin, Refout = 4, 0x03, 0x00, True, False
        Poly <<= (8 - Width)
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-5/EPC	x5 + x3 + 1
    # *Width: 5
    # *Poly: 0x09
    # *Init: 0x09
    # *Xorout: 0x00
    # *Refin: False
    # *Refout: False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_5_epc(self, bytes):
        Width, Poly, Init, Refin, Refout = 5, 0x09, 0x09, False, False
        Init <<= (8 - Width)
        Poly <<= (8 - Width)
        result = self._ufunc(bytes, Width, Poly, Init, Refin, Refout)
        return self._get_crc(Width, (int(result, 16) >> 3), Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-5/ITU	x5 + x4 + x2  + 1
    # *Width: 5
    # *Poly: 0x15
    # *Init: 0x00
    # *Xorout: 0x00
    # *Refin: True
    # *Refout: True  False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_5_itu(self, bytes):
        Width, Poly, Init, Refin, Refout = 5, 0x15, 0x00, True, False
        Poly <<= (8 - Width)
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-5/USB	x5 + x2  + 1
    # *Width: 5
    # *Poly: 0x05
    # *Init: 0x1F
    # *Xorout: 0x1F
    # *Refin: True
    # *Refout: True  False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_5_usb(self, bytes):
        Width, Poly, Init, Xorout, Refin, Refout = 5, 0x05, 0x1F, 0x1F, True, False
        Poly <<= (8 - Width)
        result = self._ufunc(bytes, Width, Poly, Init, Refin, Refout)
        return self._get_crc(Width, (int(result, 16) ^ Xorout), Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-6/ITU	x6 + x  + 1
    # *Width: 6
    # *Poly: 0x03
    # *Init: 0x00
    # *Xorout: 0x00
    # *Refin: True
    # *Refout: True  False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_6_itu(self, bytes):
        Width, Poly, Init, Refin, Refout = 6, 0x03, 0x00, True, False
        Poly <<= (8 - Width)
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-7/MMC	x7 + x3  + 1
    # *Width: 7
    # *Poly: 0x09
    # *Init: 0x00
    # *Xorout: 0x00
    # *Refin: False
    # *Refout: False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_7_mmc(self, bytes):
        Width, Poly, Init, Refin, Refout = 7, 0x09, 0x00, False, False
        Poly <<= (8 - Width)
        result = self._ufunc(bytes, Width, Poly, Init, Refin, Refout)
        return self._get_crc(Width, (int(result, 16) >> 1), Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-8	x8 + x2 + x + 1
    # *Width: 8
    # *Poly: 0x07
    # *Init: 0x00
    # *Xorout: 0x00
    # *Refin: False
    # *Refout: False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_8(self, bytes):
        Width, Poly, Init, Refin, Refout = 8, 0x07, 0x00, False, False
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-8/ITU	x8 + x2 + x + 1
    # *Width: 8
    # *Poly: 0x07
    # *Init: 0x00
    # *Xorout: 0x55
    # *Refin: False
    # *Refout: False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_8_itu(self, bytes):
        Width, Poly, Init, Xorout, Refin, Refout = 8, 0x07, 0x00, 0x55, False, False
        result = self._ufunc(bytes, Width, Poly, Init, Refin, Refout)
        return self._get_crc(Width, (int(result, 16) ^ Xorout), Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-8/ROHC	x8 + x2 + x + 1
    # *Width: 8
    # *Poly: 0x07
    # *Init: 0xFF
    # *Xorout: 0x00
    # *Refin: True
    # *Refout: True   False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_8_rohc(self, bytes):
        Width, Poly, Init, Refin, Refout = 8, 0x07, 0xFF, True, False
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-8/MAXIM	x8 + x5 + x4 + 1
    # *Width: 8
    # *Poly: 0x31
    # *Init: 0x00
    # *Xorout: 0x00
    # *Refin: True
    # *Refout: True   False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_8_maxim(self, bytes):
        Width, Poly, Init, Refin, Refout = 8, 0x31, 0x00, True, False
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-16/IBM	x16 + x15 + x2 + 1
    # *Width: 16
    # *Poly: 0x8005
    # *Init: 0x0000
    # *Xorout: 0x0000
    # *Refin: True
    # *Refout: True   False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_16_ibm(self, bytes):
        Width, Poly, Init, Refin, Refout = 16, 0x8005, 0x0000, True, False
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-16/MAXIM	x16 + x15 + x2 + 1
    # *Width: 16
    # *Poly: 0x8005
    # *Init: 0x0000
    # *Xorout: 0xFFFF
    # *Refin: True
    # *Refout: True
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_16_maxim(self, bytes):
        Width, Poly, Init, Refin, Refout = 16, 0x8005, 0x0000, True, True
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-16/USB	x16 + x15 + x2 + 1
    # *Width: 16
    # *Poly: 0x8005
    # *Init: 0xFFFF
    # *Xorout: 0xFFFF
    # *Refin: True
    # *Refout: True
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_16_usb(self, bytes):
        Width, Poly, Init, Refin, Refout = 16, 0x8005, 0xFFFF, True, True
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-16/MODBUS	x16 + x15 + x2 + 1
    # *Width: 16
    # *Poly: 0x8005
    # *Init: 0xFFFF
    # *Xorout: 0x0000
    # *Refin: True
    # *Refout: True  False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_16_modbus(self, bytes):
        Width, Poly, Init, Refin, Refout = 16, 0x8005, 0xFFFF, True, False
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-16/CCITT	x16 + x12 + x5 + 1
    # *Width: 16
    # *Poly: 0x1021
    # *Init: 0x0000
    # *Xorout: 0x0000
    # *Refin: True
    # *Refout: True  False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_16_ccitt(self, bytes):
        Width, Poly, Init, Refin, Refout = 16, 0x1021, 0x0000, True, False
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-16/CCITT-FALSE	x16 + x12 + x5 + 1
    # *Width: 16
    # *Poly: 0x1021
    # *Init: 0xFFFF
    # *Xorout: 0x0000
    # *Refin: False
    # *Refout: False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_16_ccitt_false(self, bytes):
        Width, Poly, Init, Refin, Refout = 16, 0x1021, 0xFFFF, False, False
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-16/X25	x16 + x12 + x5 + 1
    # *Width: 16
    # *Poly: 0x1021
    # *Init: 0xFFFF
    # *Xorout: 0xFFFF
    # *Refin: True
    # *Refout: True
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_16_x25(self, bytes):
        Width, Poly, Init, Refin, Refout = 16, 0x1021, 0xFFFF, True, True
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-16/XMODEM	x16 + x12 + x5 + 1
    # *Width: 16
    # *Poly: 0x1021
    # *Init: 0x0000
    # *Xorout: 0x0000
    # *Refin: False
    # *Refout: False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_16_xmodem(self, bytes):
        Width, Poly, Init, Refin, Refout = 16, 0x1021, 0x0000, False, False
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-16/DNP x16 + x13 + x12 + x11 + x10 + x8 + x6 + x5 + x2 + 1
    # *Width: 16
    # *Poly: 0x3D65
    # *Init: 0x0000
    # *Xorout: 0xFFFF
    # *Refin: True
    # *Refout: True
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_16_dnp(self, bytes):
        Width, Poly, Init, Refin, Refout = 16, 0x3D65, 0x0000, True, True
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-32 x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x + 1
    # *Width: 32
    # *Poly: 0x4C11DB7
    # *Init: 0xFFFFFFF
    # *Xorout: 0xFFFFFFF
    # *Refin: True
    # *Refout: True
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    def _crc_32(self, bytes):
        Width, Poly, Init, Refin, Refout = 32, 0x04C11DB7, 0xFFFFFFFF, True, True
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    # *Name: CRC-32/MPEG-2 x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x + 1
    # *Width: 32
    # *Poly: 0x4C11DB7
    # *Init: 0xFFFFFFF
    # *Xorout: 0x0000000
    # *Refin: False
    # *Refout: False
    # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
    def _crc_32_mpeg_2(self, bytes):
        Width, Poly, Init, Refin, Refout = 32, 0x04C11DB7, 0xFFFFFFFF, False, False
        return self._ufunc(bytes, Width, Poly, Init, Refin, Refout)

    def _ufunc(self, bytes, Width, Poly, Init, Refin, Refout):
        Poly = self._get_poly(Width, Poly, Refin)
        scope = self._get_scope(Width, Refin)
        offset = Width - 8
        for buffer in bytes:
            if Refin:
                Init ^= buffer
            else:
                Init ^= buffer << (offset if offset > 0 else 0)
            Init = self._get_course(Init, scope, Width, Refin, Poly)
        return self._get_crc(Width, Init, Refout)

    def _get_poly(self, Width, Poly, Refin):
        if Refin:
            Poly = int((bin(Poly)[2:]).zfill(Width if Width > 8 else 8)[::-1], 2)
        return Poly

    def _get_scope(self, Width, Refin):
        if not Refin:
            return 1 << (Width - 1 if Width >= 8 else 7)
        return 1

    def _get_course(self, Init, scope, Width, Refin, Poly):
        for index in range(0, 8):
            if Init & scope:
                if Refin:
                    Init >>= 1
                else:
                    Init <<= 1
                Init = self._get_equilong(Init, Width)
                Init ^= Poly
            else:
                if Refin:
                    Init >>= 1
                else:
                    Init <<= 1
                Init = self._get_equilong(Init, Width)
        return Init

    def _get_equilong(self, src, Width):
        Width = Width if Width > 8 else 8
        return int(bin(src)[2:].zfill(Width)[-Width:], 2)

    def _get_crc(self, Width, Init, Refout):
        real_width = Width
        Width = Width if Width > 8 else 8
        result = bin(Init)[2:].zfill(Width)
        if Refout:
            result = result.replace("0", "2").replace("1", "0").replace("2", "1")
        Init = int(result[-Width:], 2)
        length = real_width // 4 if real_width % 4 == 0 else (real_width // 4 + 1)
        return (hex(Init)[2:]).zfill(Width // 4).upper()[-length:]
