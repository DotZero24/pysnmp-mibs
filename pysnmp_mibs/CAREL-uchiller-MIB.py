# SNMP MIB module (CAREL-uchiller-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/carel/CAREL-uchiller-MIB
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

uchillerMIB = ModuleIdentity(
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


class _Res_antig_c1_Type(Integer32):
    """Custom type res_antig_c1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Res_antig_c1_Type.__name__ = "Integer32"
_Res_antig_c1_Object = MibScalar
res_antig_c1 = _Res_antig_c1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 1),
    _Res_antig_c1_Type()
)
res_antig_c1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    res_antig_c1.setStatus("current")
if mibBuilder.loadTexts:
    res_antig_c1.setUnits("N/A")


class _Valv_inv_c1_Type(Integer32):
    """Custom type valv_inv_c1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Valv_inv_c1_Type.__name__ = "Integer32"
_Valv_inv_c1_Object = MibScalar
valv_inv_c1 = _Valv_inv_c1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 3),
    _Valv_inv_c1_Type()
)
valv_inv_c1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valv_inv_c1.setStatus("current")
if mibBuilder.loadTexts:
    valv_inv_c1.setUnits("N/A")


class _Allarme_Type(Integer32):
    """Custom type allarme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Allarme_Type.__name__ = "Integer32"
_Allarme_Object = MibScalar
allarme = _Allarme_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 5),
    _Allarme_Type()
)
allarme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allarme.setStatus("current")
if mibBuilder.loadTexts:
    allarme.setUnits("N/A")


class _Antifreeze_resist_c2_Type(Integer32):
    """Custom type antifreeze_resist_c2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Antifreeze_resist_c2_Type.__name__ = "Integer32"
_Antifreeze_resist_c2_Object = MibScalar
antifreeze_resist_c2 = _Antifreeze_resist_c2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 6),
    _Antifreeze_resist_c2_Type()
)
antifreeze_resist_c2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antifreeze_resist_c2.setStatus("current")
if mibBuilder.loadTexts:
    antifreeze_resist_c2.setUnits("flag")


class _Compressore_c2_Type(Integer32):
    """Custom type compressore_c2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Compressore_c2_Type.__name__ = "Integer32"
_Compressore_c2_Object = MibScalar
compressore_c2 = _Compressore_c2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 7),
    _Compressore_c2_Type()
)
compressore_c2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressore_c2.setStatus("current")
if mibBuilder.loadTexts:
    compressore_c2.setUnits("flag")


class _Valv_inv_c2_Type(Integer32):
    """Custom type valv_inv_c2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Valv_inv_c2_Type.__name__ = "Integer32"
_Valv_inv_c2_Object = MibScalar
valv_inv_c2 = _Valv_inv_c2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 8),
    _Valv_inv_c2_Type()
)
valv_inv_c2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valv_inv_c2.setStatus("current")
if mibBuilder.loadTexts:
    valv_inv_c2.setUnits("flag")


class _Err_sonda_s1_Type(Integer32):
    """Custom type err_sonda_s1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Err_sonda_s1_Type.__name__ = "Integer32"
_Err_sonda_s1_Object = MibScalar
err_sonda_s1 = _Err_sonda_s1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 9),
    _Err_sonda_s1_Type()
)
err_sonda_s1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    err_sonda_s1.setStatus("current")
if mibBuilder.loadTexts:
    err_sonda_s1.setUnits("N/A")


class _Err_sonda_s2_Type(Integer32):
    """Custom type err_sonda_s2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Err_sonda_s2_Type.__name__ = "Integer32"
_Err_sonda_s2_Object = MibScalar
err_sonda_s2 = _Err_sonda_s2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 10),
    _Err_sonda_s2_Type()
)
err_sonda_s2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    err_sonda_s2.setStatus("current")
if mibBuilder.loadTexts:
    err_sonda_s2.setUnits("N/A")


class _Err_sonda_s3_Type(Integer32):
    """Custom type err_sonda_s3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Err_sonda_s3_Type.__name__ = "Integer32"
_Err_sonda_s3_Object = MibScalar
err_sonda_s3 = _Err_sonda_s3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 11),
    _Err_sonda_s3_Type()
)
err_sonda_s3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    err_sonda_s3.setStatus("current")
if mibBuilder.loadTexts:
    err_sonda_s3.setUnits("N/A")


class _Err_sonda_s4_Type(Integer32):
    """Custom type err_sonda_s4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Err_sonda_s4_Type.__name__ = "Integer32"
_Err_sonda_s4_Object = MibScalar
err_sonda_s4 = _Err_sonda_s4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 12),
    _Err_sonda_s4_Type()
)
err_sonda_s4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    err_sonda_s4.setStatus("current")
if mibBuilder.loadTexts:
    err_sonda_s4.setUnits("N/A")


class _Err_sonda_s5_Type(Integer32):
    """Custom type err_sonda_s5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Err_sonda_s5_Type.__name__ = "Integer32"
_Err_sonda_s5_Object = MibScalar
err_sonda_s5 = _Err_sonda_s5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 13),
    _Err_sonda_s5_Type()
)
err_sonda_s5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    err_sonda_s5.setStatus("current")
if mibBuilder.loadTexts:
    err_sonda_s5.setUnits("N/A")


class _Err_eeprom_Type(Integer32):
    """Custom type err_eeprom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Err_eeprom_Type.__name__ = "Integer32"
_Err_eeprom_Object = MibScalar
err_eeprom = _Err_eeprom_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 14),
    _Err_eeprom_Type()
)
err_eeprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    err_eeprom.setStatus("current")
if mibBuilder.loadTexts:
    err_eeprom.setUnits("N/A")


class _Freq_rete_Type(Integer32):
    """Custom type freq_rete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Freq_rete_Type.__name__ = "Integer32"
_Freq_rete_Object = MibScalar
freq_rete = _Freq_rete_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 15),
    _Freq_rete_Type()
)
freq_rete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freq_rete.setStatus("current")
if mibBuilder.loadTexts:
    freq_rete.setUnits("N/A")


class _Allarme_terminale_disconnesso_Type(Integer32):
    """Custom type allarme_terminale_disconnesso based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Allarme_terminale_disconnesso_Type.__name__ = "Integer32"
_Allarme_terminale_disconnesso_Object = MibScalar
allarme_terminale_disconnesso = _Allarme_terminale_disconnesso_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 16),
    _Allarme_terminale_disconnesso_Type()
)
allarme_terminale_disconnesso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allarme_terminale_disconnesso.setStatus("current")
if mibBuilder.loadTexts:
    allarme_terminale_disconnesso.setUnits("N/A")


class _Defrost_st_1_Type(Integer32):
    """Custom type defrost_st_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Defrost_st_1_Type.__name__ = "Integer32"
_Defrost_st_1_Object = MibScalar
defrost_st_1 = _Defrost_st_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 17),
    _Defrost_st_1_Type()
)
defrost_st_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defrost_st_1.setStatus("current")
if mibBuilder.loadTexts:
    defrost_st_1.setUnits("N/A")


class _Defrost_st_2_Type(Integer32):
    """Custom type defrost_st_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Defrost_st_2_Type.__name__ = "Integer32"
_Defrost_st_2_Object = MibScalar
defrost_st_2 = _Defrost_st_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 19),
    _Defrost_st_2_Type()
)
defrost_st_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defrost_st_2.setStatus("current")
if mibBuilder.loadTexts:
    defrost_st_2.setUnits("N/A")


class _All_h_press_c1_Type(Integer32):
    """Custom type all_h_press_c1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_h_press_c1_Type.__name__ = "Integer32"
_All_h_press_c1_Object = MibScalar
all_h_press_c1 = _All_h_press_c1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 20),
    _All_h_press_c1_Type()
)
all_h_press_c1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_h_press_c1.setStatus("current")
if mibBuilder.loadTexts:
    all_h_press_c1.setUnits("N/A")


class _All_l_press_c1_Type(Integer32):
    """Custom type all_l_press_c1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_l_press_c1_Type.__name__ = "Integer32"
_All_l_press_c1_Object = MibScalar
all_l_press_c1 = _All_l_press_c1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 21),
    _All_l_press_c1_Type()
)
all_l_press_c1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_l_press_c1.setStatus("current")
if mibBuilder.loadTexts:
    all_l_press_c1.setUnits("N/A")


class _All_term_compc1_Type(Integer32):
    """Custom type all_term_compc1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_term_compc1_Type.__name__ = "Integer32"
_All_term_compc1_Object = MibScalar
all_term_compc1 = _All_term_compc1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 22),
    _All_term_compc1_Type()
)
all_term_compc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_term_compc1.setStatus("current")
if mibBuilder.loadTexts:
    all_term_compc1.setUnits("N/A")


class _All_term_fanc1_Type(Integer32):
    """Custom type all_term_fanc1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_term_fanc1_Type.__name__ = "Integer32"
_All_term_fanc1_Object = MibScalar
all_term_fanc1 = _All_term_fanc1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 23),
    _All_term_fanc1_Type()
)
all_term_fanc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_term_fanc1.setStatus("current")
if mibBuilder.loadTexts:
    all_term_fanc1.setUnits("N/A")


class _All_flusso_Type(Integer32):
    """Custom type all_flusso based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_flusso_Type.__name__ = "Integer32"
_All_flusso_Object = MibScalar
all_flusso = _All_flusso_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 24),
    _All_flusso_Type()
)
all_flusso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_flusso.setStatus("current")
if mibBuilder.loadTexts:
    all_flusso.setUnits("N/A")


class _Est_inv_Type(Integer32):
    """Custom type est_inv based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Est_inv_Type.__name__ = "Integer32"
_Est_inv_Object = MibScalar
est_inv = _Est_inv_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 26),
    _Est_inv_Type()
)
est_inv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    est_inv.setStatus("current")
if mibBuilder.loadTexts:
    est_inv.setUnits("C/F")


class _All_h_press_c2_Type(Integer32):
    """Custom type all_h_press_c2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_h_press_c2_Type.__name__ = "Integer32"
_All_h_press_c2_Object = MibScalar
all_h_press_c2 = _All_h_press_c2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 27),
    _All_h_press_c2_Type()
)
all_h_press_c2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_h_press_c2.setStatus("current")
if mibBuilder.loadTexts:
    all_h_press_c2.setUnits("N/A")


class _All_l_press_c2_Type(Integer32):
    """Custom type all_l_press_c2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_l_press_c2_Type.__name__ = "Integer32"
_All_l_press_c2_Object = MibScalar
all_l_press_c2 = _All_l_press_c2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 28),
    _All_l_press_c2_Type()
)
all_l_press_c2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_l_press_c2.setStatus("current")
if mibBuilder.loadTexts:
    all_l_press_c2.setUnits("N/A")


class _All_term_compc2_Type(Integer32):
    """Custom type all_term_compc2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_term_compc2_Type.__name__ = "Integer32"
_All_term_compc2_Object = MibScalar
all_term_compc2 = _All_term_compc2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 29),
    _All_term_compc2_Type()
)
all_term_compc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_term_compc2.setStatus("current")
if mibBuilder.loadTexts:
    all_term_compc2.setUnits("N/A")


class _All_term_fanc2_Type(Integer32):
    """Custom type all_term_fanc2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_term_fanc2_Type.__name__ = "Integer32"
_All_term_fanc2_Object = MibScalar
all_term_fanc2 = _All_term_fanc2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 30),
    _All_term_fanc2_Type()
)
all_term_fanc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_term_fanc2.setStatus("current")
if mibBuilder.loadTexts:
    all_term_fanc2.setUnits("N/A")


class _Rich_manut_c2_Type(Integer32):
    """Custom type rich_manut_c2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Rich_manut_c2_Type.__name__ = "Integer32"
_Rich_manut_c2_Object = MibScalar
rich_manut_c2 = _Rich_manut_c2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 32),
    _Rich_manut_c2_Type()
)
rich_manut_c2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rich_manut_c2.setStatus("current")
if mibBuilder.loadTexts:
    rich_manut_c2.setUnits("N/A")


class _All_antigelo_c1_Type(Integer32):
    """Custom type all_antigelo_c1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_antigelo_c1_Type.__name__ = "Integer32"
_All_antigelo_c1_Object = MibScalar
all_antigelo_c1 = _All_antigelo_c1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 33),
    _All_antigelo_c1_Type()
)
all_antigelo_c1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_antigelo_c1.setStatus("current")
if mibBuilder.loadTexts:
    all_antigelo_c1.setUnits("N/A")


class _All_antigelo_c2_Type(Integer32):
    """Custom type all_antigelo_c2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_antigelo_c2_Type.__name__ = "Integer32"
_All_antigelo_c2_Object = MibScalar
all_antigelo_c2 = _All_antigelo_c2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 34),
    _All_antigelo_c2_Type()
)
all_antigelo_c2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_antigelo_c2.setStatus("current")
if mibBuilder.loadTexts:
    all_antigelo_c2.setUnits("N/A")


class _All_defrost_c1_Type(Integer32):
    """Custom type all_defrost_c1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_defrost_c1_Type.__name__ = "Integer32"
_All_defrost_c1_Object = MibScalar
all_defrost_c1 = _All_defrost_c1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 35),
    _All_defrost_c1_Type()
)
all_defrost_c1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_defrost_c1.setStatus("current")
if mibBuilder.loadTexts:
    all_defrost_c1.setUnits("N/A")


class _All_defrost_c2_Type(Integer32):
    """Custom type all_defrost_c2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_defrost_c2_Type.__name__ = "Integer32"
_All_defrost_c2_Object = MibScalar
all_defrost_c2 = _All_defrost_c2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 36),
    _All_defrost_c2_Type()
)
all_defrost_c2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_defrost_c2.setStatus("current")
if mibBuilder.loadTexts:
    all_defrost_c2.setUnits("N/A")


class _Tsonda_inev__1_Type(Integer32):
    """Custom type tsonda_inev__1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Tsonda_inev__1_Type.__name__ = "Integer32"
_Tsonda_inev__1_Object = MibScalar
tsonda_inev__1 = _Tsonda_inev__1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 37),
    _Tsonda_inev__1_Type()
)
tsonda_inev__1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsonda_inev__1.setStatus("current")
if mibBuilder.loadTexts:
    tsonda_inev__1.setUnits("flag")


class _Tsonda_outev__2_Type(Integer32):
    """Custom type tsonda_outev__2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Tsonda_outev__2_Type.__name__ = "Integer32"
_Tsonda_outev__2_Object = MibScalar
tsonda_outev__2 = _Tsonda_outev__2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 38),
    _Tsonda_outev__2_Type()
)
tsonda_outev__2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsonda_outev__2.setStatus("current")
if mibBuilder.loadTexts:
    tsonda_outev__2.setUnits("flag")


class _Out_per_fan_f1_Type(Integer32):
    """Custom type out_per_fan_f1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Out_per_fan_f1_Type.__name__ = "Integer32"
_Out_per_fan_f1_Object = MibScalar
out_per_fan_f1 = _Out_per_fan_f1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 40),
    _Out_per_fan_f1_Type()
)
out_per_fan_f1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    out_per_fan_f1.setStatus("current")
if mibBuilder.loadTexts:
    out_per_fan_f1.setUnits("N/A")


class _Defr_antig_d1_Type(Integer32):
    """Custom type defr_antig_d1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Defr_antig_d1_Type.__name__ = "Integer32"
_Defr_antig_d1_Object = MibScalar
defr_antig_d1 = _Defr_antig_d1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 41),
    _Defr_antig_d1_Type()
)
defr_antig_d1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defr_antig_d1.setStatus("current")
if mibBuilder.loadTexts:
    defr_antig_d1.setUnits("min")


class _Num_fan_h2_Type(Integer32):
    """Custom type num_fan_h2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Num_fan_h2_Type.__name__ = "Integer32"
_Num_fan_h2_Object = MibScalar
num_fan_h2 = _Num_fan_h2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 43),
    _Num_fan_h2_Type()
)
num_fan_h2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    num_fan_h2.setStatus("current")
if mibBuilder.loadTexts:
    num_fan_h2.setUnits("flag")


class _Num_evap_h3_Type(Integer32):
    """Custom type num_evap_h3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Num_evap_h3_Type.__name__ = "Integer32"
_Num_evap_h3_Object = MibScalar
num_evap_h3 = _Num_evap_h3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 44),
    _Num_evap_h3_Type()
)
num_evap_h3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    num_evap_h3.setStatus("current")
if mibBuilder.loadTexts:
    num_evap_h3.setUnits("N/A")


class _Compr_parz_h4_Type(Integer32):
    """Custom type compr_parz_h4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Compr_parz_h4_Type.__name__ = "Integer32"
_Compr_parz_h4_Object = MibScalar
compr_parz_h4 = _Compr_parz_h4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 45),
    _Compr_parz_h4_Type()
)
compr_parz_h4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compr_parz_h4.setStatus("current")
if mibBuilder.loadTexts:
    compr_parz_h4.setUnits("flag")


class _En_din_e_i_h6_Type(Integer32):
    """Custom type en_din_e_i_h6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_din_e_i_h6_Type.__name__ = "Integer32"
_En_din_e_i_h6_Object = MibScalar
en_din_e_i_h6 = _En_din_e_i_h6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 46),
    _En_din_e_i_h6_Type()
)
en_din_e_i_h6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    en_din_e_i_h6.setStatus("current")
if mibBuilder.loadTexts:
    en_din_e_i_h6.setUnits("N/A")


class _En_din_a_s_h7_Type(Integer32):
    """Custom type en_din_a_s_h7 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_din_a_s_h7_Type.__name__ = "Integer32"
_En_din_a_s_h7_Object = MibScalar
en_din_a_s_h7 = _En_din_a_s_h7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 47),
    _En_din_a_s_h7_Type()
)
en_din_a_s_h7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    en_din_a_s_h7.setStatus("current")
if mibBuilder.loadTexts:
    en_din_a_s_h7.setUnits("flag")


class _Num_termin_h8_Type(Integer32):
    """Custom type num_termin_h8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Num_termin_h8_Type.__name__ = "Integer32"
_Num_termin_h8_Object = MibScalar
num_termin_h8 = _Num_termin_h8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 48),
    _Num_termin_h8_Type()
)
num_termin_h8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    num_termin_h8.setStatus("current")
if mibBuilder.loadTexts:
    num_termin_h8.setUnits("flag")


class _Num_compressori_Type(Integer32):
    """Custom type num_compressori based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Num_compressori_Type.__name__ = "Integer32"
_Num_compressori_Object = MibScalar
num_compressori = _Num_compressori_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 49),
    _Num_compressori_Type()
)
num_compressori.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    num_compressori.setStatus("current")
if mibBuilder.loadTexts:
    num_compressori.setUnits("flag")


class _Comp_rot_r5_Type(Integer32):
    """Custom type comp_rot_r5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Comp_rot_r5_Type.__name__ = "Integer32"
_Comp_rot_r5_Object = MibScalar
comp_rot_r5 = _Comp_rot_r5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 50),
    _Comp_rot_r5_Type()
)
comp_rot_r5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comp_rot_r5.setStatus("current")
if mibBuilder.loadTexts:
    comp_rot_r5.setUnits("flag")


class _Def_ext_da_Type(Integer32):
    """Custom type def_ext_da based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Def_ext_da_Type.__name__ = "Integer32"
_Def_ext_da_Object = MibScalar
def_ext_da = _Def_ext_da_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 51),
    _Def_ext_da_Type()
)
def_ext_da.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    def_ext_da.setStatus("current")
if mibBuilder.loadTexts:
    def_ext_da.setUnits("flag")


class _Anti_def_db_Type(Integer32):
    """Custom type anti_def_db based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Anti_def_db_Type.__name__ = "Integer32"
_Anti_def_db_Object = MibScalar
anti_def_db = _Anti_def_db_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 52),
    _Anti_def_db_Type()
)
anti_def_db.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anti_def_db.setStatus("current")
if mibBuilder.loadTexts:
    anti_def_db.setUnits("flag")


class _End_def_de_Type(Integer32):
    """Custom type end_def_de based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_End_def_de_Type.__name__ = "Integer32"
_End_def_de_Object = MibScalar
end_def_de = _End_def_de_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 53),
    _End_def_de_Type()
)
end_def_de.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    end_def_de.setStatus("current")
if mibBuilder.loadTexts:
    end_def_de.setUnits("flag")


class _Sup_probe_a6_Type(Integer32):
    """Custom type sup_probe_a6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sup_probe_a6_Type.__name__ = "Integer32"
_Sup_probe_a6_Object = MibScalar
sup_probe_a6 = _Sup_probe_a6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 54),
    _Sup_probe_a6_Type()
)
sup_probe_a6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sup_probe_a6.setStatus("current")
if mibBuilder.loadTexts:
    sup_probe_a6.setUnits("flag")


class _Reset_alarm_p5_Type(Integer32):
    """Custom type reset_alarm_p5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Reset_alarm_p5_Type.__name__ = "Integer32"
_Reset_alarm_p5_Object = MibScalar
reset_alarm_p5 = _Reset_alarm_p5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 55),
    _Reset_alarm_p5_Type()
)
reset_alarm_p5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reset_alarm_p5.setStatus("current")
if mibBuilder.loadTexts:
    reset_alarm_p5.setUnits("flag")


class _Set_2_param_p6_Type(Integer32):
    """Custom type set_2_param_p6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Set_2_param_p6_Type.__name__ = "Integer32"
_Set_2_param_p6_Object = MibScalar
set_2_param_p6 = _Set_2_param_p6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 56),
    _Set_2_param_p6_Type()
)
set_2_param_p6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_2_param_p6.setStatus("current")
if mibBuilder.loadTexts:
    set_2_param_p6.setUnits("flag")


class _Low_press_alarm_p7_Type(Integer32):
    """Custom type low_press_alarm_p7 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Low_press_alarm_p7_Type.__name__ = "Integer32"
_Low_press_alarm_p7_Object = MibScalar
low_press_alarm_p7 = _Low_press_alarm_p7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 57),
    _Low_press_alarm_p7_Type()
)
low_press_alarm_p7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    low_press_alarm_p7.setStatus("current")
if mibBuilder.loadTexts:
    low_press_alarm_p7.setUnits("flag")
_AnalogObjects_ObjectIdentity = ObjectIdentity
analogObjects = _AnalogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2)
)


class _Sonda_s1_Type(Integer32):
    """Custom type sonda_s1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Sonda_s1_Type.__name__ = "Integer32"
_Sonda_s1_Object = MibScalar
sonda_s1 = _Sonda_s1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 1),
    _Sonda_s1_Type()
)
sonda_s1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonda_s1.setStatus("current")
if mibBuilder.loadTexts:
    sonda_s1.setUnits("C x10")


class _Sonda_s2_r6_Type(Integer32):
    """Custom type sonda_s2_r6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Sonda_s2_r6_Type.__name__ = "Integer32"
_Sonda_s2_r6_Object = MibScalar
sonda_s2_r6 = _Sonda_s2_r6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 2),
    _Sonda_s2_r6_Type()
)
sonda_s2_r6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonda_s2_r6.setStatus("current")
if mibBuilder.loadTexts:
    sonda_s2_r6.setUnits("C/F x10")


class _Sonda_s3_r7_Type(Integer32):
    """Custom type sonda_s3_r7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Sonda_s3_r7_Type.__name__ = "Integer32"
_Sonda_s3_r7_Object = MibScalar
sonda_s3_r7 = _Sonda_s3_r7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 3),
    _Sonda_s3_r7_Type()
)
sonda_s3_r7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonda_s3_r7.setStatus("current")
if mibBuilder.loadTexts:
    sonda_s3_r7.setUnits("C/F x10")


class _Sonda_s4_r8_Type(Integer32):
    """Custom type sonda_s4_r8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Sonda_s4_r8_Type.__name__ = "Integer32"
_Sonda_s4_r8_Object = MibScalar
sonda_s4_r8 = _Sonda_s4_r8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 4),
    _Sonda_s4_r8_Type()
)
sonda_s4_r8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonda_s4_r8.setStatus("current")
if mibBuilder.loadTexts:
    sonda_s4_r8.setUnits("bar x10")


class _Sonda_s5_r9_Type(Integer32):
    """Custom type sonda_s5_r9 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Sonda_s5_r9_Type.__name__ = "Integer32"
_Sonda_s5_r9_Object = MibScalar
sonda_s5_r9 = _Sonda_s5_r9_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 5),
    _Sonda_s5_r9_Type()
)
sonda_s5_r9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonda_s5_r9.setStatus("current")
if mibBuilder.loadTexts:
    sonda_s5_r9.setUnits("bar x10")


class _Calibra_s1__6_Type(Integer32):
    """Custom type calibra_s1__6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 60),
    )


_Calibra_s1__6_Type.__name__ = "Integer32"
_Calibra_s1__6_Object = MibScalar
calibra_s1__6 = _Calibra_s1__6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 6),
    _Calibra_s1__6_Type()
)
calibra_s1__6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibra_s1__6.setStatus("current")
if mibBuilder.loadTexts:
    calibra_s1__6.setUnits("C/F x10")


class _Calibra_s2__7_Type(Integer32):
    """Custom type calibra_s2__7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 60),
    )


_Calibra_s2__7_Type.__name__ = "Integer32"
_Calibra_s2__7_Object = MibScalar
calibra_s2__7 = _Calibra_s2__7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 7),
    _Calibra_s2__7_Type()
)
calibra_s2__7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibra_s2__7.setStatus("current")
if mibBuilder.loadTexts:
    calibra_s2__7.setUnits("C x10")


class _Calibra_s3__8_Type(Integer32):
    """Custom type calibra_s3__8 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 60),
    )


_Calibra_s3__8_Type.__name__ = "Integer32"
_Calibra_s3__8_Object = MibScalar
calibra_s3__8 = _Calibra_s3__8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 8),
    _Calibra_s3__8_Type()
)
calibra_s3__8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibra_s3__8.setStatus("current")
if mibBuilder.loadTexts:
    calibra_s3__8.setUnits("C/F x10")


class _Calibra_s4__9_Type(Integer32):
    """Custom type calibra_s4__9 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 60),
    )


_Calibra_s4__9_Type.__name__ = "Integer32"
_Calibra_s4__9_Object = MibScalar
calibra_s4__9 = _Calibra_s4__9_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 9),
    _Calibra_s4__9_Type()
)
calibra_s4__9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibra_s4__9.setStatus("current")
if mibBuilder.loadTexts:
    calibra_s4__9.setUnits("C/F x10")


class _Calibra_s5__a_Type(Integer32):
    """Custom type calibra_s5__a based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 90),
    )


_Calibra_s5__a_Type.__name__ = "Integer32"
_Calibra_s5__a_Object = MibScalar
calibra_s5__a = _Calibra_s5__a_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 10),
    _Calibra_s5__a_Type()
)
calibra_s5__a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibra_s5__a.setStatus("current")
if mibBuilder.loadTexts:
    calibra_s5__a.setUnits("C/F bar x10")


class _Setp_est_r1_Type(Integer32):
    """Custom type setp_est_r1 based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Setp_est_r1_Type.__name__ = "Integer32"
_Setp_est_r1_Object = MibScalar
setp_est_r1 = _Setp_est_r1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 11),
    _Setp_est_r1_Type()
)
setp_est_r1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setp_est_r1.setStatus("current")
if mibBuilder.loadTexts:
    setp_est_r1.setUnits("C/F x10")


class _Differ_est_r2_Type(Integer32):
    """Custom type differ_est_r2 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 198),
    )


_Differ_est_r2_Type.__name__ = "Integer32"
_Differ_est_r2_Object = MibScalar
differ_est_r2 = _Differ_est_r2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 12),
    _Differ_est_r2_Type()
)
differ_est_r2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differ_est_r2.setStatus("current")
if mibBuilder.loadTexts:
    differ_est_r2.setUnits("C/F x10")


class _Setp_inv_r3_Type(Integer32):
    """Custom type setp_inv_r3 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Setp_inv_r3_Type.__name__ = "Integer32"
_Setp_inv_r3_Object = MibScalar
setp_inv_r3 = _Setp_inv_r3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 13),
    _Setp_inv_r3_Type()
)
setp_inv_r3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setp_inv_r3.setStatus("current")
if mibBuilder.loadTexts:
    setp_inv_r3.setUnits("C/F x10")


class _Differ_inv_r4_Type(Integer32):
    """Custom type differ_inv_r4 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 198),
    )


_Differ_inv_r4_Type.__name__ = "Integer32"
_Differ_inv_r4_Object = MibScalar
differ_inv_r4 = _Differ_inv_r4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 14),
    _Differ_inv_r4_Type()
)
differ_inv_r4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differ_inv_r4.setStatus("current")
if mibBuilder.loadTexts:
    differ_inv_r4.setUnits("C/F x10")


class _Set_min_est_ra_Type(Integer32):
    """Custom type set_min_est_ra based on Integer32"""
    defaultValue = -400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 32767),
    )


_Set_min_est_ra_Type.__name__ = "Integer32"
_Set_min_est_ra_Object = MibScalar
set_min_est_ra = _Set_min_est_ra_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 15),
    _Set_min_est_ra_Type()
)
set_min_est_ra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_min_est_ra.setStatus("current")
if mibBuilder.loadTexts:
    set_min_est_ra.setUnits("C/F x10")


class _Set_max_est_rb_Type(Integer32):
    """Custom type set_max_est_rb based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 1940),
    )


_Set_max_est_rb_Type.__name__ = "Integer32"
_Set_max_est_rb_Object = MibScalar
set_max_est_rb = _Set_max_est_rb_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 16),
    _Set_max_est_rb_Type()
)
set_max_est_rb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_max_est_rb.setStatus("current")
if mibBuilder.loadTexts:
    set_max_est_rb.setUnits("C/F x10")


class _Set_min_inv_rc_Type(Integer32):
    """Custom type set_min_inv_rc based on Integer32"""
    defaultValue = -400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 32767),
    )


_Set_min_inv_rc_Type.__name__ = "Integer32"
_Set_min_inv_rc_Object = MibScalar
set_min_inv_rc = _Set_min_inv_rc_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 17),
    _Set_min_inv_rc_Type()
)
set_min_inv_rc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_min_inv_rc.setStatus("current")
if mibBuilder.loadTexts:
    set_min_inv_rc.setUnits("C/F x10")


class _Set_max_inv_rd_Type(Integer32):
    """Custom type set_max_inv_rd based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 1940),
    )


_Set_max_inv_rd_Type.__name__ = "Integer32"
_Set_max_inv_rd_Object = MibScalar
set_max_inv_rd = _Set_max_inv_rd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 18),
    _Set_max_inv_rd_Type()
)
set_max_inv_rd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_max_inv_rd.setStatus("current")
if mibBuilder.loadTexts:
    set_max_inv_rd.setUnits("C/F x10")


class _Tmin_vel_est_f5_Type(Integer32):
    """Custom type tmin_vel_est_f5 based on Integer32"""
    defaultValue = 130

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Tmin_vel_est_f5_Type.__name__ = "Integer32"
_Tmin_vel_est_f5_Object = MibScalar
tmin_vel_est_f5 = _Tmin_vel_est_f5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 19),
    _Tmin_vel_est_f5_Type()
)
tmin_vel_est_f5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmin_vel_est_f5.setStatus("current")
if mibBuilder.loadTexts:
    tmin_vel_est_f5.setUnits("bar x10")


class _Tmax_vel_est_f6_Type(Integer32):
    """Custom type tmax_vel_est_f6 based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 500),
    )


_Tmax_vel_est_f6_Type.__name__ = "Integer32"
_Tmax_vel_est_f6_Object = MibScalar
tmax_vel_est_f6 = _Tmax_vel_est_f6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 20),
    _Tmax_vel_est_f6_Type()
)
tmax_vel_est_f6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmax_vel_est_f6.setStatus("current")
if mibBuilder.loadTexts:
    tmax_vel_est_f6.setUnits("bar x10")


class _Tmin_vel_inv_f7_Type(Integer32):
    """Custom type tmin_vel_inv_f7 based on Integer32"""
    defaultValue = 130

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 500),
    )


_Tmin_vel_inv_f7_Type.__name__ = "Integer32"
_Tmin_vel_inv_f7_Object = MibScalar
tmin_vel_inv_f7 = _Tmin_vel_inv_f7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 21),
    _Tmin_vel_inv_f7_Type()
)
tmin_vel_inv_f7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmin_vel_inv_f7.setStatus("current")
if mibBuilder.loadTexts:
    tmin_vel_inv_f7.setUnits("bar x10")


class _Tmax_vel_inv_f8_Type(Integer32):
    """Custom type tmax_vel_inv_f8 based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Tmax_vel_inv_f8_Type.__name__ = "Integer32"
_Tmax_vel_inv_f8_Object = MibScalar
tmax_vel_inv_f8 = _Tmax_vel_inv_f8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 22),
    _Tmax_vel_inv_f8_Type()
)
tmax_vel_inv_f8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmax_vel_inv_f8.setStatus("current")
if mibBuilder.loadTexts:
    tmax_vel_inv_f8.setUnits("bar x10")


class _Toff_fan_est_f9_Type(Integer32):
    """Custom type toff_fan_est_f9 based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Toff_fan_est_f9_Type.__name__ = "Integer32"
_Toff_fan_est_f9_Object = MibScalar
toff_fan_est_f9 = _Toff_fan_est_f9_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 23),
    _Toff_fan_est_f9_Type()
)
toff_fan_est_f9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    toff_fan_est_f9.setStatus("current")
if mibBuilder.loadTexts:
    toff_fan_est_f9.setUnits("bar x10")


class _Toff_fan_inv_fa_Type(Integer32):
    """Custom type toff_fan_inv_fa based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 500),
    )


_Toff_fan_inv_fa_Type.__name__ = "Integer32"
_Toff_fan_inv_fa_Object = MibScalar
toff_fan_inv_fa = _Toff_fan_inv_fa_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 24),
    _Toff_fan_inv_fa_Type()
)
toff_fan_inv_fa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    toff_fan_inv_fa.setStatus("current")
if mibBuilder.loadTexts:
    toff_fan_inv_fa.setUnits("bar x10")


class _Tp_start_def_d3_Type(Integer32):
    """Custom type tp_start_def_d3 based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 32767),
    )


_Tp_start_def_d3_Type.__name__ = "Integer32"
_Tp_start_def_d3_Object = MibScalar
tp_start_def_d3 = _Tp_start_def_d3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 25),
    _Tp_start_def_d3_Type()
)
tp_start_def_d3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp_start_def_d3.setStatus("current")
if mibBuilder.loadTexts:
    tp_start_def_d3.setUnits("bar x10")


class _Tp_end_def_d4_Type(Integer32):
    """Custom type tp_end_def_d4 based on Integer32"""
    defaultValue = 140

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 500),
    )


_Tp_end_def_d4_Type.__name__ = "Integer32"
_Tp_end_def_d4_Object = MibScalar
tp_end_def_d4 = _Tp_end_def_d4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 26),
    _Tp_end_def_d4_Type()
)
tp_end_def_d4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp_end_def_d4.setStatus("current")
if mibBuilder.loadTexts:
    tp_end_def_d4.setUnits("bar x10")


class _Set_al_agelo_a1_Type(Integer32):
    """Custom type set_al_agelo_a1 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 32767),
    )


_Set_al_agelo_a1_Type.__name__ = "Integer32"
_Set_al_agelo_a1_Object = MibScalar
set_al_agelo_a1 = _Set_al_agelo_a1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 27),
    _Set_al_agelo_a1_Type()
)
set_al_agelo_a1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_al_agelo_a1.setStatus("current")
if mibBuilder.loadTexts:
    set_al_agelo_a1.setUnits("C/F x10")


class _Dif_al_agelo_a2_Type(Integer32):
    """Custom type dif_al_agelo_a2 based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 198),
    )


_Dif_al_agelo_a2_Type.__name__ = "Integer32"
_Dif_al_agelo_a2_Object = MibScalar
dif_al_agelo_a2 = _Dif_al_agelo_a2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 28),
    _Dif_al_agelo_a2_Type()
)
dif_al_agelo_a2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dif_al_agelo_a2.setStatus("current")
if mibBuilder.loadTexts:
    dif_al_agelo_a2.setUnits("C/F x10")


class _Set_res_gelo_a4_Type(Integer32):
    """Custom type set_res_gelo_a4 based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Set_res_gelo_a4_Type.__name__ = "Integer32"
_Set_res_gelo_a4_Object = MibScalar
set_res_gelo_a4 = _Set_res_gelo_a4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 29),
    _Set_res_gelo_a4_Type()
)
set_res_gelo_a4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_res_gelo_a4.setStatus("current")
if mibBuilder.loadTexts:
    set_res_gelo_a4.setUnits("C/F x10")


class _Dif_res_gelo_a5_Type(Integer32):
    """Custom type dif_res_gelo_a5 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1220),
    )


_Dif_res_gelo_a5_Type.__name__ = "Integer32"
_Dif_res_gelo_a5_Object = MibScalar
dif_res_gelo_a5 = _Dif_res_gelo_a5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 30),
    _Dif_res_gelo_a5_Type()
)
dif_res_gelo_a5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dif_res_gelo_a5.setStatus("current")
if mibBuilder.loadTexts:
    dif_res_gelo_a5.setUnits("C/F x10")
_IntegerObjects_ObjectIdentity = ObjectIdentity
integerObjects = _IntegerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3)
)


class _Tipo_sonda__3_Type(Integer32):
    """Custom type tipo_sonda__3 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Tipo_sonda__3_Type.__name__ = "Integer32"
_Tipo_sonda__3_Object = MibScalar
tipo_sonda__3 = _Tipo_sonda__3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 1),
    _Tipo_sonda__3_Type()
)
tipo_sonda__3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tipo_sonda__3.setStatus("current")
if mibBuilder.loadTexts:
    tipo_sonda__3.setUnits("flag")


class _Min_in_corr__4_Type(Integer32):
    """Custom type min_in_corr__4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Min_in_corr__4_Type.__name__ = "Integer32"
_Min_in_corr__4_Object = MibScalar
min_in_corr__4 = _Min_in_corr__4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 2),
    _Min_in_corr__4_Type()
)
min_in_corr__4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    min_in_corr__4.setStatus("current")
if mibBuilder.loadTexts:
    min_in_corr__4.setUnits("bar")


class _Max_in_corr__5_Type(Integer32):
    """Custom type max_in_corr__5 based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 35),
    )


_Max_in_corr__5_Type.__name__ = "Integer32"
_Max_in_corr__5_Object = MibScalar
max_in_corr__5 = _Max_in_corr__5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 3),
    _Max_in_corr__5_Type()
)
max_in_corr__5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_in_corr__5.setStatus("current")
if mibBuilder.loadTexts:
    max_in_corr__5.setUnits("bar")


class _Filtro_dig__b_Type(Integer32):
    """Custom type filtro_dig__b based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Filtro_dig__b_Type.__name__ = "Integer32"
_Filtro_dig__b_Object = MibScalar
filtro_dig__b = _Filtro_dig__b_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 4),
    _Filtro_dig__b_Type()
)
filtro_dig__b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filtro_dig__b.setStatus("current")
if mibBuilder.loadTexts:
    filtro_dig__b.setUnits("N/A")


class _Limitaz_in__c_Type(Integer32):
    """Custom type limitaz_in__c based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Limitaz_in__c_Type.__name__ = "Integer32"
_Limitaz_in__c_Object = MibScalar
limitaz_in__c = _Limitaz_in__c_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 5),
    _Limitaz_in__c_Type()
)
limitaz_in__c.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitaz_in__c.setStatus("current")
if mibBuilder.loadTexts:
    limitaz_in__c.setUnits("N/A")


class _Tmin_on_comp_c1_Type(Integer32):
    """Custom type tmin_on_comp_c1 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_Tmin_on_comp_c1_Type.__name__ = "Integer32"
_Tmin_on_comp_c1_Object = MibScalar
tmin_on_comp_c1 = _Tmin_on_comp_c1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 6),
    _Tmin_on_comp_c1_Type()
)
tmin_on_comp_c1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmin_on_comp_c1.setStatus("current")
if mibBuilder.loadTexts:
    tmin_on_comp_c1.setUnits("sec")


class _Time_2_acc_c3_Type(Integer32):
    """Custom type time_2_acc_c3 based on Integer32"""
    defaultValue = 36

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_Time_2_acc_c3_Type.__name__ = "Integer32"
_Time_2_acc_c3_Object = MibScalar
time_2_acc_c3 = _Time_2_acc_c3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 8),
    _Time_2_acc_c3_Type()
)
time_2_acc_c3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_2_acc_c3.setStatus("current")
if mibBuilder.loadTexts:
    time_2_acc_c3.setUnits("10 sec")


class _Rit_off_2c_c5_Type(Integer32):
    """Custom type rit_off_2c_c5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Rit_off_2c_c5_Type.__name__ = "Integer32"
_Rit_off_2c_c5_Object = MibScalar
rit_off_2c_c5 = _Rit_off_2c_c5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 10),
    _Rit_off_2c_c5_Type()
)
rit_off_2c_c5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_off_2c_c5.setStatus("current")
if mibBuilder.loadTexts:
    rit_off_2c_c5.setUnits("sec")


class _Rit_on_comp_c6_Type(Integer32):
    """Custom type rit_on_comp_c6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_Rit_on_comp_c6_Type.__name__ = "Integer32"
_Rit_on_comp_c6_Object = MibScalar
rit_on_comp_c6 = _Rit_on_comp_c6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 11),
    _Rit_on_comp_c6_Type()
)
rit_on_comp_c6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_on_comp_c6.setStatus("current")
if mibBuilder.loadTexts:
    rit_on_comp_c6.setUnits("sec")


class _Rit_c_on_pmp_c7_Type(Integer32):
    """Custom type rit_c_on_pmp_c7 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_Rit_c_on_pmp_c7_Type.__name__ = "Integer32"
_Rit_c_on_pmp_c7_Object = MibScalar
rit_c_on_pmp_c7 = _Rit_c_on_pmp_c7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 12),
    _Rit_c_on_pmp_c7_Type()
)
rit_c_on_pmp_c7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_c_on_pmp_c7.setStatus("current")
if mibBuilder.loadTexts:
    rit_c_on_pmp_c7.setUnits("sec")


class _Off_p_off_c_c8_Type(Integer32):
    """Custom type off_p_off_c_c8 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_Off_p_off_c_c8_Type.__name__ = "Integer32"
_Off_p_off_c_c8_Object = MibScalar
off_p_off_c_c8 = _Off_p_off_c_c8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 13),
    _Off_p_off_c_c8_Type()
)
off_p_off_c_c8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    off_p_off_c_c8.setStatus("current")
if mibBuilder.loadTexts:
    off_p_off_c_c8.setUnits("min")


class _Ore_comp1_c9_Type(Integer32):
    """Custom type ore_comp1_c9 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19900),
    )


_Ore_comp1_c9_Type.__name__ = "Integer32"
_Ore_comp1_c9_Object = MibScalar
ore_comp1_c9 = _Ore_comp1_c9_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 14),
    _Ore_comp1_c9_Type()
)
ore_comp1_c9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ore_comp1_c9.setStatus("current")
if mibBuilder.loadTexts:
    ore_comp1_c9.setUnits("hours")


class _Ore_comp2_ca_Type(Integer32):
    """Custom type ore_comp2_ca based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19900),
    )


_Ore_comp2_ca_Type.__name__ = "Integer32"
_Ore_comp2_ca_Object = MibScalar
ore_comp2_ca = _Ore_comp2_ca_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 17),
    _Ore_comp2_ca_Type()
)
ore_comp2_ca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ore_comp2_ca.setStatus("current")
if mibBuilder.loadTexts:
    ore_comp2_ca.setUnits("N/A")


class _Max_ore_comp_cb_Type(Integer32):
    """Custom type max_ore_comp_cb based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Max_ore_comp_cb_Type.__name__ = "Integer32"
_Max_ore_comp_cb_Object = MibScalar
max_ore_comp_cb = _Max_ore_comp_cb_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 18),
    _Max_ore_comp_cb_Type()
)
max_ore_comp_cb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_ore_comp_cb.setStatus("current")
if mibBuilder.loadTexts:
    max_ore_comp_cb.setUnits("step")


class _Ore_pompa_cc_Type(Integer32):
    """Custom type ore_pompa_cc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19900),
    )


_Ore_pompa_cc_Type.__name__ = "Integer32"
_Ore_pompa_cc_Object = MibScalar
ore_pompa_cc = _Ore_pompa_cc_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 19),
    _Ore_pompa_cc_Type()
)
ore_pompa_cc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ore_pompa_cc.setStatus("current")
if mibBuilder.loadTexts:
    ore_pompa_cc.setUnits("ore")


class _Rit_c_f_cond_cd_Type(Integer32):
    """Custom type rit_c_f_cond_cd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Rit_c_f_cond_cd_Type.__name__ = "Integer32"
_Rit_c_f_cond_cd_Object = MibScalar
rit_c_f_cond_cd = _Rit_c_f_cond_cd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 20),
    _Rit_c_f_cond_cd_Type()
)
rit_c_f_cond_cd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_c_f_cond_cd.setStatus("current")
if mibBuilder.loadTexts:
    rit_c_f_cond_cd.setUnits("sec")


class _Modo_fan_f2_Type(Integer32):
    """Custom type modo_fan_f2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Modo_fan_f2_Type.__name__ = "Integer32"
_Modo_fan_f2_Object = MibScalar
modo_fan_f2 = _Modo_fan_f2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 21),
    _Modo_fan_f2_Type()
)
modo_fan_f2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modo_fan_f2.setStatus("current")
if mibBuilder.loadTexts:
    modo_fan_f2.setUnits("msec")


class _Min_volt_f3_Type(Integer32):
    """Custom type min_volt_f3 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 150),
    )


_Min_volt_f3_Type.__name__ = "Integer32"
_Min_volt_f3_Object = MibScalar
min_volt_f3 = _Min_volt_f3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 22),
    _Min_volt_f3_Type()
)
min_volt_f3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    min_volt_f3.setStatus("current")
if mibBuilder.loadTexts:
    min_volt_f3.setUnits("sec")


class _Max_volt_f4_Type(Integer32):
    """Custom type max_volt_f4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_Max_volt_f4_Type.__name__ = "Integer32"
_Max_volt_f4_Object = MibScalar
max_volt_f4 = _Max_volt_f4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 23),
    _Max_volt_f4_Type()
)
max_volt_f4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_volt_f4.setStatus("current")
if mibBuilder.loadTexts:
    max_volt_f4.setUnits("N/A")


class _T_spunto_f_fb_Type(Integer32):
    """Custom type t_spunto_f_fb based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_T_spunto_f_fb_Type.__name__ = "Integer32"
_T_spunto_f_fb_Object = MibScalar
t_spunto_f_fb = _T_spunto_f_fb_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 24),
    _T_spunto_f_fb_Type()
)
t_spunto_f_fb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t_spunto_f_fb.setStatus("current")
if mibBuilder.loadTexts:
    t_spunto_f_fb.setUnits("min")


class _T_min_on_def_d5_Type(Integer32):
    """Custom type t_min_on_def_d5 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 150),
    )


_T_min_on_def_d5_Type.__name__ = "Integer32"
_T_min_on_def_d5_Object = MibScalar
t_min_on_def_d5 = _T_min_on_def_d5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 25),
    _T_min_on_def_d5_Type()
)
t_min_on_def_d5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t_min_on_def_d5.setStatus("current")
if mibBuilder.loadTexts:
    t_min_on_def_d5.setUnits("sec")


class _T_min_def_d6_Type(Integer32):
    """Custom type t_min_def_d6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_T_min_def_d6_Type.__name__ = "Integer32"
_T_min_def_d6_Object = MibScalar
t_min_def_d6 = _T_min_def_d6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 26),
    _T_min_def_d6_Type()
)
t_min_def_d6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t_min_def_d6.setStatus("current")
if mibBuilder.loadTexts:
    t_min_def_d6.setUnits("sec")


class _T_max_def_d7_Type(Integer32):
    """Custom type t_max_def_d7 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_T_max_def_d7_Type.__name__ = "Integer32"
_T_max_def_d7_Object = MibScalar
t_max_def_d7 = _T_max_def_d7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 27),
    _T_max_def_d7_Type()
)
t_max_def_d7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t_max_def_d7.setStatus("current")
if mibBuilder.loadTexts:
    t_max_def_d7.setUnits("min")


class _Rit_2def_1c_d8_Type(Integer32):
    """Custom type rit_2def_1c_d8 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 150),
    )


_Rit_2def_1c_d8_Type.__name__ = "Integer32"
_Rit_2def_1c_d8_Object = MibScalar
rit_2def_1c_d8 = _Rit_2def_1c_d8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 28),
    _Rit_2def_1c_d8_Type()
)
rit_2def_1c_d8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_2def_1c_d8.setStatus("current")
if mibBuilder.loadTexts:
    rit_2def_1c_d8.setUnits("min")


class _Rit_def_2c_d9_Type(Integer32):
    """Custom type rit_def_2c_d9 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_Rit_def_2c_d9_Type.__name__ = "Integer32"
_Rit_def_2c_d9_Object = MibScalar
rit_def_2c_d9 = _Rit_def_2c_d9_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 29),
    _Rit_def_2c_d9_Type()
)
rit_def_2c_d9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_def_2c_d9.setStatus("current")
if mibBuilder.loadTexts:
    rit_def_2c_d9.setUnits("min")


class _Rit_all_ag_a3_Type(Integer32):
    """Custom type rit_all_ag_a3 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_Rit_all_ag_a3_Type.__name__ = "Integer32"
_Rit_all_ag_a3_Object = MibScalar
rit_all_ag_a3 = _Rit_all_ag_a3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 30),
    _Rit_all_ag_a3_Type()
)
rit_all_ag_a3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_all_ag_a3.setStatus("current")
if mibBuilder.loadTexts:
    rit_all_ag_a3.setUnits("sec")


class _Rall_on_flux_p1_Type(Integer32):
    """Custom type rall_on_flux_p1 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_Rall_on_flux_p1_Type.__name__ = "Integer32"
_Rall_on_flux_p1_Object = MibScalar
rall_on_flux_p1 = _Rall_on_flux_p1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 31),
    _Rall_on_flux_p1_Type()
)
rall_on_flux_p1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rall_on_flux_p1.setStatus("current")
if mibBuilder.loadTexts:
    rall_on_flux_p1.setUnits("sec")


class _Rall_rg_flux_p2_Type(Integer32):
    """Custom type rall_rg_flux_p2 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_Rall_rg_flux_p2_Type.__name__ = "Integer32"
_Rall_rg_flux_p2_Object = MibScalar
rall_rg_flux_p2 = _Rall_rg_flux_p2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 32),
    _Rall_rg_flux_p2_Type()
)
rall_rg_flux_p2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rall_rg_flux_p2.setStatus("current")
if mibBuilder.loadTexts:
    rall_rg_flux_p2.setUnits("sec")


class _Rit_all_bp_p3_Type(Integer32):
    """Custom type rit_all_bp_p3 based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_Rit_all_bp_p3_Type.__name__ = "Integer32"
_Rit_all_bp_p3_Object = MibScalar
rit_all_bp_p3 = _Rit_all_bp_p3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 33),
    _Rit_all_bp_p3_Type()
)
rit_all_bp_p3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_all_bp_p3.setStatus("current")
if mibBuilder.loadTexts:
    rit_all_bp_p3.setUnits("sec")


class _Buzzer_p4_Type(Integer32):
    """Custom type buzzer_p4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Buzzer_p4_Type.__name__ = "Integer32"
_Buzzer_p4_Object = MibScalar
buzzer_p4 = _Buzzer_p4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 34),
    _Buzzer_p4_Type()
)
buzzer_p4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buzzer_p4.setStatus("current")
if mibBuilder.loadTexts:
    buzzer_p4.setUnits("N/A")


class _Modello_h1_Type(Integer32):
    """Custom type modello_h1 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Modello_h1_Type.__name__ = "Integer32"
_Modello_h1_Object = MibScalar
modello_h1 = _Modello_h1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 35),
    _Modello_h1_Type()
)
modello_h1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modello_h1.setStatus("current")
if mibBuilder.loadTexts:
    modello_h1.setUnits("N/A")


class _Modo_pompa_h5_Type(Integer32):
    """Custom type modo_pompa_h5 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Modo_pompa_h5_Type.__name__ = "Integer32"
_Modo_pompa_h5_Object = MibScalar
modo_pompa_h5 = _Modo_pompa_h5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 36),
    _Modo_pompa_h5_Type()
)
modo_pompa_h5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modo_pompa_h5.setStatus("current")
if mibBuilder.loadTexts:
    modo_pompa_h5.setUnits("flag")


class _Blocca_tasti_h9_Type(Integer32):
    """Custom type blocca_tasti_h9 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Blocca_tasti_h9_Type.__name__ = "Integer32"
_Blocca_tasti_h9_Object = MibScalar
blocca_tasti_h9 = _Blocca_tasti_h9_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 37),
    _Blocca_tasti_h9_Type()
)
blocca_tasti_h9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blocca_tasti_h9.setStatus("current")
if mibBuilder.loadTexts:
    blocca_tasti_h9.setUnits("flag")


class _Delay_def_dc_Type(Integer32):
    """Custom type delay_def_dc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Delay_def_dc_Type.__name__ = "Integer32"
_Delay_def_dc_Object = MibScalar
delay_def_dc = _Delay_def_dc_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 39),
    _Delay_def_dc_Type()
)
delay_def_dc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_def_dc.setStatus("current")
if mibBuilder.loadTexts:
    delay_def_dc.setUnits("min")


class _Time_wait_def_dd_Type(Integer32):
    """Custom type time_wait_def_dd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Time_wait_def_dd_Type.__name__ = "Integer32"
_Time_wait_def_dd_Object = MibScalar
time_wait_def_dd = _Time_wait_def_dd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 40),
    _Time_wait_def_dd_Type()
)
time_wait_def_dd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_wait_def_dd.setStatus("current")
if mibBuilder.loadTexts:
    time_wait_def_dd.setUnits("N/A")


class _Valve_status_Type(Integer32):
    """Custom type valve_status based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Valve_status_Type.__name__ = "Integer32"
_Valve_status_Object = MibScalar
valve_status = _Valve_status_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 41),
    _Valve_status_Type()
)
valve_status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valve_status.setStatus("current")
if mibBuilder.loadTexts:
    valve_status.setUnits("N/A")


class _Machine_config_Type(Integer32):
    """Custom type machine_config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Machine_config_Type.__name__ = "Integer32"
_Machine_config_Object = MibScalar
machine_config = _Machine_config_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 50),
    _Machine_config_Type()
)
machine_config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machine_config.setStatus("current")
if mibBuilder.loadTexts:
    machine_config.setUnits("N/A")


class _Swrel_Type(Integer32):
    """Custom type swrel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Swrel_Type.__name__ = "Integer32"
_Swrel_Object = MibScalar
swrel = _Swrel_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 51),
    _Swrel_Type()
)
swrel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swrel.setStatus("current")
if mibBuilder.loadTexts:
    swrel.setUnits("N/A")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAREL-uchiller-MIB",
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
       "uchillerMIB": uchillerMIB,
       "digitalObjects": digitalObjects,
       "res_antig_c1": res_antig_c1,
       "valv_inv_c1": valv_inv_c1,
       "allarme": allarme,
       "antifreeze_resist_c2": antifreeze_resist_c2,
       "compressore_c2": compressore_c2,
       "valv_inv_c2": valv_inv_c2,
       "err_sonda_s1": err_sonda_s1,
       "err_sonda_s2": err_sonda_s2,
       "err_sonda_s3": err_sonda_s3,
       "err_sonda_s4": err_sonda_s4,
       "err_sonda_s5": err_sonda_s5,
       "err_eeprom": err_eeprom,
       "freq_rete": freq_rete,
       "allarme_terminale_disconnesso": allarme_terminale_disconnesso,
       "defrost_st_1": defrost_st_1,
       "defrost_st_2": defrost_st_2,
       "all_h_press_c1": all_h_press_c1,
       "all_l_press_c1": all_l_press_c1,
       "all_term_compc1": all_term_compc1,
       "all_term_fanc1": all_term_fanc1,
       "all_flusso": all_flusso,
       "est_inv": est_inv,
       "all_h_press_c2": all_h_press_c2,
       "all_l_press_c2": all_l_press_c2,
       "all_term_compc2": all_term_compc2,
       "all_term_fanc2": all_term_fanc2,
       "rich_manut_c2": rich_manut_c2,
       "all_antigelo_c1": all_antigelo_c1,
       "all_antigelo_c2": all_antigelo_c2,
       "all_defrost_c1": all_defrost_c1,
       "all_defrost_c2": all_defrost_c2,
       "tsonda_inev__1": tsonda_inev__1,
       "tsonda_outev__2": tsonda_outev__2,
       "out_per_fan_f1": out_per_fan_f1,
       "defr_antig_d1": defr_antig_d1,
       "num_fan_h2": num_fan_h2,
       "num_evap_h3": num_evap_h3,
       "compr_parz_h4": compr_parz_h4,
       "en_din_e_i_h6": en_din_e_i_h6,
       "en_din_a_s_h7": en_din_a_s_h7,
       "num_termin_h8": num_termin_h8,
       "num_compressori": num_compressori,
       "comp_rot_r5": comp_rot_r5,
       "def_ext_da": def_ext_da,
       "anti_def_db": anti_def_db,
       "end_def_de": end_def_de,
       "sup_probe_a6": sup_probe_a6,
       "reset_alarm_p5": reset_alarm_p5,
       "set_2_param_p6": set_2_param_p6,
       "low_press_alarm_p7": low_press_alarm_p7,
       "analogObjects": analogObjects,
       "sonda_s1": sonda_s1,
       "sonda_s2_r6": sonda_s2_r6,
       "sonda_s3_r7": sonda_s3_r7,
       "sonda_s4_r8": sonda_s4_r8,
       "sonda_s5_r9": sonda_s5_r9,
       "calibra_s1__6": calibra_s1__6,
       "calibra_s2__7": calibra_s2__7,
       "calibra_s3__8": calibra_s3__8,
       "calibra_s4__9": calibra_s4__9,
       "calibra_s5__a": calibra_s5__a,
       "setp_est_r1": setp_est_r1,
       "differ_est_r2": differ_est_r2,
       "setp_inv_r3": setp_inv_r3,
       "differ_inv_r4": differ_inv_r4,
       "set_min_est_ra": set_min_est_ra,
       "set_max_est_rb": set_max_est_rb,
       "set_min_inv_rc": set_min_inv_rc,
       "set_max_inv_rd": set_max_inv_rd,
       "tmin_vel_est_f5": tmin_vel_est_f5,
       "tmax_vel_est_f6": tmax_vel_est_f6,
       "tmin_vel_inv_f7": tmin_vel_inv_f7,
       "tmax_vel_inv_f8": tmax_vel_inv_f8,
       "toff_fan_est_f9": toff_fan_est_f9,
       "toff_fan_inv_fa": toff_fan_inv_fa,
       "tp_start_def_d3": tp_start_def_d3,
       "tp_end_def_d4": tp_end_def_d4,
       "set_al_agelo_a1": set_al_agelo_a1,
       "dif_al_agelo_a2": dif_al_agelo_a2,
       "set_res_gelo_a4": set_res_gelo_a4,
       "dif_res_gelo_a5": dif_res_gelo_a5,
       "integerObjects": integerObjects,
       "tipo_sonda__3": tipo_sonda__3,
       "min_in_corr__4": min_in_corr__4,
       "max_in_corr__5": max_in_corr__5,
       "filtro_dig__b": filtro_dig__b,
       "limitaz_in__c": limitaz_in__c,
       "tmin_on_comp_c1": tmin_on_comp_c1,
       "time_2_acc_c3": time_2_acc_c3,
       "rit_off_2c_c5": rit_off_2c_c5,
       "rit_on_comp_c6": rit_on_comp_c6,
       "rit_c_on_pmp_c7": rit_c_on_pmp_c7,
       "off_p_off_c_c8": off_p_off_c_c8,
       "ore_comp1_c9": ore_comp1_c9,
       "ore_comp2_ca": ore_comp2_ca,
       "max_ore_comp_cb": max_ore_comp_cb,
       "ore_pompa_cc": ore_pompa_cc,
       "rit_c_f_cond_cd": rit_c_f_cond_cd,
       "modo_fan_f2": modo_fan_f2,
       "min_volt_f3": min_volt_f3,
       "max_volt_f4": max_volt_f4,
       "t_spunto_f_fb": t_spunto_f_fb,
       "t_min_on_def_d5": t_min_on_def_d5,
       "t_min_def_d6": t_min_def_d6,
       "t_max_def_d7": t_max_def_d7,
       "rit_2def_1c_d8": rit_2def_1c_d8,
       "rit_def_2c_d9": rit_def_2c_d9,
       "rit_all_ag_a3": rit_all_ag_a3,
       "rall_on_flux_p1": rall_on_flux_p1,
       "rall_rg_flux_p2": rall_rg_flux_p2,
       "rit_all_bp_p3": rit_all_bp_p3,
       "buzzer_p4": buzzer_p4,
       "modello_h1": modello_h1,
       "modo_pompa_h5": modo_pompa_h5,
       "blocca_tasti_h9": blocca_tasti_h9,
       "delay_def_dc": delay_def_dc,
       "time_wait_def_dd": time_wait_def_dd,
       "valve_status": valve_status,
       "machine_config": machine_config,
       "swrel": swrel}
)
