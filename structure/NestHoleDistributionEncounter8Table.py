# automatically generated by the FlatBuffers compiler, do not modify

# namespace: structure

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()

class NestHoleDistributionEncounter8Table(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsNestHoleDistributionEncounter8Table(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NestHoleDistributionEncounter8Table()
        x.Init(buf, n + offset)
        return x

    # NestHoleDistributionEncounter8Table
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NestHoleDistributionEncounter8Table
    def TableID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8Table
    def GameVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8Table
    def Field02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8Table
    def Field03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8Table
    def Entries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from structure.NestHoleDistributionEncounter8 import NestHoleDistributionEncounter8
            obj = NestHoleDistributionEncounter8()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # NestHoleDistributionEncounter8Table
    def EntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # NestHoleDistributionEncounter8Table
    def EntriesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def NestHoleDistributionEncounter8TableStart(builder): builder.StartObject(5)
def NestHoleDistributionEncounter8TableAddTableID(builder, TableID): builder.PrependUint64Slot(0, TableID, 0)
def NestHoleDistributionEncounter8TableAddGameVersion(builder, GameVersion): builder.PrependUint32Slot(1, GameVersion, 0)
def NestHoleDistributionEncounter8TableAddField02(builder, Field02): builder.PrependInt8Slot(2, Field02, 0)
def NestHoleDistributionEncounter8TableAddField03(builder, Field03): builder.PrependInt8Slot(3, Field03, 0)
def NestHoleDistributionEncounter8TableAddEntries(builder, Entries): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(Entries), 0)
def NestHoleDistributionEncounter8TableStartEntriesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def NestHoleDistributionEncounter8TableEnd(builder): return builder.EndObject()
