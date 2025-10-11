# SNMP MIB module (CAREL-mastercase-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/carel/CAREL-mastercase-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:02 2025
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

mastercaseMIB = ModuleIdentity(
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


class _On_off_status_Type(Integer32):
    """Custom type on_off_status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_On_off_status_Type.__name__ = "Integer32"
_On_off_status_Object = MibScalar
on_off_status = _On_off_status_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 1),
    _On_off_status_Type()
)
on_off_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    on_off_status.setStatus("current")
if mibBuilder.loadTexts:
    on_off_status.setUnits("N/A")


class _En_dec_point_Type(Integer32):
    """Custom type en_dec_point based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_dec_point_Type.__name__ = "Integer32"
_En_dec_point_Object = MibScalar
en_dec_point = _En_dec_point_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 2),
    _En_dec_point_Type()
)
en_dec_point.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    en_dec_point.setStatus("current")
if mibBuilder.loadTexts:
    en_dec_point.setUnits("N/A")


class _Defrost_con_sonda_3_Type(Integer32):
    """Custom type defrost_con_sonda_3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Defrost_con_sonda_3_Type.__name__ = "Integer32"
_Defrost_con_sonda_3_Object = MibScalar
defrost_con_sonda_3 = _Defrost_con_sonda_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 3),
    _Defrost_con_sonda_3_Type()
)
defrost_con_sonda_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_con_sonda_3.setStatus("current")
if mibBuilder.loadTexts:
    defrost_con_sonda_3.setUnits("N/A")


class _Enable_ed_alarm_Type(Integer32):
    """Custom type enable_ed_alarm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_ed_alarm_Type.__name__ = "Integer32"
_Enable_ed_alarm_Object = MibScalar
enable_ed_alarm = _Enable_ed_alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 4),
    _Enable_ed_alarm_Type()
)
enable_ed_alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_ed_alarm.setStatus("current")
if mibBuilder.loadTexts:
    enable_ed_alarm.setUnits("N/A")


class _Enable_monitor_temp_maxmin_Type(Integer32):
    """Custom type enable_monitor_temp_maxmin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enable_monitor_temp_maxmin_Type.__name__ = "Integer32"
_Enable_monitor_temp_maxmin_Object = MibScalar
enable_monitor_temp_maxmin = _Enable_monitor_temp_maxmin_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 5),
    _Enable_monitor_temp_maxmin_Type()
)
enable_monitor_temp_maxmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_monitor_temp_maxmin.setStatus("current")
if mibBuilder.loadTexts:
    enable_monitor_temp_maxmin.setUnits("N/A")


class _Regol_notturna_sonda_3_Type(Integer32):
    """Custom type regol_notturna_sonda_3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Regol_notturna_sonda_3_Type.__name__ = "Integer32"
_Regol_notturna_sonda_3_Object = MibScalar
regol_notturna_sonda_3 = _Regol_notturna_sonda_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 6),
    _Regol_notturna_sonda_3_Type()
)
regol_notturna_sonda_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regol_notturna_sonda_3.setStatus("current")
if mibBuilder.loadTexts:
    regol_notturna_sonda_3.setUnits("N/A")


class _Disable_pid_Type(Integer32):
    """Custom type disable_pid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Disable_pid_Type.__name__ = "Integer32"
_Disable_pid_Object = MibScalar
disable_pid = _Disable_pid_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 7),
    _Disable_pid_Type()
)
disable_pid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disable_pid.setStatus("current")
if mibBuilder.loadTexts:
    disable_pid.setUnits("N/A")


class _En_exenq_5_Type(Integer32):
    """Custom type en_exenq_5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_exenq_5_Type.__name__ = "Integer32"
_En_exenq_5_Object = MibScalar
en_exenq_5 = _En_exenq_5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 8),
    _En_exenq_5_Type()
)
en_exenq_5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    en_exenq_5.setStatus("current")
if mibBuilder.loadTexts:
    en_exenq_5.setUnits("N/A")


class _Pressure_probe_from_master_Type(Integer32):
    """Custom type pressure_probe_from_master based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pressure_probe_from_master_Type.__name__ = "Integer32"
_Pressure_probe_from_master_Object = MibScalar
pressure_probe_from_master = _Pressure_probe_from_master_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 9),
    _Pressure_probe_from_master_Type()
)
pressure_probe_from_master.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pressure_probe_from_master.setStatus("current")
if mibBuilder.loadTexts:
    pressure_probe_from_master.setUnits("N/A")


class _All_alta_temp_Type(Integer32):
    """Custom type all_alta_temp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_alta_temp_Type.__name__ = "Integer32"
_All_alta_temp_Object = MibScalar
all_alta_temp = _All_alta_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 42),
    _All_alta_temp_Type()
)
all_alta_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_alta_temp.setStatus("current")
if mibBuilder.loadTexts:
    all_alta_temp.setUnits("N/A")


class _All_bassa_temp_Type(Integer32):
    """Custom type all_bassa_temp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_bassa_temp_Type.__name__ = "Integer32"
_All_bassa_temp_Object = MibScalar
all_bassa_temp = _All_bassa_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 43),
    _All_bassa_temp_Type()
)
all_bassa_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_bassa_temp.setStatus("current")
if mibBuilder.loadTexts:
    all_bassa_temp.setUnits("N/A")


class _All_clean_management_Type(Integer32):
    """Custom type all_clean_management based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_clean_management_Type.__name__ = "Integer32"
_All_clean_management_Object = MibScalar
all_clean_management = _All_clean_management_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 44),
    _All_clean_management_Type()
)
all_clean_management.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_clean_management.setStatus("current")
if mibBuilder.loadTexts:
    all_clean_management.setUnits("N/A")


class _All_def_tout_Type(Integer32):
    """Custom type all_def_tout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_def_tout_Type.__name__ = "Integer32"
_All_def_tout_Object = MibScalar
all_def_tout = _All_def_tout_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 45),
    _All_def_tout_Type()
)
all_def_tout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_def_tout.setStatus("current")
if mibBuilder.loadTexts:
    all_def_tout.setUnits("N/A")


class _All_driver_lan_Type(Integer32):
    """Custom type all_driver_lan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_driver_lan_Type.__name__ = "Integer32"
_All_driver_lan_Object = MibScalar
all_driver_lan = _All_driver_lan_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 46),
    _All_driver_lan_Type()
)
all_driver_lan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_driver_lan.setStatus("current")
if mibBuilder.loadTexts:
    all_driver_lan.setUnits("N/A")


class _All_driver_probe_1_Type(Integer32):
    """Custom type all_driver_probe_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_driver_probe_1_Type.__name__ = "Integer32"
_All_driver_probe_1_Object = MibScalar
all_driver_probe_1 = _All_driver_probe_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 47),
    _All_driver_probe_1_Type()
)
all_driver_probe_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_driver_probe_1.setStatus("current")
if mibBuilder.loadTexts:
    all_driver_probe_1.setUnits("N/A")


class _All_driver_probe_2_Type(Integer32):
    """Custom type all_driver_probe_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_driver_probe_2_Type.__name__ = "Integer32"
_All_driver_probe_2_Object = MibScalar
all_driver_probe_2 = _All_driver_probe_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 48),
    _All_driver_probe_2_Type()
)
all_driver_probe_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_driver_probe_2.setStatus("current")
if mibBuilder.loadTexts:
    all_driver_probe_2.setUnits("N/A")


class _All_duty_set_Type(Integer32):
    """Custom type all_duty_set based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_duty_set_Type.__name__ = "Integer32"
_All_duty_set_Object = MibScalar
all_duty_set = _All_duty_set_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 50),
    _All_duty_set_Type()
)
all_duty_set.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_duty_set.setStatus("current")
if mibBuilder.loadTexts:
    all_duty_set.setUnits("N/A")


class _All_ext_del_Type(Integer32):
    """Custom type all_ext_del based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_ext_del_Type.__name__ = "Integer32"
_All_ext_del_Object = MibScalar
all_ext_del = _All_ext_del_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 51),
    _All_ext_del_Type()
)
all_ext_del.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_ext_del.setStatus("current")
if mibBuilder.loadTexts:
    all_ext_del.setUnits("N/A")


class _All_ext_ist_Type(Integer32):
    """Custom type all_ext_ist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_ext_ist_Type.__name__ = "Integer32"
_All_ext_ist_Object = MibScalar
all_ext_ist = _All_ext_ist_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 52),
    _All_ext_ist_Type()
)
all_ext_ist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_ext_ist.setStatus("current")
if mibBuilder.loadTexts:
    all_ext_ist.setUnits("N/A")


class _All_ha_Type(Integer32):
    """Custom type all_ha based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_ha_Type.__name__ = "Integer32"
_All_ha_Object = MibScalar
all_ha = _All_ha_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 53),
    _All_ha_Type()
)
all_ha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_ha.setStatus("current")
if mibBuilder.loadTexts:
    all_ha.setUnits("N/A")


class _All_hf_Type(Integer32):
    """Custom type all_hf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_hf_Type.__name__ = "Integer32"
_All_hf_Object = MibScalar
all_hf = _All_hf_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 54),
    _All_hf_Type()
)
all_hf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_hf.setStatus("current")
if mibBuilder.loadTexts:
    all_hf.setUnits("N/A")


class _All_sonda_amb_Type(Integer32):
    """Custom type all_sonda_amb based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_sonda_amb_Type.__name__ = "Integer32"
_All_sonda_amb_Object = MibScalar
all_sonda_amb = _All_sonda_amb_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 55),
    _All_sonda_amb_Type()
)
all_sonda_amb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_sonda_amb.setStatus("current")
if mibBuilder.loadTexts:
    all_sonda_amb.setUnits("N/A")


class _All_sonda_def_Type(Integer32):
    """Custom type all_sonda_def based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_sonda_def_Type.__name__ = "Integer32"
_All_sonda_def_Object = MibScalar
all_sonda_def = _All_sonda_def_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 56),
    _All_sonda_def_Type()
)
all_sonda_def.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_sonda_def.setStatus("current")
if mibBuilder.loadTexts:
    all_sonda_def.setUnits("N/A")


class _All_sonda_prod_Type(Integer32):
    """Custom type all_sonda_prod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_sonda_prod_Type.__name__ = "Integer32"
_All_sonda_prod_Object = MibScalar
all_sonda_prod = _All_sonda_prod_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 57),
    _All_sonda_prod_Type()
)
all_sonda_prod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_sonda_prod.setStatus("current")
if mibBuilder.loadTexts:
    all_sonda_prod.setUnits("N/A")


class _All_sonda_reg_Type(Integer32):
    """Custom type all_sonda_reg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_sonda_reg_Type.__name__ = "Integer32"
_All_sonda_reg_Object = MibScalar
all_sonda_reg = _All_sonda_reg_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 58),
    _All_sonda_reg_Type()
)
all_sonda_reg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_sonda_reg.setStatus("current")
if mibBuilder.loadTexts:
    all_sonda_reg.setUnits("N/A")


class _All_tem_min_s1_Type(Integer32):
    """Custom type all_tem_min_s1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_All_tem_min_s1_Type.__name__ = "Integer32"
_All_tem_min_s1_Object = MibScalar
all_tem_min_s1 = _All_tem_min_s1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 59),
    _All_tem_min_s1_Type()
)
all_tem_min_s1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    all_tem_min_s1.setStatus("current")
if mibBuilder.loadTexts:
    all_tem_min_s1.setUnits("N/A")


class _Digital_out_2_Type(Integer32):
    """Custom type digital_out_2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digital_out_2_Type.__name__ = "Integer32"
_Digital_out_2_Object = MibScalar
digital_out_2 = _Digital_out_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 71),
    _Digital_out_2_Type()
)
digital_out_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_out_2.setStatus("current")
if mibBuilder.loadTexts:
    digital_out_2.setUnits("N/A")


class _Digital_out_4_Type(Integer32):
    """Custom type digital_out_4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digital_out_4_Type.__name__ = "Integer32"
_Digital_out_4_Object = MibScalar
digital_out_4 = _Digital_out_4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 73),
    _Digital_out_4_Type()
)
digital_out_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_out_4.setStatus("current")
if mibBuilder.loadTexts:
    digital_out_4.setUnits("N/A")


class _Digital_out_6_Type(Integer32):
    """Custom type digital_out_6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digital_out_6_Type.__name__ = "Integer32"
_Digital_out_6_Object = MibScalar
digital_out_6 = _Digital_out_6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 75),
    _Digital_out_6_Type()
)
digital_out_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_out_6.setStatus("current")
if mibBuilder.loadTexts:
    digital_out_6.setUnits("N/A")


class _Digital_out_7_Type(Integer32):
    """Custom type digital_out_7 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digital_out_7_Type.__name__ = "Integer32"
_Digital_out_7_Object = MibScalar
digital_out_7 = _Digital_out_7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 76),
    _Digital_out_7_Type()
)
digital_out_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_out_7.setStatus("current")
if mibBuilder.loadTexts:
    digital_out_7.setUnits("N/A")


class _Digital_out_8_Type(Integer32):
    """Custom type digital_out_8 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digital_out_8_Type.__name__ = "Integer32"
_Digital_out_8_Object = MibScalar
digital_out_8 = _Digital_out_8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 77),
    _Digital_out_8_Type()
)
digital_out_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_out_8.setStatus("current")
if mibBuilder.loadTexts:
    digital_out_8.setUnits("N/A")


class _Digital_out_9_Type(Integer32):
    """Custom type digital_out_9 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digital_out_9_Type.__name__ = "Integer32"
_Digital_out_9_Object = MibScalar
digital_out_9 = _Digital_out_9_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 78),
    _Digital_out_9_Type()
)
digital_out_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_out_9.setStatus("current")
if mibBuilder.loadTexts:
    digital_out_9.setUnits("N/A")


class _Sl_alm_1_Type(Integer32):
    """Custom type sl_alm_1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sl_alm_1_Type.__name__ = "Integer32"
_Sl_alm_1_Object = MibScalar
sl_alm_1 = _Sl_alm_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 88),
    _Sl_alm_1_Type()
)
sl_alm_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sl_alm_1.setStatus("current")
if mibBuilder.loadTexts:
    sl_alm_1.setUnits("N/A")


class _Sv_mst_defrost_end_Type(Integer32):
    """Custom type sv_mst_defrost_end based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sv_mst_defrost_end_Type.__name__ = "Integer32"
_Sv_mst_defrost_end_Object = MibScalar
sv_mst_defrost_end = _Sv_mst_defrost_end_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 95),
    _Sv_mst_defrost_end_Type()
)
sv_mst_defrost_end.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sv_mst_defrost_end.setStatus("current")
if mibBuilder.loadTexts:
    sv_mst_defrost_end.setUnits("N/A")


class _Sv_mst_defrost_start_Type(Integer32):
    """Custom type sv_mst_defrost_start based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sv_mst_defrost_start_Type.__name__ = "Integer32"
_Sv_mst_defrost_start_Object = MibScalar
sv_mst_defrost_start = _Sv_mst_defrost_start_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 96),
    _Sv_mst_defrost_start_Type()
)
sv_mst_defrost_start.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sv_mst_defrost_start.setStatus("current")
if mibBuilder.loadTexts:
    sv_mst_defrost_start.setUnits("N/A")


class _Sw_door_brk_Type(Integer32):
    """Custom type sw_door_brk based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sw_door_brk_Type.__name__ = "Integer32"
_Sw_door_brk_Object = MibScalar
sw_door_brk = _Sw_door_brk_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 97),
    _Sw_door_brk_Type()
)
sw_door_brk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw_door_brk.setStatus("current")
if mibBuilder.loadTexts:
    sw_door_brk.setUnits("N/A")


class _En_high_refresh_Type(Integer32):
    """Custom type en_high_refresh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_high_refresh_Type.__name__ = "Integer32"
_En_high_refresh_Object = MibScalar
en_high_refresh = _En_high_refresh_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 103),
    _En_high_refresh_Type()
)
en_high_refresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    en_high_refresh.setStatus("current")
if mibBuilder.loadTexts:
    en_high_refresh.setUnits("N/A")
_AnalogObjects_ObjectIdentity = ObjectIdentity
analogObjects = _AnalogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2)
)


class _Calibrazione_sonda_3_Type(Integer32):
    """Custom type calibrazione_sonda_3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_Calibrazione_sonda_3_Type.__name__ = "Integer32"
_Calibrazione_sonda_3_Object = MibScalar
calibrazione_sonda_3 = _Calibrazione_sonda_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 1),
    _Calibrazione_sonda_3_Type()
)
calibrazione_sonda_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibrazione_sonda_3.setStatus("current")
if mibBuilder.loadTexts:
    calibrazione_sonda_3.setUnits("C x10")


class _Calibr_sonda_ambiente_Type(Integer32):
    """Custom type calibr_sonda_ambiente based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_Calibr_sonda_ambiente_Type.__name__ = "Integer32"
_Calibr_sonda_ambiente_Object = MibScalar
calibr_sonda_ambiente = _Calibr_sonda_ambiente_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 2),
    _Calibr_sonda_ambiente_Type()
)
calibr_sonda_ambiente.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibr_sonda_ambiente.setStatus("current")
if mibBuilder.loadTexts:
    calibr_sonda_ambiente.setUnits("C x10")


class _Calibrazione_sonda_defrost_Type(Integer32):
    """Custom type calibrazione_sonda_defrost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_Calibrazione_sonda_defrost_Type.__name__ = "Integer32"
_Calibrazione_sonda_defrost_Object = MibScalar
calibrazione_sonda_defrost = _Calibrazione_sonda_defrost_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 3),
    _Calibrazione_sonda_defrost_Type()
)
calibrazione_sonda_defrost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibrazione_sonda_defrost.setStatus("current")
if mibBuilder.loadTexts:
    calibrazione_sonda_defrost.setUnits("C x10")


class _Differenziale_alrm_ventole_Type(Integer32):
    """Custom type differenziale_alrm_ventole based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_Differenziale_alrm_ventole_Type.__name__ = "Integer32"
_Differenziale_alrm_ventole_Object = MibScalar
differenziale_alrm_ventole = _Differenziale_alrm_ventole_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 4),
    _Differenziale_alrm_ventole_Type()
)
differenziale_alrm_ventole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differenziale_alrm_ventole.setStatus("current")
if mibBuilder.loadTexts:
    differenziale_alrm_ventole.setUnits("C x10")


class _Alrm_alta_temp_Type(Integer32):
    """Custom type alrm_alta_temp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Alrm_alta_temp_Type.__name__ = "Integer32"
_Alrm_alta_temp_Object = MibScalar
alrm_alta_temp = _Alrm_alta_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 5),
    _Alrm_alta_temp_Type()
)
alrm_alta_temp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrm_alta_temp.setStatus("current")
if mibBuilder.loadTexts:
    alrm_alta_temp.setUnits("C x10")


class _Alrm_bassa_temp_Type(Integer32):
    """Custom type alrm_bassa_temp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Alrm_bassa_temp_Type.__name__ = "Integer32"
_Alrm_bassa_temp_Object = MibScalar
alrm_bassa_temp = _Alrm_bassa_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 6),
    _Alrm_bassa_temp_Type()
)
alrm_bassa_temp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrm_bassa_temp.setStatus("current")
if mibBuilder.loadTexts:
    alrm_bassa_temp.setUnits("C x10")


class _Temp_ventole_on_Type(Integer32):
    """Custom type temp_ventole_on based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 500),
    )


_Temp_ventole_on_Type.__name__ = "Integer32"
_Temp_ventole_on_Object = MibScalar
temp_ventole_on = _Temp_ventole_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 7),
    _Temp_ventole_on_Type()
)
temp_ventole_on.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temp_ventole_on.setStatus("current")
if mibBuilder.loadTexts:
    temp_ventole_on.setUnits("C x10")


class _Set_point_temperatura_Type(Integer32):
    """Custom type set_point_temperatura based on Integer32"""
    defaultValue = -200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Set_point_temperatura_Type.__name__ = "Integer32"
_Set_point_temperatura_Object = MibScalar
set_point_temperatura = _Set_point_temperatura_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 8),
    _Set_point_temperatura_Type()
)
set_point_temperatura.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_point_temperatura.setStatus("current")
if mibBuilder.loadTexts:
    set_point_temperatura.setUnits("C x10")


class _Temp_fine_sbrin_Type(Integer32):
    """Custom type temp_fine_sbrin based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 300),
    )


_Temp_fine_sbrin_Type.__name__ = "Integer32"
_Temp_fine_sbrin_Object = MibScalar
temp_fine_sbrin = _Temp_fine_sbrin_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 9),
    _Temp_fine_sbrin_Type()
)
temp_fine_sbrin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temp_fine_sbrin.setStatus("current")
if mibBuilder.loadTexts:
    temp_fine_sbrin.setUnits("C x10")


class _Min_assegnaz_consentita_utente_Type(Integer32):
    """Custom type min_assegnaz_consentita_utente based on Integer32"""
    defaultValue = -500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 32767),
    )


_Min_assegnaz_consentita_utente_Type.__name__ = "Integer32"
_Min_assegnaz_consentita_utente_Object = MibScalar
min_assegnaz_consentita_utente = _Min_assegnaz_consentita_utente_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 10),
    _Min_assegnaz_consentita_utente_Type()
)
min_assegnaz_consentita_utente.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    min_assegnaz_consentita_utente.setStatus("current")
if mibBuilder.loadTexts:
    min_assegnaz_consentita_utente.setUnits("C x10")


class _Max_assegnaz_consentita_utente_Type(Integer32):
    """Custom type max_assegnaz_consentita_utente based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 990),
    )


_Max_assegnaz_consentita_utente_Type.__name__ = "Integer32"
_Max_assegnaz_consentita_utente_Object = MibScalar
max_assegnaz_consentita_utente = _Max_assegnaz_consentita_utente_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 11),
    _Max_assegnaz_consentita_utente_Type()
)
max_assegnaz_consentita_utente.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_assegnaz_consentita_utente.setStatus("current")
if mibBuilder.loadTexts:
    max_assegnaz_consentita_utente.setUnits("C x10")


class _Variaz_autom_setpoint_notturno_Type(Integer32):
    """Custom type variaz_autom_setpoint_notturno based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_Variaz_autom_setpoint_notturno_Type.__name__ = "Integer32"
_Variaz_autom_setpoint_notturno_Object = MibScalar
variaz_autom_setpoint_notturno = _Variaz_autom_setpoint_notturno_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 12),
    _Variaz_autom_setpoint_notturno_Type()
)
variaz_autom_setpoint_notturno.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    variaz_autom_setpoint_notturno.setStatus("current")
if mibBuilder.loadTexts:
    variaz_autom_setpoint_notturno.setUnits("C x10")


class _Temperatura_rilev_max_Type(Integer32):
    """Custom type temperatura_rilev_max based on Integer32"""
    defaultValue = -50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Temperatura_rilev_max_Type.__name__ = "Integer32"
_Temperatura_rilev_max_Object = MibScalar
temperatura_rilev_max = _Temperatura_rilev_max_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 13),
    _Temperatura_rilev_max_Type()
)
temperatura_rilev_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatura_rilev_max.setStatus("current")
if mibBuilder.loadTexts:
    temperatura_rilev_max.setUnits("C x10")


class _Temperatura_rilev_min_Type(Integer32):
    """Custom type temperatura_rilev_min based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Temperatura_rilev_min_Type.__name__ = "Integer32"
_Temperatura_rilev_min_Object = MibScalar
temperatura_rilev_min = _Temperatura_rilev_min_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 14),
    _Temperatura_rilev_min_Type()
)
temperatura_rilev_min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatura_rilev_min.setStatus("current")
if mibBuilder.loadTexts:
    temperatura_rilev_min.setUnits("C x10")


class _Differenziale_regolatore_Type(Integer32):
    """Custom type differenziale_regolatore based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1990),
    )


_Differenziale_regolatore_Type.__name__ = "Integer32"
_Differenziale_regolatore_Object = MibScalar
differenziale_regolatore = _Differenziale_regolatore_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 15),
    _Differenziale_regolatore_Type()
)
differenziale_regolatore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    differenziale_regolatore.setStatus("current")
if mibBuilder.loadTexts:
    differenziale_regolatore.setUnits("C x10")


class _Temp_minima_s1_Type(Integer32):
    """Custom type temp_minima_s1 based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 900),
    )


_Temp_minima_s1_Type.__name__ = "Integer32"
_Temp_minima_s1_Object = MibScalar
temp_minima_s1 = _Temp_minima_s1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 16),
    _Temp_minima_s1_Type()
)
temp_minima_s1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temp_minima_s1.setStatus("current")
if mibBuilder.loadTexts:
    temp_minima_s1.setUnits("C x10")


class _Tmp_evap_satura_Type(Integer32):
    """Custom type tmp_evap_satura based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Tmp_evap_satura_Type.__name__ = "Integer32"
_Tmp_evap_satura_Object = MibScalar
tmp_evap_satura = _Tmp_evap_satura_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 18),
    _Tmp_evap_satura_Type()
)
tmp_evap_satura.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp_evap_satura.setStatus("current")
if mibBuilder.loadTexts:
    tmp_evap_satura.setUnits("C x10")


class _Superheat_set_Type(Integer32):
    """Custom type superheat_set based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_Superheat_set_Type.__name__ = "Integer32"
_Superheat_set_Object = MibScalar
superheat_set = _Superheat_set_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 20),
    _Superheat_set_Type()
)
superheat_set.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superheat_set.setStatus("current")
if mibBuilder.loadTexts:
    superheat_set.setUnits("C x10")


class _K_int_Type(Integer32):
    """Custom type k_int based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_K_int_Type.__name__ = "Integer32"
_K_int_Object = MibScalar
k_int = _K_int_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 21),
    _K_int_Type()
)
k_int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    k_int.setStatus("current")
if mibBuilder.loadTexts:
    k_int.setUnits("N/A")


class _Td_int_Type(Integer32):
    """Custom type td_int based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Td_int_Type.__name__ = "Integer32"
_Td_int_Object = MibScalar
td_int = _Td_int_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 22),
    _Td_int_Type()
)
td_int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    td_int.setStatus("current")
if mibBuilder.loadTexts:
    td_int.setUnits("sec. x10")


class _Lim_inf_int_Type(Integer32):
    """Custom type lim_inf_int based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Lim_inf_int_Type.__name__ = "Integer32"
_Lim_inf_int_Object = MibScalar
lim_inf_int = _Lim_inf_int_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 23),
    _Lim_inf_int_Type()
)
lim_inf_int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lim_inf_int.setStatus("current")
if mibBuilder.loadTexts:
    lim_inf_int.setUnits("N/A")


class _Offset_sh_Type(Integer32):
    """Custom type offset_sh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Offset_sh_Type.__name__ = "Integer32"
_Offset_sh_Object = MibScalar
offset_sh = _Offset_sh_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 24),
    _Offset_sh_Type()
)
offset_sh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offset_sh.setStatus("current")
if mibBuilder.loadTexts:
    offset_sh.setUnits("N/A")


class _Sonda_6_Type(Integer32):
    """Custom type sonda_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Sonda_6_Type.__name__ = "Integer32"
_Sonda_6_Object = MibScalar
sonda_6 = _Sonda_6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 61),
    _Sonda_6_Type()
)
sonda_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonda_6.setStatus("current")
if mibBuilder.loadTexts:
    sonda_6.setUnits("C x10")


class _Sonda_7_Type(Integer32):
    """Custom type sonda_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Sonda_7_Type.__name__ = "Integer32"
_Sonda_7_Object = MibScalar
sonda_7 = _Sonda_7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 62),
    _Sonda_7_Type()
)
sonda_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonda_7.setStatus("current")
if mibBuilder.loadTexts:
    sonda_7.setUnits("C x10")


class _Sonda_8_Type(Integer32):
    """Custom type sonda_8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Sonda_8_Type.__name__ = "Integer32"
_Sonda_8_Object = MibScalar
sonda_8 = _Sonda_8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 63),
    _Sonda_8_Type()
)
sonda_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonda_8.setStatus("current")
if mibBuilder.loadTexts:
    sonda_8.setUnits("C x10")


class _Surriscaldamento_Type(Integer32):
    """Custom type surriscaldamento based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_Surriscaldamento_Type.__name__ = "Integer32"
_Surriscaldamento_Object = MibScalar
surriscaldamento = _Surriscaldamento_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 66),
    _Surriscaldamento_Type()
)
surriscaldamento.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    surriscaldamento.setStatus("current")
if mibBuilder.loadTexts:
    surriscaldamento.setUnits("C x10")


class _Tmp_superheat_Type(Integer32):
    """Custom type tmp_superheat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_Tmp_superheat_Type.__name__ = "Integer32"
_Tmp_superheat_Object = MibScalar
tmp_superheat = _Tmp_superheat_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 67),
    _Tmp_superheat_Type()
)
tmp_superheat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmp_superheat.setStatus("current")
if mibBuilder.loadTexts:
    tmp_superheat.setUnits("C x10")
_IntegerObjects_ObjectIdentity = ObjectIdentity
integerObjects = _IntegerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3)
)


class _Id_firm_vers_Type(Integer32):
    """Custom type id_firm_vers based on Integer32"""
    defaultValue = 29

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Id_firm_vers_Type.__name__ = "Integer32"
_Id_firm_vers_Object = MibScalar
id_firm_vers = _Id_firm_vers_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 1),
    _Id_firm_vers_Type()
)
id_firm_vers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    id_firm_vers.setStatus("current")
if mibBuilder.loadTexts:
    id_firm_vers.setUnits("N/A")


class _Stabilita_misura_Type(Integer32):
    """Custom type stabilita_misura based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Stabilita_misura_Type.__name__ = "Integer32"
_Stabilita_misura_Object = MibScalar
stabilita_misura = _Stabilita_misura_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 2),
    _Stabilita_misura_Type()
)
stabilita_misura.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stabilita_misura.setStatus("current")
if mibBuilder.loadTexts:
    stabilita_misura.setUnits("N/A")


class _Sonda_virtuale_Type(Integer32):
    """Custom type sonda_virtuale based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Sonda_virtuale_Type.__name__ = "Integer32"
_Sonda_virtuale_Object = MibScalar
sonda_virtuale = _Sonda_virtuale_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 3),
    _Sonda_virtuale_Type()
)
sonda_virtuale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonda_virtuale.setStatus("current")
if mibBuilder.loadTexts:
    sonda_virtuale.setUnits("N/A")


class _Vis_ripetitore_Type(Integer32):
    """Custom type vis_ripetitore based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Vis_ripetitore_Type.__name__ = "Integer32"
_Vis_ripetitore_Object = MibScalar
vis_ripetitore = _Vis_ripetitore_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 4),
    _Vis_ripetitore_Type()
)
vis_ripetitore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vis_ripetitore.setStatus("current")
if mibBuilder.loadTexts:
    vis_ripetitore.setUnits("N/A")


class _Esiste_sonda_Type(Integer32):
    """Custom type esiste_sonda based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Esiste_sonda_Type.__name__ = "Integer32"
_Esiste_sonda_Object = MibScalar
esiste_sonda = _Esiste_sonda_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 5),
    _Esiste_sonda_Type()
)
esiste_sonda.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiste_sonda.setStatus("current")
if mibBuilder.loadTexts:
    esiste_sonda.setUnits("N/A")


class _Vis_terminale_Type(Integer32):
    """Custom type vis_terminale based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Vis_terminale_Type.__name__ = "Integer32"
_Vis_terminale_Object = MibScalar
vis_terminale = _Vis_terminale_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 6),
    _Vis_terminale_Type()
)
vis_terminale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vis_terminale.setStatus("current")
if mibBuilder.loadTexts:
    vis_terminale.setUnits("N/A")


class _Config_in_digit_1_Type(Integer32):
    """Custom type config_in_digit_1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Config_in_digit_1_Type.__name__ = "Integer32"
_Config_in_digit_1_Object = MibScalar
config_in_digit_1 = _Config_in_digit_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 7),
    _Config_in_digit_1_Type()
)
config_in_digit_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config_in_digit_1.setStatus("current")
if mibBuilder.loadTexts:
    config_in_digit_1.setUnits("N/A")


class _Config_in_digit_2_Type(Integer32):
    """Custom type config_in_digit_2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Config_in_digit_2_Type.__name__ = "Integer32"
_Config_in_digit_2_Object = MibScalar
config_in_digit_2 = _Config_in_digit_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 8),
    _Config_in_digit_2_Type()
)
config_in_digit_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config_in_digit_2.setStatus("current")
if mibBuilder.loadTexts:
    config_in_digit_2.setUnits("N/A")


class _Config_in_digit_3_Type(Integer32):
    """Custom type config_in_digit_3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Config_in_digit_3_Type.__name__ = "Integer32"
_Config_in_digit_3_Object = MibScalar
config_in_digit_3 = _Config_in_digit_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 9),
    _Config_in_digit_3_Type()
)
config_in_digit_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config_in_digit_3.setStatus("current")
if mibBuilder.loadTexts:
    config_in_digit_3.setUnits("N/A")


class _Config_in_digit_4_Type(Integer32):
    """Custom type config_in_digit_4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Config_in_digit_4_Type.__name__ = "Integer32"
_Config_in_digit_4_Object = MibScalar
config_in_digit_4 = _Config_in_digit_4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 10),
    _Config_in_digit_4_Type()
)
config_in_digit_4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config_in_digit_4.setStatus("current")
if mibBuilder.loadTexts:
    config_in_digit_4.setUnits("N/A")


class _Config_in_digit_5_Type(Integer32):
    """Custom type config_in_digit_5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Config_in_digit_5_Type.__name__ = "Integer32"
_Config_in_digit_5_Object = MibScalar
config_in_digit_5 = _Config_in_digit_5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 11),
    _Config_in_digit_5_Type()
)
config_in_digit_5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config_in_digit_5.setStatus("current")
if mibBuilder.loadTexts:
    config_in_digit_5.setUnits("N/A")


class _Time_delay_rilevaz_ingresso_Type(Integer32):
    """Custom type time_delay_rilevaz_ingresso based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_Time_delay_rilevaz_ingresso_Type.__name__ = "Integer32"
_Time_delay_rilevaz_ingresso_Object = MibScalar
time_delay_rilevaz_ingresso = _Time_delay_rilevaz_ingresso_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 12),
    _Time_delay_rilevaz_ingresso_Type()
)
time_delay_rilevaz_ingresso.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_delay_rilevaz_ingresso.setStatus("current")
if mibBuilder.loadTexts:
    time_delay_rilevaz_ingresso.setUnits("min")


class _Config_virt_din_Type(Integer32):
    """Custom type config_virt_din based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Config_virt_din_Type.__name__ = "Integer32"
_Config_virt_din_Object = MibScalar
config_virt_din = _Config_virt_din_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 13),
    _Config_virt_din_Type()
)
config_virt_din.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config_virt_din.setStatus("current")
if mibBuilder.loadTexts:
    config_virt_din.setUnits("N/A")


class _Delay_alrm_temp_Type(Integer32):
    """Custom type delay_alrm_temp based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Delay_alrm_temp_Type.__name__ = "Integer32"
_Delay_alrm_temp_Object = MibScalar
delay_alrm_temp = _Delay_alrm_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 14),
    _Delay_alrm_temp_Type()
)
delay_alrm_temp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_alrm_temp.setStatus("current")
if mibBuilder.loadTexts:
    delay_alrm_temp.setUnits("min")


class _Remote_alarms_dsply_enable_Type(Integer32):
    """Custom type remote_alarms_dsply_enable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Remote_alarms_dsply_enable_Type.__name__ = "Integer32"
_Remote_alarms_dsply_enable_Object = MibScalar
remote_alarms_dsply_enable = _Remote_alarms_dsply_enable_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 15),
    _Remote_alarms_dsply_enable_Type()
)
remote_alarms_dsply_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remote_alarms_dsply_enable.setStatus("current")
if mibBuilder.loadTexts:
    remote_alarms_dsply_enable.setUnits("N/A")


class _Gestione_ventole_Type(Integer32):
    """Custom type gestione_ventole based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Gestione_ventole_Type.__name__ = "Integer32"
_Gestione_ventole_Object = MibScalar
gestione_ventole = _Gestione_ventole_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 16),
    _Gestione_ventole_Type()
)
gestione_ventole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gestione_ventole.setStatus("current")
if mibBuilder.loadTexts:
    gestione_ventole.setUnits("N/A")


class _Ventole_off_se_compr_off_Type(Integer32):
    """Custom type ventole_off_se_compr_off based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ventole_off_se_compr_off_Type.__name__ = "Integer32"
_Ventole_off_se_compr_off_Object = MibScalar
ventole_off_se_compr_off = _Ventole_off_se_compr_off_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 17),
    _Ventole_off_se_compr_off_Type()
)
ventole_off_se_compr_off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ventole_off_se_compr_off.setStatus("current")
if mibBuilder.loadTexts:
    ventole_off_se_compr_off.setUnits("N/A")


class _Ventole_stop_in_sbrin_Type(Integer32):
    """Custom type ventole_stop_in_sbrin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ventole_stop_in_sbrin_Type.__name__ = "Integer32"
_Ventole_stop_in_sbrin_Object = MibScalar
ventole_stop_in_sbrin = _Ventole_stop_in_sbrin_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 18),
    _Ventole_stop_in_sbrin_Type()
)
ventole_stop_in_sbrin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ventole_stop_in_sbrin.setStatus("current")
if mibBuilder.loadTexts:
    ventole_stop_in_sbrin.setUnits("N/A")


class _Time_fermo_post_gocciol_Type(Integer32):
    """Custom type time_fermo_post_gocciol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Time_fermo_post_gocciol_Type.__name__ = "Integer32"
_Time_fermo_post_gocciol_Object = MibScalar
time_fermo_post_gocciol = _Time_fermo_post_gocciol_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 19),
    _Time_fermo_post_gocciol_Type()
)
time_fermo_post_gocciol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_fermo_post_gocciol.setStatus("current")
if mibBuilder.loadTexts:
    time_fermo_post_gocciol.setUnits("min")


class _Address_seriale_Type(Integer32):
    """Custom type address_seriale based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Address_seriale_Type.__name__ = "Integer32"
_Address_seriale_Object = MibScalar
address_seriale = _Address_seriale_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 20),
    _Address_seriale_Type()
)
address_seriale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    address_seriale.setStatus("current")
if mibBuilder.loadTexts:
    address_seriale.setUnits("N/A")


class _En_dis_tasti_ir_Type(Integer32):
    """Custom type en_dis_tasti_ir based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_En_dis_tasti_ir_Type.__name__ = "Integer32"
_En_dis_tasti_ir_Object = MibScalar
en_dis_tasti_ir = _En_dis_tasti_ir_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 21),
    _En_dis_tasti_ir_Type()
)
en_dis_tasti_ir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    en_dis_tasti_ir.setStatus("current")
if mibBuilder.loadTexts:
    en_dis_tasti_ir.setUnits("N/A")


class _Codice_abilit_progr_telec_ir_Type(Integer32):
    """Custom type codice_abilit_progr_telec_ir based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Codice_abilit_progr_telec_ir_Type.__name__ = "Integer32"
_Codice_abilit_progr_telec_ir_Object = MibScalar
codice_abilit_progr_telec_ir = _Codice_abilit_progr_telec_ir_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 22),
    _Codice_abilit_progr_telec_ir_Type()
)
codice_abilit_progr_telec_ir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    codice_abilit_progr_telec_ir.setStatus("current")
if mibBuilder.loadTexts:
    codice_abilit_progr_telec_ir.setUnits("N/A")


class _Loc_on_off_ena_Type(Integer32):
    """Custom type loc_on_off_ena based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Loc_on_off_ena_Type.__name__ = "Integer32"
_Loc_on_off_ena_Object = MibScalar
loc_on_off_ena = _Loc_on_off_ena_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 23),
    _Loc_on_off_ena_Type()
)
loc_on_off_ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loc_on_off_ena.setStatus("current")
if mibBuilder.loadTexts:
    loc_on_off_ena.setUnits("N/A")


class _Lan_on_off_ena_Type(Integer32):
    """Custom type lan_on_off_ena based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lan_on_off_ena_Type.__name__ = "Integer32"
_Lan_on_off_ena_Object = MibScalar
lan_on_off_ena = _Lan_on_off_ena_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 24),
    _Lan_on_off_ena_Type()
)
lan_on_off_ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan_on_off_ena.setStatus("current")
if mibBuilder.loadTexts:
    lan_on_off_ena.setUnits("N/A")


class _Config_out_digit_4_Type(Integer32):
    """Custom type config_out_digit_4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Config_out_digit_4_Type.__name__ = "Integer32"
_Config_out_digit_4_Object = MibScalar
config_out_digit_4 = _Config_out_digit_4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 25),
    _Config_out_digit_4_Type()
)
config_out_digit_4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config_out_digit_4.setStatus("current")
if mibBuilder.loadTexts:
    config_out_digit_4.setUnits("N/A")


class _Config_out_digit_7_Type(Integer32):
    """Custom type config_out_digit_7 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Config_out_digit_7_Type.__name__ = "Integer32"
_Config_out_digit_7_Object = MibScalar
config_out_digit_7 = _Config_out_digit_7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 26),
    _Config_out_digit_7_Type()
)
config_out_digit_7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config_out_digit_7.setStatus("current")
if mibBuilder.loadTexts:
    config_out_digit_7.setUnits("N/A")


class _Local_mode_Type(Integer32):
    """Custom type local_mode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Local_mode_Type.__name__ = "Integer32"
_Local_mode_Object = MibScalar
local_mode = _Local_mode_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 27),
    _Local_mode_Type()
)
local_mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    local_mode.setStatus("current")
if mibBuilder.loadTexts:
    local_mode.setUnits("N/A")


class _Lan_len_Type(Integer32):
    """Custom type lan_len based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Lan_len_Type.__name__ = "Integer32"
_Lan_len_Object = MibScalar
lan_len = _Lan_len_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 28),
    _Lan_len_Type()
)
lan_len.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan_len.setStatus("current")
if mibBuilder.loadTexts:
    lan_len.setUnits("N/A")


class _Delay_start_compressore_Type(Integer32):
    """Custom type delay_start_compressore based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Delay_start_compressore_Type.__name__ = "Integer32"
_Delay_start_compressore_Object = MibScalar
delay_start_compressore = _Delay_start_compressore_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 29),
    _Delay_start_compressore_Type()
)
delay_start_compressore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_start_compressore.setStatus("current")
if mibBuilder.loadTexts:
    delay_start_compressore.setUnits("min")


class _Time_min_tra_acc_compr_Type(Integer32):
    """Custom type time_min_tra_acc_compr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Time_min_tra_acc_compr_Type.__name__ = "Integer32"
_Time_min_tra_acc_compr_Object = MibScalar
time_min_tra_acc_compr = _Time_min_tra_acc_compr_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 30),
    _Time_min_tra_acc_compr_Type()
)
time_min_tra_acc_compr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_min_tra_acc_compr.setStatus("current")
if mibBuilder.loadTexts:
    time_min_tra_acc_compr.setUnits("min")


class _Time_min_compr_off_Type(Integer32):
    """Custom type time_min_compr_off based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Time_min_compr_off_Type.__name__ = "Integer32"
_Time_min_compr_off_Object = MibScalar
time_min_compr_off = _Time_min_compr_off_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 31),
    _Time_min_compr_off_Type()
)
time_min_compr_off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_min_compr_off.setStatus("current")
if mibBuilder.loadTexts:
    time_min_compr_off.setUnits("min")


class _Time_min_compr_on_Type(Integer32):
    """Custom type time_min_compr_on based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Time_min_compr_on_Type.__name__ = "Integer32"
_Time_min_compr_on_Object = MibScalar
time_min_compr_on = _Time_min_compr_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 32),
    _Time_min_compr_on_Type()
)
time_min_compr_on.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_min_compr_on.setStatus("current")
if mibBuilder.loadTexts:
    time_min_compr_on.setUnits("min")


class _Sicurezza_rele_Type(Integer32):
    """Custom type sicurezza_rele based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Sicurezza_rele_Type.__name__ = "Integer32"
_Sicurezza_rele_Object = MibScalar
sicurezza_rele = _Sicurezza_rele_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 33),
    _Sicurezza_rele_Type()
)
sicurezza_rele.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sicurezza_rele.setStatus("current")
if mibBuilder.loadTexts:
    sicurezza_rele.setUnits("min")


class _Time_escl_alrm_dopo_ciclo_cont_Type(Integer32):
    """Custom type time_escl_alrm_dopo_ciclo_cont based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Time_escl_alrm_dopo_ciclo_cont_Type.__name__ = "Integer32"
_Time_escl_alrm_dopo_ciclo_cont_Object = MibScalar
time_escl_alrm_dopo_ciclo_cont = _Time_escl_alrm_dopo_ciclo_cont_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 34),
    _Time_escl_alrm_dopo_ciclo_cont_Type()
)
time_escl_alrm_dopo_ciclo_cont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_escl_alrm_dopo_ciclo_cont.setStatus("current")
if mibBuilder.loadTexts:
    time_escl_alrm_dopo_ciclo_cont.setUnits("hours")


class _Delay_start_valve_comp_Type(Integer32):
    """Custom type delay_start_valve_comp based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Delay_start_valve_comp_Type.__name__ = "Integer32"
_Delay_start_valve_comp_Object = MibScalar
delay_start_valve_comp = _Delay_start_valve_comp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 35),
    _Delay_start_valve_comp_Type()
)
delay_start_valve_comp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_start_valve_comp.setStatus("current")
if mibBuilder.loadTexts:
    delay_start_valve_comp.setUnits("sec")


class _Durata_ciclo_continuo_Type(Integer32):
    """Custom type durata_ciclo_continuo based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Durata_ciclo_continuo_Type.__name__ = "Integer32"
_Durata_ciclo_continuo_Object = MibScalar
durata_ciclo_continuo = _Durata_ciclo_continuo_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 36),
    _Durata_ciclo_continuo_Type()
)
durata_ciclo_continuo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    durata_ciclo_continuo.setStatus("current")
if mibBuilder.loadTexts:
    durata_ciclo_continuo.setUnits("hours")


class _Tipo_sbrinamento_Type(Integer32):
    """Custom type tipo_sbrinamento based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Tipo_sbrinamento_Type.__name__ = "Integer32"
_Tipo_sbrinamento_Object = MibScalar
tipo_sbrinamento = _Tipo_sbrinamento_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 37),
    _Tipo_sbrinamento_Type()
)
tipo_sbrinamento.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tipo_sbrinamento.setStatus("current")
if mibBuilder.loadTexts:
    tipo_sbrinamento.setUnits("N/A")


class _Defrost_cmd_Type(Integer32):
    """Custom type defrost_cmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Defrost_cmd_Type.__name__ = "Integer32"
_Defrost_cmd_Object = MibScalar
defrost_cmd = _Defrost_cmd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 38),
    _Defrost_cmd_Type()
)
defrost_cmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_cmd.setStatus("current")
if mibBuilder.loadTexts:
    defrost_cmd.setUnits("N/A")


class _Threshold_val_comp_run_def_Type(Integer32):
    """Custom type threshold_val_comp_run_def based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Threshold_val_comp_run_def_Type.__name__ = "Integer32"
_Threshold_val_comp_run_def_Object = MibScalar
threshold_val_comp_run_def = _Threshold_val_comp_run_def_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 39),
    _Threshold_val_comp_run_def_Type()
)
threshold_val_comp_run_def.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threshold_val_comp_run_def.setStatus("current")
if mibBuilder.loadTexts:
    threshold_val_comp_run_def.setUnits("hours")


class _Sbrin_se_ast_da_off_ad_on_Type(Integer32):
    """Custom type sbrin_se_ast_da_off_ad_on based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sbrin_se_ast_da_off_ad_on_Type.__name__ = "Integer32"
_Sbrin_se_ast_da_off_ad_on_Object = MibScalar
sbrin_se_ast_da_off_ad_on = _Sbrin_se_ast_da_off_ad_on_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 40),
    _Sbrin_se_ast_da_off_ad_on_Type()
)
sbrin_se_ast_da_off_ad_on.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbrin_se_ast_da_off_ad_on.setStatus("current")
if mibBuilder.loadTexts:
    sbrin_se_ast_da_off_ad_on.setUnits("N/A")


class _Delay_sbrin_astoffon_o_digin_Type(Integer32):
    """Custom type delay_sbrin_astoffon_o_digin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_Delay_sbrin_astoffon_o_digin_Type.__name__ = "Integer32"
_Delay_sbrin_astoffon_o_digin_Object = MibScalar
delay_sbrin_astoffon_o_digin = _Delay_sbrin_astoffon_o_digin_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 41),
    _Delay_sbrin_astoffon_o_digin_Type()
)
delay_sbrin_astoffon_o_digin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_sbrin_astoffon_o_digin.setStatus("current")
if mibBuilder.loadTexts:
    delay_sbrin_astoffon_o_digin.setUnits("min")


class _Stop_vis_in_sbrin_Type(Integer32):
    """Custom type stop_vis_in_sbrin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Stop_vis_in_sbrin_Type.__name__ = "Integer32"
_Stop_vis_in_sbrin_Object = MibScalar
stop_vis_in_sbrin = _Stop_vis_in_sbrin_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 42),
    _Stop_vis_in_sbrin_Type()
)
stop_vis_in_sbrin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stop_vis_in_sbrin.setStatus("current")
if mibBuilder.loadTexts:
    stop_vis_in_sbrin.setUnits("N/A")


class _Skip_defrost_enable_Type(Integer32):
    """Custom type skip_defrost_enable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Skip_defrost_enable_Type.__name__ = "Integer32"
_Skip_defrost_enable_Object = MibScalar
skip_defrost_enable = _Skip_defrost_enable_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 43),
    _Skip_defrost_enable_Type()
)
skip_defrost_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skip_defrost_enable.setStatus("current")
if mibBuilder.loadTexts:
    skip_defrost_enable.setUnits("N/A")


class _Time_escl_alrm_dopo_sbrin_Type(Integer32):
    """Custom type time_escl_alrm_dopo_sbrin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Time_escl_alrm_dopo_sbrin_Type.__name__ = "Integer32"
_Time_escl_alrm_dopo_sbrin_Object = MibScalar
time_escl_alrm_dopo_sbrin = _Time_escl_alrm_dopo_sbrin_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 44),
    _Time_escl_alrm_dopo_sbrin_Type()
)
time_escl_alrm_dopo_sbrin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_escl_alrm_dopo_sbrin.setStatus("current")
if mibBuilder.loadTexts:
    time_escl_alrm_dopo_sbrin.setUnits("hours")


class _Priority_sbrin_su_protez_compr_Type(Integer32):
    """Custom type priority_sbrin_su_protez_compr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Priority_sbrin_su_protez_compr_Type.__name__ = "Integer32"
_Priority_sbrin_su_protez_compr_Object = MibScalar
priority_sbrin_su_protez_compr = _Priority_sbrin_su_protez_compr_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 45),
    _Priority_sbrin_su_protez_compr_Type()
)
priority_sbrin_su_protez_compr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority_sbrin_su_protez_compr.setStatus("current")
if mibBuilder.loadTexts:
    priority_sbrin_su_protez_compr.setUnits("flag")


class _Intervallo_tra_sbrin_Type(Integer32):
    """Custom type intervallo_tra_sbrin based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_Intervallo_tra_sbrin_Type.__name__ = "Integer32"
_Intervallo_tra_sbrin_Object = MibScalar
intervallo_tra_sbrin = _Intervallo_tra_sbrin_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 46),
    _Intervallo_tra_sbrin_Type()
)
intervallo_tra_sbrin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intervallo_tra_sbrin.setStatus("current")
if mibBuilder.loadTexts:
    intervallo_tra_sbrin.setUnits("hours")


class _Intervallo_tra_pulizie_Type(Integer32):
    """Custom type intervallo_tra_pulizie based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_Intervallo_tra_pulizie_Type.__name__ = "Integer32"
_Intervallo_tra_pulizie_Object = MibScalar
intervallo_tra_pulizie = _Intervallo_tra_pulizie_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 47),
    _Intervallo_tra_pulizie_Type()
)
intervallo_tra_pulizie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intervallo_tra_pulizie.setStatus("current")
if mibBuilder.loadTexts:
    intervallo_tra_pulizie.setUnits("hours")


class _Max_durata_sbrin_Type(Integer32):
    """Custom type max_durata_sbrin based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_Max_durata_sbrin_Type.__name__ = "Integer32"
_Max_durata_sbrin_Object = MibScalar
max_durata_sbrin = _Max_durata_sbrin_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 48),
    _Max_durata_sbrin_Type()
)
max_durata_sbrin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_durata_sbrin.setStatus("current")
if mibBuilder.loadTexts:
    max_durata_sbrin.setUnits("min")


class _Time_gocciol_dopo_sbrin_Type(Integer32):
    """Custom type time_gocciol_dopo_sbrin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Time_gocciol_dopo_sbrin_Type.__name__ = "Integer32"
_Time_gocciol_dopo_sbrin_Object = MibScalar
time_gocciol_dopo_sbrin = _Time_gocciol_dopo_sbrin_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 49),
    _Time_gocciol_dopo_sbrin_Type()
)
time_gocciol_dopo_sbrin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_gocciol_dopo_sbrin.setStatus("current")
if mibBuilder.loadTexts:
    time_gocciol_dopo_sbrin.setUnits("min")


class _Intervallo_rilev_temp_maxmin_Type(Integer32):
    """Custom type intervallo_rilev_temp_maxmin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Intervallo_rilev_temp_maxmin_Type.__name__ = "Integer32"
_Intervallo_rilev_temp_maxmin_Object = MibScalar
intervallo_rilev_temp_maxmin = _Intervallo_rilev_temp_maxmin_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 50),
    _Intervallo_rilev_temp_maxmin_Type()
)
intervallo_rilev_temp_maxmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervallo_rilev_temp_maxmin.setStatus("current")
if mibBuilder.loadTexts:
    intervallo_rilev_temp_maxmin.setUnits("hours")


class _Stn_Type(Integer32):
    """Custom type stn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Stn_Type.__name__ = "Integer32"
_Stn_Object = MibScalar
stn = _Stn_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 51),
    _Stn_Type()
)
stn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stn.setStatus("current")
if mibBuilder.loadTexts:
    stn.setUnits("N/A")


class _Durata_pulizia_Type(Integer32):
    """Custom type durata_pulizia based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Durata_pulizia_Type.__name__ = "Integer32"
_Durata_pulizia_Object = MibScalar
durata_pulizia = _Durata_pulizia_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 52),
    _Durata_pulizia_Type()
)
durata_pulizia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    durata_pulizia.setStatus("current")
if mibBuilder.loadTexts:
    durata_pulizia.setUnits("min")


class _Par_ora1_Type(Integer32):
    """Custom type par_ora1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Par_ora1_Type.__name__ = "Integer32"
_Par_ora1_Object = MibScalar
par_ora1 = _Par_ora1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 53),
    _Par_ora1_Type()
)
par_ora1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    par_ora1.setStatus("current")
if mibBuilder.loadTexts:
    par_ora1.setUnits("hours")


class _Par_ora2_Type(Integer32):
    """Custom type par_ora2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Par_ora2_Type.__name__ = "Integer32"
_Par_ora2_Object = MibScalar
par_ora2 = _Par_ora2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 54),
    _Par_ora2_Type()
)
par_ora2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    par_ora2.setStatus("current")
if mibBuilder.loadTexts:
    par_ora2.setUnits("hours")


class _Manual_position_Type(Integer32):
    """Custom type manual_position based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_Manual_position_Type.__name__ = "Integer32"
_Manual_position_Object = MibScalar
manual_position = _Manual_position_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 55),
    _Manual_position_Type()
)
manual_position.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manual_position.setStatus("current")
if mibBuilder.loadTexts:
    manual_position.setUnits("N/A")


class _Posizione_valvola_perc_Type(Integer32):
    """Custom type posizione_valvola_perc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Posizione_valvola_perc_Type.__name__ = "Integer32"
_Posizione_valvola_perc_Object = MibScalar
posizione_valvola_perc = _Posizione_valvola_perc_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 56),
    _Posizione_valvola_perc_Type()
)
posizione_valvola_perc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posizione_valvola_perc.setStatus("current")
if mibBuilder.loadTexts:
    posizione_valvola_perc.setUnits("%")


class _Modello_valvola_Type(Integer32):
    """Custom type modello_valvola based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Modello_valvola_Type.__name__ = "Integer32"
_Modello_valvola_Object = MibScalar
modello_valvola = _Modello_valvola_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 57),
    _Modello_valvola_Type()
)
modello_valvola.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modello_valvola.setStatus("current")
if mibBuilder.loadTexts:
    modello_valvola.setUnits("N/A")


class _Ti_int_Type(Integer32):
    """Custom type ti_int based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Ti_int_Type.__name__ = "Integer32"
_Ti_int_Object = MibScalar
ti_int = _Ti_int_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 58),
    _Ti_int_Type()
)
ti_int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ti_int.setStatus("current")
if mibBuilder.loadTexts:
    ti_int.setUnits("N/A")


class _Ti_low_Type(Integer32):
    """Custom type ti_low based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ti_low_Type.__name__ = "Integer32"
_Ti_low_Object = MibScalar
ti_low = _Ti_low_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 59),
    _Ti_low_Type()
)
ti_low.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ti_low.setStatus("current")
if mibBuilder.loadTexts:
    ti_low.setUnits("sec/10")


class _Tipogas_Type(Integer32):
    """Custom type tipogas based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Tipogas_Type.__name__ = "Integer32"
_Tipogas_Object = MibScalar
tipogas = _Tipogas_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 60),
    _Tipogas_Type()
)
tipogas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tipogas.setStatus("current")
if mibBuilder.loadTexts:
    tipogas.setUnits("N/A")


class _Delay_pressure_probe_alarm_Type(Integer32):
    """Custom type delay_pressure_probe_alarm based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Delay_pressure_probe_alarm_Type.__name__ = "Integer32"
_Delay_pressure_probe_alarm_Object = MibScalar
delay_pressure_probe_alarm = _Delay_pressure_probe_alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 61),
    _Delay_pressure_probe_alarm_Type()
)
delay_pressure_probe_alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delay_pressure_probe_alarm.setStatus("current")
if mibBuilder.loadTexts:
    delay_pressure_probe_alarm.setUnits("min")


class _Tipo_sonda_eva_Type(Integer32):
    """Custom type tipo_sonda_eva based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Tipo_sonda_eva_Type.__name__ = "Integer32"
_Tipo_sonda_eva_Object = MibScalar
tipo_sonda_eva = _Tipo_sonda_eva_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 62),
    _Tipo_sonda_eva_Type()
)
tipo_sonda_eva.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tipo_sonda_eva.setStatus("current")
if mibBuilder.loadTexts:
    tipo_sonda_eva.setUnits("N/A")


class _Cmp_start_valve_position_Type(Integer32):
    """Custom type cmp_start_valve_position based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_Cmp_start_valve_position_Type.__name__ = "Integer32"
_Cmp_start_valve_position_Object = MibScalar
cmp_start_valve_position = _Cmp_start_valve_position_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 64),
    _Cmp_start_valve_position_Type()
)
cmp_start_valve_position.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmp_start_valve_position.setStatus("current")
if mibBuilder.loadTexts:
    cmp_start_valve_position.setUnits("N/A")


class _Dd_1_Type(Integer32):
    """Custom type dd_1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dd_1_Type.__name__ = "Integer32"
_Dd_1_Object = MibScalar
dd_1 = _Dd_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 65),
    _Dd_1_Type()
)
dd_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dd_1.setStatus("current")
if mibBuilder.loadTexts:
    dd_1.setUnits("days")


class _Hh_1_Type(Integer32):
    """Custom type hh_1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh_1_Type.__name__ = "Integer32"
_Hh_1_Object = MibScalar
hh_1 = _Hh_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 66),
    _Hh_1_Type()
)
hh_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh_1.setStatus("current")
if mibBuilder.loadTexts:
    hh_1.setUnits("hours")


class _Mm_1_Type(Integer32):
    """Custom type mm_1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Mm_1_Type.__name__ = "Integer32"
_Mm_1_Object = MibScalar
mm_1 = _Mm_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 67),
    _Mm_1_Type()
)
mm_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mm_1.setStatus("current")
if mibBuilder.loadTexts:
    mm_1.setUnits("min")


class _Dd_2_Type(Integer32):
    """Custom type dd_2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dd_2_Type.__name__ = "Integer32"
_Dd_2_Object = MibScalar
dd_2 = _Dd_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 68),
    _Dd_2_Type()
)
dd_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dd_2.setStatus("current")
if mibBuilder.loadTexts:
    dd_2.setUnits("days")


class _Hh_2_Type(Integer32):
    """Custom type hh_2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh_2_Type.__name__ = "Integer32"
_Hh_2_Object = MibScalar
hh_2 = _Hh_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 69),
    _Hh_2_Type()
)
hh_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh_2.setStatus("current")
if mibBuilder.loadTexts:
    hh_2.setUnits("hours")


class _Mm_2_Type(Integer32):
    """Custom type mm_2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Mm_2_Type.__name__ = "Integer32"
_Mm_2_Object = MibScalar
mm_2 = _Mm_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 70),
    _Mm_2_Type()
)
mm_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mm_2.setStatus("current")
if mibBuilder.loadTexts:
    mm_2.setUnits("min")


class _Dd_3_Type(Integer32):
    """Custom type dd_3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dd_3_Type.__name__ = "Integer32"
_Dd_3_Object = MibScalar
dd_3 = _Dd_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 71),
    _Dd_3_Type()
)
dd_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dd_3.setStatus("current")
if mibBuilder.loadTexts:
    dd_3.setUnits("days")


class _Hh_3_Type(Integer32):
    """Custom type hh_3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh_3_Type.__name__ = "Integer32"
_Hh_3_Object = MibScalar
hh_3 = _Hh_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 72),
    _Hh_3_Type()
)
hh_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh_3.setStatus("current")
if mibBuilder.loadTexts:
    hh_3.setUnits("hours")


class _Mm_3_Type(Integer32):
    """Custom type mm_3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Mm_3_Type.__name__ = "Integer32"
_Mm_3_Object = MibScalar
mm_3 = _Mm_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 73),
    _Mm_3_Type()
)
mm_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mm_3.setStatus("current")
if mibBuilder.loadTexts:
    mm_3.setUnits("min")


class _Dd_4_Type(Integer32):
    """Custom type dd_4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dd_4_Type.__name__ = "Integer32"
_Dd_4_Object = MibScalar
dd_4 = _Dd_4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 74),
    _Dd_4_Type()
)
dd_4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dd_4.setStatus("current")
if mibBuilder.loadTexts:
    dd_4.setUnits("days")


class _Hh_4_Type(Integer32):
    """Custom type hh_4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh_4_Type.__name__ = "Integer32"
_Hh_4_Object = MibScalar
hh_4 = _Hh_4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 75),
    _Hh_4_Type()
)
hh_4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh_4.setStatus("current")
if mibBuilder.loadTexts:
    hh_4.setUnits("hours")


class _Mm_4_Type(Integer32):
    """Custom type mm_4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Mm_4_Type.__name__ = "Integer32"
_Mm_4_Object = MibScalar
mm_4 = _Mm_4_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 76),
    _Mm_4_Type()
)
mm_4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mm_4.setStatus("current")
if mibBuilder.loadTexts:
    mm_4.setUnits("min")


class _Dd_5_Type(Integer32):
    """Custom type dd_5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dd_5_Type.__name__ = "Integer32"
_Dd_5_Object = MibScalar
dd_5 = _Dd_5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 77),
    _Dd_5_Type()
)
dd_5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dd_5.setStatus("current")
if mibBuilder.loadTexts:
    dd_5.setUnits("days")


class _Hh_5_Type(Integer32):
    """Custom type hh_5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh_5_Type.__name__ = "Integer32"
_Hh_5_Object = MibScalar
hh_5 = _Hh_5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 78),
    _Hh_5_Type()
)
hh_5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh_5.setStatus("current")
if mibBuilder.loadTexts:
    hh_5.setUnits("hours")


class _Mm_5_Type(Integer32):
    """Custom type mm_5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Mm_5_Type.__name__ = "Integer32"
_Mm_5_Object = MibScalar
mm_5 = _Mm_5_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 79),
    _Mm_5_Type()
)
mm_5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mm_5.setStatus("current")
if mibBuilder.loadTexts:
    mm_5.setUnits("min")


class _Dd_6_Type(Integer32):
    """Custom type dd_6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dd_6_Type.__name__ = "Integer32"
_Dd_6_Object = MibScalar
dd_6 = _Dd_6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 80),
    _Dd_6_Type()
)
dd_6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dd_6.setStatus("current")
if mibBuilder.loadTexts:
    dd_6.setUnits("days")


class _Hh_6_Type(Integer32):
    """Custom type hh_6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh_6_Type.__name__ = "Integer32"
_Hh_6_Object = MibScalar
hh_6 = _Hh_6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 81),
    _Hh_6_Type()
)
hh_6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh_6.setStatus("current")
if mibBuilder.loadTexts:
    hh_6.setUnits("hours")


class _Mm_6_Type(Integer32):
    """Custom type mm_6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Mm_6_Type.__name__ = "Integer32"
_Mm_6_Object = MibScalar
mm_6 = _Mm_6_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 82),
    _Mm_6_Type()
)
mm_6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mm_6.setStatus("current")
if mibBuilder.loadTexts:
    mm_6.setUnits("min")


class _Dd_7_Type(Integer32):
    """Custom type dd_7 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dd_7_Type.__name__ = "Integer32"
_Dd_7_Object = MibScalar
dd_7 = _Dd_7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 83),
    _Dd_7_Type()
)
dd_7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dd_7.setStatus("current")
if mibBuilder.loadTexts:
    dd_7.setUnits("days")


class _Hh_7_Type(Integer32):
    """Custom type hh_7 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh_7_Type.__name__ = "Integer32"
_Hh_7_Object = MibScalar
hh_7 = _Hh_7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 84),
    _Hh_7_Type()
)
hh_7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh_7.setStatus("current")
if mibBuilder.loadTexts:
    hh_7.setUnits("hours")


class _Mm_7_Type(Integer32):
    """Custom type mm_7 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Mm_7_Type.__name__ = "Integer32"
_Mm_7_Object = MibScalar
mm_7 = _Mm_7_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 85),
    _Mm_7_Type()
)
mm_7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mm_7.setStatus("current")
if mibBuilder.loadTexts:
    mm_7.setUnits("min")


class _Dd_8_Type(Integer32):
    """Custom type dd_8 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dd_8_Type.__name__ = "Integer32"
_Dd_8_Object = MibScalar
dd_8 = _Dd_8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 86),
    _Dd_8_Type()
)
dd_8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dd_8.setStatus("current")
if mibBuilder.loadTexts:
    dd_8.setUnits("days")


class _Hh_8_Type(Integer32):
    """Custom type hh_8 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh_8_Type.__name__ = "Integer32"
_Hh_8_Object = MibScalar
hh_8 = _Hh_8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 87),
    _Hh_8_Type()
)
hh_8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh_8.setStatus("current")
if mibBuilder.loadTexts:
    hh_8.setUnits("hours")


class _Mm_8_Type(Integer32):
    """Custom type mm_8 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Mm_8_Type.__name__ = "Integer32"
_Mm_8_Object = MibScalar
mm_8 = _Mm_8_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 88),
    _Mm_8_Type()
)
mm_8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mm_8.setStatus("current")
if mibBuilder.loadTexts:
    mm_8.setUnits("min")


class _Pos_uscita_pid_Type(Integer32):
    """Custom type pos_uscita_pid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_Pos_uscita_pid_Type.__name__ = "Integer32"
_Pos_uscita_pid_Object = MibScalar
pos_uscita_pid = _Pos_uscita_pid_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 123),
    _Pos_uscita_pid_Type()
)
pos_uscita_pid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos_uscita_pid.setStatus("current")
if mibBuilder.loadTexts:
    pos_uscita_pid.setUnits("N/A")


class _Posizione_valvola_Type(Integer32):
    """Custom type posizione_valvola based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_Posizione_valvola_Type.__name__ = "Integer32"
_Posizione_valvola_Object = MibScalar
posizione_valvola = _Posizione_valvola_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 124),
    _Posizione_valvola_Type()
)
posizione_valvola.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posizione_valvola.setStatus("current")
if mibBuilder.loadTexts:
    posizione_valvola.setUnits("N/A")


class _Pst_superheat_Type(Integer32):
    """Custom type pst_superheat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_Pst_superheat_Type.__name__ = "Integer32"
_Pst_superheat_Object = MibScalar
pst_superheat = _Pst_superheat_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 125),
    _Pst_superheat_Type()
)
pst_superheat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pst_superheat.setStatus("current")
if mibBuilder.loadTexts:
    pst_superheat.setUnits("barg/100")


class _Dd_s_Type(Integer32):
    """Custom type dd_s based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Dd_s_Type.__name__ = "Integer32"
_Dd_s_Object = MibScalar
dd_s = _Dd_s_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 126),
    _Dd_s_Type()
)
dd_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dd_s.setStatus("current")
if mibBuilder.loadTexts:
    dd_s.setUnits("day")


class _Hh_s_Type(Integer32):
    """Custom type hh_s based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh_s_Type.__name__ = "Integer32"
_Hh_s_Object = MibScalar
hh_s = _Hh_s_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 127),
    _Hh_s_Type()
)
hh_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh_s.setStatus("current")
if mibBuilder.loadTexts:
    hh_s.setUnits("hours")


class _Mm_s_Type(Integer32):
    """Custom type mm_s based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Mm_s_Type.__name__ = "Integer32"
_Mm_s_Object = MibScalar
mm_s = _Mm_s_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 128),
    _Mm_s_Type()
)
mm_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mm_s.setStatus("current")
if mibBuilder.loadTexts:
    mm_s.setUnits("min")


class _Config_out_digit_9_Type(Integer32):
    """Custom type config_out_digit_9 based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Config_out_digit_9_Type.__name__ = "Integer32"
_Config_out_digit_9_Object = MibScalar
config_out_digit_9 = _Config_out_digit_9_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 1008),
    _Config_out_digit_9_Type()
)
config_out_digit_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    config_out_digit_9.setStatus("current")
if mibBuilder.loadTexts:
    config_out_digit_9.setUnits("N/A")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAREL-mastercase-MIB",
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
       "mastercaseMIB": mastercaseMIB,
       "digitalObjects": digitalObjects,
       "on_off_status": on_off_status,
       "en_dec_point": en_dec_point,
       "defrost_con_sonda_3": defrost_con_sonda_3,
       "enable_ed_alarm": enable_ed_alarm,
       "enable_monitor_temp_maxmin": enable_monitor_temp_maxmin,
       "regol_notturna_sonda_3": regol_notturna_sonda_3,
       "disable_pid": disable_pid,
       "en_exenq_5": en_exenq_5,
       "pressure_probe_from_master": pressure_probe_from_master,
       "all_alta_temp": all_alta_temp,
       "all_bassa_temp": all_bassa_temp,
       "all_clean_management": all_clean_management,
       "all_def_tout": all_def_tout,
       "all_driver_lan": all_driver_lan,
       "all_driver_probe_1": all_driver_probe_1,
       "all_driver_probe_2": all_driver_probe_2,
       "all_duty_set": all_duty_set,
       "all_ext_del": all_ext_del,
       "all_ext_ist": all_ext_ist,
       "all_ha": all_ha,
       "all_hf": all_hf,
       "all_sonda_amb": all_sonda_amb,
       "all_sonda_def": all_sonda_def,
       "all_sonda_prod": all_sonda_prod,
       "all_sonda_reg": all_sonda_reg,
       "all_tem_min_s1": all_tem_min_s1,
       "digital_out_2": digital_out_2,
       "digital_out_4": digital_out_4,
       "digital_out_6": digital_out_6,
       "digital_out_7": digital_out_7,
       "digital_out_8": digital_out_8,
       "digital_out_9": digital_out_9,
       "sl_alm_1": sl_alm_1,
       "sv_mst_defrost_end": sv_mst_defrost_end,
       "sv_mst_defrost_start": sv_mst_defrost_start,
       "sw_door_brk": sw_door_brk,
       "en_high_refresh": en_high_refresh,
       "analogObjects": analogObjects,
       "calibrazione_sonda_3": calibrazione_sonda_3,
       "calibr_sonda_ambiente": calibr_sonda_ambiente,
       "calibrazione_sonda_defrost": calibrazione_sonda_defrost,
       "differenziale_alrm_ventole": differenziale_alrm_ventole,
       "alrm_alta_temp": alrm_alta_temp,
       "alrm_bassa_temp": alrm_bassa_temp,
       "temp_ventole_on": temp_ventole_on,
       "set_point_temperatura": set_point_temperatura,
       "temp_fine_sbrin": temp_fine_sbrin,
       "min_assegnaz_consentita_utente": min_assegnaz_consentita_utente,
       "max_assegnaz_consentita_utente": max_assegnaz_consentita_utente,
       "variaz_autom_setpoint_notturno": variaz_autom_setpoint_notturno,
       "temperatura_rilev_max": temperatura_rilev_max,
       "temperatura_rilev_min": temperatura_rilev_min,
       "differenziale_regolatore": differenziale_regolatore,
       "temp_minima_s1": temp_minima_s1,
       "tmp_evap_satura": tmp_evap_satura,
       "superheat_set": superheat_set,
       "k_int": k_int,
       "td_int": td_int,
       "lim_inf_int": lim_inf_int,
       "offset_sh": offset_sh,
       "sonda_6": sonda_6,
       "sonda_7": sonda_7,
       "sonda_8": sonda_8,
       "surriscaldamento": surriscaldamento,
       "tmp_superheat": tmp_superheat,
       "integerObjects": integerObjects,
       "id_firm_vers": id_firm_vers,
       "stabilita_misura": stabilita_misura,
       "sonda_virtuale": sonda_virtuale,
       "vis_ripetitore": vis_ripetitore,
       "esiste_sonda": esiste_sonda,
       "vis_terminale": vis_terminale,
       "config_in_digit_1": config_in_digit_1,
       "config_in_digit_2": config_in_digit_2,
       "config_in_digit_3": config_in_digit_3,
       "config_in_digit_4": config_in_digit_4,
       "config_in_digit_5": config_in_digit_5,
       "time_delay_rilevaz_ingresso": time_delay_rilevaz_ingresso,
       "config_virt_din": config_virt_din,
       "delay_alrm_temp": delay_alrm_temp,
       "remote_alarms_dsply_enable": remote_alarms_dsply_enable,
       "gestione_ventole": gestione_ventole,
       "ventole_off_se_compr_off": ventole_off_se_compr_off,
       "ventole_stop_in_sbrin": ventole_stop_in_sbrin,
       "time_fermo_post_gocciol": time_fermo_post_gocciol,
       "address_seriale": address_seriale,
       "en_dis_tasti_ir": en_dis_tasti_ir,
       "codice_abilit_progr_telec_ir": codice_abilit_progr_telec_ir,
       "loc_on_off_ena": loc_on_off_ena,
       "lan_on_off_ena": lan_on_off_ena,
       "config_out_digit_4": config_out_digit_4,
       "config_out_digit_7": config_out_digit_7,
       "local_mode": local_mode,
       "lan_len": lan_len,
       "delay_start_compressore": delay_start_compressore,
       "time_min_tra_acc_compr": time_min_tra_acc_compr,
       "time_min_compr_off": time_min_compr_off,
       "time_min_compr_on": time_min_compr_on,
       "sicurezza_rele": sicurezza_rele,
       "time_escl_alrm_dopo_ciclo_cont": time_escl_alrm_dopo_ciclo_cont,
       "delay_start_valve_comp": delay_start_valve_comp,
       "durata_ciclo_continuo": durata_ciclo_continuo,
       "tipo_sbrinamento": tipo_sbrinamento,
       "defrost_cmd": defrost_cmd,
       "threshold_val_comp_run_def": threshold_val_comp_run_def,
       "sbrin_se_ast_da_off_ad_on": sbrin_se_ast_da_off_ad_on,
       "delay_sbrin_astoffon_o_digin": delay_sbrin_astoffon_o_digin,
       "stop_vis_in_sbrin": stop_vis_in_sbrin,
       "skip_defrost_enable": skip_defrost_enable,
       "time_escl_alrm_dopo_sbrin": time_escl_alrm_dopo_sbrin,
       "priority_sbrin_su_protez_compr": priority_sbrin_su_protez_compr,
       "intervallo_tra_sbrin": intervallo_tra_sbrin,
       "intervallo_tra_pulizie": intervallo_tra_pulizie,
       "max_durata_sbrin": max_durata_sbrin,
       "time_gocciol_dopo_sbrin": time_gocciol_dopo_sbrin,
       "intervallo_rilev_temp_maxmin": intervallo_rilev_temp_maxmin,
       "stn": stn,
       "durata_pulizia": durata_pulizia,
       "par_ora1": par_ora1,
       "par_ora2": par_ora2,
       "manual_position": manual_position,
       "posizione_valvola_perc": posizione_valvola_perc,
       "modello_valvola": modello_valvola,
       "ti_int": ti_int,
       "ti_low": ti_low,
       "tipogas": tipogas,
       "delay_pressure_probe_alarm": delay_pressure_probe_alarm,
       "tipo_sonda_eva": tipo_sonda_eva,
       "cmp_start_valve_position": cmp_start_valve_position,
       "dd_1": dd_1,
       "hh_1": hh_1,
       "mm_1": mm_1,
       "dd_2": dd_2,
       "hh_2": hh_2,
       "mm_2": mm_2,
       "dd_3": dd_3,
       "hh_3": hh_3,
       "mm_3": mm_3,
       "dd_4": dd_4,
       "hh_4": hh_4,
       "mm_4": mm_4,
       "dd_5": dd_5,
       "hh_5": hh_5,
       "mm_5": mm_5,
       "dd_6": dd_6,
       "hh_6": hh_6,
       "mm_6": mm_6,
       "dd_7": dd_7,
       "hh_7": hh_7,
       "mm_7": mm_7,
       "dd_8": dd_8,
       "hh_8": hh_8,
       "mm_8": mm_8,
       "pos_uscita_pid": pos_uscita_pid,
       "posizione_valvola": posizione_valvola,
       "pst_superheat": pst_superheat,
       "dd_s": dd_s,
       "hh_s": hh_s,
       "mm_s": mm_s,
       "config_out_digit_9": config_out_digit_9}
)
