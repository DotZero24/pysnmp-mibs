# SNMP MIB module (CAREL-mcella-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/carel/CAREL-mcella-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:05 2025
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

mcellaMIB = ModuleIdentity(
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


class _Ciclo_continuo_Type(Integer32):
    """Custom type ciclo_continuo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ciclo_continuo_Type.__name__ = "Integer32"
_Ciclo_continuo_Object = MibScalar
ciclo_continuo = _Ciclo_continuo_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 1),
    _Ciclo_continuo_Type()
)
ciclo_continuo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciclo_continuo.setStatus("current")
if mibBuilder.loadTexts:
    ciclo_continuo.setUnits("N/A")


class _Ventilatori_Type(Integer32):
    """Custom type ventilatori based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ventilatori_Type.__name__ = "Integer32"
_Ventilatori_Object = MibScalar
ventilatori = _Ventilatori_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 2),
    _Ventilatori_Type()
)
ventilatori.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ventilatori.setStatus("current")
if mibBuilder.loadTexts:
    ventilatori.setUnits("N/A")


class _Compressor_Type(Integer32):
    """Custom type compressor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Compressor_Type.__name__ = "Integer32"
_Compressor_Object = MibScalar
compressor = _Compressor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 4),
    _Compressor_Type()
)
compressor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressor.setStatus("current")
if mibBuilder.loadTexts:
    compressor.setUnits("N/A")


class _Aux_out_Type(Integer32):
    """Custom type aux_out based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Aux_out_Type.__name__ = "Integer32"
_Aux_out_Object = MibScalar
aux_out = _Aux_out_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 5),
    _Aux_out_Type()
)
aux_out.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aux_out.setStatus("current")
if mibBuilder.loadTexts:
    aux_out.setUnits("N/A")


class _Valv_inv_ciclo_Type(Integer32):
    """Custom type valv_inv_ciclo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Valv_inv_ciclo_Type.__name__ = "Integer32"
_Valv_inv_ciclo_Object = MibScalar
valv_inv_ciclo = _Valv_inv_ciclo_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 6),
    _Valv_inv_ciclo_Type()
)
valv_inv_ciclo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valv_inv_ciclo.setStatus("current")
if mibBuilder.loadTexts:
    valv_inv_ciclo.setUnits("N/A")


class _All_eeprom_Type(Integer32):
    """Custom type all_eeprom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_eeprom_Type.__name__ = "Integer32"
_All_eeprom_Object = MibScalar
all_eeprom = _All_eeprom_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 8),
    _All_eeprom_Type()
)
all_eeprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_eeprom.setStatus("current")
if mibBuilder.loadTexts:
    all_eeprom.setUnits("N/A")


class _All_timeout_def_Type(Integer32):
    """Custom type all_timeout_def based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_timeout_def_Type.__name__ = "Integer32"
_All_timeout_def_Object = MibScalar
all_timeout_def = _All_timeout_def_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 9),
    _All_timeout_def_Type()
)
all_timeout_def.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_timeout_def.setStatus("current")
if mibBuilder.loadTexts:
    all_timeout_def.setUnits("N/A")


class _All_bassa_temp_Type(Integer32):
    """Custom type all_bassa_temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_bassa_temp_Type.__name__ = "Integer32"
_All_bassa_temp_Object = MibScalar
all_bassa_temp = _All_bassa_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 10),
    _All_bassa_temp_Type()
)
all_bassa_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_bassa_temp.setStatus("current")
if mibBuilder.loadTexts:
    all_bassa_temp.setUnits("N/A")


class _All_alta_temp_Type(Integer32):
    """Custom type all_alta_temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_alta_temp_Type.__name__ = "Integer32"
_All_alta_temp_Object = MibScalar
all_alta_temp = _All_alta_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 11),
    _All_alta_temp_Type()
)
all_alta_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_alta_temp.setStatus("current")
if mibBuilder.loadTexts:
    all_alta_temp.setUnits("N/A")


class _All_sonda_amb_Type(Integer32):
    """Custom type all_sonda_amb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_sonda_amb_Type.__name__ = "Integer32"
_All_sonda_amb_Object = MibScalar
all_sonda_amb = _All_sonda_amb_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 12),
    _All_sonda_amb_Type()
)
all_sonda_amb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_sonda_amb.setStatus("current")
if mibBuilder.loadTexts:
    all_sonda_amb.setUnits("N/A")


class _All_sonda_def_Type(Integer32):
    """Custom type all_sonda_def based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_sonda_def_Type.__name__ = "Integer32"
_All_sonda_def_Object = MibScalar
all_sonda_def = _All_sonda_def_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 13),
    _All_sonda_def_Type()
)
all_sonda_def.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_sonda_def.setStatus("current")
if mibBuilder.loadTexts:
    all_sonda_def.setUnits("N/A")


class _All_imm_ai_Type(Integer32):
    """Custom type all_imm_ai based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_imm_ai_Type.__name__ = "Integer32"
_All_imm_ai_Object = MibScalar
all_imm_ai = _All_imm_ai_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 14),
    _All_imm_ai_Type()
)
all_imm_ai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_imm_ai.setStatus("current")
if mibBuilder.loadTexts:
    all_imm_ai.setUnits("N/A")


class _All_rit_ad_Type(Integer32):
    """Custom type all_rit_ad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_rit_ad_Type.__name__ = "Integer32"
_All_rit_ad_Object = MibScalar
all_rit_ad = _All_rit_ad_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 15),
    _All_rit_ad_Type()
)
all_rit_ad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_rit_ad.setStatus("current")
if mibBuilder.loadTexts:
    all_rit_ad.setUnits("N/A")


class _Sbrinam_on_Type(Integer32):
    """Custom type sbrinam_on based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sbrinam_on_Type.__name__ = "Integer32"
_Sbrinam_on_Object = MibScalar
sbrinam_on = _Sbrinam_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 17),
    _Sbrinam_on_Type()
)
sbrinam_on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbrinam_on.setStatus("current")
if mibBuilder.loadTexts:
    sbrinam_on.setUnits("N/A")


class _C_f__5_Type(Integer32):
    """Custom type c_f__5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_C_f__5_Type.__name__ = "Integer32"
_C_f__5_Object = MibScalar
c_f__5 = _C_f__5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 26),
    _C_f__5_Type()
)
c_f__5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c_f__5.setStatus("current")
if mibBuilder.loadTexts:
    c_f__5.setUnits("flag")


class _En_ed_alarm_Type(Integer32):
    """Custom type en_ed_alarm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_ed_alarm_Type.__name__ = "Integer32"
_En_ed_alarm_Object = MibScalar
en_ed_alarm = _En_ed_alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 27),
    _En_ed_alarm_Type()
)
en_ed_alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    en_ed_alarm.setStatus("current")
if mibBuilder.loadTexts:
    en_ed_alarm.setUnits("flag")


class _Def_uni_up_Type(Integer32):
    """Custom type def_uni_up based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Def_uni_up_Type.__name__ = "Integer32"
_Def_uni_up_Object = MibScalar
def_uni_up = _Def_uni_up_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 29),
    _Def_uni_up_Type()
)
def_uni_up.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    def_uni_up.setStatus("current")
if mibBuilder.loadTexts:
    def_uni_up.setUnits("flag")


class _Def_pri_Type(Integer32):
    """Custom type def_pri based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Def_pri_Type.__name__ = "Integer32"
_Def_pri_Object = MibScalar
def_pri = _Def_pri_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 30),
    _Def_pri_Type()
)
def_pri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    def_pri.setStatus("current")
if mibBuilder.loadTexts:
    def_pri.setUnits("flag")


class _Time_base_dc_Type(Integer32):
    """Custom type time_base_dc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Time_base_dc_Type.__name__ = "Integer32"
_Time_base_dc_Object = MibScalar
time_base_dc = _Time_base_dc_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 31),
    _Time_base_dc_Type()
)
time_base_dc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_base_dc.setStatus("current")
if mibBuilder.loadTexts:
    time_base_dc.setUnits("flag")


class _Stop_fan_f2_Type(Integer32):
    """Custom type stop_fan_f2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Stop_fan_f2_Type.__name__ = "Integer32"
_Stop_fan_f2_Object = MibScalar
stop_fan_f2 = _Stop_fan_f2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 33),
    _Stop_fan_f2_Type()
)
stop_fan_f2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stop_fan_f2.setStatus("current")
if mibBuilder.loadTexts:
    stop_fan_f2.setUnits("flag")


class _Stop_fan_f3_Type(Integer32):
    """Custom type stop_fan_f3 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Stop_fan_f3_Type.__name__ = "Integer32"
_Stop_fan_f3_Object = MibScalar
stop_fan_f3 = _Stop_fan_f3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 34),
    _Stop_fan_f3_Type()
)
stop_fan_f3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stop_fan_f3.setStatus("current")
if mibBuilder.loadTexts:
    stop_fan_f3.setUnits("flag")


class _M_def_Type(Integer32):
    """Custom type m_def based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_M_def_Type.__name__ = "Integer32"
_M_def_Object = MibScalar
m_def = _M_def_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 39),
    _M_def_Type()
)
m_def.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m_def.setStatus("current")
if mibBuilder.loadTexts:
    m_def.setUnits("N/A")


class _Int_display_Type(Integer32):
    """Custom type int_display based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Int_display_Type.__name__ = "Integer32"
_Int_display_Object = MibScalar
int_display = _Int_display_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 42),
    _Int_display_Type()
)
int_display.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    int_display.setStatus("current")
if mibBuilder.loadTexts:
    int_display.setUnits("flag")


class _En_max_min_Type(Integer32):
    """Custom type en_max_min based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_max_min_Type.__name__ = "Integer32"
_En_max_min_Object = MibScalar
en_max_min = _En_max_min_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 43),
    _En_max_min_Type()
)
en_max_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    en_max_min.setStatus("current")
if mibBuilder.loadTexts:
    en_max_min.setUnits("flag")


class _Blocco_vis_sbrin_Type(Integer32):
    """Custom type blocco_vis_sbrin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Blocco_vis_sbrin_Type.__name__ = "Integer32"
_Blocco_vis_sbrin_Object = MibScalar
blocco_vis_sbrin = _Blocco_vis_sbrin_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 44),
    _Blocco_vis_sbrin_Type()
)
blocco_vis_sbrin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blocco_vis_sbrin.setStatus("current")
if mibBuilder.loadTexts:
    blocco_vis_sbrin.setUnits("flag")
_AnalogObjects_ObjectIdentity = ObjectIdentity
analogObjects = _AnalogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2)
)


class _Temp_ambiente_Type(Integer32):
    """Custom type temp_ambiente based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Temp_ambiente_Type.__name__ = "Integer32"
_Temp_ambiente_Object = MibScalar
temp_ambiente = _Temp_ambiente_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 1),
    _Temp_ambiente_Type()
)
temp_ambiente.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp_ambiente.setStatus("current")
if mibBuilder.loadTexts:
    temp_ambiente.setUnits("C x10")


class _Temp_evap_Type(Integer32):
    """Custom type temp_evap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Temp_evap_Type.__name__ = "Integer32"
_Temp_evap_Object = MibScalar
temp_evap = _Temp_evap_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 2),
    _Temp_evap_Type()
)
temp_evap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp_evap.setStatus("current")
if mibBuilder.loadTexts:
    temp_evap.setUnits("C x10")


class _Set_point_Type(Integer32):
    """Custom type set_point based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Set_point_Type.__name__ = "Integer32"
_Set_point_Object = MibScalar
set_point = _Set_point_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 3),
    _Set_point_Type()
)
set_point.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_point.setStatus("current")
if mibBuilder.loadTexts:
    set_point.setUnits("C/F x10")


class _Offset_probe_Type(Integer32):
    """Custom type offset_probe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_Offset_probe_Type.__name__ = "Integer32"
_Offset_probe_Object = MibScalar
offset_probe = _Offset_probe_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 4),
    _Offset_probe_Type()
)
offset_probe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offset_probe.setStatus("current")
if mibBuilder.loadTexts:
    offset_probe.setUnits("C/F x10")


class _Control_delta_Type(Integer32):
    """Custom type control_delta based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_Control_delta_Type.__name__ = "Integer32"
_Control_delta_Object = MibScalar
control_delta = _Control_delta_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 5),
    _Control_delta_Type()
)
control_delta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    control_delta.setStatus("current")
if mibBuilder.loadTexts:
    control_delta.setUnits("C/F x10")


class _Set_point_min_Type(Integer32):
    """Custom type set_point_min based on Integer32"""
    defaultValue = -500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 32767),
    )


_Set_point_min_Type.__name__ = "Integer32"
_Set_point_min_Object = MibScalar
set_point_min = _Set_point_min_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 6),
    _Set_point_min_Type()
)
set_point_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_point_min.setStatus("current")
if mibBuilder.loadTexts:
    set_point_min.setUnits("C/F x10")


class _Set_point_max_Type(Integer32):
    """Custom type set_point_max based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 1990),
    )


_Set_point_max_Type.__name__ = "Integer32"
_Set_point_max_Object = MibScalar
set_point_max = _Set_point_max_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 7),
    _Set_point_max_Type()
)
set_point_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_point_max.setStatus("current")
if mibBuilder.loadTexts:
    set_point_max.setUnits("C/F x10")


class _Defrost_end_temperature_Type(Integer32):
    """Custom type defrost_end_temperature based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 1990),
    )


_Defrost_end_temperature_Type.__name__ = "Integer32"
_Defrost_end_temperature_Object = MibScalar
defrost_end_temperature = _Defrost_end_temperature_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 8),
    _Defrost_end_temperature_Type()
)
defrost_end_temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_end_temperature.setStatus("current")
if mibBuilder.loadTexts:
    defrost_end_temperature.setUnits("C/F x10")


class _Diff_alarm_fan_Type(Integer32):
    """Custom type diff_alarm_fan based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_Diff_alarm_fan_Type.__name__ = "Integer32"
_Diff_alarm_fan_Object = MibScalar
diff_alarm_fan = _Diff_alarm_fan_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 9),
    _Diff_alarm_fan_Type()
)
diff_alarm_fan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diff_alarm_fan.setStatus("current")
if mibBuilder.loadTexts:
    diff_alarm_fan.setUnits("C/F x10")


class _Sgl_alarm_min_rel_Type(Integer32):
    """Custom type sgl_alarm_min_rel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1990),
    )


_Sgl_alarm_min_rel_Type.__name__ = "Integer32"
_Sgl_alarm_min_rel_Object = MibScalar
sgl_alarm_min_rel = _Sgl_alarm_min_rel_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 10),
    _Sgl_alarm_min_rel_Type()
)
sgl_alarm_min_rel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgl_alarm_min_rel.setStatus("current")
if mibBuilder.loadTexts:
    sgl_alarm_min_rel.setUnits("C/F x10")


class _Sgl_alarl_max_rel_Type(Integer32):
    """Custom type sgl_alarl_max_rel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1990),
    )


_Sgl_alarl_max_rel_Type.__name__ = "Integer32"
_Sgl_alarl_max_rel_Object = MibScalar
sgl_alarl_max_rel = _Sgl_alarl_max_rel_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 11),
    _Sgl_alarl_max_rel_Type()
)
sgl_alarl_max_rel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sgl_alarl_max_rel.setStatus("current")
if mibBuilder.loadTexts:
    sgl_alarl_max_rel.setUnits("C/F x10")


class _Set_fan_off_rel_Type(Integer32):
    """Custom type set_fan_off_rel based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 200),
    )


_Set_fan_off_rel_Type.__name__ = "Integer32"
_Set_fan_off_rel_Object = MibScalar
set_fan_off_rel = _Set_fan_off_rel_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 12),
    _Set_fan_off_rel_Type()
)
set_fan_off_rel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_fan_off_rel.setStatus("current")
if mibBuilder.loadTexts:
    set_fan_off_rel.setUnits("C/F x10")


class _Delta_set_point_Type(Integer32):
    """Custom type delta_set_point based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Delta_set_point_Type.__name__ = "Integer32"
_Delta_set_point_Object = MibScalar
delta_set_point = _Delta_set_point_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 13),
    _Delta_set_point_Type()
)
delta_set_point.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delta_set_point.setStatus("current")
if mibBuilder.loadTexts:
    delta_set_point.setUnits("C/F x10")
_IntegerObjects_ObjectIdentity = ObjectIdentity
integerObjects = _IntegerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3)
)


class _Modello_Type(Integer32):
    """Custom type modello based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Modello_Type.__name__ = "Integer32"
_Modello_Object = MibScalar
modello = _Modello_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 1),
    _Modello_Type()
)
modello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modello.setStatus("current")
if mibBuilder.loadTexts:
    modello.setUnits("N/A")


class _Type_defrost_Type(Integer32):
    """Custom type type_defrost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Type_defrost_Type.__name__ = "Integer32"
_Type_defrost_Object = MibScalar
type_defrost = _Type_defrost_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 2),
    _Type_defrost_Type()
)
type_defrost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    type_defrost.setStatus("current")
if mibBuilder.loadTexts:
    type_defrost.setUnits("flag")


class _Filter_digital_Type(Integer32):
    """Custom type filter_digital based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Filter_digital_Type.__name__ = "Integer32"
_Filter_digital_Object = MibScalar
filter_digital = _Filter_digital_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 3),
    _Filter_digital_Type()
)
filter_digital.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filter_digital.setStatus("current")
if mibBuilder.loadTexts:
    filter_digital.setUnits("N/A")


class _Derivata_Type(Integer32):
    """Custom type derivata based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Derivata_Type.__name__ = "Integer32"
_Derivata_Object = MibScalar
derivata = _Derivata_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 4),
    _Derivata_Type()
)
derivata.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    derivata.setStatus("current")
if mibBuilder.loadTexts:
    derivata.setUnits("N/A")


class _Virtual_probe_Type(Integer32):
    """Custom type virtual_probe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Virtual_probe_Type.__name__ = "Integer32"
_Virtual_probe_Object = MibScalar
virtual_probe = _Virtual_probe_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 5),
    _Virtual_probe_Type()
)
virtual_probe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtual_probe.setStatus("current")
if mibBuilder.loadTexts:
    virtual_probe.setUnits("N/A")


class _Delay_from_startup_Type(Integer32):
    """Custom type delay_from_startup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Delay_from_startup_Type.__name__ = "Integer32"
_Delay_from_startup_Object = MibScalar
delay_from_startup = _Delay_from_startup_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 6),
    _Delay_from_startup_Type()
)
delay_from_startup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_from_startup.setStatus("current")
if mibBuilder.loadTexts:
    delay_from_startup.setUnits("min")


class _Interval_between_2_start_up_Type(Integer32):
    """Custom type interval_between_2_start_up based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Interval_between_2_start_up_Type.__name__ = "Integer32"
_Interval_between_2_start_up_Object = MibScalar
interval_between_2_start_up = _Interval_between_2_start_up_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 7),
    _Interval_between_2_start_up_Type()
)
interval_between_2_start_up.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interval_between_2_start_up.setStatus("current")
if mibBuilder.loadTexts:
    interval_between_2_start_up.setUnits("min")


class _Time_min_off_Type(Integer32):
    """Custom type time_min_off based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Time_min_off_Type.__name__ = "Integer32"
_Time_min_off_Object = MibScalar
time_min_off = _Time_min_off_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 8),
    _Time_min_off_Type()
)
time_min_off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_min_off.setStatus("current")
if mibBuilder.loadTexts:
    time_min_off.setUnits("min")


class _Time_min_on_Type(Integer32):
    """Custom type time_min_on based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Time_min_on_Type.__name__ = "Integer32"
_Time_min_on_Object = MibScalar
time_min_on = _Time_min_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 9),
    _Time_min_on_Type()
)
time_min_on.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_min_on.setStatus("current")
if mibBuilder.loadTexts:
    time_min_on.setUnits("min")


class _Safety_relay_Type(Integer32):
    """Custom type safety_relay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Safety_relay_Type.__name__ = "Integer32"
_Safety_relay_Object = MibScalar
safety_relay = _Safety_relay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 10),
    _Safety_relay_Type()
)
safety_relay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safety_relay.setStatus("current")
if mibBuilder.loadTexts:
    safety_relay.setUnits("min")


class _Duration_cc_Type(Integer32):
    """Custom type duration_cc based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Duration_cc_Type.__name__ = "Integer32"
_Duration_cc_Object = MibScalar
duration_cc = _Duration_cc_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 11),
    _Duration_cc_Type()
)
duration_cc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duration_cc.setStatus("current")
if mibBuilder.loadTexts:
    duration_cc.setUnits("hour")


class _No_alarm_after_cc_Type(Integer32):
    """Custom type no_alarm_after_cc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_No_alarm_after_cc_Type.__name__ = "Integer32"
_No_alarm_after_cc_Object = MibScalar
no_alarm_after_cc = _No_alarm_after_cc_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 12),
    _No_alarm_after_cc_Type()
)
no_alarm_after_cc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    no_alarm_after_cc.setStatus("current")
if mibBuilder.loadTexts:
    no_alarm_after_cc.setUnits("hour")


class _Interval_between_defrost_Type(Integer32):
    """Custom type interval_between_defrost based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Interval_between_defrost_Type.__name__ = "Integer32"
_Interval_between_defrost_Object = MibScalar
interval_between_defrost = _Interval_between_defrost_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 13),
    _Interval_between_defrost_Type()
)
interval_between_defrost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interval_between_defrost.setStatus("current")
if mibBuilder.loadTexts:
    interval_between_defrost.setUnits("hours")


class _Duration_def_Type(Integer32):
    """Custom type duration_def based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_Duration_def_Type.__name__ = "Integer32"
_Duration_def_Object = MibScalar
duration_def = _Duration_def_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 14),
    _Duration_def_Type()
)
duration_def.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duration_def.setStatus("current")
if mibBuilder.loadTexts:
    duration_def.setUnits("min")


class _Delay_def_after_sturt_up_Type(Integer32):
    """Custom type delay_def_after_sturt_up based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Delay_def_after_sturt_up_Type.__name__ = "Integer32"
_Delay_def_after_sturt_up_Object = MibScalar
delay_def_after_sturt_up = _Delay_def_after_sturt_up_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 15),
    _Delay_def_after_sturt_up_Type()
)
delay_def_after_sturt_up.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_def_after_sturt_up.setStatus("current")
if mibBuilder.loadTexts:
    delay_def_after_sturt_up.setUnits("min")


class _Dripping_iyme_Type(Integer32):
    """Custom type dripping_iyme based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dripping_iyme_Type.__name__ = "Integer32"
_Dripping_iyme_Object = MibScalar
dripping_iyme = _Dripping_iyme_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 16),
    _Dripping_iyme_Type()
)
dripping_iyme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dripping_iyme.setStatus("current")
if mibBuilder.loadTexts:
    dripping_iyme.setUnits("min")


class _Duration_of_alarm_Type(Integer32):
    """Custom type duration_of_alarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Duration_of_alarm_Type.__name__ = "Integer32"
_Duration_of_alarm_Object = MibScalar
duration_of_alarm = _Duration_of_alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 17),
    _Duration_of_alarm_Type()
)
duration_of_alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duration_of_alarm.setStatus("current")
if mibBuilder.loadTexts:
    duration_of_alarm.setUnits("hours")


class _Rit_all_temp_Type(Integer32):
    """Custom type rit_all_temp based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Rit_all_temp_Type.__name__ = "Integer32"
_Rit_all_temp_Object = MibScalar
rit_all_temp = _Rit_all_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 18),
    _Rit_all_temp_Type()
)
rit_all_temp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rit_all_temp.setStatus("current")
if mibBuilder.loadTexts:
    rit_all_temp.setUnits("min")


class _Config_dig_in1_Type(Integer32):
    """Custom type config_dig_in1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Config_dig_in1_Type.__name__ = "Integer32"
_Config_dig_in1_Object = MibScalar
config_dig_in1 = _Config_dig_in1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 19),
    _Config_dig_in1_Type()
)
config_dig_in1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config_dig_in1.setStatus("current")
if mibBuilder.loadTexts:
    config_dig_in1.setUnits("N/A")


class _Config_dig_in2_Type(Integer32):
    """Custom type config_dig_in2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Config_dig_in2_Type.__name__ = "Integer32"
_Config_dig_in2_Object = MibScalar
config_dig_in2 = _Config_dig_in2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 20),
    _Config_dig_in2_Type()
)
config_dig_in2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config_dig_in2.setStatus("current")
if mibBuilder.loadTexts:
    config_dig_in2.setUnits("N/A")


class _Look_comp_ext_Type(Integer32):
    """Custom type look_comp_ext based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Look_comp_ext_Type.__name__ = "Integer32"
_Look_comp_ext_Object = MibScalar
look_comp_ext = _Look_comp_ext_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 21),
    _Look_comp_ext_Type()
)
look_comp_ext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    look_comp_ext.setStatus("current")
if mibBuilder.loadTexts:
    look_comp_ext.setUnits("min")


class _Delay_activ_alr_Type(Integer32):
    """Custom type delay_activ_alr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Delay_activ_alr_Type.__name__ = "Integer32"
_Delay_activ_alr_Object = MibScalar
delay_activ_alr = _Delay_activ_alr_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 22),
    _Delay_activ_alr_Type()
)
delay_activ_alr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_activ_alr.setStatus("current")
if mibBuilder.loadTexts:
    delay_activ_alr.setUnits("min")


class _Enabling_telecom_Type(Integer32):
    """Custom type enabling_telecom based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Enabling_telecom_Type.__name__ = "Integer32"
_Enabling_telecom_Object = MibScalar
enabling_telecom = _Enabling_telecom_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 23),
    _Enabling_telecom_Type()
)
enabling_telecom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enabling_telecom.setStatus("current")
if mibBuilder.loadTexts:
    enabling_telecom.setUnits("N/A")


class _Sto_after_drip_Type(Integer32):
    """Custom type sto_after_drip based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Sto_after_drip_Type.__name__ = "Integer32"
_Sto_after_drip_Object = MibScalar
sto_after_drip = _Sto_after_drip_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 24),
    _Sto_after_drip_Type()
)
sto_after_drip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sto_after_drip.setStatus("current")
if mibBuilder.loadTexts:
    sto_after_drip.setUnits("min")


class _Key_lock_Type(Integer32):
    """Custom type key_lock based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Key_lock_Type.__name__ = "Integer32"
_Key_lock_Object = MibScalar
key_lock = _Key_lock_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 25),
    _Key_lock_Type()
)
key_lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    key_lock.setStatus("current")
if mibBuilder.loadTexts:
    key_lock.setUnits("flag")


class _Fan_man_f0_Type(Integer32):
    """Custom type fan_man_f0 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Fan_man_f0_Type.__name__ = "Integer32"
_Fan_man_f0_Object = MibScalar
fan_man_f0 = _Fan_man_f0_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 26),
    _Fan_man_f0_Type()
)
fan_man_f0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan_man_f0.setStatus("current")
if mibBuilder.loadTexts:
    fan_man_f0.setUnits("flag")


class _Oper_mode_h1_Type(Integer32):
    """Custom type oper_mode_h1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Oper_mode_h1_Type.__name__ = "Integer32"
_Oper_mode_h1_Object = MibScalar
oper_mode_h1 = _Oper_mode_h1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 27),
    _Oper_mode_h1_Type()
)
oper_mode_h1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oper_mode_h1.setStatus("current")
if mibBuilder.loadTexts:
    oper_mode_h1.setUnits("N/A")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAREL-mcella-MIB",
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
       "mcellaMIB": mcellaMIB,
       "digitalObjects": digitalObjects,
       "ciclo_continuo": ciclo_continuo,
       "ventilatori": ventilatori,
       "compressor": compressor,
       "aux_out": aux_out,
       "valv_inv_ciclo": valv_inv_ciclo,
       "all_eeprom": all_eeprom,
       "all_timeout_def": all_timeout_def,
       "all_bassa_temp": all_bassa_temp,
       "all_alta_temp": all_alta_temp,
       "all_sonda_amb": all_sonda_amb,
       "all_sonda_def": all_sonda_def,
       "all_imm_ai": all_imm_ai,
       "all_rit_ad": all_rit_ad,
       "sbrinam_on": sbrinam_on,
       "c_f__5": c_f__5,
       "en_ed_alarm": en_ed_alarm,
       "def_uni_up": def_uni_up,
       "def_pri": def_pri,
       "time_base_dc": time_base_dc,
       "stop_fan_f2": stop_fan_f2,
       "stop_fan_f3": stop_fan_f3,
       "m_def": m_def,
       "int_display": int_display,
       "en_max_min": en_max_min,
       "blocco_vis_sbrin": blocco_vis_sbrin,
       "analogObjects": analogObjects,
       "temp_ambiente": temp_ambiente,
       "temp_evap": temp_evap,
       "set_point": set_point,
       "offset_probe": offset_probe,
       "control_delta": control_delta,
       "set_point_min": set_point_min,
       "set_point_max": set_point_max,
       "defrost_end_temperature": defrost_end_temperature,
       "diff_alarm_fan": diff_alarm_fan,
       "sgl_alarm_min_rel": sgl_alarm_min_rel,
       "sgl_alarl_max_rel": sgl_alarl_max_rel,
       "set_fan_off_rel": set_fan_off_rel,
       "delta_set_point": delta_set_point,
       "integerObjects": integerObjects,
       "modello": modello,
       "type_defrost": type_defrost,
       "filter_digital": filter_digital,
       "derivata": derivata,
       "virtual_probe": virtual_probe,
       "delay_from_startup": delay_from_startup,
       "interval_between_2_start-up": interval_between_2_start_up,
       "time_min_off": time_min_off,
       "time_min_on": time_min_on,
       "safety_relay": safety_relay,
       "duration_cc": duration_cc,
       "no_alarm_after_cc": no_alarm_after_cc,
       "interval_between_defrost": interval_between_defrost,
       "duration_def": duration_def,
       "delay_def_after_sturt_up": delay_def_after_sturt_up,
       "dripping_iyme": dripping_iyme,
       "duration_of_alarm": duration_of_alarm,
       "rit_all_temp": rit_all_temp,
       "config_dig_in1": config_dig_in1,
       "config_dig_in2": config_dig_in2,
       "look_comp_ext": look_comp_ext,
       "delay_activ_alr": delay_activ_alr,
       "enabling_telecom": enabling_telecom,
       "sto_after_drip": sto_after_drip,
       "key_lock": key_lock,
       "fan_man_f0": fan_man_f0,
       "oper_mode_h1": oper_mode_h1}
)
