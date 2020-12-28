实现功能

    CRC（循环冗余校验），LRC校验(纵向冗余校验)，BCC校验(异或校验)
安装
    
    pip install PyCRC-Hex
升级

    pip install --upgrade PyCRC-Hex
CRC校验（循环冗余校验）
    
    CRC即循环冗余校验码（Cyclic Redundancy Check）：是数据通信领域中最常用的一种查错校验码，其特征是信息字段和校验字段的长度可以任意选定。循环冗余检查（CRC）是一种数据传输检错功能，对数据进行多项式计算，并将得到的结果附在帧的后面，接收设备也执行类似的算法，以保证数据传输的正确性和完整性。
实现的CRC算法名称
    
    CRC-4/ITU
    CRC-5/EPC
    CRC-5/ITU
    CRC-5/USB
    CRC-6/ITU
    CRC-7/MMC
    CRC-8
    CRC-8/ITU
    CRC-8/ROHC
    CRC-8/MAXIM
    CRC-16/IBM
    CRC-16/MAXIM
    CRC-16/USB
    CRC-16/MODBUS
    CRC-16/CCITT
    CRC-16/CCITT-FALSE
    CRC-16/X25
    CRC-16/XMODEM
    CRC-16/DNP
    CRC-32
    CRC-32/MPEG-2
用法
    
    HEX:
    
    import PyCRC
    from PyCRC.crc import CRC
    
    hex_str = "31 32 33 34"
    model = PyCRC.CRC_16_CCITT
    crc = CRC.CRC(hex_str, model)
    print(crc)
        
    >8832
    
    hex_str：待计算数据（16进制字符串）
    model:CRC算法名称
    CRC校验结果：8832
    
    -----------------------------------------------------
    
    ASCII:
    
    import PyCRC
    from PyCRC.crc import CRC
    
    ascii = "1234"
    model = PyCRC.CRC_16_CCITT
    crc = CRC.CRC(ascii, model,True)
    print(crc)
    
    >8832
    
    ascii：待计算数据（字符串）
    model:CRC算法名称
    CRC校验结果：8832
    


LRC校验(纵向冗余校验)
    
    纵向冗余校验（Longitudinal Redundancy Check，简称：LRC）是通信中常用的一种校验形式，也称LRC校验或纵向校验。它是一种从纵向通道上的特定比特串产生校验比特的错误检测方法。在行列格式中（如磁带），LRC经常是与VRC一起使用，这样就会为每个字符校验码。在工业领域Modbus协议Ascii模式采用该算法。
用法

    HEX:

    from PyCRC.lrc import LRC

    hex_str = "31 32 33 34"
    lrc = LRC.LRC(hex_str)
    print(lrc)
    
    >36
    
    hex_str：待计算数据（16进制字符串）
    LRC校验结果：36
    
    -----------------------------------------------------
    
    ASCII:
    
    from PyCRC.lrc import LRC
    
    ascii = "1234"
    lrc = LRC.LRC(ascii,True)
    print(lrc)
    
    >36
    
    ascii：待计算数据（字符串）
    LRC校验结果：36
    
    
BCC校验(异或校验)
    
    BCC(Block Check Character/信息组校验码)，因校验码是将所有数据异或得出，故俗称异或校验。具体算法是：将每一个字节的数据（一般是两个16进制的字符）进行异或后即得到校验码。
用法

    HEX:
    
    from PyCRC.bcc import BCC

    hex_str = "31 32 33 34"
    bcc = BCC.BCC(hex_str)
    print(bcc) 
    
    >04
    
    hex_str：待计算数据（16进制字符串）
    BCC校验结果：04    
    
    -----------------------------------------------------
    
    ASCII:
    
    from PyCRC.bcc import BCC
    
    ascii = "1234"
    bcc = BCC.BCC(ascii, True)
    print(bcc)
    
    >04
    
    ascii：待计算数据（字符串）
    BCC校验结果：04    
    
    
    
