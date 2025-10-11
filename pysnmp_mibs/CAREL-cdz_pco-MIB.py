# SNMP MIB module (CAREL-cdz_pco-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/carel/CAREL-cdz_pco-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:03 2025
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

cdz_pcoMIB = ModuleIdentity(
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


class _Z1_Type(Integer32):
    """Custom type z1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Z1_Type.__name__ = "Integer32"
_Z1_Object = MibScalar
z1 = _Z1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 1),
    _Z1_Type()
)
z1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    z1.setStatus("current")
if mibBuilder.loadTexts:
    z1.setUnits("N/A")


class _Z3_Type(Integer32):
    """Custom type z3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Z3_Type.__name__ = "Integer32"
_Z3_Object = MibScalar
z3 = _Z3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 3),
    _Z3_Type()
)
z3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    z3.setStatus("current")
if mibBuilder.loadTexts:
    z3.setUnits("N/A")


class _Z4_Type(Integer32):
    """Custom type z4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Z4_Type.__name__ = "Integer32"
_Z4_Object = MibScalar
z4 = _Z4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 4),
    _Z4_Type()
)
z4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    z4.setStatus("current")
if mibBuilder.loadTexts:
    z4.setUnits("N/A")


class _Z5_Type(Integer32):
    """Custom type z5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Z5_Type.__name__ = "Integer32"
_Z5_Object = MibScalar
z5 = _Z5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 5),
    _Z5_Type()
)
z5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    z5.setStatus("current")
if mibBuilder.loadTexts:
    z5.setUnits("N/A")


class _Z6_Type(Integer32):
    """Custom type z6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Z6_Type.__name__ = "Integer32"
_Z6_Object = MibScalar
z6 = _Z6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 6),
    _Z6_Type()
)
z6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    z6.setStatus("current")
if mibBuilder.loadTexts:
    z6.setUnits("N/A")


class _Z7_Type(Integer32):
    """Custom type z7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Z7_Type.__name__ = "Integer32"
_Z7_Object = MibScalar
z7 = _Z7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 7),
    _Z7_Type()
)
z7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    z7.setStatus("current")
if mibBuilder.loadTexts:
    z7.setUnits("N/A")


class _Onr_Type(Integer32):
    """Custom type onr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Onr_Type.__name__ = "Integer32"
_Onr_Object = MibScalar
onr = _Onr_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 8),
    _Onr_Type()
)
onr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onr.setStatus("current")
if mibBuilder.loadTexts:
    onr.setUnits("N/A")


class _Z9_Type(Integer32):
    """Custom type z9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Z9_Type.__name__ = "Integer32"
_Z9_Object = MibScalar
z9 = _Z9_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 9),
    _Z9_Type()
)
z9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    z9.setStatus("current")
if mibBuilder.loadTexts:
    z9.setUnits("N/A")


class _Z10_Type(Integer32):
    """Custom type z10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Z10_Type.__name__ = "Integer32"
_Z10_Object = MibScalar
z10 = _Z10_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 10),
    _Z10_Type()
)
z10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    z10.setStatus("current")
if mibBuilder.loadTexts:
    z10.setUnits("N/A")


class _Z12_Type(Integer32):
    """Custom type z12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Z12_Type.__name__ = "Integer32"
_Z12_Object = MibScalar
z12 = _Z12_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 11),
    _Z12_Type()
)
z12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    z12.setStatus("current")
if mibBuilder.loadTexts:
    z12.setUnits("N/A")


class _Val_par_Type(Integer32):
    """Custom type val_par based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Val_par_Type.__name__ = "Integer32"
_Val_par_Object = MibScalar
val_par = _Val_par_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 12),
    _Val_par_Type()
)
val_par.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    val_par.setStatus("current")
if mibBuilder.loadTexts:
    val_par.setUnits("N/A")


class _Syson2_Type(Integer32):
    """Custom type syson2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Syson2_Type.__name__ = "Integer32"
_Syson2_Object = MibScalar
syson2 = _Syson2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 13),
    _Syson2_Type()
)
syson2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syson2.setStatus("current")
if mibBuilder.loadTexts:
    syson2.setUnits("N/A")


class _Val_es_ok_Type(Integer32):
    """Custom type val_es_ok based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Val_es_ok_Type.__name__ = "Integer32"
_Val_es_ok_Object = MibScalar
val_es_ok = _Val_es_ok_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 14),
    _Val_es_ok_Type()
)
val_es_ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    val_es_ok.setStatus("current")
if mibBuilder.loadTexts:
    val_es_ok.setUnits("N/A")


class _Umidifica_Type(Integer32):
    """Custom type umidifica based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Umidifica_Type.__name__ = "Integer32"
_Umidifica_Object = MibScalar
umidifica = _Umidifica_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 15),
    _Umidifica_Type()
)
umidifica.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umidifica.setStatus("current")
if mibBuilder.loadTexts:
    umidifica.setUnits("N/A")


class _Parz1_Type(Integer32):
    """Custom type parz1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Parz1_Type.__name__ = "Integer32"
_Parz1_Object = MibScalar
parz1 = _Parz1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 16),
    _Parz1_Type()
)
parz1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parz1.setStatus("current")
if mibBuilder.loadTexts:
    parz1.setUnits("N/A")


class _Parz2_Type(Integer32):
    """Custom type parz2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Parz2_Type.__name__ = "Integer32"
_Parz2_Object = MibScalar
parz2 = _Parz2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 17),
    _Parz2_Type()
)
parz2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parz2.setStatus("current")
if mibBuilder.loadTexts:
    parz2.setUnits("N/A")


class _Valfre_Type(Integer32):
    """Custom type valfre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Valfre_Type.__name__ = "Integer32"
_Valfre_Object = MibScalar
valfre = _Valfre_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 18),
    _Valfre_Type()
)
valfre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valfre.setStatus("current")
if mibBuilder.loadTexts:
    valfre.setUnits("N/A")


class _Valfre1_Type(Integer32):
    """Custom type valfre1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Valfre1_Type.__name__ = "Integer32"
_Valfre1_Object = MibScalar
valfre1 = _Valfre1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 19),
    _Valfre1_Type()
)
valfre1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valfre1.setStatus("current")
if mibBuilder.loadTexts:
    valfre1.setUnits("N/A")


class _Valca_Type(Integer32):
    """Custom type valca based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Valca_Type.__name__ = "Integer32"
_Valca_Object = MibScalar
valca = _Valca_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 20),
    _Valca_Type()
)
valca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valca.setStatus("current")
if mibBuilder.loadTexts:
    valca.setUnits("N/A")


class _Valca1_Type(Integer32):
    """Custom type valca1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Valca1_Type.__name__ = "Integer32"
_Valca1_Object = MibScalar
valca1 = _Valca1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 21),
    _Valca1_Type()
)
valca1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valca1.setStatus("current")
if mibBuilder.loadTexts:
    valca1.setUnits("N/A")


class _Glb_al_Type(Integer32):
    """Custom type glb_al based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Glb_al_Type.__name__ = "Integer32"
_Glb_al_Object = MibScalar
glb_al = _Glb_al_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 22),
    _Glb_al_Type()
)
glb_al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    glb_al.setStatus("current")
if mibBuilder.loadTexts:
    glb_al.setUnits("N/A")


class _S_firmanook_Type(Integer32):
    """Custom type s_firmanook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_firmanook_Type.__name__ = "Integer32"
_S_firmanook_Object = MibScalar
s_firmanook = _S_firmanook_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 23),
    _S_firmanook_Type()
)
s_firmanook.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s_firmanook.setStatus("current")
if mibBuilder.loadTexts:
    s_firmanook.setUnits("N/A")


class _S_error_io_Type(Integer32):
    """Custom type s_error_io based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_error_io_Type.__name__ = "Integer32"
_S_error_io_Object = MibScalar
s_error_io = _S_error_io_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 24),
    _S_error_io_Type()
)
s_error_io.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_error_io.setStatus("current")
if mibBuilder.loadTexts:
    s_error_io.setUnits("N/A")


class _S_bp1_Type(Integer32):
    """Custom type s_bp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_bp1_Type.__name__ = "Integer32"
_S_bp1_Object = MibScalar
s_bp1 = _S_bp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 25),
    _S_bp1_Type()
)
s_bp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_bp1.setStatus("current")
if mibBuilder.loadTexts:
    s_bp1.setUnits("N/A")


class _S_bp2_Type(Integer32):
    """Custom type s_bp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_bp2_Type.__name__ = "Integer32"
_S_bp2_Object = MibScalar
s_bp2 = _S_bp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 26),
    _S_bp2_Type()
)
s_bp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_bp2.setStatus("current")
if mibBuilder.loadTexts:
    s_bp2.setUnits("N/A")


class _S_fl1_Type(Integer32):
    """Custom type s_fl1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_fl1_Type.__name__ = "Integer32"
_S_fl1_Object = MibScalar
s_fl1 = _S_fl1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 27),
    _S_fl1_Type()
)
s_fl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_fl1.setStatus("current")
if mibBuilder.loadTexts:
    s_fl1.setUnits("N/A")


class _S_trf_Type(Integer32):
    """Custom type s_trf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_trf_Type.__name__ = "Integer32"
_S_trf_Object = MibScalar
s_trf = _S_trf_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 28),
    _S_trf_Type()
)
s_trf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_trf.setStatus("current")
if mibBuilder.loadTexts:
    s_trf.setUnits("N/A")


class _S_trs1_Type(Integer32):
    """Custom type s_trs1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_trs1_Type.__name__ = "Integer32"
_S_trs1_Object = MibScalar
s_trs1 = _S_trs1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 29),
    _S_trs1_Type()
)
s_trs1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_trs1.setStatus("current")
if mibBuilder.loadTexts:
    s_trs1.setUnits("N/A")


class _S_trs2_Type(Integer32):
    """Custom type s_trs2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_trs2_Type.__name__ = "Integer32"
_S_trs2_Object = MibScalar
s_trs2 = _S_trs2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 30),
    _S_trs2_Type()
)
s_trs2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_trs2.setStatus("current")
if mibBuilder.loadTexts:
    s_trs2.setUnits("N/A")


class _S_fsa_Type(Integer32):
    """Custom type s_fsa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_fsa_Type.__name__ = "Integer32"
_S_fsa_Object = MibScalar
s_fsa = _S_fsa_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 31),
    _S_fsa_Type()
)
s_fsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_fsa.setStatus("current")
if mibBuilder.loadTexts:
    s_fsa.setUnits("N/A")


class _S_flt_Type(Integer32):
    """Custom type s_flt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_flt_Type.__name__ = "Integer32"
_S_flt_Object = MibScalar
s_flt = _S_flt_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 32),
    _S_flt_Type()
)
s_flt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_flt.setStatus("current")
if mibBuilder.loadTexts:
    s_flt.setUnits("N/A")


class _S_all_h_temp_Type(Integer32):
    """Custom type s_all_h_temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_all_h_temp_Type.__name__ = "Integer32"
_S_all_h_temp_Object = MibScalar
s_all_h_temp = _S_all_h_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 33),
    _S_all_h_temp_Type()
)
s_all_h_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_all_h_temp.setStatus("current")
if mibBuilder.loadTexts:
    s_all_h_temp.setUnits("N/A")


class _S_all_l_temp_Type(Integer32):
    """Custom type s_all_l_temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_all_l_temp_Type.__name__ = "Integer32"
_S_all_l_temp_Object = MibScalar
s_all_l_temp = _S_all_l_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 34),
    _S_all_l_temp_Type()
)
s_all_l_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_all_l_temp.setStatus("current")
if mibBuilder.loadTexts:
    s_all_l_temp.setUnits("N/A")


class _S_all_h_umid_Type(Integer32):
    """Custom type s_all_h_umid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_all_h_umid_Type.__name__ = "Integer32"
_S_all_h_umid_Object = MibScalar
s_all_h_umid = _S_all_h_umid_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 35),
    _S_all_h_umid_Type()
)
s_all_h_umid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_all_h_umid.setStatus("current")
if mibBuilder.loadTexts:
    s_all_h_umid.setUnits("N/A")


class _S_all_l_umid_Type(Integer32):
    """Custom type s_all_l_umid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_all_l_umid_Type.__name__ = "Integer32"
_S_all_l_umid_Object = MibScalar
s_all_l_umid = _S_all_l_umid_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 36),
    _S_all_l_umid_Type()
)
s_all_l_umid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_all_l_umid.setStatus("current")
if mibBuilder.loadTexts:
    s_all_l_umid.setUnits("N/A")


class _S_al_ore_comp1_Type(Integer32):
    """Custom type s_al_ore_comp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_al_ore_comp1_Type.__name__ = "Integer32"
_S_al_ore_comp1_Object = MibScalar
s_al_ore_comp1 = _S_al_ore_comp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 37),
    _S_al_ore_comp1_Type()
)
s_al_ore_comp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_al_ore_comp1.setStatus("current")
if mibBuilder.loadTexts:
    s_al_ore_comp1.setUnits("N/A")


class _S_al_ore_comp2_Type(Integer32):
    """Custom type s_al_ore_comp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_al_ore_comp2_Type.__name__ = "Integer32"
_S_al_ore_comp2_Object = MibScalar
s_al_ore_comp2 = _S_al_ore_comp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 38),
    _S_al_ore_comp2_Type()
)
s_al_ore_comp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_al_ore_comp2.setStatus("current")
if mibBuilder.loadTexts:
    s_al_ore_comp2.setUnits("N/A")


class _S_al_ore_umidif_Type(Integer32):
    """Custom type s_al_ore_umidif based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_al_ore_umidif_Type.__name__ = "Integer32"
_S_al_ore_umidif_Object = MibScalar
s_al_ore_umidif = _S_al_ore_umidif_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 39),
    _S_al_ore_umidif_Type()
)
s_al_ore_umidif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_al_ore_umidif.setStatus("current")
if mibBuilder.loadTexts:
    s_al_ore_umidif.setUnits("N/A")


class _S_al_ore_mac_Type(Integer32):
    """Custom type s_al_ore_mac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_al_ore_mac_Type.__name__ = "Integer32"
_S_al_ore_mac_Object = MibScalar
s_al_ore_mac = _S_al_ore_mac_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 40),
    _S_al_ore_mac_Type()
)
s_al_ore_mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_al_ore_mac.setStatus("current")
if mibBuilder.loadTexts:
    s_al_ore_mac.setUnits("N/A")


class _S_al_ore_res1_Type(Integer32):
    """Custom type s_al_ore_res1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_al_ore_res1_Type.__name__ = "Integer32"
_S_al_ore_res1_Object = MibScalar
s_al_ore_res1 = _S_al_ore_res1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 41),
    _S_al_ore_res1_Type()
)
s_al_ore_res1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_al_ore_res1.setStatus("current")
if mibBuilder.loadTexts:
    s_al_ore_res1.setUnits("N/A")


class _S_al_ore_res2_Type(Integer32):
    """Custom type s_al_ore_res2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_al_ore_res2_Type.__name__ = "Integer32"
_S_al_ore_res2_Object = MibScalar
s_al_ore_res2 = _S_al_ore_res2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 42),
    _S_al_ore_res2_Type()
)
s_al_ore_res2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_al_ore_res2.setStatus("current")
if mibBuilder.loadTexts:
    s_al_ore_res2.setUnits("N/A")


class _S_all_h_free_Type(Integer32):
    """Custom type s_all_h_free based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_all_h_free_Type.__name__ = "Integer32"
_S_all_h_free_Object = MibScalar
s_all_h_free = _S_all_h_free_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 43),
    _S_all_h_free_Type()
)
s_all_h_free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_all_h_free.setStatus("current")
if mibBuilder.loadTexts:
    s_all_h_free.setUnits("N/A")


class _S_all_l_free_Type(Integer32):
    """Custom type s_all_l_free based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_all_l_free_Type.__name__ = "Integer32"
_S_all_l_free_Object = MibScalar
s_all_l_free = _S_all_l_free_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 44),
    _S_all_l_free_Type()
)
s_all_l_free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_all_l_free.setStatus("current")
if mibBuilder.loadTexts:
    s_all_l_free.setUnits("N/A")


class _S_sonda1_ko_Type(Integer32):
    """Custom type s_sonda1_ko based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_sonda1_ko_Type.__name__ = "Integer32"
_S_sonda1_ko_Object = MibScalar
s_sonda1_ko = _S_sonda1_ko_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 45),
    _S_sonda1_ko_Type()
)
s_sonda1_ko.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_sonda1_ko.setStatus("current")
if mibBuilder.loadTexts:
    s_sonda1_ko.setUnits("N/A")


class _S_sonda2_ko_Type(Integer32):
    """Custom type s_sonda2_ko based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_sonda2_ko_Type.__name__ = "Integer32"
_S_sonda2_ko_Object = MibScalar
s_sonda2_ko = _S_sonda2_ko_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 46),
    _S_sonda2_ko_Type()
)
s_sonda2_ko.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_sonda2_ko.setStatus("current")
if mibBuilder.loadTexts:
    s_sonda2_ko.setUnits("N/A")


class _S_sonda4_ko_Type(Integer32):
    """Custom type s_sonda4_ko based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_sonda4_ko_Type.__name__ = "Integer32"
_S_sonda4_ko_Object = MibScalar
s_sonda4_ko = _S_sonda4_ko_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 47),
    _S_sonda4_ko_Type()
)
s_sonda4_ko.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_sonda4_ko.setStatus("current")
if mibBuilder.loadTexts:
    s_sonda4_ko.setUnits("N/A")


class _S_sonda6_ko_Type(Integer32):
    """Custom type s_sonda6_ko based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_sonda6_ko_Type.__name__ = "Integer32"
_S_sonda6_ko_Object = MibScalar
s_sonda6_ko = _S_sonda6_ko_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 48),
    _S_sonda6_ko_Type()
)
s_sonda6_ko.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_sonda6_ko.setStatus("current")
if mibBuilder.loadTexts:
    s_sonda6_ko.setUnits("N/A")


class _S_sondau_ko_Type(Integer32):
    """Custom type s_sondau_ko based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_sondau_ko_Type.__name__ = "Integer32"
_S_sondau_ko_Object = MibScalar
s_sondau_ko = _S_sondau_ko_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 49),
    _S_sondau_ko_Type()
)
s_sondau_ko.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_sondau_ko.setStatus("current")
if mibBuilder.loadTexts:
    s_sondau_ko.setUnits("N/A")


class _S_epromnook_Type(Integer32):
    """Custom type s_epromnook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_epromnook_Type.__name__ = "Integer32"
_S_epromnook_Object = MibScalar
s_epromnook = _S_epromnook_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 51),
    _S_epromnook_Type()
)
s_epromnook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_epromnook.setStatus("current")
if mibBuilder.loadTexts:
    s_epromnook.setUnits("N/A")


class _Pro_pi_Type(Integer32):
    """Custom type pro_pi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pro_pi_Type.__name__ = "Integer32"
_Pro_pi_Object = MibScalar
pro_pi = _Pro_pi_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 53),
    _Pro_pi_Type()
)
pro_pi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pro_pi.setStatus("current")
if mibBuilder.loadTexts:
    pro_pi.setUnits("N/A")


class _Si_sond_umid_Type(Integer32):
    """Custom type si_sond_umid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_sond_umid_Type.__name__ = "Integer32"
_Si_sond_umid_Object = MibScalar
si_sond_umid = _Si_sond_umid_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 55),
    _Si_sond_umid_Type()
)
si_sond_umid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_sond_umid.setStatus("current")
if mibBuilder.loadTexts:
    si_sond_umid.setUnits("N/A")


class _Si_sond_acqua_Type(Integer32):
    """Custom type si_sond_acqua based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_sond_acqua_Type.__name__ = "Integer32"
_Si_sond_acqua_Object = MibScalar
si_sond_acqua = _Si_sond_acqua_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 56),
    _Si_sond_acqua_Type()
)
si_sond_acqua.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_sond_acqua.setStatus("current")
if mibBuilder.loadTexts:
    si_sond_acqua.setUnits("N/A")


class _Si_sond_aria_Type(Integer32):
    """Custom type si_sond_aria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_sond_aria_Type.__name__ = "Integer32"
_Si_sond_aria_Object = MibScalar
si_sond_aria = _Si_sond_aria_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 57),
    _Si_sond_aria_Type()
)
si_sond_aria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_sond_aria.setStatus("current")
if mibBuilder.loadTexts:
    si_sond_aria.setUnits("N/A")


class _Si_sond_acquain_Type(Integer32):
    """Custom type si_sond_acquain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_sond_acquain_Type.__name__ = "Integer32"
_Si_sond_acquain_Object = MibScalar
si_sond_acquain = _Si_sond_acquain_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 58),
    _Si_sond_acquain_Type()
)
si_sond_acquain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_sond_acquain.setStatus("current")
if mibBuilder.loadTexts:
    si_sond_acquain.setUnits("N/A")


class _Si_sond_ariain_Type(Integer32):
    """Custom type si_sond_ariain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_sond_ariain_Type.__name__ = "Integer32"
_Si_sond_ariain_Object = MibScalar
si_sond_ariain = _Si_sond_ariain_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 59),
    _Si_sond_ariain_Type()
)
si_sond_ariain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_sond_ariain.setStatus("current")
if mibBuilder.loadTexts:
    si_sond_ariain.setUnits("N/A")


class _Bin_sta_Type(Integer32):
    """Custom type bin_sta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Bin_sta_Type.__name__ = "Integer32"
_Bin_sta_Object = MibScalar
bin_sta = _Bin_sta_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 60),
    _Bin_sta_Type()
)
bin_sta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bin_sta.setStatus("current")
if mibBuilder.loadTexts:
    bin_sta.setUnits("N/A")


class _Si_rampap_Type(Integer32):
    """Custom type si_rampap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_rampap_Type.__name__ = "Integer32"
_Si_rampap_Object = MibScalar
si_rampap = _Si_rampap_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 61),
    _Si_rampap_Type()
)
si_rampap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_rampap.setStatus("current")
if mibBuilder.loadTexts:
    si_rampap.setUnits("N/A")


class _Es_Type(Integer32):
    """Custom type es based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Es_Type.__name__ = "Integer32"
_Es_Object = MibScalar
es = _Es_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 62),
    _Es_Type()
)
es.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es.setStatus("current")
if mibBuilder.loadTexts:
    es.setUnits("N/A")


class _Si_comp_es_Type(Integer32):
    """Custom type si_comp_es based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_comp_es_Type.__name__ = "Integer32"
_Si_comp_es_Object = MibScalar
si_comp_es = _Si_comp_es_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 63),
    _Si_comp_es_Type()
)
si_comp_es.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_comp_es.setStatus("current")
if mibBuilder.loadTexts:
    si_comp_es.setUnits("N/A")


class _Si_rampan_Type(Integer32):
    """Custom type si_rampan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_rampan_Type.__name__ = "Integer32"
_Si_rampan_Object = MibScalar
si_rampan = _Si_rampan_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 64),
    _Si_rampan_Type()
)
si_rampan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_rampan.setStatus("current")
if mibBuilder.loadTexts:
    si_rampan.setUnits("N/A")


class _Si_parz_Type(Integer32):
    """Custom type si_parz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_parz_Type.__name__ = "Integer32"
_Si_parz_Object = MibScalar
si_parz = _Si_parz_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 65),
    _Si_parz_Type()
)
si_parz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_parz.setStatus("current")
if mibBuilder.loadTexts:
    si_parz.setUnits("N/A")


class _Si_rot2_Type(Integer32):
    """Custom type si_rot2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_rot2_Type.__name__ = "Integer32"
_Si_rot2_Object = MibScalar
si_rot2 = _Si_rot2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 66),
    _Si_rot2_Type()
)
si_rot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_rot2.setStatus("current")
if mibBuilder.loadTexts:
    si_rot2.setUnits("N/A")


class _Si_comp1_deu_Type(Integer32):
    """Custom type si_comp1_deu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_comp1_deu_Type.__name__ = "Integer32"
_Si_comp1_deu_Object = MibScalar
si_comp1_deu = _Si_comp1_deu_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 67),
    _Si_comp1_deu_Type()
)
si_comp1_deu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_comp1_deu.setStatus("current")
if mibBuilder.loadTexts:
    si_comp1_deu.setUnits("N/A")


class _Si_comp2_deu_Type(Integer32):
    """Custom type si_comp2_deu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_comp2_deu_Type.__name__ = "Integer32"
_Si_comp2_deu_Object = MibScalar
si_comp2_deu = _Si_comp2_deu_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 68),
    _Si_comp2_deu_Type()
)
si_comp2_deu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_comp2_deu.setStatus("current")
if mibBuilder.loadTexts:
    si_comp2_deu.setUnits("N/A")


class _Si_fasce_Type(Integer32):
    """Custom type si_fasce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_fasce_Type.__name__ = "Integer32"
_Si_fasce_Object = MibScalar
si_fasce = _Si_fasce_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 71),
    _Si_fasce_Type()
)
si_fasce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_fasce.setStatus("current")
if mibBuilder.loadTexts:
    si_fasce.setUnits("N/A")


class _Syson_Type(Integer32):
    """Custom type syson based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Syson_Type.__name__ = "Integer32"
_Syson_Object = MibScalar
syson = _Syson_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 73),
    _Syson_Type()
)
syson.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syson.setStatus("current")
if mibBuilder.loadTexts:
    syson.setUnits("N/A")


class _Si_rampap3v_Type(Integer32):
    """Custom type si_rampap3v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_rampap3v_Type.__name__ = "Integer32"
_Si_rampap3v_Object = MibScalar
si_rampap3v = _Si_rampap3v_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 74),
    _Si_rampap3v_Type()
)
si_rampap3v.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_rampap3v.setStatus("current")
if mibBuilder.loadTexts:
    si_rampap3v.setUnits("N/A")


class _Si_rampan3v_Type(Integer32):
    """Custom type si_rampan3v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Si_rampan3v_Type.__name__ = "Integer32"
_Si_rampan3v_Object = MibScalar
si_rampan3v = _Si_rampan3v_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 75),
    _Si_rampan3v_Type()
)
si_rampan3v.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    si_rampan3v.setStatus("current")
if mibBuilder.loadTexts:
    si_rampan3v.setUnits("N/A")


class _Manuale_Type(Integer32):
    """Custom type manuale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Manuale_Type.__name__ = "Integer32"
_Manuale_Object = MibScalar
manuale = _Manuale_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 76),
    _Manuale_Type()
)
manuale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manuale.setStatus("current")
if mibBuilder.loadTexts:
    manuale.setUnits("N/A")


class _Start_off_Type(Integer32):
    """Custom type start_off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Start_off_Type.__name__ = "Integer32"
_Start_off_Object = MibScalar
start_off = _Start_off_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 77),
    _Start_off_Type()
)
start_off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    start_off.setStatus("current")
if mibBuilder.loadTexts:
    start_off.setUnits("N/A")


class _Alarm_e06_Type(Integer32):
    """Custom type alarm_e06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm_e06_Type.__name__ = "Integer32"
_Alarm_e06_Object = MibScalar
alarm_e06 = _Alarm_e06_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 80),
    _Alarm_e06_Type()
)
alarm_e06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm_e06.setStatus("current")
if mibBuilder.loadTexts:
    alarm_e06.setUnits("N/A")


class _Alarm_e08_Type(Integer32):
    """Custom type alarm_e08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm_e08_Type.__name__ = "Integer32"
_Alarm_e08_Object = MibScalar
alarm_e08 = _Alarm_e08_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 81),
    _Alarm_e08_Type()
)
alarm_e08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm_e08.setStatus("current")
if mibBuilder.loadTexts:
    alarm_e08.setUnits("N/A")


class _Alarm_e09_Type(Integer32):
    """Custom type alarm_e09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm_e09_Type.__name__ = "Integer32"
_Alarm_e09_Object = MibScalar
alarm_e09 = _Alarm_e09_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 82),
    _Alarm_e09_Type()
)
alarm_e09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm_e09.setStatus("current")
if mibBuilder.loadTexts:
    alarm_e09.setUnits("N/A")


class _Alarm_e10_Type(Integer32):
    """Custom type alarm_e10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm_e10_Type.__name__ = "Integer32"
_Alarm_e10_Object = MibScalar
alarm_e10 = _Alarm_e10_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 83),
    _Alarm_e10_Type()
)
alarm_e10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm_e10.setStatus("current")
if mibBuilder.loadTexts:
    alarm_e10.setUnits("N/A")


class _Alarm_e11_Type(Integer32):
    """Custom type alarm_e11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm_e11_Type.__name__ = "Integer32"
_Alarm_e11_Object = MibScalar
alarm_e11 = _Alarm_e11_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 84),
    _Alarm_e11_Type()
)
alarm_e11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm_e11.setStatus("current")
if mibBuilder.loadTexts:
    alarm_e11.setUnits("N/A")


class _Alarm_e12_Type(Integer32):
    """Custom type alarm_e12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm_e12_Type.__name__ = "Integer32"
_Alarm_e12_Object = MibScalar
alarm_e12 = _Alarm_e12_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 85),
    _Alarm_e12_Type()
)
alarm_e12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm_e12.setStatus("current")
if mibBuilder.loadTexts:
    alarm_e12.setUnits("N/A")
_AnalogObjects_ObjectIdentity = ObjectIdentity
analogObjects = _AnalogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2)
)


class _Temp_Type(Integer32):
    """Custom type temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Temp_Type.__name__ = "Integer32"
_Temp_Object = MibScalar
temp = _Temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 1),
    _Temp_Type()
)
temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp.setStatus("current")
if mibBuilder.loadTexts:
    temp.setUnits("N/A")


class _Umid_Type(Integer32):
    """Custom type umid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Umid_Type.__name__ = "Integer32"
_Umid_Object = MibScalar
umid = _Umid_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 2),
    _Umid_Type()
)
umid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umid.setStatus("current")
if mibBuilder.loadTexts:
    umid.setUnits("N/A")


class _Acqua_Type(Integer32):
    """Custom type acqua based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Acqua_Type.__name__ = "Integer32"
_Acqua_Object = MibScalar
acqua = _Acqua_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 3),
    _Acqua_Type()
)
acqua.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqua.setStatus("current")
if mibBuilder.loadTexts:
    acqua.setUnits("N/A")


class _Aria_acqua_in_Type(Integer32):
    """Custom type aria_acqua_in based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Aria_acqua_in_Type.__name__ = "Integer32"
_Aria_acqua_in_Object = MibScalar
aria_acqua_in = _Aria_acqua_in_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 4),
    _Aria_acqua_in_Type()
)
aria_acqua_in.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aria_acqua_in.setStatus("current")
if mibBuilder.loadTexts:
    aria_acqua_in.setUnits("N/A")


class _Temp_aria_man_Type(Integer32):
    """Custom type temp_aria_man based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Temp_aria_man_Type.__name__ = "Integer32"
_Temp_aria_man_Object = MibScalar
temp_aria_man = _Temp_aria_man_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 5),
    _Temp_aria_man_Type()
)
temp_aria_man.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp_aria_man.setStatus("current")
if mibBuilder.loadTexts:
    temp_aria_man.setUnits("N/A")


class _Zona_morta_Type(Integer32):
    """Custom type zona_morta based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Zona_morta_Type.__name__ = "Integer32"
_Zona_morta_Object = MibScalar
zona_morta = _Zona_morta_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 6),
    _Zona_morta_Type()
)
zona_morta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zona_morta.setStatus("current")
if mibBuilder.loadTexts:
    zona_morta.setUnits("C x10")


class _Banda_hum_Type(Integer32):
    """Custom type banda_hum based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Banda_hum_Type.__name__ = "Integer32"
_Banda_hum_Object = MibScalar
banda_hum = _Banda_hum_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 7),
    _Banda_hum_Type()
)
banda_hum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    banda_hum.setStatus("current")
if mibBuilder.loadTexts:
    banda_hum.setUnits("% x10")


class _Set_hum_a_Type(Integer32):
    """Custom type set_hum_a based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Set_hum_a_Type.__name__ = "Integer32"
_Set_hum_a_Object = MibScalar
set_hum_a = _Set_hum_a_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 8),
    _Set_hum_a_Type()
)
set_hum_a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_hum_a.setStatus("current")
if mibBuilder.loadTexts:
    set_hum_a.setUnits("% x10")


class _Sgl_l_temp_Type(Integer32):
    """Custom type sgl_l_temp based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Sgl_l_temp_Type.__name__ = "Integer32"
_Sgl_l_temp_Object = MibScalar
sgl_l_temp = _Sgl_l_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 9),
    _Sgl_l_temp_Type()
)
sgl_l_temp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgl_l_temp.setStatus("current")
if mibBuilder.loadTexts:
    sgl_l_temp.setUnits("C x10")


class _Sgl_h_temp_Type(Integer32):
    """Custom type sgl_h_temp based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Sgl_h_temp_Type.__name__ = "Integer32"
_Sgl_h_temp_Object = MibScalar
sgl_h_temp = _Sgl_h_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 10),
    _Sgl_h_temp_Type()
)
sgl_h_temp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgl_h_temp.setStatus("current")
if mibBuilder.loadTexts:
    sgl_h_temp.setUnits("C x10")


class _Sgl_l_umid_Type(Integer32):
    """Custom type sgl_l_umid based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Sgl_l_umid_Type.__name__ = "Integer32"
_Sgl_l_umid_Object = MibScalar
sgl_l_umid = _Sgl_l_umid_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 11),
    _Sgl_l_umid_Type()
)
sgl_l_umid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgl_l_umid.setStatus("current")
if mibBuilder.loadTexts:
    sgl_l_umid.setUnits("% x10")


class _Sgl_h_umid_Type(Integer32):
    """Custom type sgl_h_umid based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Sgl_h_umid_Type.__name__ = "Integer32"
_Sgl_h_umid_Object = MibScalar
sgl_h_umid = _Sgl_h_umid_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 12),
    _Sgl_h_umid_Type()
)
sgl_h_umid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgl_h_umid.setStatus("current")
if mibBuilder.loadTexts:
    sgl_h_umid.setUnits("% x10")


class _Set_temp_a_Type(Integer32):
    """Custom type set_temp_a based on Integer32"""
    defaultValue = 230

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Set_temp_a_Type.__name__ = "Integer32"
_Set_temp_a_Object = MibScalar
set_temp_a = _Set_temp_a_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 13),
    _Set_temp_a_Type()
)
set_temp_a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_temp_a.setStatus("current")
if mibBuilder.loadTexts:
    set_temp_a.setUnits("C x10")


class _Banda_temp_Type(Integer32):
    """Custom type banda_temp based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Banda_temp_Type.__name__ = "Integer32"
_Banda_temp_Object = MibScalar
banda_temp = _Banda_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 17),
    _Banda_temp_Type()
)
banda_temp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    banda_temp.setStatus("current")
if mibBuilder.loadTexts:
    banda_temp.setUnits("C x10")


class _Sgl_l_free_Type(Integer32):
    """Custom type sgl_l_free based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Sgl_l_free_Type.__name__ = "Integer32"
_Sgl_l_free_Object = MibScalar
sgl_l_free = _Sgl_l_free_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 18),
    _Sgl_l_free_Type()
)
sgl_l_free.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgl_l_free.setStatus("current")
if mibBuilder.loadTexts:
    sgl_l_free.setUnits("C x10")


class _Sgl_h_free_Type(Integer32):
    """Custom type sgl_h_free based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )


_Sgl_h_free_Type.__name__ = "Integer32"
_Sgl_h_free_Object = MibScalar
sgl_h_free = _Sgl_h_free_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 19),
    _Sgl_h_free_Type()
)
sgl_h_free.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgl_h_free.setStatus("current")
if mibBuilder.loadTexts:
    sgl_h_free.setUnits("C x10")
_IntegerObjects_ObjectIdentity = ObjectIdentity
integerObjects = _IntegerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3)
)


class _In_rampa_p_Type(Integer32):
    """Custom type in_rampa_p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_In_rampa_p_Type.__name__ = "Integer32"
_In_rampa_p_Object = MibScalar
in_rampa_p = _In_rampa_p_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 10),
    _In_rampa_p_Type()
)
in_rampa_p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    in_rampa_p.setStatus("current")
if mibBuilder.loadTexts:
    in_rampa_p.setUnits("%")


class _Fin_rampa_p_Type(Integer32):
    """Custom type fin_rampa_p based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fin_rampa_p_Type.__name__ = "Integer32"
_Fin_rampa_p_Object = MibScalar
fin_rampa_p = _Fin_rampa_p_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 11),
    _Fin_rampa_p_Type()
)
fin_rampa_p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fin_rampa_p.setStatus("current")
if mibBuilder.loadTexts:
    fin_rampa_p.setUnits("%")


class _In_rampa_n_Type(Integer32):
    """Custom type in_rampa_n based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_In_rampa_n_Type.__name__ = "Integer32"
_In_rampa_n_Object = MibScalar
in_rampa_n = _In_rampa_n_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 12),
    _In_rampa_n_Type()
)
in_rampa_n.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    in_rampa_n.setStatus("current")
if mibBuilder.loadTexts:
    in_rampa_n.setUnits("%")


class _Fin_rampa_n_Type(Integer32):
    """Custom type fin_rampa_n based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fin_rampa_n_Type.__name__ = "Integer32"
_Fin_rampa_n_Object = MibScalar
fin_rampa_n = _Fin_rampa_n_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 13),
    _Fin_rampa_n_Type()
)
fin_rampa_n.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fin_rampa_n.setStatus("current")
if mibBuilder.loadTexts:
    fin_rampa_n.setUnits("%")


class _Set_comp1_cw_Type(Integer32):
    """Custom type set_comp1_cw based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Set_comp1_cw_Type.__name__ = "Integer32"
_Set_comp1_cw_Object = MibScalar
set_comp1_cw = _Set_comp1_cw_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 16),
    _Set_comp1_cw_Type()
)
set_comp1_cw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_comp1_cw.setStatus("current")
if mibBuilder.loadTexts:
    set_comp1_cw.setUnits("%")


class _Ist_comp1_cw_Type(Integer32):
    """Custom type ist_comp1_cw based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ist_comp1_cw_Type.__name__ = "Integer32"
_Ist_comp1_cw_Object = MibScalar
ist_comp1_cw = _Ist_comp1_cw_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 17),
    _Ist_comp1_cw_Type()
)
ist_comp1_cw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ist_comp1_cw.setStatus("current")
if mibBuilder.loadTexts:
    ist_comp1_cw.setUnits("%")


class _Set_comp2_cw_Type(Integer32):
    """Custom type set_comp2_cw based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Set_comp2_cw_Type.__name__ = "Integer32"
_Set_comp2_cw_Object = MibScalar
set_comp2_cw = _Set_comp2_cw_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 18),
    _Set_comp2_cw_Type()
)
set_comp2_cw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_comp2_cw.setStatus("current")
if mibBuilder.loadTexts:
    set_comp2_cw.setUnits("%")


class _Ist_comp2_cw_Type(Integer32):
    """Custom type ist_comp2_cw based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ist_comp2_cw_Type.__name__ = "Integer32"
_Ist_comp2_cw_Object = MibScalar
ist_comp2_cw = _Ist_comp2_cw_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 19),
    _Ist_comp2_cw_Type()
)
ist_comp2_cw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ist_comp2_cw.setStatus("current")
if mibBuilder.loadTexts:
    ist_comp2_cw.setUnits("%")


class _Set_comp1_es_Type(Integer32):
    """Custom type set_comp1_es based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Set_comp1_es_Type.__name__ = "Integer32"
_Set_comp1_es_Object = MibScalar
set_comp1_es = _Set_comp1_es_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 22),
    _Set_comp1_es_Type()
)
set_comp1_es.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_comp1_es.setStatus("current")
if mibBuilder.loadTexts:
    set_comp1_es.setUnits("%")


class _Ist_comp1_es_Type(Integer32):
    """Custom type ist_comp1_es based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ist_comp1_es_Type.__name__ = "Integer32"
_Ist_comp1_es_Object = MibScalar
ist_comp1_es = _Ist_comp1_es_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 23),
    _Ist_comp1_es_Type()
)
ist_comp1_es.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ist_comp1_es.setStatus("current")
if mibBuilder.loadTexts:
    ist_comp1_es.setUnits("%")


class _Set_comp2_es_Type(Integer32):
    """Custom type set_comp2_es based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Set_comp2_es_Type.__name__ = "Integer32"
_Set_comp2_es_Object = MibScalar
set_comp2_es = _Set_comp2_es_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 24),
    _Set_comp2_es_Type()
)
set_comp2_es.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_comp2_es.setStatus("current")
if mibBuilder.loadTexts:
    set_comp2_es.setUnits("%")


class _Ist_comp2_es_Type(Integer32):
    """Custom type ist_comp2_es based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ist_comp2_es_Type.__name__ = "Integer32"
_Ist_comp2_es_Object = MibScalar
ist_comp2_es = _Ist_comp2_es_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 25),
    _Ist_comp2_es_Type()
)
ist_comp2_es.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ist_comp2_es.setStatus("current")
if mibBuilder.loadTexts:
    ist_comp2_es.setUnits("%")


class _Rit_fra_ins_Type(Integer32):
    """Custom type rit_fra_ins based on Integer32"""
    defaultValue = 360

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Rit_fra_ins_Type.__name__ = "Integer32"
_Rit_fra_ins_Object = MibScalar
rit_fra_ins = _Rit_fra_ins_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 26),
    _Rit_fra_ins_Type()
)
rit_fra_ins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_fra_ins.setStatus("current")
if mibBuilder.loadTexts:
    rit_fra_ins.setUnits("sec")


class _Rit_bassa_pres_Type(Integer32):
    """Custom type rit_bassa_pres based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Rit_bassa_pres_Type.__name__ = "Integer32"
_Rit_bassa_pres_Object = MibScalar
rit_bassa_pres = _Rit_bassa_pres_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 28),
    _Rit_bassa_pres_Type()
)
rit_bassa_pres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_bassa_pres.setStatus("current")
if mibBuilder.loadTexts:
    rit_bassa_pres.setUnits("sec")


class _Rit_riaccen_Type(Integer32):
    """Custom type rit_riaccen based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Rit_riaccen_Type.__name__ = "Integer32"
_Rit_riaccen_Object = MibScalar
rit_riaccen = _Rit_riaccen_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 29),
    _Rit_riaccen_Type()
)
rit_riaccen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_riaccen.setStatus("current")
if mibBuilder.loadTexts:
    rit_riaccen.setUnits("sec")


class _Rit_tra_ins_Type(Integer32):
    """Custom type rit_tra_ins based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Rit_tra_ins_Type.__name__ = "Integer32"
_Rit_tra_ins_Object = MibScalar
rit_tra_ins = _Rit_tra_ins_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 30),
    _Rit_tra_ins_Type()
)
rit_tra_ins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_tra_ins.setStatus("current")
if mibBuilder.loadTexts:
    rit_tra_ins.setUnits("sec")


class _N_res_Type(Integer32):
    """Custom type n_res based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_N_res_Type.__name__ = "Integer32"
_N_res_Object = MibScalar
n_res = _N_res_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 31),
    _N_res_Type()
)
n_res.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_res.setStatus("current")
if mibBuilder.loadTexts:
    n_res.setUnits("N/A")


class _N_comp_Type(Integer32):
    """Custom type n_comp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_N_comp_Type.__name__ = "Integer32"
_N_comp_Object = MibScalar
n_comp = _N_comp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 32),
    _N_comp_Type()
)
n_comp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_comp.setStatus("current")
if mibBuilder.loadTexts:
    n_comp.setUnits("N/A")


class _Rit_hl_Type(Integer32):
    """Custom type rit_hl based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Rit_hl_Type.__name__ = "Integer32"
_Rit_hl_Object = MibScalar
rit_hl = _Rit_hl_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 33),
    _Rit_hl_Type()
)
rit_hl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_hl.setStatus("current")
if mibBuilder.loadTexts:
    rit_hl.setUnits("sec")


class _Rit_resistenze_Type(Integer32):
    """Custom type rit_resistenze based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Rit_resistenze_Type.__name__ = "Integer32"
_Rit_resistenze_Object = MibScalar
rit_resistenze = _Rit_resistenze_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 34),
    _Rit_resistenze_Type()
)
rit_resistenze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_resistenze.setStatus("current")
if mibBuilder.loadTexts:
    rit_resistenze.setUnits("sec")


class _Set_parz1_cw_Type(Integer32):
    """Custom type set_parz1_cw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Set_parz1_cw_Type.__name__ = "Integer32"
_Set_parz1_cw_Object = MibScalar
set_parz1_cw = _Set_parz1_cw_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 38),
    _Set_parz1_cw_Type()
)
set_parz1_cw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_parz1_cw.setStatus("current")
if mibBuilder.loadTexts:
    set_parz1_cw.setUnits("%")


class _Ist_parz1_cw_Type(Integer32):
    """Custom type ist_parz1_cw based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ist_parz1_cw_Type.__name__ = "Integer32"
_Ist_parz1_cw_Object = MibScalar
ist_parz1_cw = _Ist_parz1_cw_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 39),
    _Ist_parz1_cw_Type()
)
ist_parz1_cw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ist_parz1_cw.setStatus("current")
if mibBuilder.loadTexts:
    ist_parz1_cw.setUnits("%")


class _Set_parz2_cw_Type(Integer32):
    """Custom type set_parz2_cw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Set_parz2_cw_Type.__name__ = "Integer32"
_Set_parz2_cw_Object = MibScalar
set_parz2_cw = _Set_parz2_cw_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 40),
    _Set_parz2_cw_Type()
)
set_parz2_cw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_parz2_cw.setStatus("current")
if mibBuilder.loadTexts:
    set_parz2_cw.setUnits("%")


class _Ist_parz2_cw_Type(Integer32):
    """Custom type ist_parz2_cw based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ist_parz2_cw_Type.__name__ = "Integer32"
_Ist_parz2_cw_Object = MibScalar
ist_parz2_cw = _Ist_parz2_cw_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 41),
    _Ist_parz2_cw_Type()
)
ist_parz2_cw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ist_parz2_cw.setStatus("current")
if mibBuilder.loadTexts:
    ist_parz2_cw.setUnits("%")


class _Set_parz1_es_Type(Integer32):
    """Custom type set_parz1_es based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Set_parz1_es_Type.__name__ = "Integer32"
_Set_parz1_es_Object = MibScalar
set_parz1_es = _Set_parz1_es_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 44),
    _Set_parz1_es_Type()
)
set_parz1_es.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_parz1_es.setStatus("current")
if mibBuilder.loadTexts:
    set_parz1_es.setUnits("%")


class _Ist_parz1_es_Type(Integer32):
    """Custom type ist_parz1_es based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ist_parz1_es_Type.__name__ = "Integer32"
_Ist_parz1_es_Object = MibScalar
ist_parz1_es = _Ist_parz1_es_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 45),
    _Ist_parz1_es_Type()
)
ist_parz1_es.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ist_parz1_es.setStatus("current")
if mibBuilder.loadTexts:
    ist_parz1_es.setUnits("%")


class _Set_parz2_es_Type(Integer32):
    """Custom type set_parz2_es based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Set_parz2_es_Type.__name__ = "Integer32"
_Set_parz2_es_Object = MibScalar
set_parz2_es = _Set_parz2_es_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 46),
    _Set_parz2_es_Type()
)
set_parz2_es.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_parz2_es.setStatus("current")
if mibBuilder.loadTexts:
    set_parz2_es.setUnits("%")


class _Ist_parz2_es_Type(Integer32):
    """Custom type ist_parz2_es based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ist_parz2_es_Type.__name__ = "Integer32"
_Ist_parz2_es_Object = MibScalar
ist_parz2_es = _Ist_parz2_es_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 47),
    _Ist_parz2_es_Type()
)
ist_parz2_es.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ist_parz2_es.setStatus("current")
if mibBuilder.loadTexts:
    ist_parz2_es.setUnits("%")


class _T_int_Type(Integer32):
    """Custom type t_int based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_T_int_Type.__name__ = "Integer32"
_T_int_Object = MibScalar
t_int = _T_int_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 48),
    _T_int_Type()
)
t_int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t_int.setStatus("current")
if mibBuilder.loadTexts:
    t_int.setUnits("sec")


class _Sgl_ore_mac_Type(Integer32):
    """Custom type sgl_ore_mac based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Sgl_ore_mac_Type.__name__ = "Integer32"
_Sgl_ore_mac_Object = MibScalar
sgl_ore_mac = _Sgl_ore_mac_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 50),
    _Sgl_ore_mac_Type()
)
sgl_ore_mac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgl_ore_mac.setStatus("current")
if mibBuilder.loadTexts:
    sgl_ore_mac.setUnits("sec")


class _Sgl_ore_comp1_Type(Integer32):
    """Custom type sgl_ore_comp1 based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Sgl_ore_comp1_Type.__name__ = "Integer32"
_Sgl_ore_comp1_Object = MibScalar
sgl_ore_comp1 = _Sgl_ore_comp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 51),
    _Sgl_ore_comp1_Type()
)
sgl_ore_comp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgl_ore_comp1.setStatus("current")
if mibBuilder.loadTexts:
    sgl_ore_comp1.setUnits("sec")


class _Sgl_ore_comp2_Type(Integer32):
    """Custom type sgl_ore_comp2 based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Sgl_ore_comp2_Type.__name__ = "Integer32"
_Sgl_ore_comp2_Object = MibScalar
sgl_ore_comp2 = _Sgl_ore_comp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 52),
    _Sgl_ore_comp2_Type()
)
sgl_ore_comp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgl_ore_comp2.setStatus("current")
if mibBuilder.loadTexts:
    sgl_ore_comp2.setUnits("sec")


class _In_rampa_p3v_Type(Integer32):
    """Custom type in_rampa_p3v based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_In_rampa_p3v_Type.__name__ = "Integer32"
_In_rampa_p3v_Object = MibScalar
in_rampa_p3v = _In_rampa_p3v_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 54),
    _In_rampa_p3v_Type()
)
in_rampa_p3v.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    in_rampa_p3v.setStatus("current")
if mibBuilder.loadTexts:
    in_rampa_p3v.setUnits("%")


class _Fin_rampa_p3v_Type(Integer32):
    """Custom type fin_rampa_p3v based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fin_rampa_p3v_Type.__name__ = "Integer32"
_Fin_rampa_p3v_Object = MibScalar
fin_rampa_p3v = _Fin_rampa_p3v_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 55),
    _Fin_rampa_p3v_Type()
)
fin_rampa_p3v.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fin_rampa_p3v.setStatus("current")
if mibBuilder.loadTexts:
    fin_rampa_p3v.setUnits("%")


class _In_rampa_n3v_Type(Integer32):
    """Custom type in_rampa_n3v based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_In_rampa_n3v_Type.__name__ = "Integer32"
_In_rampa_n3v_Object = MibScalar
in_rampa_n3v = _In_rampa_n3v_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 56),
    _In_rampa_n3v_Type()
)
in_rampa_n3v.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    in_rampa_n3v.setStatus("current")
if mibBuilder.loadTexts:
    in_rampa_n3v.setUnits("%")


class _Fin_rampa_n3v_Type(Integer32):
    """Custom type fin_rampa_n3v based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fin_rampa_n3v_Type.__name__ = "Integer32"
_Fin_rampa_n3v_Object = MibScalar
fin_rampa_n3v = _Fin_rampa_n3v_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 57),
    _Fin_rampa_n3v_Type()
)
fin_rampa_n3v.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fin_rampa_n3v.setStatus("current")
if mibBuilder.loadTexts:
    fin_rampa_n3v.setUnits("%")


class _Tempo_run_Type(Integer32):
    """Custom type tempo_run based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Tempo_run_Type.__name__ = "Integer32"
_Tempo_run_Object = MibScalar
tempo_run = _Tempo_run_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 58),
    _Tempo_run_Type()
)
tempo_run.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempo_run.setStatus("current")
if mibBuilder.loadTexts:
    tempo_run.setUnits("sec")


class _Rit_syson_Type(Integer32):
    """Custom type rit_syson based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Rit_syson_Type.__name__ = "Integer32"
_Rit_syson_Object = MibScalar
rit_syson = _Rit_syson_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 59),
    _Rit_syson_Type()
)
rit_syson.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_syson.setStatus("current")
if mibBuilder.loadTexts:
    rit_syson.setUnits("sec")


class _Vr1cen_Type(Integer32):
    """Custom type vr1cen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Vr1cen_Type.__name__ = "Integer32"
_Vr1cen_Object = MibScalar
vr1cen = _Vr1cen_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 61),
    _Vr1cen_Type()
)
vr1cen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vr1cen.setStatus("current")
if mibBuilder.loadTexts:
    vr1cen.setUnits("N/A")


class _Vr2cen_Type(Integer32):
    """Custom type vr2cen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Vr2cen_Type.__name__ = "Integer32"
_Vr2cen_Object = MibScalar
vr2cen = _Vr2cen_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 62),
    _Vr2cen_Type()
)
vr2cen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vr2cen.setStatus("current")
if mibBuilder.loadTexts:
    vr2cen.setUnits("N/A")


class _Ore_mac_Type(Integer32):
    """Custom type ore_mac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ore_mac_Type.__name__ = "Integer32"
_Ore_mac_Object = MibScalar
ore_mac = _Ore_mac_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 63),
    _Ore_mac_Type()
)
ore_mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ore_mac.setStatus("current")
if mibBuilder.loadTexts:
    ore_mac.setUnits("N/A")


class _Ore_comp1_Type(Integer32):
    """Custom type ore_comp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ore_comp1_Type.__name__ = "Integer32"
_Ore_comp1_Object = MibScalar
ore_comp1 = _Ore_comp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 65),
    _Ore_comp1_Type()
)
ore_comp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ore_comp1.setStatus("current")
if mibBuilder.loadTexts:
    ore_comp1.setUnits("N/A")


class _Ore_comp2_Type(Integer32):
    """Custom type ore_comp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ore_comp2_Type.__name__ = "Integer32"
_Ore_comp2_Object = MibScalar
ore_comp2 = _Ore_comp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 66),
    _Ore_comp2_Type()
)
ore_comp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ore_comp2.setStatus("current")
if mibBuilder.loadTexts:
    ore_comp2.setUnits("N/A")


class _X_h_main_fan_Type(Integer32):
    """Custom type x_h_main_fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_X_h_main_fan_Type.__name__ = "Integer32"
_X_h_main_fan_Object = MibScalar
x_h_main_fan = _X_h_main_fan_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 67),
    _X_h_main_fan_Type()
)
x_h_main_fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x_h_main_fan.setStatus("current")
if mibBuilder.loadTexts:
    x_h_main_fan.setUnits("N/A")


class _X_h_valve_comp1_Type(Integer32):
    """Custom type x_h_valve_comp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_X_h_valve_comp1_Type.__name__ = "Integer32"
_X_h_valve_comp1_Object = MibScalar
x_h_valve_comp1 = _X_h_valve_comp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 68),
    _X_h_valve_comp1_Type()
)
x_h_valve_comp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x_h_valve_comp1.setStatus("current")
if mibBuilder.loadTexts:
    x_h_valve_comp1.setUnits("N/A")


class _X_h_valve_comp2_Type(Integer32):
    """Custom type x_h_valve_comp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_X_h_valve_comp2_Type.__name__ = "Integer32"
_X_h_valve_comp2_Object = MibScalar
x_h_valve_comp2 = _X_h_valve_comp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 69),
    _X_h_valve_comp2_Type()
)
x_h_valve_comp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x_h_valve_comp2.setStatus("current")
if mibBuilder.loadTexts:
    x_h_valve_comp2.setUnits("N/A")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAREL-cdz_pco-MIB",
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
       "cdz_pcoMIB": cdz_pcoMIB,
       "digitalObjects": digitalObjects,
       "z1": z1,
       "z3": z3,
       "z4": z4,
       "z5": z5,
       "z6": z6,
       "z7": z7,
       "onr": onr,
       "z9": z9,
       "z10": z10,
       "z12": z12,
       "val_par": val_par,
       "syson2": syson2,
       "val_es_ok": val_es_ok,
       "umidifica": umidifica,
       "parz1": parz1,
       "parz2": parz2,
       "valfre": valfre,
       "valfre1": valfre1,
       "valca": valca,
       "valca1": valca1,
       "glb_al": glb_al,
       "s_firmanook": s_firmanook,
       "s_error_io": s_error_io,
       "s_bp1": s_bp1,
       "s_bp2": s_bp2,
       "s_fl1": s_fl1,
       "s_trf": s_trf,
       "s_trs1": s_trs1,
       "s_trs2": s_trs2,
       "s_fsa": s_fsa,
       "s_flt": s_flt,
       "s_all_h_temp": s_all_h_temp,
       "s_all_l_temp": s_all_l_temp,
       "s_all_h_umid": s_all_h_umid,
       "s_all_l_umid": s_all_l_umid,
       "s_al_ore_comp1": s_al_ore_comp1,
       "s_al_ore_comp2": s_al_ore_comp2,
       "s_al_ore_umidif": s_al_ore_umidif,
       "s_al_ore_mac": s_al_ore_mac,
       "s_al_ore_res1": s_al_ore_res1,
       "s_al_ore_res2": s_al_ore_res2,
       "s_all_h_free": s_all_h_free,
       "s_all_l_free": s_all_l_free,
       "s_sonda1_ko": s_sonda1_ko,
       "s_sonda2_ko": s_sonda2_ko,
       "s_sonda4_ko": s_sonda4_ko,
       "s_sonda6_ko": s_sonda6_ko,
       "s_sondau_ko": s_sondau_ko,
       "s_epromnook": s_epromnook,
       "pro_pi": pro_pi,
       "si_sond_umid": si_sond_umid,
       "si_sond_acqua": si_sond_acqua,
       "si_sond_aria": si_sond_aria,
       "si_sond_acquain": si_sond_acquain,
       "si_sond_ariain": si_sond_ariain,
       "bin_sta": bin_sta,
       "si_rampap": si_rampap,
       "es": es,
       "si_comp_es": si_comp_es,
       "si_rampan": si_rampan,
       "si_parz": si_parz,
       "si_rot2": si_rot2,
       "si_comp1_deu": si_comp1_deu,
       "si_comp2_deu": si_comp2_deu,
       "si_fasce": si_fasce,
       "syson": syson,
       "si_rampap3v": si_rampap3v,
       "si_rampan3v": si_rampan3v,
       "manuale": manuale,
       "start_off": start_off,
       "alarm_e06": alarm_e06,
       "alarm_e08": alarm_e08,
       "alarm_e09": alarm_e09,
       "alarm_e10": alarm_e10,
       "alarm_e11": alarm_e11,
       "alarm_e12": alarm_e12,
       "analogObjects": analogObjects,
       "temp": temp,
       "umid": umid,
       "acqua": acqua,
       "aria_acqua_in": aria_acqua_in,
       "temp_aria_man": temp_aria_man,
       "zona_morta": zona_morta,
       "banda_hum": banda_hum,
       "set_hum_a": set_hum_a,
       "sgl_l_temp": sgl_l_temp,
       "sgl_h_temp": sgl_h_temp,
       "sgl_l_umid": sgl_l_umid,
       "sgl_h_umid": sgl_h_umid,
       "set_temp_a": set_temp_a,
       "banda_temp": banda_temp,
       "sgl_l_free": sgl_l_free,
       "sgl_h_free": sgl_h_free,
       "integerObjects": integerObjects,
       "in_rampa_p": in_rampa_p,
       "fin_rampa_p": fin_rampa_p,
       "in_rampa_n": in_rampa_n,
       "fin_rampa_n": fin_rampa_n,
       "set_comp1_cw": set_comp1_cw,
       "ist_comp1_cw": ist_comp1_cw,
       "set_comp2_cw": set_comp2_cw,
       "ist_comp2_cw": ist_comp2_cw,
       "set_comp1_es": set_comp1_es,
       "ist_comp1_es": ist_comp1_es,
       "set_comp2_es": set_comp2_es,
       "ist_comp2_es": ist_comp2_es,
       "rit_fra_ins": rit_fra_ins,
       "rit_bassa_pres": rit_bassa_pres,
       "rit_riaccen": rit_riaccen,
       "rit_tra_ins": rit_tra_ins,
       "n_res": n_res,
       "n_comp": n_comp,
       "rit_hl": rit_hl,
       "rit_resistenze": rit_resistenze,
       "set_parz1_cw": set_parz1_cw,
       "ist_parz1_cw": ist_parz1_cw,
       "set_parz2_cw": set_parz2_cw,
       "ist_parz2_cw": ist_parz2_cw,
       "set_parz1_es": set_parz1_es,
       "ist_parz1_es": ist_parz1_es,
       "set_parz2_es": set_parz2_es,
       "ist_parz2_es": ist_parz2_es,
       "t_int": t_int,
       "sgl_ore_mac": sgl_ore_mac,
       "sgl_ore_comp1": sgl_ore_comp1,
       "sgl_ore_comp2": sgl_ore_comp2,
       "in_rampa_p3v": in_rampa_p3v,
       "fin_rampa_p3v": fin_rampa_p3v,
       "in_rampa_n3v": in_rampa_n3v,
       "fin_rampa_n3v": fin_rampa_n3v,
       "tempo_run": tempo_run,
       "rit_syson": rit_syson,
       "vr1cen": vr1cen,
       "vr2cen": vr2cen,
       "ore_mac": ore_mac,
       "ore_comp1": ore_comp1,
       "ore_comp2": ore_comp2,
       "x_h_main_fan": x_h_main_fan,
       "x_h_valve_comp1": x_h_valve_comp1,
       "x_h_valve_comp2": x_h_valve_comp2}
)
