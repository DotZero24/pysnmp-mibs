# SNMP MIB module (CAREL-mio-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/carel/CAREL-mio-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:04 2025
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

mioMIB = ModuleIdentity(
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


class _Buz_Type(Integer32):
    """Custom type buz based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Buz_Type.__name__ = "Integer32"
_Buz_Object = MibScalar
buz = _Buz_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 1),
    _Buz_Type()
)
buz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buz.setStatus("current")
if mibBuilder.loadTexts:
    buz.setUnits("N/A")


class _Cf_Type(Integer32):
    """Custom type cf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cf_Type.__name__ = "Integer32"
_Cf_Object = MibScalar
cf = _Cf_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 2),
    _Cf_Type()
)
cf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cf.setStatus("current")
if mibBuilder.loadTexts:
    cf.setUnits("N/A")


class _Mtd1_Type(Integer32):
    """Custom type mtd1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mtd1_Type.__name__ = "Integer32"
_Mtd1_Object = MibScalar
mtd1 = _Mtd1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 3),
    _Mtd1_Type()
)
mtd1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtd1.setStatus("current")
if mibBuilder.loadTexts:
    mtd1.setUnits("N/A")


class _Mtd2_Type(Integer32):
    """Custom type mtd2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mtd2_Type.__name__ = "Integer32"
_Mtd2_Object = MibScalar
mtd2 = _Mtd2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 4),
    _Mtd2_Type()
)
mtd2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtd2.setStatus("current")
if mibBuilder.loadTexts:
    mtd2.setUnits("N/A")


class _Mtd5_Type(Integer32):
    """Custom type mtd5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mtd5_Type.__name__ = "Integer32"
_Mtd5_Object = MibScalar
mtd5 = _Mtd5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 7),
    _Mtd5_Type()
)
mtd5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtd5.setStatus("current")
if mibBuilder.loadTexts:
    mtd5.setUnits("N/A")


class _Mtd6_Type(Integer32):
    """Custom type mtd6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mtd6_Type.__name__ = "Integer32"
_Mtd6_Object = MibScalar
mtd6 = _Mtd6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 8),
    _Mtd6_Type()
)
mtd6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtd6.setStatus("current")
if mibBuilder.loadTexts:
    mtd6.setUnits("N/A")


class _Rele1_pwup_Type(Integer32):
    """Custom type rele1_pwup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Rele1_pwup_Type.__name__ = "Integer32"
_Rele1_pwup_Object = MibScalar
rele1_pwup = _Rele1_pwup_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 9),
    _Rele1_pwup_Type()
)
rele1_pwup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rele1_pwup.setStatus("current")
if mibBuilder.loadTexts:
    rele1_pwup.setUnits("N/A")


class _Buzz_pwup_Type(Integer32):
    """Custom type buzz_pwup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Buzz_pwup_Type.__name__ = "Integer32"
_Buzz_pwup_Object = MibScalar
buzz_pwup = _Buzz_pwup_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 13),
    _Buzz_pwup_Type()
)
buzz_pwup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buzz_pwup.setStatus("current")
if mibBuilder.loadTexts:
    buzz_pwup.setUnits("N/A")


class _Di1_Type(Integer32):
    """Custom type di1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Di1_Type.__name__ = "Integer32"
_Di1_Object = MibScalar
di1 = _Di1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 14),
    _Di1_Type()
)
di1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    di1.setStatus("current")
if mibBuilder.loadTexts:
    di1.setUnits("N/A")


class _Di2_Type(Integer32):
    """Custom type di2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Di2_Type.__name__ = "Integer32"
_Di2_Object = MibScalar
di2 = _Di2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 15),
    _Di2_Type()
)
di2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    di2.setStatus("current")
if mibBuilder.loadTexts:
    di2.setUnits("N/A")


class _Di5_Type(Integer32):
    """Custom type di5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Di5_Type.__name__ = "Integer32"
_Di5_Object = MibScalar
di5 = _Di5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 18),
    _Di5_Type()
)
di5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    di5.setStatus("current")
if mibBuilder.loadTexts:
    di5.setUnits("N/A")


class _Di6_Type(Integer32):
    """Custom type di6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Di6_Type.__name__ = "Integer32"
_Di6_Object = MibScalar
di6 = _Di6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 19),
    _Di6_Type()
)
di6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    di6.setStatus("current")
if mibBuilder.loadTexts:
    di6.setUnits("N/A")


class _Ag_Type(Integer32):
    """Custom type ag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ag_Type.__name__ = "Integer32"
_Ag_Object = MibScalar
ag = _Ag_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 20),
    _Ag_Type()
)
ag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ag.setStatus("current")
if mibBuilder.loadTexts:
    ag.setUnits("N/A")


class _At1h_Type(Integer32):
    """Custom type at1h based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_At1h_Type.__name__ = "Integer32"
_At1h_Object = MibScalar
at1h = _At1h_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 21),
    _At1h_Type()
)
at1h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at1h.setStatus("current")
if mibBuilder.loadTexts:
    at1h.setUnits("N/A")


class _At1l_Type(Integer32):
    """Custom type at1l based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_At1l_Type.__name__ = "Integer32"
_At1l_Object = MibScalar
at1l = _At1l_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 22),
    _At1l_Type()
)
at1l.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at1l.setStatus("current")
if mibBuilder.loadTexts:
    at1l.setUnits("N/A")


class _At2h_Type(Integer32):
    """Custom type at2h based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_At2h_Type.__name__ = "Integer32"
_At2h_Object = MibScalar
at2h = _At2h_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 23),
    _At2h_Type()
)
at2h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at2h.setStatus("current")
if mibBuilder.loadTexts:
    at2h.setUnits("N/A")


class _At2l_Type(Integer32):
    """Custom type at2l based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_At2l_Type.__name__ = "Integer32"
_At2l_Object = MibScalar
at2l = _At2l_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 24),
    _At2l_Type()
)
at2l.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at2l.setStatus("current")
if mibBuilder.loadTexts:
    at2l.setUnits("N/A")


class _At3h_Type(Integer32):
    """Custom type at3h based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_At3h_Type.__name__ = "Integer32"
_At3h_Object = MibScalar
at3h = _At3h_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 25),
    _At3h_Type()
)
at3h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at3h.setStatus("current")
if mibBuilder.loadTexts:
    at3h.setUnits("N/A")


class _At3l_Type(Integer32):
    """Custom type at3l based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_At3l_Type.__name__ = "Integer32"
_At3l_Object = MibScalar
at3l = _At3l_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 26),
    _At3l_Type()
)
at3l.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at3l.setStatus("current")
if mibBuilder.loadTexts:
    at3l.setUnits("N/A")


class _At4h_Type(Integer32):
    """Custom type at4h based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_At4h_Type.__name__ = "Integer32"
_At4h_Object = MibScalar
at4h = _At4h_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 27),
    _At4h_Type()
)
at4h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at4h.setStatus("current")
if mibBuilder.loadTexts:
    at4h.setUnits("N/A")


class _At4l_Type(Integer32):
    """Custom type at4l based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_At4l_Type.__name__ = "Integer32"
_At4l_Object = MibScalar
at4l = _At4l_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 28),
    _At4l_Type()
)
at4l.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at4l.setStatus("current")
if mibBuilder.loadTexts:
    at4l.setUnits("N/A")


class _Af1_Type(Integer32):
    """Custom type af1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Af1_Type.__name__ = "Integer32"
_Af1_Object = MibScalar
af1 = _Af1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 29),
    _Af1_Type()
)
af1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    af1.setStatus("current")
if mibBuilder.loadTexts:
    af1.setUnits("N/A")


class _Af2_Type(Integer32):
    """Custom type af2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Af2_Type.__name__ = "Integer32"
_Af2_Object = MibScalar
af2 = _Af2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 30),
    _Af2_Type()
)
af2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    af2.setStatus("current")
if mibBuilder.loadTexts:
    af2.setUnits("N/A")


class _Af5_Type(Integer32):
    """Custom type af5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Af5_Type.__name__ = "Integer32"
_Af5_Object = MibScalar
af5 = _Af5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 33),
    _Af5_Type()
)
af5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    af5.setStatus("current")
if mibBuilder.loadTexts:
    af5.setUnits("N/A")


class _Af6_Type(Integer32):
    """Custom type af6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Af6_Type.__name__ = "Integer32"
_Af6_Object = MibScalar
af6 = _Af6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 34),
    _Af6_Type()
)
af6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    af6.setStatus("current")
if mibBuilder.loadTexts:
    af6.setUnits("N/A")


class _As1_Type(Integer32):
    """Custom type as1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_As1_Type.__name__ = "Integer32"
_As1_Object = MibScalar
as1 = _As1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 35),
    _As1_Type()
)
as1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as1.setStatus("current")
if mibBuilder.loadTexts:
    as1.setUnits("N/A")


class _As2_Type(Integer32):
    """Custom type as2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_As2_Type.__name__ = "Integer32"
_As2_Object = MibScalar
as2 = _As2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 36),
    _As2_Type()
)
as2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2.setStatus("current")
if mibBuilder.loadTexts:
    as2.setUnits("N/A")


class _As3_Type(Integer32):
    """Custom type as3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_As3_Type.__name__ = "Integer32"
_As3_Object = MibScalar
as3 = _As3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 37),
    _As3_Type()
)
as3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as3.setStatus("current")
if mibBuilder.loadTexts:
    as3.setUnits("N/A")


class _As4_Type(Integer32):
    """Custom type as4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_As4_Type.__name__ = "Integer32"
_As4_Object = MibScalar
as4 = _As4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 38),
    _As4_Type()
)
as4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as4.setStatus("current")
if mibBuilder.loadTexts:
    as4.setUnits("N/A")


class _Ahw_Type(Integer32):
    """Custom type ahw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ahw_Type.__name__ = "Integer32"
_Ahw_Object = MibScalar
ahw = _Ahw_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 39),
    _Ahw_Type()
)
ahw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahw.setStatus("current")
if mibBuilder.loadTexts:
    ahw.setUnits("N/A")


class _Td1_Type(Integer32):
    """Custom type td1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Td1_Type.__name__ = "Integer32"
_Td1_Object = MibScalar
td1 = _Td1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 40),
    _Td1_Type()
)
td1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    td1.setStatus("current")
if mibBuilder.loadTexts:
    td1.setUnits("N/A")


class _Td2_Type(Integer32):
    """Custom type td2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Td2_Type.__name__ = "Integer32"
_Td2_Object = MibScalar
td2 = _Td2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 41),
    _Td2_Type()
)
td2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    td2.setStatus("current")
if mibBuilder.loadTexts:
    td2.setUnits("N/A")


class _Td5_Type(Integer32):
    """Custom type td5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Td5_Type.__name__ = "Integer32"
_Td5_Object = MibScalar
td5 = _Td5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 44),
    _Td5_Type()
)
td5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    td5.setStatus("current")
if mibBuilder.loadTexts:
    td5.setUnits("N/A")


class _Td6_Type(Integer32):
    """Custom type td6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Td6_Type.__name__ = "Integer32"
_Td6_Object = MibScalar
td6 = _Td6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 45),
    _Td6_Type()
)
td6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    td6.setStatus("current")
if mibBuilder.loadTexts:
    td6.setUnits("N/A")


class _Ct_Type(Integer32):
    """Custom type ct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ct_Type.__name__ = "Integer32"
_Ct_Object = MibScalar
ct = _Ct_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 46),
    _Ct_Type()
)
ct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ct.setStatus("current")
if mibBuilder.loadTexts:
    ct.setUnits("N/A")


class _Buzz_Type(Integer32):
    """Custom type buzz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Buzz_Type.__name__ = "Integer32"
_Buzz_Object = MibScalar
buzz = _Buzz_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 47),
    _Buzz_Type()
)
buzz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buzz.setStatus("current")
if mibBuilder.loadTexts:
    buzz.setUnits("N/A")


class _Rele1_stato_Type(Integer32):
    """Custom type rele1_stato based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Rele1_stato_Type.__name__ = "Integer32"
_Rele1_stato_Object = MibScalar
rele1_stato = _Rele1_stato_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 48),
    _Rele1_stato_Type()
)
rele1_stato.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rele1_stato.setStatus("current")
if mibBuilder.loadTexts:
    rele1_stato.setUnits("N/A")


class _Buzz_output_Type(Integer32):
    """Custom type buzz_output based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Buzz_output_Type.__name__ = "Integer32"
_Buzz_output_Object = MibScalar
buzz_output = _Buzz_output_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 52),
    _Buzz_output_Type()
)
buzz_output.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buzz_output.setStatus("current")
if mibBuilder.loadTexts:
    buzz_output.setUnits("N/A")


class _Rele1_output_Type(Integer32):
    """Custom type rele1_output based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Rele1_output_Type.__name__ = "Integer32"
_Rele1_output_Object = MibScalar
rele1_output = _Rele1_output_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 53),
    _Rele1_output_Type()
)
rele1_output.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rele1_output.setStatus("current")
if mibBuilder.loadTexts:
    rele1_output.setUnits("N/A")
_AnalogObjects_ObjectIdentity = ObjectIdentity
analogObjects = _AnalogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2)
)


class _H1_Type(Integer32):
    """Custom type h1 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 10000),
    )


_H1_Type.__name__ = "Integer32"
_H1_Object = MibScalar
h1 = _H1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 1),
    _H1_Type()
)
h1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h1.setStatus("current")
if mibBuilder.loadTexts:
    h1.setUnits("C/F x10")


class _L1_Type(Integer32):
    """Custom type l1 based on Integer32"""
    defaultValue = -1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 32767),
    )


_L1_Type.__name__ = "Integer32"
_L1_Object = MibScalar
l1 = _L1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 2),
    _L1_Type()
)
l1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l1.setStatus("current")
if mibBuilder.loadTexts:
    l1.setUnits("C/F x10")


class _H2_Type(Integer32):
    """Custom type h2 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 10000),
    )


_H2_Type.__name__ = "Integer32"
_H2_Object = MibScalar
h2 = _H2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 3),
    _H2_Type()
)
h2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h2.setStatus("current")
if mibBuilder.loadTexts:
    h2.setUnits("C/F x10")


class _L2_Type(Integer32):
    """Custom type l2 based on Integer32"""
    defaultValue = -1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 32767),
    )


_L2_Type.__name__ = "Integer32"
_L2_Object = MibScalar
l2 = _L2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 4),
    _L2_Type()
)
l2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2.setStatus("current")
if mibBuilder.loadTexts:
    l2.setUnits("C/F x10")


class _H3_Type(Integer32):
    """Custom type h3 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 10000),
    )


_H3_Type.__name__ = "Integer32"
_H3_Object = MibScalar
h3 = _H3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 5),
    _H3_Type()
)
h3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3.setStatus("current")
if mibBuilder.loadTexts:
    h3.setUnits("C/F x10")


class _L3_Type(Integer32):
    """Custom type l3 based on Integer32"""
    defaultValue = -1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 32767),
    )


_L3_Type.__name__ = "Integer32"
_L3_Object = MibScalar
l3 = _L3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 6),
    _L3_Type()
)
l3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3.setStatus("current")
if mibBuilder.loadTexts:
    l3.setUnits("C/F x10")


class _H4_Type(Integer32):
    """Custom type h4 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 10000),
    )


_H4_Type.__name__ = "Integer32"
_H4_Object = MibScalar
h4 = _H4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 7),
    _H4_Type()
)
h4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h4.setStatus("current")
if mibBuilder.loadTexts:
    h4.setUnits("C/F x10")


class _L4_Type(Integer32):
    """Custom type l4 based on Integer32"""
    defaultValue = -1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 32767),
    )


_L4_Type.__name__ = "Integer32"
_L4_Object = MibScalar
l4 = _L4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 8),
    _L4_Type()
)
l4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l4.setStatus("current")
if mibBuilder.loadTexts:
    l4.setUnits("C/F x10")


class _V3l_Type(Integer32):
    """Custom type v3l based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 32767),
    )


_V3l_Type.__name__ = "Integer32"
_V3l_Object = MibScalar
v3l = _V3l_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 9),
    _V3l_Type()
)
v3l.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3l.setStatus("current")
if mibBuilder.loadTexts:
    v3l.setUnits("bar/ x10")


class _V3h_Type(Integer32):
    """Custom type v3h based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 10000),
    )


_V3h_Type.__name__ = "Integer32"
_V3h_Object = MibScalar
v3h = _V3h_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 10),
    _V3h_Type()
)
v3h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3h.setStatus("current")
if mibBuilder.loadTexts:
    v3h.setUnits("bar/ x10")


class _V4l_Type(Integer32):
    """Custom type v4l based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 32767),
    )


_V4l_Type.__name__ = "Integer32"
_V4l_Object = MibScalar
v4l = _V4l_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 11),
    _V4l_Type()
)
v4l.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4l.setStatus("current")
if mibBuilder.loadTexts:
    v4l.setUnits("bar/ x10")


class _V4h_Type(Integer32):
    """Custom type v4h based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 10000),
    )


_V4h_Type.__name__ = "Integer32"
_V4h_Object = MibScalar
v4h = _V4h_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 12),
    _V4h_Type()
)
v4h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v4h.setStatus("current")
if mibBuilder.loadTexts:
    v4h.setUnits("bar/ x10")


class _O1_Type(Integer32):
    """Custom type o1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_O1_Type.__name__ = "Integer32"
_O1_Object = MibScalar
o1 = _O1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 13),
    _O1_Type()
)
o1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    o1.setStatus("current")
if mibBuilder.loadTexts:
    o1.setUnits("C/F x10")


class _O2_Type(Integer32):
    """Custom type o2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_O2_Type.__name__ = "Integer32"
_O2_Object = MibScalar
o2 = _O2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 14),
    _O2_Type()
)
o2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    o2.setStatus("current")
if mibBuilder.loadTexts:
    o2.setUnits("C/F x10")


class _O3_Type(Integer32):
    """Custom type o3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_O3_Type.__name__ = "Integer32"
_O3_Object = MibScalar
o3 = _O3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 15),
    _O3_Type()
)
o3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    o3.setStatus("current")
if mibBuilder.loadTexts:
    o3.setUnits("C/F x10")


class _O4_Type(Integer32):
    """Custom type o4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_O4_Type.__name__ = "Integer32"
_O4_Object = MibScalar
o4 = _O4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 16),
    _O4_Type()
)
o4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    o4.setStatus("current")
if mibBuilder.loadTexts:
    o4.setUnits("C/F x10")


class _Ds1_Type(Integer32):
    """Custom type ds1 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Ds1_Type.__name__ = "Integer32"
_Ds1_Object = MibScalar
ds1 = _Ds1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 17),
    _Ds1_Type()
)
ds1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1.setStatus("current")
if mibBuilder.loadTexts:
    ds1.setUnits("C/F x10")


class _Ds2_Type(Integer32):
    """Custom type ds2 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Ds2_Type.__name__ = "Integer32"
_Ds2_Object = MibScalar
ds2 = _Ds2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 18),
    _Ds2_Type()
)
ds2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds2.setStatus("current")
if mibBuilder.loadTexts:
    ds2.setUnits("C/F x10")


class _Ds3_Type(Integer32):
    """Custom type ds3 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Ds3_Type.__name__ = "Integer32"
_Ds3_Object = MibScalar
ds3 = _Ds3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 19),
    _Ds3_Type()
)
ds3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3.setStatus("current")
if mibBuilder.loadTexts:
    ds3.setUnits("C/F x10")


class _Ds4_Type(Integer32):
    """Custom type ds4 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Ds4_Type.__name__ = "Integer32"
_Ds4_Object = MibScalar
ds4 = _Ds4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 20),
    _Ds4_Type()
)
ds4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds4.setStatus("current")
if mibBuilder.loadTexts:
    ds4.setUnits("C/F x10")


class _S1_Type(Integer32):
    """Custom type s1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_S1_Type.__name__ = "Integer32"
_S1_Object = MibScalar
s1 = _S1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 21),
    _S1_Type()
)
s1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s1.setStatus("current")
if mibBuilder.loadTexts:
    s1.setUnits("C/F x10")


class _S2_Type(Integer32):
    """Custom type s2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_S2_Type.__name__ = "Integer32"
_S2_Object = MibScalar
s2 = _S2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 22),
    _S2_Type()
)
s2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2.setStatus("current")
if mibBuilder.loadTexts:
    s2.setUnits("C/F x10")


class _S3_Type(Integer32):
    """Custom type s3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_S3_Type.__name__ = "Integer32"
_S3_Object = MibScalar
s3 = _S3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 23),
    _S3_Type()
)
s3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3.setStatus("current")
if mibBuilder.loadTexts:
    s3.setUnits("C/F x10")


class _S4_Type(Integer32):
    """Custom type s4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_S4_Type.__name__ = "Integer32"
_S4_Object = MibScalar
s4 = _S4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 24),
    _S4_Type()
)
s4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s4.setStatus("current")
if mibBuilder.loadTexts:
    s4.setUnits("C/F x10")
_IntegerObjects_ObjectIdentity = ObjectIdentity
integerObjects = _IntegerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3)
)


class _Mod_Type(Integer32):
    """Custom type mod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mod_Type.__name__ = "Integer32"
_Mod_Object = MibScalar
mod = _Mod_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 1),
    _Mod_Type()
)
mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mod.setStatus("current")
if mibBuilder.loadTexts:
    mod.setUnits("N/A")


class _Sonde_Type(Integer32):
    """Custom type sonde based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Sonde_Type.__name__ = "Integer32"
_Sonde_Object = MibScalar
sonde = _Sonde_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 2),
    _Sonde_Type()
)
sonde.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonde.setStatus("current")
if mibBuilder.loadTexts:
    sonde.setUnits("N/A")


class _A1_Type(Integer32):
    """Custom type a1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_A1_Type.__name__ = "Integer32"
_A1_Object = MibScalar
a1 = _A1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 3),
    _A1_Type()
)
a1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1.setStatus("current")
if mibBuilder.loadTexts:
    a1.setUnits("N/A")


class _A2_Type(Integer32):
    """Custom type a2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_A2_Type.__name__ = "Integer32"
_A2_Object = MibScalar
a2 = _A2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 4),
    _A2_Type()
)
a2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2.setStatus("current")
if mibBuilder.loadTexts:
    a2.setUnits("N/A")


class _A5_Type(Integer32):
    """Custom type a5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_A5_Type.__name__ = "Integer32"
_A5_Object = MibScalar
a5 = _A5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 7),
    _A5_Type()
)
a5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a5.setStatus("current")
if mibBuilder.loadTexts:
    a5.setUnits("N/A")


class _A6_Type(Integer32):
    """Custom type a6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_A6_Type.__name__ = "Integer32"
_A6_Object = MibScalar
a6 = _A6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 8),
    _A6_Type()
)
a6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a6.setStatus("current")
if mibBuilder.loadTexts:
    a6.setUnits("N/A")


class _D1_Type(Integer32):
    """Custom type d1 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_D1_Type.__name__ = "Integer32"
_D1_Object = MibScalar
d1 = _D1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 9),
    _D1_Type()
)
d1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d1.setStatus("current")
if mibBuilder.loadTexts:
    d1.setUnits("sec.")


class _D2_Type(Integer32):
    """Custom type d2 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_D2_Type.__name__ = "Integer32"
_D2_Object = MibScalar
d2 = _D2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 10),
    _D2_Type()
)
d2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d2.setStatus("current")
if mibBuilder.loadTexts:
    d2.setUnits("sec.")


class _D5_Type(Integer32):
    """Custom type d5 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_D5_Type.__name__ = "Integer32"
_D5_Object = MibScalar
d5 = _D5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 13),
    _D5_Type()
)
d5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5.setStatus("current")
if mibBuilder.loadTexts:
    d5.setUnits("sec.")


class _D6_Type(Integer32):
    """Custom type d6 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_D6_Type.__name__ = "Integer32"
_D6_Object = MibScalar
d6 = _D6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 14),
    _D6_Type()
)
d6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d6.setStatus("current")
if mibBuilder.loadTexts:
    d6.setUnits("sec.")


class _N1_Type(Integer32):
    """Custom type n1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_N1_Type.__name__ = "Integer32"
_N1_Object = MibScalar
n1 = _N1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 15),
    _N1_Type()
)
n1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n1.setStatus("current")
if mibBuilder.loadTexts:
    n1.setUnits("N/A")


class _R1_Type(Integer32):
    """Custom type r1 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_R1_Type.__name__ = "Integer32"
_R1_Object = MibScalar
r1 = _R1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 16),
    _R1_Type()
)
r1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r1.setStatus("current")
if mibBuilder.loadTexts:
    r1.setUnits("min.")


class _F1_Type(Integer32):
    """Custom type f1 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_F1_Type.__name__ = "Integer32"
_F1_Object = MibScalar
f1 = _F1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 17),
    _F1_Type()
)
f1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f1.setStatus("current")
if mibBuilder.loadTexts:
    f1.setUnits("N/A")


class _N2_Type(Integer32):
    """Custom type n2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_N2_Type.__name__ = "Integer32"
_N2_Object = MibScalar
n2 = _N2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 18),
    _N2_Type()
)
n2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n2.setStatus("current")
if mibBuilder.loadTexts:
    n2.setUnits("N/A")


class _R2_Type(Integer32):
    """Custom type r2 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_R2_Type.__name__ = "Integer32"
_R2_Object = MibScalar
r2 = _R2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 19),
    _R2_Type()
)
r2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r2.setStatus("current")
if mibBuilder.loadTexts:
    r2.setUnits("min.")


class _F2_Type(Integer32):
    """Custom type f2 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_F2_Type.__name__ = "Integer32"
_F2_Object = MibScalar
f2 = _F2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 20),
    _F2_Type()
)
f2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f2.setStatus("current")
if mibBuilder.loadTexts:
    f2.setUnits("N/A")


class _N3_Type(Integer32):
    """Custom type n3 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_N3_Type.__name__ = "Integer32"
_N3_Object = MibScalar
n3 = _N3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 21),
    _N3_Type()
)
n3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n3.setStatus("current")
if mibBuilder.loadTexts:
    n3.setUnits("N/A")


class _R3_Type(Integer32):
    """Custom type r3 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_R3_Type.__name__ = "Integer32"
_R3_Object = MibScalar
r3 = _R3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 22),
    _R3_Type()
)
r3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r3.setStatus("current")
if mibBuilder.loadTexts:
    r3.setUnits("min.")


class _F3_Type(Integer32):
    """Custom type f3 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_F3_Type.__name__ = "Integer32"
_F3_Object = MibScalar
f3 = _F3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 23),
    _F3_Type()
)
f3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3.setStatus("current")
if mibBuilder.loadTexts:
    f3.setUnits("N/A")


class _N4_Type(Integer32):
    """Custom type n4 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_N4_Type.__name__ = "Integer32"
_N4_Object = MibScalar
n4 = _N4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 24),
    _N4_Type()
)
n4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n4.setStatus("current")
if mibBuilder.loadTexts:
    n4.setUnits("N/A")


class _R4_Type(Integer32):
    """Custom type r4 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_R4_Type.__name__ = "Integer32"
_R4_Object = MibScalar
r4 = _R4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 25),
    _R4_Type()
)
r4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r4.setStatus("current")
if mibBuilder.loadTexts:
    r4.setUnits("min.")


class _F4_Type(Integer32):
    """Custom type f4 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_F4_Type.__name__ = "Integer32"
_F4_Object = MibScalar
f4 = _F4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 26),
    _F4_Type()
)
f4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f4.setStatus("current")
if mibBuilder.loadTexts:
    f4.setUnits("N/A")


class _Out_Type(Integer32):
    """Custom type out based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Out_Type.__name__ = "Integer32"
_Out_Object = MibScalar
out = _Out_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 27),
    _Out_Type()
)
out.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    out.setStatus("current")
if mibBuilder.loadTexts:
    out.setUnits("N/A")


class _Mode_Type(Integer32):
    """Custom type mode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Mode_Type.__name__ = "Integer32"
_Mode_Object = MibScalar
mode = _Mode_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 28),
    _Mode_Type()
)
mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mode.setStatus("current")
if mibBuilder.loadTexts:
    mode.setUnits("N/A")


class _Link1_Type(Integer32):
    """Custom type link1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Link1_Type.__name__ = "Integer32"
_Link1_Object = MibScalar
link1 = _Link1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 29),
    _Link1_Type()
)
link1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    link1.setStatus("current")
if mibBuilder.loadTexts:
    link1.setUnits("N/A")


class _Link2_Type(Integer32):
    """Custom type link2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Link2_Type.__name__ = "Integer32"
_Link2_Object = MibScalar
link2 = _Link2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 30),
    _Link2_Type()
)
link2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    link2.setStatus("current")
if mibBuilder.loadTexts:
    link2.setUnits("N/A")


class _Outl1_Type(Integer32):
    """Custom type outl1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Outl1_Type.__name__ = "Integer32"
_Outl1_Object = MibScalar
outl1 = _Outl1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 31),
    _Outl1_Type()
)
outl1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outl1.setStatus("current")
if mibBuilder.loadTexts:
    outl1.setUnits("N/A")


class _Outl2_Type(Integer32):
    """Custom type outl2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Outl2_Type.__name__ = "Integer32"
_Outl2_Object = MibScalar
outl2 = _Outl2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 32),
    _Outl2_Type()
)
outl2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outl2.setStatus("current")
if mibBuilder.loadTexts:
    outl2.setUnits("N/A")


class _Priority_Type(Integer32):
    """Custom type priority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Priority_Type.__name__ = "Integer32"
_Priority_Object = MibScalar
priority = _Priority_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 33),
    _Priority_Type()
)
priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority.setStatus("current")
if mibBuilder.loadTexts:
    priority.setUnits("N/A")


class _Alcomm_Type(Integer32):
    """Custom type alcomm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Alcomm_Type.__name__ = "Integer32"
_Alcomm_Object = MibScalar
alcomm = _Alcomm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 34),
    _Alcomm_Type()
)
alcomm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcomm.setStatus("current")
if mibBuilder.loadTexts:
    alcomm.setUnits("N/A")


class _Dk1_Type(Integer32):
    """Custom type dk1 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_Dk1_Type.__name__ = "Integer32"
_Dk1_Object = MibScalar
dk1 = _Dk1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 35),
    _Dk1_Type()
)
dk1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dk1.setStatus("current")
if mibBuilder.loadTexts:
    dk1.setUnits("sec.")


class _Dk2_Type(Integer32):
    """Custom type dk2 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_Dk2_Type.__name__ = "Integer32"
_Dk2_Object = MibScalar
dk2 = _Dk2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 36),
    _Dk2_Type()
)
dk2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dk2.setStatus("current")
if mibBuilder.loadTexts:
    dk2.setUnits("sec.")


class _Dk5_Type(Integer32):
    """Custom type dk5 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_Dk5_Type.__name__ = "Integer32"
_Dk5_Object = MibScalar
dk5 = _Dk5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 39),
    _Dk5_Type()
)
dk5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dk5.setStatus("current")
if mibBuilder.loadTexts:
    dk5.setUnits("sec.")


class _Dk6_Type(Integer32):
    """Custom type dk6 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_Dk6_Type.__name__ = "Integer32"
_Dk6_Object = MibScalar
dk6 = _Dk6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 40),
    _Dk6_Type()
)
dk6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dk6.setStatus("current")
if mibBuilder.loadTexts:
    dk6.setUnits("sec.")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAREL-mio-MIB",
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
       "mioMIB": mioMIB,
       "digitalObjects": digitalObjects,
       "buz": buz,
       "cf": cf,
       "mtd1": mtd1,
       "mtd2": mtd2,
       "mtd5": mtd5,
       "mtd6": mtd6,
       "rele1_pwup": rele1_pwup,
       "buzz_pwup": buzz_pwup,
       "di1": di1,
       "di2": di2,
       "di5": di5,
       "di6": di6,
       "ag": ag,
       "at1h": at1h,
       "at1l": at1l,
       "at2h": at2h,
       "at2l": at2l,
       "at3h": at3h,
       "at3l": at3l,
       "at4h": at4h,
       "at4l": at4l,
       "af1": af1,
       "af2": af2,
       "af5": af5,
       "af6": af6,
       "as1": as1,
       "as2": as2,
       "as3": as3,
       "as4": as4,
       "ahw": ahw,
       "td1": td1,
       "td2": td2,
       "td5": td5,
       "td6": td6,
       "ct": ct,
       "buzz": buzz,
       "rele1_stato": rele1_stato,
       "buzz_output": buzz_output,
       "rele1_output": rele1_output,
       "analogObjects": analogObjects,
       "h1": h1,
       "l1": l1,
       "h2": h2,
       "l2": l2,
       "h3": h3,
       "l3": l3,
       "h4": h4,
       "l4": l4,
       "v3l": v3l,
       "v3h": v3h,
       "v4l": v4l,
       "v4h": v4h,
       "o1": o1,
       "o2": o2,
       "o3": o3,
       "o4": o4,
       "ds1": ds1,
       "ds2": ds2,
       "ds3": ds3,
       "ds4": ds4,
       "s1": s1,
       "s2": s2,
       "s3": s3,
       "s4": s4,
       "integerObjects": integerObjects,
       "mod": mod,
       "sonde": sonde,
       "a1": a1,
       "a2": a2,
       "a5": a5,
       "a6": a6,
       "d1": d1,
       "d2": d2,
       "d5": d5,
       "d6": d6,
       "n1": n1,
       "r1": r1,
       "f1": f1,
       "n2": n2,
       "r2": r2,
       "f2": f2,
       "n3": n3,
       "r3": r3,
       "f3": f3,
       "n4": n4,
       "r4": r4,
       "f4": f4,
       "out": out,
       "mode": mode,
       "link1": link1,
       "link2": link2,
       "outl1": outl1,
       "outl2": outl2,
       "priority": priority,
       "alcomm": alcomm,
       "dk1": dk1,
       "dk2": dk2,
       "dk5": dk5,
       "dk6": dk6}
)
