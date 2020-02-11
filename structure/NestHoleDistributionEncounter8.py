# automatically generated by the FlatBuffers compiler, do not modify

# namespace: structure

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class NestHoleDistributionEncounter8(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsNestHoleDistributionEncounter8(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NestHoleDistributionEncounter8()
        x.Init(buf, n + offset)
        return x

    # NestHoleDistributionEncounter8
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NestHoleDistributionEncounter8
    def EntryIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Species(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def AltForm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def DynamaxLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field05(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field06(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field07(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field08(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field09(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field0A(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Ability(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def IsGigantamax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # NestHoleDistributionEncounter8
    def DropTableID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def BonusTableID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Probabilities(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # NestHoleDistributionEncounter8
    def ProbabilitiesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # NestHoleDistributionEncounter8
    def ProbabilitiesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # NestHoleDistributionEncounter8
    def ProbabilitiesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0

    # NestHoleDistributionEncounter8
    def Gender(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def FlawlessIVs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field12(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field13(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field14(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Nature(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field16(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Move0(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Move1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Move2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Move3(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def DynamaxBoost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # NestHoleDistributionEncounter8
    def Field1C(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field1D(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field1E(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field1F(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field20(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field21(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field22(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field23(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # NestHoleDistributionEncounter8
    def Field24(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def NestHoleDistributionEncounter8Start(builder): builder.StartObject(37)
def NestHoleDistributionEncounter8AddEntryIndex(builder, EntryIndex): builder.PrependUint32Slot(0, EntryIndex, 0)
def NestHoleDistributionEncounter8AddSpecies(builder, Species): builder.PrependUint32Slot(1, Species, 0)
def NestHoleDistributionEncounter8AddAltForm(builder, AltForm): builder.PrependUint32Slot(2, AltForm, 0)
def NestHoleDistributionEncounter8AddLevel(builder, Level): builder.PrependUint32Slot(3, Level, 0)
def NestHoleDistributionEncounter8AddDynamaxLevel(builder, DynamaxLevel): builder.PrependUint16Slot(4, DynamaxLevel, 0)
def NestHoleDistributionEncounter8AddField05(builder, Field05): builder.PrependUint32Slot(5, Field05, 0)
def NestHoleDistributionEncounter8AddField06(builder, Field06): builder.PrependUint32Slot(6, Field06, 0)
def NestHoleDistributionEncounter8AddField07(builder, Field07): builder.PrependUint32Slot(7, Field07, 0)
def NestHoleDistributionEncounter8AddField08(builder, Field08): builder.PrependUint32Slot(8, Field08, 0)
def NestHoleDistributionEncounter8AddField09(builder, Field09): builder.PrependUint32Slot(9, Field09, 0)
def NestHoleDistributionEncounter8AddField0A(builder, Field0A): builder.PrependUint32Slot(10, Field0A, 0)
def NestHoleDistributionEncounter8AddAbility(builder, Ability): builder.PrependInt8Slot(11, Ability, 0)
def NestHoleDistributionEncounter8AddIsGigantamax(builder, IsGigantamax): builder.PrependBoolSlot(12, IsGigantamax, 0)
def NestHoleDistributionEncounter8AddDropTableID(builder, DropTableID): builder.PrependUint64Slot(13, DropTableID, 0)
def NestHoleDistributionEncounter8AddBonusTableID(builder, BonusTableID): builder.PrependUint64Slot(14, BonusTableID, 0)
def NestHoleDistributionEncounter8AddProbabilities(builder, Probabilities): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(Probabilities), 0)
def NestHoleDistributionEncounter8StartProbabilitiesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def NestHoleDistributionEncounter8AddGender(builder, Gender): builder.PrependInt8Slot(16, Gender, 0)
def NestHoleDistributionEncounter8AddFlawlessIVs(builder, FlawlessIVs): builder.PrependInt8Slot(17, FlawlessIVs, 0)
def NestHoleDistributionEncounter8AddField12(builder, Field12): builder.PrependInt8Slot(18, Field12, 0)
def NestHoleDistributionEncounter8AddField13(builder, Field13): builder.PrependInt8Slot(19, Field13, 0)
def NestHoleDistributionEncounter8AddField14(builder, Field14): builder.PrependInt8Slot(20, Field14, 0)
def NestHoleDistributionEncounter8AddNature(builder, Nature): builder.PrependInt8Slot(21, Nature, 0)
def NestHoleDistributionEncounter8AddField16(builder, Field16): builder.PrependUint32Slot(22, Field16, 0)
def NestHoleDistributionEncounter8AddMove0(builder, Move0): builder.PrependUint32Slot(23, Move0, 0)
def NestHoleDistributionEncounter8AddMove1(builder, Move1): builder.PrependUint32Slot(24, Move1, 0)
def NestHoleDistributionEncounter8AddMove2(builder, Move2): builder.PrependUint32Slot(25, Move2, 0)
def NestHoleDistributionEncounter8AddMove3(builder, Move3): builder.PrependUint32Slot(26, Move3, 0)
def NestHoleDistributionEncounter8AddDynamaxBoost(builder, DynamaxBoost): builder.PrependFloat32Slot(27, DynamaxBoost, 0.0)
def NestHoleDistributionEncounter8AddField1C(builder, Field1C): builder.PrependUint32Slot(28, Field1C, 0)
def NestHoleDistributionEncounter8AddField1D(builder, Field1D): builder.PrependUint32Slot(29, Field1D, 0)
def NestHoleDistributionEncounter8AddField1E(builder, Field1E): builder.PrependUint32Slot(30, Field1E, 0)
def NestHoleDistributionEncounter8AddField1F(builder, Field1F): builder.PrependUint32Slot(31, Field1F, 0)
def NestHoleDistributionEncounter8AddField20(builder, Field20): builder.PrependUint32Slot(32, Field20, 0)
def NestHoleDistributionEncounter8AddField21(builder, Field21): builder.PrependUint32Slot(33, Field21, 0)
def NestHoleDistributionEncounter8AddField22(builder, Field22): builder.PrependUint32Slot(34, Field22, 0)
def NestHoleDistributionEncounter8AddField23(builder, Field23): builder.PrependUint32Slot(35, Field23, 0)
def NestHoleDistributionEncounter8AddField24(builder, Field24): builder.PrependUint32Slot(36, Field24, 0)
def NestHoleDistributionEncounter8End(builder): return builder.EndObject()
