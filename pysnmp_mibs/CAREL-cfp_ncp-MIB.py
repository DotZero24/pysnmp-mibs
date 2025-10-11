# SNMP MIB module (CAREL-cfp_ncp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/carel/CAREL-cfp_ncp-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:06 2025
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

cfp_ncpMIB = ModuleIdentity(
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


class _Comp1_Type(Integer32):
    """Custom type comp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Comp1_Type.__name__ = "Integer32"
_Comp1_Object = MibScalar
comp1 = _Comp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 2),
    _Comp1_Type()
)
comp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comp1.setStatus("current")
if mibBuilder.loadTexts:
    comp1.setUnits("N/A")


class _Comp2_Type(Integer32):
    """Custom type comp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Comp2_Type.__name__ = "Integer32"
_Comp2_Object = MibScalar
comp2 = _Comp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 3),
    _Comp2_Type()
)
comp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comp2.setStatus("current")
if mibBuilder.loadTexts:
    comp2.setUnits("N/A")


class _Comp3_Type(Integer32):
    """Custom type comp3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Comp3_Type.__name__ = "Integer32"
_Comp3_Object = MibScalar
comp3 = _Comp3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 4),
    _Comp3_Type()
)
comp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comp3.setStatus("current")
if mibBuilder.loadTexts:
    comp3.setUnits("N/A")


class _Vent1_Type(Integer32):
    """Custom type vent1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Vent1_Type.__name__ = "Integer32"
_Vent1_Object = MibScalar
vent1 = _Vent1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 7),
    _Vent1_Type()
)
vent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vent1.setStatus("current")
if mibBuilder.loadTexts:
    vent1.setUnits("N/A")


class _Vent2_Type(Integer32):
    """Custom type vent2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Vent2_Type.__name__ = "Integer32"
_Vent2_Object = MibScalar
vent2 = _Vent2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 8),
    _Vent2_Type()
)
vent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vent2.setStatus("current")
if mibBuilder.loadTexts:
    vent2.setUnits("N/A")


class _Vent3_Type(Integer32):
    """Custom type vent3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Vent3_Type.__name__ = "Integer32"
_Vent3_Object = MibScalar
vent3 = _Vent3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 9),
    _Vent3_Type()
)
vent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vent3.setStatus("current")
if mibBuilder.loadTexts:
    vent3.setUnits("N/A")


class _Sys_on_Type(Integer32):
    """Custom type sys_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sys_on_Type.__name__ = "Integer32"
_Sys_on_Object = MibScalar
sys_on = _Sys_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 12),
    _Sys_on_Type()
)
sys_on.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sys_on.setStatus("current")
if mibBuilder.loadTexts:
    sys_on.setUnits("N/A")


class _Mask_term_klix1_Type(Integer32):
    """Custom type mask_term_klix1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_term_klix1_Type.__name__ = "Integer32"
_Mask_term_klix1_Object = MibScalar
mask_term_klix1 = _Mask_term_klix1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 13),
    _Mask_term_klix1_Type()
)
mask_term_klix1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_term_klix1.setStatus("current")
if mibBuilder.loadTexts:
    mask_term_klix1.setUnits("N/A")


class _Mask_term_klix2_Type(Integer32):
    """Custom type mask_term_klix2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_term_klix2_Type.__name__ = "Integer32"
_Mask_term_klix2_Object = MibScalar
mask_term_klix2 = _Mask_term_klix2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 14),
    _Mask_term_klix2_Type()
)
mask_term_klix2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_term_klix2.setStatus("current")
if mibBuilder.loadTexts:
    mask_term_klix2.setUnits("N/A")


class _Mask_term_klix3_Type(Integer32):
    """Custom type mask_term_klix3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_term_klix3_Type.__name__ = "Integer32"
_Mask_term_klix3_Object = MibScalar
mask_term_klix3 = _Mask_term_klix3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 15),
    _Mask_term_klix3_Type()
)
mask_term_klix3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_term_klix3.setStatus("current")
if mibBuilder.loadTexts:
    mask_term_klix3.setUnits("N/A")


class _Mask_dif_olio1_Type(Integer32):
    """Custom type mask_dif_olio1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_dif_olio1_Type.__name__ = "Integer32"
_Mask_dif_olio1_Object = MibScalar
mask_dif_olio1 = _Mask_dif_olio1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 23),
    _Mask_dif_olio1_Type()
)
mask_dif_olio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_dif_olio1.setStatus("current")
if mibBuilder.loadTexts:
    mask_dif_olio1.setUnits("sec")


class _Mask_dif_olio2_Type(Integer32):
    """Custom type mask_dif_olio2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_dif_olio2_Type.__name__ = "Integer32"
_Mask_dif_olio2_Object = MibScalar
mask_dif_olio2 = _Mask_dif_olio2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 24),
    _Mask_dif_olio2_Type()
)
mask_dif_olio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_dif_olio2.setStatus("current")
if mibBuilder.loadTexts:
    mask_dif_olio2.setUnits("N/A")


class _Mask_dif_olio3_Type(Integer32):
    """Custom type mask_dif_olio3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_dif_olio3_Type.__name__ = "Integer32"
_Mask_dif_olio3_Object = MibScalar
mask_dif_olio3 = _Mask_dif_olio3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 25),
    _Mask_dif_olio3_Type()
)
mask_dif_olio3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_dif_olio3.setStatus("current")
if mibBuilder.loadTexts:
    mask_dif_olio3.setUnits("N/A")


class _Mask_pres_lpres_Type(Integer32):
    """Custom type mask_pres_lpres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_pres_lpres_Type.__name__ = "Integer32"
_Mask_pres_lpres_Object = MibScalar
mask_pres_lpres = _Mask_pres_lpres_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 28),
    _Mask_pres_lpres_Type()
)
mask_pres_lpres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_pres_lpres.setStatus("current")
if mibBuilder.loadTexts:
    mask_pres_lpres.setUnits("N/A")


class _Mask_pres_hpres_Type(Integer32):
    """Custom type mask_pres_hpres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_pres_hpres_Type.__name__ = "Integer32"
_Mask_pres_hpres_Object = MibScalar
mask_pres_hpres = _Mask_pres_hpres_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 29),
    _Mask_pres_hpres_Type()
)
mask_pres_hpres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_pres_hpres.setStatus("current")
if mibBuilder.loadTexts:
    mask_pres_hpres.setUnits("N/A")


class _Mask_liv_liq_Type(Integer32):
    """Custom type mask_liv_liq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_liv_liq_Type.__name__ = "Integer32"
_Mask_liv_liq_Object = MibScalar
mask_liv_liq = _Mask_liv_liq_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 30),
    _Mask_liv_liq_Type()
)
mask_liv_liq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_liv_liq.setStatus("current")
if mibBuilder.loadTexts:
    mask_liv_liq.setUnits("N/A")


class _Mask_term_vent1_Type(Integer32):
    """Custom type mask_term_vent1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_term_vent1_Type.__name__ = "Integer32"
_Mask_term_vent1_Object = MibScalar
mask_term_vent1 = _Mask_term_vent1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 32),
    _Mask_term_vent1_Type()
)
mask_term_vent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_term_vent1.setStatus("current")
if mibBuilder.loadTexts:
    mask_term_vent1.setUnits("N/A")


class _Mask_term_vent2_Type(Integer32):
    """Custom type mask_term_vent2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_term_vent2_Type.__name__ = "Integer32"
_Mask_term_vent2_Object = MibScalar
mask_term_vent2 = _Mask_term_vent2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 33),
    _Mask_term_vent2_Type()
)
mask_term_vent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_term_vent2.setStatus("current")
if mibBuilder.loadTexts:
    mask_term_vent2.setUnits("N/A")


class _Mask_term_vent3_Type(Integer32):
    """Custom type mask_term_vent3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_term_vent3_Type.__name__ = "Integer32"
_Mask_term_vent3_Object = MibScalar
mask_term_vent3 = _Mask_term_vent3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 34),
    _Mask_term_vent3_Type()
)
mask_term_vent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_term_vent3.setStatus("current")
if mibBuilder.loadTexts:
    mask_term_vent3.setUnits("N/A")


class _Mask_ore_comp1_Type(Integer32):
    """Custom type mask_ore_comp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_ore_comp1_Type.__name__ = "Integer32"
_Mask_ore_comp1_Object = MibScalar
mask_ore_comp1 = _Mask_ore_comp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 37),
    _Mask_ore_comp1_Type()
)
mask_ore_comp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_ore_comp1.setStatus("current")
if mibBuilder.loadTexts:
    mask_ore_comp1.setUnits("N/A")


class _Mask_ore_comp2_Type(Integer32):
    """Custom type mask_ore_comp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_ore_comp2_Type.__name__ = "Integer32"
_Mask_ore_comp2_Object = MibScalar
mask_ore_comp2 = _Mask_ore_comp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 38),
    _Mask_ore_comp2_Type()
)
mask_ore_comp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_ore_comp2.setStatus("current")
if mibBuilder.loadTexts:
    mask_ore_comp2.setUnits("N/A")


class _Mask_ore_comp3_Type(Integer32):
    """Custom type mask_ore_comp3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_ore_comp3_Type.__name__ = "Integer32"
_Mask_ore_comp3_Object = MibScalar
mask_ore_comp3 = _Mask_ore_comp3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 39),
    _Mask_ore_comp3_Type()
)
mask_ore_comp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_ore_comp3.setStatus("current")
if mibBuilder.loadTexts:
    mask_ore_comp3.setUnits("N/A")


class _Mask_alta_mand_Type(Integer32):
    """Custom type mask_alta_mand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_alta_mand_Type.__name__ = "Integer32"
_Mask_alta_mand_Object = MibScalar
mask_alta_mand = _Mask_alta_mand_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 42),
    _Mask_alta_mand_Type()
)
mask_alta_mand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_alta_mand.setStatus("current")
if mibBuilder.loadTexts:
    mask_alta_mand.setUnits("N/A")


class _Mask_alta_asp_Type(Integer32):
    """Custom type mask_alta_asp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_alta_asp_Type.__name__ = "Integer32"
_Mask_alta_asp_Object = MibScalar
mask_alta_asp = _Mask_alta_asp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 43),
    _Mask_alta_asp_Type()
)
mask_alta_asp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_alta_asp.setStatus("current")
if mibBuilder.loadTexts:
    mask_alta_asp.setUnits("N/A")


class _Mask_ora_Type(Integer32):
    """Custom type mask_ora based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_ora_Type.__name__ = "Integer32"
_Mask_ora_Object = MibScalar
mask_ora = _Mask_ora_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 46),
    _Mask_ora_Type()
)
mask_ora.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_ora.setStatus("current")
if mibBuilder.loadTexts:
    mask_ora.setUnits("N/A")


class _Mask_epromnook_Type(Integer32):
    """Custom type mask_epromnook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_epromnook_Type.__name__ = "Integer32"
_Mask_epromnook_Object = MibScalar
mask_epromnook = _Mask_epromnook_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 48),
    _Mask_epromnook_Type()
)
mask_epromnook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_epromnook.setStatus("current")
if mibBuilder.loadTexts:
    mask_epromnook.setUnits("N/A")


class _Mask_bassa_asp_Type(Integer32):
    """Custom type mask_bassa_asp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mask_bassa_asp_Type.__name__ = "Integer32"
_Mask_bassa_asp_Object = MibScalar
mask_bassa_asp = _Mask_bassa_asp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 49),
    _Mask_bassa_asp_Type()
)
mask_bassa_asp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mask_bassa_asp.setStatus("current")
if mibBuilder.loadTexts:
    mask_bassa_asp.setUnits("N/A")


class _Glb_al_Type(Integer32):
    """Custom type glb_al based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Glb_al_Type.__name__ = "Integer32"
_Glb_al_Object = MibScalar
glb_al = _Glb_al_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 51),
    _Glb_al_Type()
)
glb_al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    glb_al.setStatus("current")
if mibBuilder.loadTexts:
    glb_al.setUnits("N/A")
_AnalogObjects_ObjectIdentity = ObjectIdentity
analogObjects = _AnalogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2)
)


class _Asp_conv_Type(Integer32):
    """Custom type asp_conv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Asp_conv_Type.__name__ = "Integer32"
_Asp_conv_Object = MibScalar
asp_conv = _Asp_conv_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 1),
    _Asp_conv_Type()
)
asp_conv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asp_conv.setStatus("current")
if mibBuilder.loadTexts:
    asp_conv.setUnits("bar x10")


class _Press_mand_conv_Type(Integer32):
    """Custom type press_mand_conv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Press_mand_conv_Type.__name__ = "Integer32"
_Press_mand_conv_Object = MibScalar
press_mand_conv = _Press_mand_conv_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 2),
    _Press_mand_conv_Type()
)
press_mand_conv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    press_mand_conv.setStatus("current")
if mibBuilder.loadTexts:
    press_mand_conv.setUnits("bar x10")


class _Set_comp_Type(Integer32):
    """Custom type set_comp based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Set_comp_Type.__name__ = "Integer32"
_Set_comp_Object = MibScalar
set_comp = _Set_comp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 3),
    _Set_comp_Type()
)
set_comp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_comp.setStatus("current")
if mibBuilder.loadTexts:
    set_comp.setUnits("bar x10")


class _Diff_comp_Type(Integer32):
    """Custom type diff_comp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_Diff_comp_Type.__name__ = "Integer32"
_Diff_comp_Object = MibScalar
diff_comp = _Diff_comp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 4),
    _Diff_comp_Type()
)
diff_comp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diff_comp.setStatus("current")
if mibBuilder.loadTexts:
    diff_comp.setUnits("bar x10")


class _Sg_bassa_asp_Type(Integer32):
    """Custom type sg_bassa_asp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 500),
    )


_Sg_bassa_asp_Type.__name__ = "Integer32"
_Sg_bassa_asp_Object = MibScalar
sg_bassa_asp = _Sg_bassa_asp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 5),
    _Sg_bassa_asp_Type()
)
sg_bassa_asp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sg_bassa_asp.setStatus("current")
if mibBuilder.loadTexts:
    sg_bassa_asp.setUnits("bar x10")


class _Set_vent_off1_Type(Integer32):
    """Custom type set_vent_off1 based on Integer32"""
    defaultValue = 155

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Set_vent_off1_Type.__name__ = "Integer32"
_Set_vent_off1_Object = MibScalar
set_vent_off1 = _Set_vent_off1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 6),
    _Set_vent_off1_Type()
)
set_vent_off1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_vent_off1.setStatus("current")
if mibBuilder.loadTexts:
    set_vent_off1.setUnits("bar x10")


class _Diff_vent_Type(Integer32):
    """Custom type diff_vent based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Diff_vent_Type.__name__ = "Integer32"
_Diff_vent_Object = MibScalar
diff_vent = _Diff_vent_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 7),
    _Diff_vent_Type()
)
diff_vent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diff_vent.setStatus("current")
if mibBuilder.loadTexts:
    diff_vent.setUnits("bar x10")


class _Sg_alta_asp_Type(Integer32):
    """Custom type sg_alta_asp based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Sg_alta_asp_Type.__name__ = "Integer32"
_Sg_alta_asp_Object = MibScalar
sg_alta_asp = _Sg_alta_asp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 8),
    _Sg_alta_asp_Type()
)
sg_alta_asp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sg_alta_asp.setStatus("current")
if mibBuilder.loadTexts:
    sg_alta_asp.setUnits("bar x10")


class _Sg_alta_mand_Type(Integer32):
    """Custom type sg_alta_mand based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Sg_alta_mand_Type.__name__ = "Integer32"
_Sg_alta_mand_Object = MibScalar
sg_alta_mand = _Sg_alta_mand_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 9),
    _Sg_alta_mand_Type()
)
sg_alta_mand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sg_alta_mand.setStatus("current")
if mibBuilder.loadTexts:
    sg_alta_mand.setUnits("bar x10")


class _Ins_comp_Type(Integer32):
    """Custom type ins_comp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ins_comp_Type.__name__ = "Integer32"
_Ins_comp_Object = MibScalar
ins_comp = _Ins_comp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 10),
    _Ins_comp_Type()
)
ins_comp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ins_comp.setStatus("current")
if mibBuilder.loadTexts:
    ins_comp.setUnits("N/A")


class _Dis_comp_Type(Integer32):
    """Custom type dis_comp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Dis_comp_Type.__name__ = "Integer32"
_Dis_comp_Object = MibScalar
dis_comp = _Dis_comp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 11),
    _Dis_comp_Type()
)
dis_comp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dis_comp.setStatus("current")
if mibBuilder.loadTexts:
    dis_comp.setUnits("N/A")
_IntegerObjects_ObjectIdentity = ObjectIdentity
integerObjects = _IntegerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3)
)


class _N_comp_Type(Integer32):
    """Custom type n_comp based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_N_comp_Type.__name__ = "Integer32"
_N_comp_Object = MibScalar
n_comp = _N_comp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 10),
    _N_comp_Type()
)
n_comp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_comp.setStatus("current")
if mibBuilder.loadTexts:
    n_comp.setUnits("N/A")


class _N_vent_Type(Integer32):
    """Custom type n_vent based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_N_vent_Type.__name__ = "Integer32"
_N_vent_Object = MibScalar
n_vent = _N_vent_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 11),
    _N_vent_Type()
)
n_vent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n_vent.setStatus("current")
if mibBuilder.loadTexts:
    n_vent.setUnits("N/A")


class _Lhour_Type(Integer32):
    """Custom type lhour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Lhour_Type.__name__ = "Integer32"
_Lhour_Object = MibScalar
lhour = _Lhour_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 12),
    _Lhour_Type()
)
lhour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lhour.setStatus("current")
if mibBuilder.loadTexts:
    lhour.setUnits("hour")


class _Lminute_Type(Integer32):
    """Custom type lminute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Lminute_Type.__name__ = "Integer32"
_Lminute_Object = MibScalar
lminute = _Lminute_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 13),
    _Lminute_Type()
)
lminute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lminute.setStatus("current")
if mibBuilder.loadTexts:
    lminute.setUnits("min")


class _Hour_Type(Integer32):
    """Custom type hour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Hour_Type.__name__ = "Integer32"
_Hour_Object = MibScalar
hour = _Hour_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 14),
    _Hour_Type()
)
hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hour.setStatus("current")
if mibBuilder.loadTexts:
    hour.setUnits("N/A")


class _Minute_Type(Integer32):
    """Custom type minute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Minute_Type.__name__ = "Integer32"
_Minute_Object = MibScalar
minute = _Minute_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 15),
    _Minute_Type()
)
minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minute.setStatus("current")
if mibBuilder.loadTexts:
    minute.setUnits("N/A")


class _Ora_autocall_Type(Integer32):
    """Custom type ora_autocall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Ora_autocall_Type.__name__ = "Integer32"
_Ora_autocall_Object = MibScalar
ora_autocall = _Ora_autocall_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 16),
    _Ora_autocall_Type()
)
ora_autocall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ora_autocall.setStatus("current")
if mibBuilder.loadTexts:
    ora_autocall.setUnits("hour")


class _Minuti_autocall_Type(Integer32):
    """Custom type minuti_autocall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Minuti_autocall_Type.__name__ = "Integer32"
_Minuti_autocall_Object = MibScalar
minuti_autocall = _Minuti_autocall_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 17),
    _Minuti_autocall_Type()
)
minuti_autocall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minuti_autocall.setStatus("current")
if mibBuilder.loadTexts:
    minuti_autocall.setUnits("min")


class _Sg_ore_comp_Type(Integer32):
    """Custom type sg_ore_comp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Sg_ore_comp_Type.__name__ = "Integer32"
_Sg_ore_comp_Object = MibScalar
sg_ore_comp = _Sg_ore_comp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 18),
    _Sg_ore_comp_Type()
)
sg_ore_comp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sg_ore_comp.setStatus("current")
if mibBuilder.loadTexts:
    sg_ore_comp.setUnits("N/A")


class _Ore_comp1_Type(Integer32):
    """Custom type ore_comp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ore_comp1_Type.__name__ = "Integer32"
_Ore_comp1_Object = MibScalar
ore_comp1 = _Ore_comp1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 19),
    _Ore_comp1_Type()
)
ore_comp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ore_comp1.setStatus("current")
if mibBuilder.loadTexts:
    ore_comp1.setUnits("hour")


class _Ore_comp2_Type(Integer32):
    """Custom type ore_comp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ore_comp2_Type.__name__ = "Integer32"
_Ore_comp2_Object = MibScalar
ore_comp2 = _Ore_comp2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 20),
    _Ore_comp2_Type()
)
ore_comp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ore_comp2.setStatus("current")
if mibBuilder.loadTexts:
    ore_comp2.setUnits("hour")


class _Ore_comp3_Type(Integer32):
    """Custom type ore_comp3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Ore_comp3_Type.__name__ = "Integer32"
_Ore_comp3_Object = MibScalar
ore_comp3 = _Ore_comp3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 21),
    _Ore_comp3_Type()
)
ore_comp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ore_comp3.setStatus("current")
if mibBuilder.loadTexts:
    ore_comp3.setUnits("hour")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAREL-cfp_ncp-MIB",
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
       "cfp_ncpMIB": cfp_ncpMIB,
       "digitalObjects": digitalObjects,
       "comp1": comp1,
       "comp2": comp2,
       "comp3": comp3,
       "vent1": vent1,
       "vent2": vent2,
       "vent3": vent3,
       "sys_on": sys_on,
       "mask_term_klix1": mask_term_klix1,
       "mask_term_klix2": mask_term_klix2,
       "mask_term_klix3": mask_term_klix3,
       "mask_dif_olio1": mask_dif_olio1,
       "mask_dif_olio2": mask_dif_olio2,
       "mask_dif_olio3": mask_dif_olio3,
       "mask_pres_lpres": mask_pres_lpres,
       "mask_pres_hpres": mask_pres_hpres,
       "mask_liv_liq": mask_liv_liq,
       "mask_term_vent1": mask_term_vent1,
       "mask_term_vent2": mask_term_vent2,
       "mask_term_vent3": mask_term_vent3,
       "mask_ore_comp1": mask_ore_comp1,
       "mask_ore_comp2": mask_ore_comp2,
       "mask_ore_comp3": mask_ore_comp3,
       "mask_alta_mand": mask_alta_mand,
       "mask_alta_asp": mask_alta_asp,
       "mask_ora": mask_ora,
       "mask_epromnook": mask_epromnook,
       "mask_bassa_asp": mask_bassa_asp,
       "glb_al": glb_al,
       "analogObjects": analogObjects,
       "asp_conv": asp_conv,
       "press_mand_conv": press_mand_conv,
       "set_comp": set_comp,
       "diff_comp": diff_comp,
       "sg_bassa_asp": sg_bassa_asp,
       "set_vent_off1": set_vent_off1,
       "diff_vent": diff_vent,
       "sg_alta_asp": sg_alta_asp,
       "sg_alta_mand": sg_alta_mand,
       "ins_comp": ins_comp,
       "dis_comp": dis_comp,
       "integerObjects": integerObjects,
       "n_comp": n_comp,
       "n_vent": n_vent,
       "lhour": lhour,
       "lminute": lminute,
       "hour": hour,
       "minute": minute,
       "ora_autocall": ora_autocall,
       "minuti_autocall": minuti_autocall,
       "sg_ore_comp": sg_ore_comp,
       "ore_comp1": ore_comp1,
       "ore_comp2": ore_comp2,
       "ore_comp3": ore_comp3}
)
