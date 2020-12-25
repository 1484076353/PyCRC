#!/usr/bin/env python
# encoding:utf8;
"""
    * Author:ChenJun
    * Time:2020/12/24
    * description:
"""
from functools import reduce


class BCC:

    @classmethod
    def BCC(cls, check_hex):
        global bytes
        check_hex = check_hex.replace(' ', '')
        try:
            bytes = [int(check_hex[i:i + 2], 16) for i in range(0, len(check_hex), 2)]
        except Exception:
            raise
        return hex(reduce(lambda i, j: i ^ j, bytes))[2:].upper().zfill(2)