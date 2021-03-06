#!/usr/bin/env python
# encoding:utf8;
"""
    * Author:ChenJun
    * Time:2020/12/24
    * description:
"""


class LRC:

    @classmethod
    def LRC(cls, check_str,ascii=False):
        global bytes
        if ascii:  # 传入参数为字符串
            try:
                bytes = [ord(item) for item in check_str]
            except Exception:
                raise
        else:
            check_hex = check_str.replace(' ', '')
            try:
                bytes = [int(check_hex[i:i + 2], 16) for i in range(0, len(check_hex), 2)]
            except Exception:
                raise
        return hex(256 - (sum(bytes) % 256))[2:].upper().zfill(2)
