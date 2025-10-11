# SNMP MIB module (CAREL-screw_compressor-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/carel/CAREL-screw_compressor-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:09 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

screw_compressorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Carel_ObjectIdentity = ObjectIdentity
carel = _Carel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839)
)
_Systm_ObjectIdentity = ObjectIdentity
systm = _Systm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 1)
)
_AgentRelease_Type = Integer32
_AgentRelease_Object = MibScalar
agentRelease = _AgentRelease_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 1),
    _AgentRelease_Type()
)
agentRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRelease.setStatus("current")
if mibBuilder.loadTexts:
    agentRelease.setUnits("N/A")
_AgentCode_Type = Integer32
_AgentCode_Object = MibScalar
agentCode = _AgentCode_Object(
    (1, 3, 6, 1, 4, 1, 9839, 1, 2),
    _AgentCode_Type()
)
agentCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCode.setStatus("current")
if mibBuilder.loadTexts:
    agentCode.setUnits("N/A")
_Instruments_ObjectIdentity = ObjectIdentity
instruments = _Instruments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2)
)
_WebGateInfo_ObjectIdentity = ObjectIdentity
webGateInfo = _WebGateInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0)
)
_AgentParameters_ObjectIdentity = ObjectIdentity
agentParameters = _AgentParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 1)
)


class _NetSize_Type(Integer32):
    """Custom type netSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NetSize_Type.__name__ = "Integer32"
_NetSize_Object = MibScalar
netSize = _NetSize_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 1, 1),
    _NetSize_Type()
)
netSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSize.setStatus("current")
if mibBuilder.loadTexts:
    netSize.setUnits("N/A")


class _BaudRate_Type(Integer32):
    """Custom type baudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 1200),
        ValueRangeConstraint(2400, 2400),
        ValueRangeConstraint(4800, 4800),
        ValueRangeConstraint(9600, 9600),
        ValueRangeConstraint(19200, 19200),
    )


_BaudRate_Type.__name__ = "Integer32"
_BaudRate_Object = MibScalar
baudRate = _BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 1, 2),
    _BaudRate_Type()
)
baudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baudRate.setStatus("current")
if mibBuilder.loadTexts:
    baudRate.setUnits("N/A")
_UnitTypeGroup_ObjectIdentity = ObjectIdentity
unitTypeGroup = _UnitTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 2)
)
_Unit1_Type_Type = DisplayString
_Unit1_Type_Object = MibScalar
unit1_Type = _Unit1_Type_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 2, 1),
    _Unit1_Type_Type()
)
unit1_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_Type.setStatus("current")
if mibBuilder.loadTexts:
    unit1_Type.setUnits("N/A")
_UnitCodeGroup_ObjectIdentity = ObjectIdentity
unitCodeGroup = _UnitCodeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 3)
)
_Unit1_Code_Type = Integer32
_Unit1_Code_Object = MibScalar
unit1_Code = _Unit1_Code_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 3, 1),
    _Unit1_Code_Type()
)
unit1_Code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_Code.setStatus("current")
if mibBuilder.loadTexts:
    unit1_Code.setUnits("N/A")
_UnitSoftwareReleaseGroup_ObjectIdentity = ObjectIdentity
unitSoftwareReleaseGroup = _UnitSoftwareReleaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 4)
)
_Unit1_SoftwareRelease_Type = Integer32
_Unit1_SoftwareRelease_Object = MibScalar
unit1_SoftwareRelease = _Unit1_SoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 4, 1),
    _Unit1_SoftwareRelease_Type()
)
unit1_SoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_SoftwareRelease.setStatus("current")
if mibBuilder.loadTexts:
    unit1_SoftwareRelease.setUnits("N/A")
_UnitMinSoftwareReleaseGroup_ObjectIdentity = ObjectIdentity
unitMinSoftwareReleaseGroup = _UnitMinSoftwareReleaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 5)
)
_Unit1_MinSoftwareRelease_Type = Integer32
_Unit1_MinSoftwareRelease_Object = MibScalar
unit1_MinSoftwareRelease = _Unit1_MinSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 5, 1),
    _Unit1_MinSoftwareRelease_Type()
)
unit1_MinSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_MinSoftwareRelease.setStatus("current")
if mibBuilder.loadTexts:
    unit1_MinSoftwareRelease.setUnits("N/A")
_UnitMaxSoftwareReleaseGroup_ObjectIdentity = ObjectIdentity
unitMaxSoftwareReleaseGroup = _UnitMaxSoftwareReleaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 6)
)
_Unit1_MaxSoftwareRelease_Type = Integer32
_Unit1_MaxSoftwareRelease_Object = MibScalar
unit1_MaxSoftwareRelease = _Unit1_MaxSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 6, 1),
    _Unit1_MaxSoftwareRelease_Type()
)
unit1_MaxSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_MaxSoftwareRelease.setStatus("current")
if mibBuilder.loadTexts:
    unit1_MaxSoftwareRelease.setUnits("N/A")
_UnitNoAnswerCounterGroup_ObjectIdentity = ObjectIdentity
unitNoAnswerCounterGroup = _UnitNoAnswerCounterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 7)
)
_Unit1_NoAnswerCounter_Type = Integer32
_Unit1_NoAnswerCounter_Object = MibScalar
unit1_NoAnswerCounter = _Unit1_NoAnswerCounter_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 7, 1),
    _Unit1_NoAnswerCounter_Type()
)
unit1_NoAnswerCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_NoAnswerCounter.setStatus("current")
if mibBuilder.loadTexts:
    unit1_NoAnswerCounter.setUnits("N/A")
_UnitErrorChecksumCounterGroup_ObjectIdentity = ObjectIdentity
unitErrorChecksumCounterGroup = _UnitErrorChecksumCounterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 8)
)
_Unit1_ErrorChecksumCounter_Type = Integer32
_Unit1_ErrorChecksumCounter_Object = MibScalar
unit1_ErrorChecksumCounter = _Unit1_ErrorChecksumCounter_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 8, 1),
    _Unit1_ErrorChecksumCounter_Type()
)
unit1_ErrorChecksumCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_ErrorChecksumCounter.setStatus("current")
if mibBuilder.loadTexts:
    unit1_ErrorChecksumCounter.setUnits("N/A")
_UnitTimeoutCounterGroup_ObjectIdentity = ObjectIdentity
unitTimeoutCounterGroup = _UnitTimeoutCounterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 9)
)
_Unit1_TimeoutCounter_Type = Integer32
_Unit1_TimeoutCounter_Object = MibScalar
unit1_TimeoutCounter = _Unit1_TimeoutCounter_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 9, 1),
    _Unit1_TimeoutCounter_Type()
)
unit1_TimeoutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_TimeoutCounter.setStatus("current")
if mibBuilder.loadTexts:
    unit1_TimeoutCounter.setUnits("N/A")
_UnitOnLineStatusGroup_ObjectIdentity = ObjectIdentity
unitOnLineStatusGroup = _UnitOnLineStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 10)
)
_Unit1_OnLineStatus_Type = Integer32
_Unit1_OnLineStatus_Object = MibScalar
unit1_OnLineStatus = _Unit1_OnLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 0, 10, 1),
    _Unit1_OnLineStatus_Type()
)
unit1_OnLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1_OnLineStatus.setStatus("current")
if mibBuilder.loadTexts:
    unit1_OnLineStatus.setUnits("N/A")
_DigitalObjects_ObjectIdentity = ObjectIdentity
digitalObjects = _DigitalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1)
)


class _Syson_s_Type(Integer32):
    """Custom type syson_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Syson_s_Type.__name__ = "Integer32"
_Syson_s_Object = MibScalar
syson_s = _Syson_s_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 1),
    _Syson_s_Type()
)
syson_s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syson_s.setStatus("current")
if mibBuilder.loadTexts:
    syson_s.setUnits("N/A")


class _Dout_1_Type(Integer32):
    """Custom type dout_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_1_Type.__name__ = "Integer32"
_Dout_1_Object = MibScalar
dout_1 = _Dout_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 2),
    _Dout_1_Type()
)
dout_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_1.setStatus("current")
if mibBuilder.loadTexts:
    dout_1.setUnits("N/A")


class _Dout_2_Type(Integer32):
    """Custom type dout_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_2_Type.__name__ = "Integer32"
_Dout_2_Object = MibScalar
dout_2 = _Dout_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 3),
    _Dout_2_Type()
)
dout_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_2.setStatus("current")
if mibBuilder.loadTexts:
    dout_2.setUnits("N/A")


class _Dout_3_Type(Integer32):
    """Custom type dout_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_3_Type.__name__ = "Integer32"
_Dout_3_Object = MibScalar
dout_3 = _Dout_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 4),
    _Dout_3_Type()
)
dout_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_3.setStatus("current")
if mibBuilder.loadTexts:
    dout_3.setUnits("N/A")


class _Dout_4_Type(Integer32):
    """Custom type dout_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_4_Type.__name__ = "Integer32"
_Dout_4_Object = MibScalar
dout_4 = _Dout_4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 5),
    _Dout_4_Type()
)
dout_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_4.setStatus("current")
if mibBuilder.loadTexts:
    dout_4.setUnits("N/A")


class _Dout_5_Type(Integer32):
    """Custom type dout_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_5_Type.__name__ = "Integer32"
_Dout_5_Object = MibScalar
dout_5 = _Dout_5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 6),
    _Dout_5_Type()
)
dout_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_5.setStatus("current")
if mibBuilder.loadTexts:
    dout_5.setUnits("N/A")


class _Dout_6_Type(Integer32):
    """Custom type dout_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_6_Type.__name__ = "Integer32"
_Dout_6_Object = MibScalar
dout_6 = _Dout_6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 7),
    _Dout_6_Type()
)
dout_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_6.setStatus("current")
if mibBuilder.loadTexts:
    dout_6.setUnits("N/A")


class _Dout_7_Type(Integer32):
    """Custom type dout_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_7_Type.__name__ = "Integer32"
_Dout_7_Object = MibScalar
dout_7 = _Dout_7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 8),
    _Dout_7_Type()
)
dout_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_7.setStatus("current")
if mibBuilder.loadTexts:
    dout_7.setUnits("N/A")


class _Dout_8_Type(Integer32):
    """Custom type dout_8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_8_Type.__name__ = "Integer32"
_Dout_8_Object = MibScalar
dout_8 = _Dout_8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 9),
    _Dout_8_Type()
)
dout_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_8.setStatus("current")
if mibBuilder.loadTexts:
    dout_8.setUnits("N/A")


class _Dout_9_Type(Integer32):
    """Custom type dout_9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_9_Type.__name__ = "Integer32"
_Dout_9_Object = MibScalar
dout_9 = _Dout_9_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 10),
    _Dout_9_Type()
)
dout_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_9.setStatus("current")
if mibBuilder.loadTexts:
    dout_9.setUnits("N/A")


class _Dout_10_Type(Integer32):
    """Custom type dout_10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_10_Type.__name__ = "Integer32"
_Dout_10_Object = MibScalar
dout_10 = _Dout_10_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 11),
    _Dout_10_Type()
)
dout_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_10.setStatus("current")
if mibBuilder.loadTexts:
    dout_10.setUnits("N/A")


class _Dout_11_Type(Integer32):
    """Custom type dout_11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_11_Type.__name__ = "Integer32"
_Dout_11_Object = MibScalar
dout_11 = _Dout_11_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 12),
    _Dout_11_Type()
)
dout_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_11.setStatus("current")
if mibBuilder.loadTexts:
    dout_11.setUnits("N/A")


class _Dout_12_Type(Integer32):
    """Custom type dout_12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_12_Type.__name__ = "Integer32"
_Dout_12_Object = MibScalar
dout_12 = _Dout_12_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 13),
    _Dout_12_Type()
)
dout_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_12.setStatus("current")
if mibBuilder.loadTexts:
    dout_12.setUnits("N/A")


class _Dout_13_Type(Integer32):
    """Custom type dout_13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dout_13_Type.__name__ = "Integer32"
_Dout_13_Object = MibScalar
dout_13 = _Dout_13_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 14),
    _Dout_13_Type()
)
dout_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dout_13.setStatus("current")
if mibBuilder.loadTexts:
    dout_13.setUnits("N/A")


class _En_evap_flow_al_Type(Integer32):
    """Custom type en_evap_flow_al based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_evap_flow_al_Type.__name__ = "Integer32"
_En_evap_flow_al_Object = MibScalar
en_evap_flow_al = _En_evap_flow_al_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 15),
    _En_evap_flow_al_Type()
)
en_evap_flow_al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    en_evap_flow_al.setStatus("current")
if mibBuilder.loadTexts:
    en_evap_flow_al.setUnits("N/A")


class _En_b1_Type(Integer32):
    """Custom type en_b1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_b1_Type.__name__ = "Integer32"
_En_b1_Object = MibScalar
en_b1 = _En_b1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 16),
    _En_b1_Type()
)
en_b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    en_b1.setStatus("current")
if mibBuilder.loadTexts:
    en_b1.setUnits("N/A")


class _En_b2_Type(Integer32):
    """Custom type en_b2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_b2_Type.__name__ = "Integer32"
_En_b2_Object = MibScalar
en_b2 = _En_b2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 17),
    _En_b2_Type()
)
en_b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    en_b2.setStatus("current")
if mibBuilder.loadTexts:
    en_b2.setUnits("N/A")


class _En_b3_Type(Integer32):
    """Custom type en_b3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_b3_Type.__name__ = "Integer32"
_En_b3_Object = MibScalar
en_b3 = _En_b3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 18),
    _En_b3_Type()
)
en_b3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    en_b3.setStatus("current")
if mibBuilder.loadTexts:
    en_b3.setUnits("N/A")


class _En_b4_Type(Integer32):
    """Custom type en_b4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_b4_Type.__name__ = "Integer32"
_En_b4_Object = MibScalar
en_b4 = _En_b4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 19),
    _En_b4_Type()
)
en_b4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    en_b4.setStatus("current")
if mibBuilder.loadTexts:
    en_b4.setUnits("N/A")


class _En_b5_Type(Integer32):
    """Custom type en_b5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_b5_Type.__name__ = "Integer32"
_En_b5_Object = MibScalar
en_b5 = _En_b5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 20),
    _En_b5_Type()
)
en_b5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    en_b5.setStatus("current")
if mibBuilder.loadTexts:
    en_b5.setUnits("N/A")


class _En_b6_Type(Integer32):
    """Custom type en_b6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_b6_Type.__name__ = "Integer32"
_En_b6_Object = MibScalar
en_b6 = _En_b6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 21),
    _En_b6_Type()
)
en_b6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    en_b6.setStatus("current")
if mibBuilder.loadTexts:
    en_b6.setUnits("N/A")


class _En_b7_Type(Integer32):
    """Custom type en_b7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_b7_Type.__name__ = "Integer32"
_En_b7_Object = MibScalar
en_b7 = _En_b7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 22),
    _En_b7_Type()
)
en_b7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    en_b7.setStatus("current")
if mibBuilder.loadTexts:
    en_b7.setUnits("N/A")


class _En_b8_Type(Integer32):
    """Custom type en_b8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_b8_Type.__name__ = "Integer32"
_En_b8_Object = MibScalar
en_b8 = _En_b8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 23),
    _En_b8_Type()
)
en_b8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    en_b8.setStatus("current")
if mibBuilder.loadTexts:
    en_b8.setUnits("N/A")


class _Superv_onoff_Type(Integer32):
    """Custom type superv_onoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Superv_onoff_Type.__name__ = "Integer32"
_Superv_onoff_Object = MibScalar
superv_onoff = _Superv_onoff_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 24),
    _Superv_onoff_Type()
)
superv_onoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superv_onoff.setStatus("current")
if mibBuilder.loadTexts:
    superv_onoff.setUnits("N/A")


class _En_start_restr_Type(Integer32):
    """Custom type en_start_restr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_start_restr_Type.__name__ = "Integer32"
_En_start_restr_Object = MibScalar
en_start_restr = _En_start_restr_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 25),
    _En_start_restr_Type()
)
en_start_restr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    en_start_restr.setStatus("current")
if mibBuilder.loadTexts:
    en_start_restr.setUnits("N/A")


class _En_modulation_Type(Integer32):
    """Custom type en_modulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_modulation_Type.__name__ = "Integer32"
_En_modulation_Object = MibScalar
en_modulation = _En_modulation_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 26),
    _En_modulation_Type()
)
en_modulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    en_modulation.setStatus("current")
if mibBuilder.loadTexts:
    en_modulation.setUnits("N/A")


class _Sun_win_sel_Type(Integer32):
    """Custom type sun_win_sel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sun_win_sel_Type.__name__ = "Integer32"
_Sun_win_sel_Object = MibScalar
sun_win_sel = _Sun_win_sel_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 27),
    _Sun_win_sel_Type()
)
sun_win_sel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sun_win_sel.setStatus("current")
if mibBuilder.loadTexts:
    sun_win_sel.setUnits("N/A")


class _Cooling_heating_Type(Integer32):
    """Custom type cooling_heating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cooling_heating_Type.__name__ = "Integer32"
_Cooling_heating_Object = MibScalar
cooling_heating = _Cooling_heating_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 29),
    _Cooling_heating_Type()
)
cooling_heating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooling_heating.setStatus("current")
if mibBuilder.loadTexts:
    cooling_heating.setUnits("N/A")


class _Inverter_Type(Integer32):
    """Custom type inverter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Inverter_Type.__name__ = "Integer32"
_Inverter_Object = MibScalar
inverter = _Inverter_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 30),
    _Inverter_Type()
)
inverter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverter.setStatus("current")
if mibBuilder.loadTexts:
    inverter.setUnits("N/A")


class _Mal_freeze_Type(Integer32):
    """Custom type mal_freeze based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_freeze_Type.__name__ = "Integer32"
_Mal_freeze_Object = MibScalar
mal_freeze = _Mal_freeze_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 46),
    _Mal_freeze_Type()
)
mal_freeze.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_freeze.setStatus("current")
if mibBuilder.loadTexts:
    mal_freeze.setUnits("N/A")


class _Mal_comp_Type(Integer32):
    """Custom type mal_comp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_comp_Type.__name__ = "Integer32"
_Mal_comp_Object = MibScalar
mal_comp = _Mal_comp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 47),
    _Mal_comp_Type()
)
mal_comp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_comp.setStatus("current")
if mibBuilder.loadTexts:
    mal_comp.setUnits("N/A")


class _Mal_evap_flow_Type(Integer32):
    """Custom type mal_evap_flow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_evap_flow_Type.__name__ = "Integer32"
_Mal_evap_flow_Object = MibScalar
mal_evap_flow = _Mal_evap_flow_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 48),
    _Mal_evap_flow_Type()
)
mal_evap_flow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_evap_flow.setStatus("current")
if mibBuilder.loadTexts:
    mal_evap_flow.setUnits("N/A")


class _Mal_cond_flow_Type(Integer32):
    """Custom type mal_cond_flow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_cond_flow_Type.__name__ = "Integer32"
_Mal_cond_flow_Object = MibScalar
mal_cond_flow = _Mal_cond_flow_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 49),
    _Mal_cond_flow_Type()
)
mal_cond_flow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_cond_flow.setStatus("current")
if mibBuilder.loadTexts:
    mal_cond_flow.setUnits("N/A")


class _Mal_high_press_Type(Integer32):
    """Custom type mal_high_press based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_high_press_Type.__name__ = "Integer32"
_Mal_high_press_Object = MibScalar
mal_high_press = _Mal_high_press_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 50),
    _Mal_high_press_Type()
)
mal_high_press.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_high_press.setStatus("current")
if mibBuilder.loadTexts:
    mal_high_press.setUnits("N/A")


class _Mal_oil_level_Type(Integer32):
    """Custom type mal_oil_level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_oil_level_Type.__name__ = "Integer32"
_Mal_oil_level_Object = MibScalar
mal_oil_level = _Mal_oil_level_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 51),
    _Mal_oil_level_Type()
)
mal_oil_level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_oil_level.setStatus("current")
if mibBuilder.loadTexts:
    mal_oil_level.setUnits("N/A")


class _Mal_low_pres_Type(Integer32):
    """Custom type mal_low_pres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_low_pres_Type.__name__ = "Integer32"
_Mal_low_pres_Object = MibScalar
mal_low_pres = _Mal_low_pres_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 52),
    _Mal_low_pres_Type()
)
mal_low_pres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_low_pres.setStatus("current")
if mibBuilder.loadTexts:
    mal_low_pres.setUnits("N/A")


class _Mal_hp_transd_Type(Integer32):
    """Custom type mal_hp_transd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_hp_transd_Type.__name__ = "Integer32"
_Mal_hp_transd_Object = MibScalar
mal_hp_transd = _Mal_hp_transd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 53),
    _Mal_hp_transd_Type()
)
mal_hp_transd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_hp_transd.setStatus("current")
if mibBuilder.loadTexts:
    mal_hp_transd.setUnits("N/A")


class _Mal_serious_Type(Integer32):
    """Custom type mal_serious based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_serious_Type.__name__ = "Integer32"
_Mal_serious_Object = MibScalar
mal_serious = _Mal_serious_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 54),
    _Mal_serious_Type()
)
mal_serious.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_serious.setStatus("current")
if mibBuilder.loadTexts:
    mal_serious.setUnits("N/A")


class _Mal_fan1_Type(Integer32):
    """Custom type mal_fan1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_fan1_Type.__name__ = "Integer32"
_Mal_fan1_Object = MibScalar
mal_fan1 = _Mal_fan1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 55),
    _Mal_fan1_Type()
)
mal_fan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_fan1.setStatus("current")
if mibBuilder.loadTexts:
    mal_fan1.setUnits("N/A")


class _Mal_fan2_Type(Integer32):
    """Custom type mal_fan2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_fan2_Type.__name__ = "Integer32"
_Mal_fan2_Object = MibScalar
mal_fan2 = _Mal_fan2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 56),
    _Mal_fan2_Type()
)
mal_fan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_fan2.setStatus("current")
if mibBuilder.loadTexts:
    mal_fan2.setUnits("N/A")


class _Mal_pump_evap_Type(Integer32):
    """Custom type mal_pump_evap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_pump_evap_Type.__name__ = "Integer32"
_Mal_pump_evap_Object = MibScalar
mal_pump_evap = _Mal_pump_evap_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 57),
    _Mal_pump_evap_Type()
)
mal_pump_evap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_pump_evap.setStatus("current")
if mibBuilder.loadTexts:
    mal_pump_evap.setUnits("N/A")


class _Mal_master_offl_Type(Integer32):
    """Custom type mal_master_offl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_master_offl_Type.__name__ = "Integer32"
_Mal_master_offl_Object = MibScalar
mal_master_offl = _Mal_master_offl_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 58),
    _Mal_master_offl_Type()
)
mal_master_offl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_master_offl.setStatus("current")
if mibBuilder.loadTexts:
    mal_master_offl.setUnits("N/A")


class _Mal_unit2_offl_Type(Integer32):
    """Custom type mal_unit2_offl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_unit2_offl_Type.__name__ = "Integer32"
_Mal_unit2_offl_Object = MibScalar
mal_unit2_offl = _Mal_unit2_offl_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 59),
    _Mal_unit2_offl_Type()
)
mal_unit2_offl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_unit2_offl.setStatus("current")
if mibBuilder.loadTexts:
    mal_unit2_offl.setUnits("N/A")


class _Mal_unit3_offl_Type(Integer32):
    """Custom type mal_unit3_offl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_unit3_offl_Type.__name__ = "Integer32"
_Mal_unit3_offl_Object = MibScalar
mal_unit3_offl = _Mal_unit3_offl_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 60),
    _Mal_unit3_offl_Type()
)
mal_unit3_offl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_unit3_offl.setStatus("current")
if mibBuilder.loadTexts:
    mal_unit3_offl.setUnits("N/A")


class _Mal_unit4_offl_Type(Integer32):
    """Custom type mal_unit4_offl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_unit4_offl_Type.__name__ = "Integer32"
_Mal_unit4_offl_Object = MibScalar
mal_unit4_offl = _Mal_unit4_offl_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 61),
    _Mal_unit4_offl_Type()
)
mal_unit4_offl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_unit4_offl.setStatus("current")
if mibBuilder.loadTexts:
    mal_unit4_offl.setUnits("N/A")


class _Mal_b1_Type(Integer32):
    """Custom type mal_b1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_b1_Type.__name__ = "Integer32"
_Mal_b1_Object = MibScalar
mal_b1 = _Mal_b1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 62),
    _Mal_b1_Type()
)
mal_b1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_b1.setStatus("current")
if mibBuilder.loadTexts:
    mal_b1.setUnits("N/A")


class _Mal_b2_Type(Integer32):
    """Custom type mal_b2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_b2_Type.__name__ = "Integer32"
_Mal_b2_Object = MibScalar
mal_b2 = _Mal_b2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 63),
    _Mal_b2_Type()
)
mal_b2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_b2.setStatus("current")
if mibBuilder.loadTexts:
    mal_b2.setUnits("N/A")


class _Mal_b3_Type(Integer32):
    """Custom type mal_b3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_b3_Type.__name__ = "Integer32"
_Mal_b3_Object = MibScalar
mal_b3 = _Mal_b3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 64),
    _Mal_b3_Type()
)
mal_b3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_b3.setStatus("current")
if mibBuilder.loadTexts:
    mal_b3.setUnits("N/A")


class _Mal_b4_Type(Integer32):
    """Custom type mal_b4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_b4_Type.__name__ = "Integer32"
_Mal_b4_Object = MibScalar
mal_b4 = _Mal_b4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 65),
    _Mal_b4_Type()
)
mal_b4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_b4.setStatus("current")
if mibBuilder.loadTexts:
    mal_b4.setUnits("N/A")


class _Mal_b5_Type(Integer32):
    """Custom type mal_b5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_b5_Type.__name__ = "Integer32"
_Mal_b5_Object = MibScalar
mal_b5 = _Mal_b5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 66),
    _Mal_b5_Type()
)
mal_b5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_b5.setStatus("current")
if mibBuilder.loadTexts:
    mal_b5.setUnits("N/A")


class _Mal_b6_Type(Integer32):
    """Custom type mal_b6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_b6_Type.__name__ = "Integer32"
_Mal_b6_Object = MibScalar
mal_b6 = _Mal_b6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 67),
    _Mal_b6_Type()
)
mal_b6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_b6.setStatus("current")
if mibBuilder.loadTexts:
    mal_b6.setUnits("N/A")


class _Mal_b7_Type(Integer32):
    """Custom type mal_b7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_b7_Type.__name__ = "Integer32"
_Mal_b7_Object = MibScalar
mal_b7 = _Mal_b7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 68),
    _Mal_b7_Type()
)
mal_b7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_b7.setStatus("current")
if mibBuilder.loadTexts:
    mal_b7.setUnits("N/A")


class _Mal_b8_Type(Integer32):
    """Custom type mal_b8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_b8_Type.__name__ = "Integer32"
_Mal_b8_Object = MibScalar
mal_b8 = _Mal_b8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 69),
    _Mal_b8_Type()
)
mal_b8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_b8.setStatus("current")
if mibBuilder.loadTexts:
    mal_b8.setUnits("N/A")


class _Mal_pump_cond_h_Type(Integer32):
    """Custom type mal_pump_cond_h based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_pump_cond_h_Type.__name__ = "Integer32"
_Mal_pump_cond_h_Object = MibScalar
mal_pump_cond_h = _Mal_pump_cond_h_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 70),
    _Mal_pump_cond_h_Type()
)
mal_pump_cond_h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_pump_cond_h.setStatus("current")
if mibBuilder.loadTexts:
    mal_pump_cond_h.setUnits("N/A")


class _Mal_comp_hour_Type(Integer32):
    """Custom type mal_comp_hour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_comp_hour_Type.__name__ = "Integer32"
_Mal_comp_hour_Object = MibScalar
mal_comp_hour = _Mal_comp_hour_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 71),
    _Mal_comp_hour_Type()
)
mal_comp_hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_comp_hour.setStatus("current")
if mibBuilder.loadTexts:
    mal_comp_hour.setUnits("N/A")


class _Mal_pump_cond_Type(Integer32):
    """Custom type mal_pump_cond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_pump_cond_Type.__name__ = "Integer32"
_Mal_pump_cond_Object = MibScalar
mal_pump_cond = _Mal_pump_cond_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 72),
    _Mal_pump_cond_Type()
)
mal_pump_cond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_pump_cond.setStatus("current")
if mibBuilder.loadTexts:
    mal_pump_cond.setUnits("N/A")


class _Mal_clock32_Type(Integer32):
    """Custom type mal_clock32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_clock32_Type.__name__ = "Integer32"
_Mal_clock32_Object = MibScalar
mal_clock32 = _Mal_clock32_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 73),
    _Mal_clock32_Type()
)
mal_clock32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_clock32.setStatus("current")
if mibBuilder.loadTexts:
    mal_clock32.setUnits("N/A")


class _Mal_phase_Type(Integer32):
    """Custom type mal_phase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_phase_Type.__name__ = "Integer32"
_Mal_phase_Object = MibScalar
mal_phase = _Mal_phase_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 74),
    _Mal_phase_Type()
)
mal_phase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_phase.setStatus("current")
if mibBuilder.loadTexts:
    mal_phase.setUnits("N/A")


class _Mal_ld_transd_Type(Integer32):
    """Custom type mal_ld_transd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_ld_transd_Type.__name__ = "Integer32"
_Mal_ld_transd_Object = MibScalar
mal_ld_transd = _Mal_ld_transd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 75),
    _Mal_ld_transd_Type()
)
mal_ld_transd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_ld_transd.setStatus("current")
if mibBuilder.loadTexts:
    mal_ld_transd.setUnits("N/A")


class _Mal_voltage_Type(Integer32):
    """Custom type mal_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_voltage_Type.__name__ = "Integer32"
_Mal_voltage_Object = MibScalar
mal_voltage = _Mal_voltage_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 76),
    _Mal_voltage_Type()
)
mal_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_voltage.setStatus("current")
if mibBuilder.loadTexts:
    mal_voltage.setUnits("N/A")


class _Mal_current_Type(Integer32):
    """Custom type mal_current based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_current_Type.__name__ = "Integer32"
_Mal_current_Object = MibScalar
mal_current = _Mal_current_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 77),
    _Mal_current_Type()
)
mal_current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_current.setStatus("current")
if mibBuilder.loadTexts:
    mal_current.setUnits("N/A")


class _Mal_pump_ev_h_Type(Integer32):
    """Custom type mal_pump_ev_h based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_pump_ev_h_Type.__name__ = "Integer32"
_Mal_pump_ev_h_Object = MibScalar
mal_pump_ev_h = _Mal_pump_ev_h_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 78),
    _Mal_pump_ev_h_Type()
)
mal_pump_ev_h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_pump_ev_h.setStatus("current")
if mibBuilder.loadTexts:
    mal_pump_ev_h.setUnits("N/A")


class _Mal_disch_temp_Type(Integer32):
    """Custom type mal_disch_temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_disch_temp_Type.__name__ = "Integer32"
_Mal_disch_temp_Object = MibScalar
mal_disch_temp = _Mal_disch_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 80),
    _Mal_disch_temp_Type()
)
mal_disch_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_disch_temp.setStatus("current")
if mibBuilder.loadTexts:
    mal_disch_temp.setUnits("N/A")


class _Mal_diff_pres_Type(Integer32):
    """Custom type mal_diff_pres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_diff_pres_Type.__name__ = "Integer32"
_Mal_diff_pres_Object = MibScalar
mal_diff_pres = _Mal_diff_pres_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 81),
    _Mal_diff_pres_Type()
)
mal_diff_pres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_diff_pres.setStatus("current")
if mibBuilder.loadTexts:
    mal_diff_pres.setUnits("N/A")


class _Mal_alco1_67_r_Type(Integer32):
    """Custom type mal_alco1_67_r based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_alco1_67_r_Type.__name__ = "Integer32"
_Mal_alco1_67_r_Object = MibScalar
mal_alco1_67_r = _Mal_alco1_67_r_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 82),
    _Mal_alco1_67_r_Type()
)
mal_alco1_67_r.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_alco1_67_r.setStatus("current")
if mibBuilder.loadTexts:
    mal_alco1_67_r.setUnits("N/A")


class _Mal_alco1_68_r_Type(Integer32):
    """Custom type mal_alco1_68_r based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_alco1_68_r_Type.__name__ = "Integer32"
_Mal_alco1_68_r_Object = MibScalar
mal_alco1_68_r = _Mal_alco1_68_r_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 83),
    _Mal_alco1_68_r_Type()
)
mal_alco1_68_r.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_alco1_68_r.setStatus("current")
if mibBuilder.loadTexts:
    mal_alco1_68_r.setUnits("N/A")


class _Mal_alco1_69_r_Type(Integer32):
    """Custom type mal_alco1_69_r based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_alco1_69_r_Type.__name__ = "Integer32"
_Mal_alco1_69_r_Object = MibScalar
mal_alco1_69_r = _Mal_alco1_69_r_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 84),
    _Mal_alco1_69_r_Type()
)
mal_alco1_69_r.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_alco1_69_r.setStatus("current")
if mibBuilder.loadTexts:
    mal_alco1_69_r.setUnits("N/A")


class _Mal_alco1_70_r_Type(Integer32):
    """Custom type mal_alco1_70_r based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_alco1_70_r_Type.__name__ = "Integer32"
_Mal_alco1_70_r_Object = MibScalar
mal_alco1_70_r = _Mal_alco1_70_r_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 85),
    _Mal_alco1_70_r_Type()
)
mal_alco1_70_r.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_alco1_70_r.setStatus("current")
if mibBuilder.loadTexts:
    mal_alco1_70_r.setUnits("N/A")


class _Mal_alco1_71_r_Type(Integer32):
    """Custom type mal_alco1_71_r based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_alco1_71_r_Type.__name__ = "Integer32"
_Mal_alco1_71_r_Object = MibScalar
mal_alco1_71_r = _Mal_alco1_71_r_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 86),
    _Mal_alco1_71_r_Type()
)
mal_alco1_71_r.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_alco1_71_r.setStatus("current")
if mibBuilder.loadTexts:
    mal_alco1_71_r.setUnits("N/A")


class _Mal_alco1_72_r_Type(Integer32):
    """Custom type mal_alco1_72_r based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_alco1_72_r_Type.__name__ = "Integer32"
_Mal_alco1_72_r_Object = MibScalar
mal_alco1_72_r = _Mal_alco1_72_r_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 87),
    _Mal_alco1_72_r_Type()
)
mal_alco1_72_r.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_alco1_72_r.setStatus("current")
if mibBuilder.loadTexts:
    mal_alco1_72_r.setUnits("N/A")


class _Mal_alco1_73_r_Type(Integer32):
    """Custom type mal_alco1_73_r based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_alco1_73_r_Type.__name__ = "Integer32"
_Mal_alco1_73_r_Object = MibScalar
mal_alco1_73_r = _Mal_alco1_73_r_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 88),
    _Mal_alco1_73_r_Type()
)
mal_alco1_73_r.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_alco1_73_r.setStatus("current")
if mibBuilder.loadTexts:
    mal_alco1_73_r.setUnits("N/A")


class _Mal_alco1_74_r_Type(Integer32):
    """Custom type mal_alco1_74_r based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_alco1_74_r_Type.__name__ = "Integer32"
_Mal_alco1_74_r_Object = MibScalar
mal_alco1_74_r = _Mal_alco1_74_r_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 89),
    _Mal_alco1_74_r_Type()
)
mal_alco1_74_r.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_alco1_74_r.setStatus("current")
if mibBuilder.loadTexts:
    mal_alco1_74_r.setUnits("N/A")


class _Mal_alco1_75_r_Type(Integer32):
    """Custom type mal_alco1_75_r based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_alco1_75_r_Type.__name__ = "Integer32"
_Mal_alco1_75_r_Object = MibScalar
mal_alco1_75_r = _Mal_alco1_75_r_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 90),
    _Mal_alco1_75_r_Type()
)
mal_alco1_75_r.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_alco1_75_r.setStatus("current")
if mibBuilder.loadTexts:
    mal_alco1_75_r.setUnits("N/A")


class _Mal_alco1_760_r_Type(Integer32):
    """Custom type mal_alco1_760_r based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_alco1_760_r_Type.__name__ = "Integer32"
_Mal_alco1_760_r_Object = MibScalar
mal_alco1_760_r = _Mal_alco1_760_r_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 91),
    _Mal_alco1_760_r_Type()
)
mal_alco1_760_r.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_alco1_760_r.setStatus("current")
if mibBuilder.loadTexts:
    mal_alco1_760_r.setUnits("N/A")


class _Mal_alco1_97_r_Type(Integer32):
    """Custom type mal_alco1_97_r based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mal_alco1_97_r_Type.__name__ = "Integer32"
_Mal_alco1_97_r_Object = MibScalar
mal_alco1_97_r = _Mal_alco1_97_r_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 92),
    _Mal_alco1_97_r_Type()
)
mal_alco1_97_r.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mal_alco1_97_r.setStatus("current")
if mibBuilder.loadTexts:
    mal_alco1_97_r.setUnits("N/A")
_AnalogObjects_ObjectIdentity = ObjectIdentity
analogObjects = _AnalogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2)
)


class _Ain_1_Type(Integer32):
    """Custom type ain_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ain_1_Type.__name__ = "Integer32"
_Ain_1_Object = MibScalar
ain_1 = _Ain_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 1),
    _Ain_1_Type()
)
ain_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ain_1.setStatus("current")
if mibBuilder.loadTexts:
    ain_1.setUnits("C/F x10")


class _Ain_2_Type(Integer32):
    """Custom type ain_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ain_2_Type.__name__ = "Integer32"
_Ain_2_Object = MibScalar
ain_2 = _Ain_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 2),
    _Ain_2_Type()
)
ain_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ain_2.setStatus("current")
if mibBuilder.loadTexts:
    ain_2.setUnits("C/F x10")


class _Ain_3_Type(Integer32):
    """Custom type ain_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ain_3_Type.__name__ = "Integer32"
_Ain_3_Object = MibScalar
ain_3 = _Ain_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 3),
    _Ain_3_Type()
)
ain_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ain_3.setStatus("current")
if mibBuilder.loadTexts:
    ain_3.setUnits("C/F x10")


class _Ain_5_Type(Integer32):
    """Custom type ain_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ain_5_Type.__name__ = "Integer32"
_Ain_5_Object = MibScalar
ain_5 = _Ain_5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 5),
    _Ain_5_Type()
)
ain_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ain_5.setStatus("current")
if mibBuilder.loadTexts:
    ain_5.setUnits("V/A/C x10")


class _Ain_6_Type(Integer32):
    """Custom type ain_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ain_6_Type.__name__ = "Integer32"
_Ain_6_Object = MibScalar
ain_6 = _Ain_6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 6),
    _Ain_6_Type()
)
ain_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ain_6.setStatus("current")
if mibBuilder.loadTexts:
    ain_6.setUnits("N/A")


class _Ain_7_Type(Integer32):
    """Custom type ain_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ain_7_Type.__name__ = "Integer32"
_Ain_7_Object = MibScalar
ain_7 = _Ain_7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 7),
    _Ain_7_Type()
)
ain_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ain_7.setStatus("current")
if mibBuilder.loadTexts:
    ain_7.setUnits("% x10")


class _Ain_8_Type(Integer32):
    """Custom type ain_8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ain_8_Type.__name__ = "Integer32"
_Ain_8_Object = MibScalar
ain_8 = _Ain_8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 8),
    _Ain_8_Type()
)
ain_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ain_8.setStatus("current")
if mibBuilder.loadTexts:
    ain_8.setUnits("N/A")


class _Aout_1_display_Type(Integer32):
    """Custom type aout_1_display based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Aout_1_display_Type.__name__ = "Integer32"
_Aout_1_display_Object = MibScalar
aout_1_display = _Aout_1_display_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 9),
    _Aout_1_display_Type()
)
aout_1_display.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aout_1_display.setStatus("current")
if mibBuilder.loadTexts:
    aout_1_display.setUnits("N/A")


class _S_temp_setpoint_Type(Integer32):
    """Custom type s_temp_setpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_S_temp_setpoint_Type.__name__ = "Integer32"
_S_temp_setpoint_Object = MibScalar
s_temp_setpoint = _S_temp_setpoint_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 11),
    _S_temp_setpoint_Type()
)
s_temp_setpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s_temp_setpoint.setStatus("current")
if mibBuilder.loadTexts:
    s_temp_setpoint.setUnits("N/A")


class _W_temp_setpoint_Type(Integer32):
    """Custom type w_temp_setpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_W_temp_setpoint_Type.__name__ = "Integer32"
_W_temp_setpoint_Object = MibScalar
w_temp_setpoint = _W_temp_setpoint_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 12),
    _W_temp_setpoint_Type()
)
w_temp_setpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w_temp_setpoint.setStatus("current")
if mibBuilder.loadTexts:
    w_temp_setpoint.setUnits("N/A")


class _Cond_setpoint_Type(Integer32):
    """Custom type cond_setpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Cond_setpoint_Type.__name__ = "Integer32"
_Cond_setpoint_Object = MibScalar
cond_setpoint = _Cond_setpoint_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 13),
    _Cond_setpoint_Type()
)
cond_setpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cond_setpoint.setStatus("current")
if mibBuilder.loadTexts:
    cond_setpoint.setUnits("N/A")


class _In_temp_band_Type(Integer32):
    """Custom type in_temp_band based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_In_temp_band_Type.__name__ = "Integer32"
_In_temp_band_Object = MibScalar
in_temp_band = _In_temp_band_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 14),
    _In_temp_band_Type()
)
in_temp_band.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    in_temp_band.setStatus("current")
if mibBuilder.loadTexts:
    in_temp_band.setUnits("N/A")
_IntegerObjects_ObjectIdentity = ObjectIdentity
integerObjects = _IntegerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3)
)


class _Unit_status_Type(Integer32):
    """Custom type unit_status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Unit_status_Type.__name__ = "Integer32"
_Unit_status_Object = MibScalar
unit_status = _Unit_status_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 1),
    _Unit_status_Type()
)
unit_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit_status.setStatus("current")
if mibBuilder.loadTexts:
    unit_status.setUnits("N/A")


class _Net_address_Type(Integer32):
    """Custom type net_address based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Net_address_Type.__name__ = "Integer32"
_Net_address_Object = MibScalar
net_address = _Net_address_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 2),
    _Net_address_Type()
)
net_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    net_address.setStatus("current")
if mibBuilder.loadTexts:
    net_address.setUnits("N/A")


class _Cound_fans_mng_Type(Integer32):
    """Custom type cound_fans_mng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Cound_fans_mng_Type.__name__ = "Integer32"
_Cound_fans_mng_Object = MibScalar
cound_fans_mng = _Cound_fans_mng_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 3),
    _Cound_fans_mng_Type()
)
cound_fans_mng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cound_fans_mng.setStatus("current")
if mibBuilder.loadTexts:
    cound_fans_mng.setUnits("N/A")


class _Config_type_Type(Integer32):
    """Custom type config_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Config_type_Type.__name__ = "Integer32"
_Config_type_Object = MibScalar
config_type = _Config_type_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 4),
    _Config_type_Type()
)
config_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config_type.setStatus("current")
if mibBuilder.loadTexts:
    config_type.setUnits("N/A")


class _Number_comps_Type(Integer32):
    """Custom type number_comps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Number_comps_Type.__name__ = "Integer32"
_Number_comps_Object = MibScalar
number_comps = _Number_comps_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 5),
    _Number_comps_Type()
)
number_comps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    number_comps.setStatus("current")
if mibBuilder.loadTexts:
    number_comps.setUnits("N/A")


class _Cond_fans_Type(Integer32):
    """Custom type cond_fans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Cond_fans_Type.__name__ = "Integer32"
_Cond_fans_Object = MibScalar
cond_fans = _Cond_fans_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 6),
    _Cond_fans_Type()
)
cond_fans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cond_fans.setStatus("current")
if mibBuilder.loadTexts:
    cond_fans.setUnits("N/A")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAREL-screw_compressor-MIB",
    **{"carel": carel,
       "systm": systm,
       "agentRelease": agentRelease,
       "agentCode": agentCode,
       "instruments": instruments,
       "webGateInfo": webGateInfo,
       "agentParameters": agentParameters,
       "netSize": netSize,
       "baudRate": baudRate,
       "unitTypeGroup": unitTypeGroup,
       "unit1-Type": unit1_Type,
       "unitCodeGroup": unitCodeGroup,
       "unit1-Code": unit1_Code,
       "unitSoftwareReleaseGroup": unitSoftwareReleaseGroup,
       "unit1-SoftwareRelease": unit1_SoftwareRelease,
       "unitMinSoftwareReleaseGroup": unitMinSoftwareReleaseGroup,
       "unit1-MinSoftwareRelease": unit1_MinSoftwareRelease,
       "unitMaxSoftwareReleaseGroup": unitMaxSoftwareReleaseGroup,
       "unit1-MaxSoftwareRelease": unit1_MaxSoftwareRelease,
       "unitNoAnswerCounterGroup": unitNoAnswerCounterGroup,
       "unit1-NoAnswerCounter": unit1_NoAnswerCounter,
       "unitErrorChecksumCounterGroup": unitErrorChecksumCounterGroup,
       "unit1-ErrorChecksumCounter": unit1_ErrorChecksumCounter,
       "unitTimeoutCounterGroup": unitTimeoutCounterGroup,
       "unit1-TimeoutCounter": unit1_TimeoutCounter,
       "unitOnLineStatusGroup": unitOnLineStatusGroup,
       "unit1-OnLineStatus": unit1_OnLineStatus,
       "screw_compressorMIB": screw_compressorMIB,
       "digitalObjects": digitalObjects,
       "syson_s": syson_s,
       "dout_1": dout_1,
       "dout_2": dout_2,
       "dout_3": dout_3,
       "dout_4": dout_4,
       "dout_5": dout_5,
       "dout_6": dout_6,
       "dout_7": dout_7,
       "dout_8": dout_8,
       "dout_9": dout_9,
       "dout_10": dout_10,
       "dout_11": dout_11,
       "dout_12": dout_12,
       "dout_13": dout_13,
       "en_evap_flow_al": en_evap_flow_al,
       "en_b1": en_b1,
       "en_b2": en_b2,
       "en_b3": en_b3,
       "en_b4": en_b4,
       "en_b5": en_b5,
       "en_b6": en_b6,
       "en_b7": en_b7,
       "en_b8": en_b8,
       "superv_onoff": superv_onoff,
       "en_start_restr": en_start_restr,
       "en_modulation": en_modulation,
       "sun_win_sel": sun_win_sel,
       "cooling_heating": cooling_heating,
       "inverter": inverter,
       "mal_freeze": mal_freeze,
       "mal_comp": mal_comp,
       "mal_evap_flow": mal_evap_flow,
       "mal_cond_flow": mal_cond_flow,
       "mal_high_press": mal_high_press,
       "mal_oil_level": mal_oil_level,
       "mal_low_pres": mal_low_pres,
       "mal_hp_transd": mal_hp_transd,
       "mal_serious": mal_serious,
       "mal_fan1": mal_fan1,
       "mal_fan2": mal_fan2,
       "mal_pump_evap": mal_pump_evap,
       "mal_master_offl": mal_master_offl,
       "mal_unit2_offl": mal_unit2_offl,
       "mal_unit3_offl": mal_unit3_offl,
       "mal_unit4_offl": mal_unit4_offl,
       "mal_b1": mal_b1,
       "mal_b2": mal_b2,
       "mal_b3": mal_b3,
       "mal_b4": mal_b4,
       "mal_b5": mal_b5,
       "mal_b6": mal_b6,
       "mal_b7": mal_b7,
       "mal_b8": mal_b8,
       "mal_pump_cond_h": mal_pump_cond_h,
       "mal_comp_hour": mal_comp_hour,
       "mal_pump_cond": mal_pump_cond,
       "mal_clock32": mal_clock32,
       "mal_phase": mal_phase,
       "mal_ld_transd": mal_ld_transd,
       "mal_voltage": mal_voltage,
       "mal_current": mal_current,
       "mal_pump_ev_h": mal_pump_ev_h,
       "mal_disch_temp": mal_disch_temp,
       "mal_diff_pres": mal_diff_pres,
       "mal_alco1_67_r": mal_alco1_67_r,
       "mal_alco1_68_r": mal_alco1_68_r,
       "mal_alco1_69_r": mal_alco1_69_r,
       "mal_alco1_70_r": mal_alco1_70_r,
       "mal_alco1_71_r": mal_alco1_71_r,
       "mal_alco1_72_r": mal_alco1_72_r,
       "mal_alco1_73_r": mal_alco1_73_r,
       "mal_alco1_74_r": mal_alco1_74_r,
       "mal_alco1_75_r": mal_alco1_75_r,
       "mal_alco1_760_r": mal_alco1_760_r,
       "mal_alco1_97_r": mal_alco1_97_r,
       "analogObjects": analogObjects,
       "ain_1": ain_1,
       "ain_2": ain_2,
       "ain_3": ain_3,
       "ain_5": ain_5,
       "ain_6": ain_6,
       "ain_7": ain_7,
       "ain_8": ain_8,
       "aout_1_display": aout_1_display,
       "s_temp_setpoint": s_temp_setpoint,
       "w_temp_setpoint": w_temp_setpoint,
       "cond_setpoint": cond_setpoint,
       "in_temp_band": in_temp_band,
       "integerObjects": integerObjects,
       "unit_status": unit_status,
       "net_address": net_address,
       "cound_fans_mng": cound_fans_mng,
       "config_type": config_type,
       "number_comps": number_comps,
       "cond_fans": cond_fans}
)
