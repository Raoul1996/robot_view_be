#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class BaseResp(object):
    """
    Attributes:
     - StatusMessage
     - StatusCode
    """


    def __init__(self, StatusMessage="", StatusCode=0,):
        self.StatusMessage = StatusMessage
        self.StatusCode = StatusCode

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.StatusMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.StatusCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('BaseResp')
        if self.StatusMessage is not None:
            oprot.writeFieldBegin('StatusMessage', TType.STRING, 1)
            oprot.writeString(self.StatusMessage.encode('utf-8') if sys.version_info[0] == 2 else self.StatusMessage)
            oprot.writeFieldEnd()
        if self.StatusCode is not None:
            oprot.writeFieldBegin('StatusCode', TType.I32, 2)
            oprot.writeI32(self.StatusCode)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CommonResponse(object):
    """
    Attributes:
     - errno
     - errmsg
     - data
     - BaseResp
    """


    def __init__(self, errno=0, errmsg="ok", data=None, BaseResp=None,):
        self.errno = errno
        self.errmsg = errmsg
        self.data = data
        self.BaseResp = BaseResp

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.errno = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.errmsg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.MAP:
                    self.data = {}
                    (_ktype1, _vtype2, _size0) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val6 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.data[_key5] = _val6
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 255:
                if ftype == TType.STRUCT:
                    self.BaseResp = BaseResp()
                    self.BaseResp.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('CommonResponse')
        if self.errno is not None:
            oprot.writeFieldBegin('errno', TType.I32, 1)
            oprot.writeI32(self.errno)
            oprot.writeFieldEnd()
        if self.errmsg is not None:
            oprot.writeFieldBegin('errmsg', TType.STRING, 2)
            oprot.writeString(self.errmsg.encode('utf-8') if sys.version_info[0] == 2 else self.errmsg)
            oprot.writeFieldEnd()
        if self.data is not None:
            oprot.writeFieldBegin('data', TType.MAP, 3)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.data))
            for kiter7, viter8 in self.data.items():
                oprot.writeString(kiter7.encode('utf-8') if sys.version_info[0] == 2 else kiter7)
                oprot.writeString(viter8.encode('utf-8') if sys.version_info[0] == 2 else viter8)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.BaseResp is not None:
            oprot.writeFieldBegin('BaseResp', TType.STRUCT, 255)
            self.BaseResp.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(BaseResp)
BaseResp.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'StatusMessage', 'UTF8', "", ),  # 1
    (2, TType.I32, 'StatusCode', None, 0, ),  # 2
)
all_structs.append(CommonResponse)
CommonResponse.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'errno', None, 0, ),  # 1
    (2, TType.STRING, 'errmsg', 'UTF8', "ok", ),  # 2
    (3, TType.MAP, 'data', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 3
    None,  # 4
    None,  # 5
    None,  # 6
    None,  # 7
    None,  # 8
    None,  # 9
    None,  # 10
    None,  # 11
    None,  # 12
    None,  # 13
    None,  # 14
    None,  # 15
    None,  # 16
    None,  # 17
    None,  # 18
    None,  # 19
    None,  # 20
    None,  # 21
    None,  # 22
    None,  # 23
    None,  # 24
    None,  # 25
    None,  # 26
    None,  # 27
    None,  # 28
    None,  # 29
    None,  # 30
    None,  # 31
    None,  # 32
    None,  # 33
    None,  # 34
    None,  # 35
    None,  # 36
    None,  # 37
    None,  # 38
    None,  # 39
    None,  # 40
    None,  # 41
    None,  # 42
    None,  # 43
    None,  # 44
    None,  # 45
    None,  # 46
    None,  # 47
    None,  # 48
    None,  # 49
    None,  # 50
    None,  # 51
    None,  # 52
    None,  # 53
    None,  # 54
    None,  # 55
    None,  # 56
    None,  # 57
    None,  # 58
    None,  # 59
    None,  # 60
    None,  # 61
    None,  # 62
    None,  # 63
    None,  # 64
    None,  # 65
    None,  # 66
    None,  # 67
    None,  # 68
    None,  # 69
    None,  # 70
    None,  # 71
    None,  # 72
    None,  # 73
    None,  # 74
    None,  # 75
    None,  # 76
    None,  # 77
    None,  # 78
    None,  # 79
    None,  # 80
    None,  # 81
    None,  # 82
    None,  # 83
    None,  # 84
    None,  # 85
    None,  # 86
    None,  # 87
    None,  # 88
    None,  # 89
    None,  # 90
    None,  # 91
    None,  # 92
    None,  # 93
    None,  # 94
    None,  # 95
    None,  # 96
    None,  # 97
    None,  # 98
    None,  # 99
    None,  # 100
    None,  # 101
    None,  # 102
    None,  # 103
    None,  # 104
    None,  # 105
    None,  # 106
    None,  # 107
    None,  # 108
    None,  # 109
    None,  # 110
    None,  # 111
    None,  # 112
    None,  # 113
    None,  # 114
    None,  # 115
    None,  # 116
    None,  # 117
    None,  # 118
    None,  # 119
    None,  # 120
    None,  # 121
    None,  # 122
    None,  # 123
    None,  # 124
    None,  # 125
    None,  # 126
    None,  # 127
    None,  # 128
    None,  # 129
    None,  # 130
    None,  # 131
    None,  # 132
    None,  # 133
    None,  # 134
    None,  # 135
    None,  # 136
    None,  # 137
    None,  # 138
    None,  # 139
    None,  # 140
    None,  # 141
    None,  # 142
    None,  # 143
    None,  # 144
    None,  # 145
    None,  # 146
    None,  # 147
    None,  # 148
    None,  # 149
    None,  # 150
    None,  # 151
    None,  # 152
    None,  # 153
    None,  # 154
    None,  # 155
    None,  # 156
    None,  # 157
    None,  # 158
    None,  # 159
    None,  # 160
    None,  # 161
    None,  # 162
    None,  # 163
    None,  # 164
    None,  # 165
    None,  # 166
    None,  # 167
    None,  # 168
    None,  # 169
    None,  # 170
    None,  # 171
    None,  # 172
    None,  # 173
    None,  # 174
    None,  # 175
    None,  # 176
    None,  # 177
    None,  # 178
    None,  # 179
    None,  # 180
    None,  # 181
    None,  # 182
    None,  # 183
    None,  # 184
    None,  # 185
    None,  # 186
    None,  # 187
    None,  # 188
    None,  # 189
    None,  # 190
    None,  # 191
    None,  # 192
    None,  # 193
    None,  # 194
    None,  # 195
    None,  # 196
    None,  # 197
    None,  # 198
    None,  # 199
    None,  # 200
    None,  # 201
    None,  # 202
    None,  # 203
    None,  # 204
    None,  # 205
    None,  # 206
    None,  # 207
    None,  # 208
    None,  # 209
    None,  # 210
    None,  # 211
    None,  # 212
    None,  # 213
    None,  # 214
    None,  # 215
    None,  # 216
    None,  # 217
    None,  # 218
    None,  # 219
    None,  # 220
    None,  # 221
    None,  # 222
    None,  # 223
    None,  # 224
    None,  # 225
    None,  # 226
    None,  # 227
    None,  # 228
    None,  # 229
    None,  # 230
    None,  # 231
    None,  # 232
    None,  # 233
    None,  # 234
    None,  # 235
    None,  # 236
    None,  # 237
    None,  # 238
    None,  # 239
    None,  # 240
    None,  # 241
    None,  # 242
    None,  # 243
    None,  # 244
    None,  # 245
    None,  # 246
    None,  # 247
    None,  # 248
    None,  # 249
    None,  # 250
    None,  # 251
    None,  # 252
    None,  # 253
    None,  # 254
    (255, TType.STRUCT, 'BaseResp', [BaseResp, None], None, ),  # 255
)
fix_spec(all_structs)
del all_structs
