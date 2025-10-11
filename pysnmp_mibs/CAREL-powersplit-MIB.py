# SNMP MIB module (CAREL-powersplit-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/carel/CAREL-powersplit-MIB
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

powersplitMIB = ModuleIdentity(
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


class _Cent_fhren_flag_Type(Integer32):
    """Custom type cent_fhren_flag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cent_fhren_flag_Type.__name__ = "Integer32"
_Cent_fhren_flag_Object = MibScalar
cent_fhren_flag = _Cent_fhren_flag_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 1),
    _Cent_fhren_flag_Type()
)
cent_fhren_flag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cent_fhren_flag.setStatus("current")
if mibBuilder.loadTexts:
    cent_fhren_flag.setUnits("N/A")


class _Autoscale_Type(Integer32):
    """Custom type autoscale based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Autoscale_Type.__name__ = "Integer32"
_Autoscale_Object = MibScalar
autoscale = _Autoscale_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 2),
    _Autoscale_Type()
)
autoscale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoscale.setStatus("current")
if mibBuilder.loadTexts:
    autoscale.setUnits("N/A")


class _Defrostprobeselect_Type(Integer32):
    """Custom type defrostprobeselect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Defrostprobeselect_Type.__name__ = "Integer32"
_Defrostprobeselect_Object = MibScalar
defrostprobeselect = _Defrostprobeselect_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 3),
    _Defrostprobeselect_Type()
)
defrostprobeselect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrostprobeselect.setStatus("current")
if mibBuilder.loadTexts:
    defrostprobeselect.setUnits("N/A")


class _Defrost_cmd_Type(Integer32):
    """Custom type defrost_cmd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Defrost_cmd_Type.__name__ = "Integer32"
_Defrost_cmd_Object = MibScalar
defrost_cmd = _Defrost_cmd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 4),
    _Defrost_cmd_Type()
)
defrost_cmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_cmd.setStatus("current")
if mibBuilder.loadTexts:
    defrost_cmd.setUnits("flag")


class _Defrost_at_startup_Type(Integer32):
    """Custom type defrost_at_startup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Defrost_at_startup_Type.__name__ = "Integer32"
_Defrost_at_startup_Object = MibScalar
defrost_at_startup = _Defrost_at_startup_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 5),
    _Defrost_at_startup_Type()
)
defrost_at_startup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_at_startup.setStatus("current")
if mibBuilder.loadTexts:
    defrost_at_startup.setUnits("flag")


class _Defrost_show_Type(Integer32):
    """Custom type defrost_show based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Defrost_show_Type.__name__ = "Integer32"
_Defrost_show_Object = MibScalar
defrost_show = _Defrost_show_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 6),
    _Defrost_show_Type()
)
defrost_show.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_show.setStatus("current")
if mibBuilder.loadTexts:
    defrost_show.setUnits("flag")


class _Defrost_priority_Type(Integer32):
    """Custom type defrost_priority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Defrost_priority_Type.__name__ = "Integer32"
_Defrost_priority_Object = MibScalar
defrost_priority = _Defrost_priority_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 7),
    _Defrost_priority_Type()
)
defrost_priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_priority.setStatus("current")
if mibBuilder.loadTexts:
    defrost_priority.setUnits("flag")


class _Fan_cfg_Type(Integer32):
    """Custom type fan_cfg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Fan_cfg_Type.__name__ = "Integer32"
_Fan_cfg_Object = MibScalar
fan_cfg = _Fan_cfg_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 8),
    _Fan_cfg_Type()
)
fan_cfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan_cfg.setStatus("current")
if mibBuilder.loadTexts:
    fan_cfg.setUnits("N/A")


class _Fan_off_ctrl_Type(Integer32):
    """Custom type fan_off_ctrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Fan_off_ctrl_Type.__name__ = "Integer32"
_Fan_off_ctrl_Object = MibScalar
fan_off_ctrl = _Fan_off_ctrl_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 9),
    _Fan_off_ctrl_Type()
)
fan_off_ctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan_off_ctrl.setStatus("current")
if mibBuilder.loadTexts:
    fan_off_ctrl.setUnits("N/A")


class _Fan_defrost_ctrl_Type(Integer32):
    """Custom type fan_defrost_ctrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Fan_defrost_ctrl_Type.__name__ = "Integer32"
_Fan_defrost_ctrl_Object = MibScalar
fan_defrost_ctrl = _Fan_defrost_ctrl_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 10),
    _Fan_defrost_ctrl_Type()
)
fan_defrost_ctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan_defrost_ctrl.setStatus("current")
if mibBuilder.loadTexts:
    fan_defrost_ctrl.setUnits("N/A")


class _Keyb_disabled_Type(Integer32):
    """Custom type keyb_disabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Keyb_disabled_Type.__name__ = "Integer32"
_Keyb_disabled_Object = MibScalar
keyb_disabled = _Keyb_disabled_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 11),
    _Keyb_disabled_Type()
)
keyb_disabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyb_disabled.setStatus("current")
if mibBuilder.loadTexts:
    keyb_disabled.setUnits("N/A")


class _Loc_on_off_ena_Type(Integer32):
    """Custom type loc_on_off_ena based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Loc_on_off_ena_Type.__name__ = "Integer32"
_Loc_on_off_ena_Object = MibScalar
loc_on_off_ena = _Loc_on_off_ena_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 13),
    _Lan_on_off_ena_Type()
)
lan_on_off_ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan_on_off_ena.setStatus("current")
if mibBuilder.loadTexts:
    lan_on_off_ena.setUnits("N/A")


class _Lan_din_Type(Integer32):
    """Custom type lan_din based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lan_din_Type.__name__ = "Integer32"
_Lan_din_Object = MibScalar
lan_din = _Lan_din_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 14),
    _Lan_din_Type()
)
lan_din.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan_din.setStatus("current")
if mibBuilder.loadTexts:
    lan_din.setUnits("N/A")


class _Defrost_tout_alarm_ena_Type(Integer32):
    """Custom type defrost_tout_alarm_ena based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Defrost_tout_alarm_ena_Type.__name__ = "Integer32"
_Defrost_tout_alarm_ena_Object = MibScalar
defrost_tout_alarm_ena = _Defrost_tout_alarm_ena_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 15),
    _Defrost_tout_alarm_ena_Type()
)
defrost_tout_alarm_ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_tout_alarm_ena.setStatus("current")
if mibBuilder.loadTexts:
    defrost_tout_alarm_ena.setUnits("N/A")


class _Minmax_store_enable_Type(Integer32):
    """Custom type minmax_store_enable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Minmax_store_enable_Type.__name__ = "Integer32"
_Minmax_store_enable_Object = MibScalar
minmax_store_enable = _Minmax_store_enable_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 16),
    _Minmax_store_enable_Type()
)
minmax_store_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minmax_store_enable.setStatus("current")
if mibBuilder.loadTexts:
    minmax_store_enable.setUnits("N/A")


class _Night_reg_probe_Type(Integer32):
    """Custom type night_reg_probe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Night_reg_probe_Type.__name__ = "Integer32"
_Night_reg_probe_Object = MibScalar
night_reg_probe = _Night_reg_probe_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 17),
    _Night_reg_probe_Type()
)
night_reg_probe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    night_reg_probe.setStatus("current")
if mibBuilder.loadTexts:
    night_reg_probe.setUnits("N/A")


class _Haccp_reset_Type(Integer32):
    """Custom type haccp_reset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Haccp_reset_Type.__name__ = "Integer32"
_Haccp_reset_Object = MibScalar
haccp_reset = _Haccp_reset_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 18),
    _Haccp_reset_Type()
)
haccp_reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    haccp_reset.setStatus("current")
if mibBuilder.loadTexts:
    haccp_reset.setUnits("N/A")


class _Dig_in_1_Type(Integer32):
    """Custom type dig_in_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dig_in_1_Type.__name__ = "Integer32"
_Dig_in_1_Object = MibScalar
dig_in_1 = _Dig_in_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 29),
    _Dig_in_1_Type()
)
dig_in_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dig_in_1.setStatus("current")
if mibBuilder.loadTexts:
    dig_in_1.setUnits("N/A")


class _Dig_in_2_Type(Integer32):
    """Custom type dig_in_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dig_in_2_Type.__name__ = "Integer32"
_Dig_in_2_Object = MibScalar
dig_in_2 = _Dig_in_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 30),
    _Dig_in_2_Type()
)
dig_in_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dig_in_2.setStatus("current")
if mibBuilder.loadTexts:
    dig_in_2.setUnits("N/A")


class _S_comp_Type(Integer32):
    """Custom type s_comp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_comp_Type.__name__ = "Integer32"
_S_comp_Object = MibScalar
s_comp = _S_comp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 33),
    _S_comp_Type()
)
s_comp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_comp.setStatus("current")
if mibBuilder.loadTexts:
    s_comp.setUnits("N/A")


class _S_fan_Type(Integer32):
    """Custom type s_fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_fan_Type.__name__ = "Integer32"
_S_fan_Object = MibScalar
s_fan = _S_fan_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 34),
    _S_fan_Type()
)
s_fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_fan.setStatus("current")
if mibBuilder.loadTexts:
    s_fan.setUnits("N/A")


class _S_defrost_Type(Integer32):
    """Custom type s_defrost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_defrost_Type.__name__ = "Integer32"
_S_defrost_Object = MibScalar
s_defrost = _S_defrost_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 35),
    _S_defrost_Type()
)
s_defrost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_defrost.setStatus("current")
if mibBuilder.loadTexts:
    s_defrost.setUnits("N/A")


class _S_aux_2_Type(Integer32):
    """Custom type s_aux_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_aux_2_Type.__name__ = "Integer32"
_S_aux_2_Object = MibScalar
s_aux_2 = _S_aux_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 36),
    _S_aux_2_Type()
)
s_aux_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_aux_2.setStatus("current")
if mibBuilder.loadTexts:
    s_aux_2.setUnits("N/A")


class _S_alarm_Type(Integer32):
    """Custom type s_alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_alarm_Type.__name__ = "Integer32"
_S_alarm_Object = MibScalar
s_alarm = _S_alarm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 37),
    _S_alarm_Type()
)
s_alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_alarm.setStatus("current")
if mibBuilder.loadTexts:
    s_alarm.setUnits("N/A")


class _S_light_Type(Integer32):
    """Custom type s_light based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_S_light_Type.__name__ = "Integer32"
_S_light_Object = MibScalar
s_light = _S_light_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 39),
    _S_light_Type()
)
s_light.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s_light.setStatus("current")
if mibBuilder.loadTexts:
    s_light.setUnits("N/A")


class _Dr_supervisor_Type(Integer32):
    """Custom type dr_supervisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dr_supervisor_Type.__name__ = "Integer32"
_Dr_supervisor_Object = MibScalar
dr_supervisor = _Dr_supervisor_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 40),
    _Dr_supervisor_Type()
)
dr_supervisor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dr_supervisor.setStatus("current")
if mibBuilder.loadTexts:
    dr_supervisor.setUnits("N/A")


class _Dr_svendreq_Type(Integer32):
    """Custom type dr_svendreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Dr_svendreq_Type.__name__ = "Integer32"
_Dr_svendreq_Object = MibScalar
dr_svendreq = _Dr_svendreq_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 41),
    _Dr_svendreq_Type()
)
dr_svendreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dr_svendreq.setStatus("current")
if mibBuilder.loadTexts:
    dr_svendreq.setUnits("N/A")


class _A1_e1_Type(Integer32):
    """Custom type a1_e1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A1_e1_Type.__name__ = "Integer32"
_A1_e1_Object = MibScalar
a1_e1 = _A1_e1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 44),
    _A1_e1_Type()
)
a1_e1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1_e1.setStatus("current")
if mibBuilder.loadTexts:
    a1_e1.setUnits("N/A")


class _A1_e2_Type(Integer32):
    """Custom type a1_e2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A1_e2_Type.__name__ = "Integer32"
_A1_e2_Object = MibScalar
a1_e2 = _A1_e2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 45),
    _A1_e2_Type()
)
a1_e2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1_e2.setStatus("current")
if mibBuilder.loadTexts:
    a1_e2.setUnits("N/A")


class _A1_e3_Type(Integer32):
    """Custom type a1_e3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A1_e3_Type.__name__ = "Integer32"
_A1_e3_Object = MibScalar
a1_e3 = _A1_e3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 46),
    _A1_e3_Type()
)
a1_e3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1_e3.setStatus("current")
if mibBuilder.loadTexts:
    a1_e3.setUnits("N/A")


class _A1_ia_Type(Integer32):
    """Custom type a1_ia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A1_ia_Type.__name__ = "Integer32"
_A1_ia_Object = MibScalar
a1_ia = _A1_ia_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 47),
    _A1_ia_Type()
)
a1_ia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1_ia.setStatus("current")
if mibBuilder.loadTexts:
    a1_ia.setUnits("N/A")


class _A1_da_Type(Integer32):
    """Custom type a1_da based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A1_da_Type.__name__ = "Integer32"
_A1_da_Object = MibScalar
a1_da = _A1_da_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 48),
    _A1_da_Type()
)
a1_da.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1_da.setStatus("current")
if mibBuilder.loadTexts:
    a1_da.setUnits("N/A")


class _A1_ea_Type(Integer32):
    """Custom type a1_ea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A1_ea_Type.__name__ = "Integer32"
_A1_ea_Object = MibScalar
a1_ea = _A1_ea_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 49),
    _A1_ea_Type()
)
a1_ea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1_ea.setStatus("current")
if mibBuilder.loadTexts:
    a1_ea.setUnits("N/A")


class _A1_re_Type(Integer32):
    """Custom type a1_re based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A1_re_Type.__name__ = "Integer32"
_A1_re_Object = MibScalar
a1_re = _A1_re_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 50),
    _A1_re_Type()
)
a1_re.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1_re.setStatus("current")
if mibBuilder.loadTexts:
    a1_re.setUnits("N/A")


class _A1_id_Type(Integer32):
    """Custom type a1_id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A1_id_Type.__name__ = "Integer32"
_A1_id_Object = MibScalar
a1_id = _A1_id_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 51),
    _A1_id_Type()
)
a1_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1_id.setStatus("current")
if mibBuilder.loadTexts:
    a1_id.setUnits("N/A")


class _A2_hi_Type(Integer32):
    """Custom type a2_hi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A2_hi_Type.__name__ = "Integer32"
_A2_hi_Object = MibScalar
a2_hi = _A2_hi_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 52),
    _A2_hi_Type()
)
a2_hi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2_hi.setStatus("current")
if mibBuilder.loadTexts:
    a2_hi.setUnits("N/A")


class _A2_lo_Type(Integer32):
    """Custom type a2_lo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A2_lo_Type.__name__ = "Integer32"
_A2_lo_Object = MibScalar
a2_lo = _A2_lo_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 53),
    _A2_lo_Type()
)
a2_lo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2_lo.setStatus("current")
if mibBuilder.loadTexts:
    a2_lo.setUnits("N/A")


class _A2_ha_Type(Integer32):
    """Custom type a2_ha based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A2_ha_Type.__name__ = "Integer32"
_A2_ha_Object = MibScalar
a2_ha = _A2_ha_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 54),
    _A2_ha_Type()
)
a2_ha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2_ha.setStatus("current")
if mibBuilder.loadTexts:
    a2_ha.setUnits("N/A")


class _A2_hf_Type(Integer32):
    """Custom type a2_hf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A2_hf_Type.__name__ = "Integer32"
_A2_hf_Object = MibScalar
a2_hf = _A2_hf_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 55),
    _A2_hf_Type()
)
a2_hf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2_hf.setStatus("current")
if mibBuilder.loadTexts:
    a2_hf.setUnits("N/A")


class _A2_ed_Type(Integer32):
    """Custom type a2_ed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_A2_ed_Type.__name__ = "Integer32"
_A2_ed_Object = MibScalar
a2_ed = _A2_ed_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 1, 56),
    _A2_ed_Type()
)
a2_ed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2_ed.setStatus("current")
if mibBuilder.loadTexts:
    a2_ed.setUnits("N/A")
_AnalogObjects_ObjectIdentity = ObjectIdentity
analogObjects = _AnalogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2)
)


class _Probeoffset_3_Type(Integer32):
    """Custom type probeoffset_3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-199, 199),
    )


_Probeoffset_3_Type.__name__ = "Integer32"
_Probeoffset_3_Object = MibScalar
probeoffset_3 = _Probeoffset_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 1),
    _Probeoffset_3_Type()
)
probeoffset_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeoffset_3.setStatus("current")
if mibBuilder.loadTexts:
    probeoffset_3.setUnits("C/F x10")


class _Probeoffset_1_Type(Integer32):
    """Custom type probeoffset_1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-199, 199),
    )


_Probeoffset_1_Type.__name__ = "Integer32"
_Probeoffset_1_Object = MibScalar
probeoffset_1 = _Probeoffset_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 2),
    _Probeoffset_1_Type()
)
probeoffset_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeoffset_1.setStatus("current")
if mibBuilder.loadTexts:
    probeoffset_1.setUnits("C/F x10")


class _Probeoffset_2_Type(Integer32):
    """Custom type probeoffset_2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-199, 199),
    )


_Probeoffset_2_Type.__name__ = "Integer32"
_Probeoffset_2_Object = MibScalar
probeoffset_2 = _Probeoffset_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 3),
    _Probeoffset_2_Type()
)
probeoffset_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeoffset_2.setStatus("current")
if mibBuilder.loadTexts:
    probeoffset_2.setUnits("C/F x10")


class _Fan_alarm_hyst_Type(Integer32):
    """Custom type fan_alarm_hyst based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_Fan_alarm_hyst_Type.__name__ = "Integer32"
_Fan_alarm_hyst_Object = MibScalar
fan_alarm_hyst = _Fan_alarm_hyst_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 4),
    _Fan_alarm_hyst_Type()
)
fan_alarm_hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan_alarm_hyst.setStatus("current")
if mibBuilder.loadTexts:
    fan_alarm_hyst.setUnits("C/F x10")


class _Alarm_max_delta_Type(Integer32):
    """Custom type alarm_max_delta based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1990),
    )


_Alarm_max_delta_Type.__name__ = "Integer32"
_Alarm_max_delta_Object = MibScalar
alarm_max_delta = _Alarm_max_delta_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 5),
    _Alarm_max_delta_Type()
)
alarm_max_delta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm_max_delta.setStatus("current")
if mibBuilder.loadTexts:
    alarm_max_delta.setUnits("C/F x10")


class _Alarm_min_delta_Type(Integer32):
    """Custom type alarm_min_delta based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1990),
    )


_Alarm_min_delta_Type.__name__ = "Integer32"
_Alarm_min_delta_Object = MibScalar
alarm_min_delta = _Alarm_min_delta_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 6),
    _Alarm_min_delta_Type()
)
alarm_min_delta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm_min_delta.setStatus("current")
if mibBuilder.loadTexts:
    alarm_min_delta.setUnits("C/F x10")


class _Defrost_end_temp_Type(Integer32):
    """Custom type defrost_end_temp based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 199),
    )


_Defrost_end_temp_Type.__name__ = "Integer32"
_Defrost_end_temp_Object = MibScalar
defrost_end_temp = _Defrost_end_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 7),
    _Defrost_end_temp_Type()
)
defrost_end_temp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_end_temp.setStatus("current")
if mibBuilder.loadTexts:
    defrost_end_temp.setUnits("C/F x10")


class _Fan_on_temp_Type(Integer32):
    """Custom type fan_on_temp based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 500),
    )


_Fan_on_temp_Type.__name__ = "Integer32"
_Fan_on_temp_Object = MibScalar
fan_on_temp = _Fan_on_temp_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 8),
    _Fan_on_temp_Type()
)
fan_on_temp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan_on_temp.setStatus("current")
if mibBuilder.loadTexts:
    fan_on_temp.setUnits("C/F x10")


class _Setpoint_min_Type(Integer32):
    """Custom type setpoint_min based on Integer32"""
    defaultValue = -500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 32767),
    )


_Setpoint_min_Type.__name__ = "Integer32"
_Setpoint_min_Object = MibScalar
setpoint_min = _Setpoint_min_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 9),
    _Setpoint_min_Type()
)
setpoint_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_min.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_min.setUnits("C/F x10")


class _Setpoint_max_Type(Integer32):
    """Custom type setpoint_max based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 1990),
    )


_Setpoint_max_Type.__name__ = "Integer32"
_Setpoint_max_Object = MibScalar
setpoint_max = _Setpoint_max_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 10),
    _Setpoint_max_Type()
)
setpoint_max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_max.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_max.setUnits("C/F x10")


class _Setpoint_night_Type(Integer32):
    """Custom type setpoint_night based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_Setpoint_night_Type.__name__ = "Integer32"
_Setpoint_night_Object = MibScalar
setpoint_night = _Setpoint_night_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 11),
    _Setpoint_night_Type()
)
setpoint_night.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint_night.setStatus("current")
if mibBuilder.loadTexts:
    setpoint_night.setUnits("C/F x10")


class _Reghyst_Type(Integer32):
    """Custom type reghyst based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Reghyst_Type.__name__ = "Integer32"
_Reghyst_Object = MibScalar
reghyst = _Reghyst_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 12),
    _Reghyst_Type()
)
reghyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reghyst.setStatus("current")
if mibBuilder.loadTexts:
    reghyst.setUnits("C/F x10")


class _Max_store_value_Type(Integer32):
    """Custom type max_store_value based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Max_store_value_Type.__name__ = "Integer32"
_Max_store_value_Object = MibScalar
max_store_value = _Max_store_value_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 13),
    _Max_store_value_Type()
)
max_store_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    max_store_value.setStatus("current")
if mibBuilder.loadTexts:
    max_store_value.setUnits("C/F x10")


class _Min_store_value_Type(Integer32):
    """Custom type min_store_value based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Min_store_value_Type.__name__ = "Integer32"
_Min_store_value_Object = MibScalar
min_store_value = _Min_store_value_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 14),
    _Min_store_value_Type()
)
min_store_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    min_store_value.setStatus("current")
if mibBuilder.loadTexts:
    min_store_value.setUnits("C/F x10")


class _Setpoint_Type(Integer32):
    """Custom type setpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Setpoint_Type.__name__ = "Integer32"
_Setpoint_Object = MibScalar
setpoint = _Setpoint_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 15),
    _Setpoint_Type()
)
setpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpoint.setStatus("current")
if mibBuilder.loadTexts:
    setpoint.setUnits("C/F x10")


class _Probe_1_Type(Integer32):
    """Custom type probe_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Probe_1_Type.__name__ = "Integer32"
_Probe_1_Object = MibScalar
probe_1 = _Probe_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 26),
    _Probe_1_Type()
)
probe_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probe_1.setStatus("current")
if mibBuilder.loadTexts:
    probe_1.setUnits("C/F x10")


class _Probe_2_Type(Integer32):
    """Custom type probe_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Probe_2_Type.__name__ = "Integer32"
_Probe_2_Object = MibScalar
probe_2 = _Probe_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 27),
    _Probe_2_Type()
)
probe_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probe_2.setStatus("current")
if mibBuilder.loadTexts:
    probe_2.setUnits("C/F x10")


class _Probe_3_Type(Integer32):
    """Custom type probe_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Probe_3_Type.__name__ = "Integer32"
_Probe_3_Object = MibScalar
probe_3 = _Probe_3_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 28),
    _Probe_3_Type()
)
probe_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probe_3.setStatus("current")
if mibBuilder.loadTexts:
    probe_3.setUnits("C/F x10")


class _Probe_virtual_Type(Integer32):
    """Custom type probe_virtual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Probe_virtual_Type.__name__ = "Integer32"
_Probe_virtual_Object = MibScalar
probe_virtual = _Probe_virtual_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 29),
    _Probe_virtual_Type()
)
probe_virtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probe_virtual.setStatus("current")
if mibBuilder.loadTexts:
    probe_virtual.setUnits("C/F x10")


class _Power_supply_voltage_Type(Integer32):
    """Custom type power_supply_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Power_supply_voltage_Type.__name__ = "Integer32"
_Power_supply_voltage_Object = MibScalar
power_supply_voltage = _Power_supply_voltage_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 2, 30),
    _Power_supply_voltage_Type()
)
power_supply_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power_supply_voltage.setStatus("current")
if mibBuilder.loadTexts:
    power_supply_voltage.setUnits("V x10")
_IntegerObjects_ObjectIdentity = ObjectIdentity
integerObjects = _IntegerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3)
)


class _Probe_stability_Type(Integer32):
    """Custom type probe_stability based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Probe_stability_Type.__name__ = "Integer32"
_Probe_stability_Object = MibScalar
probe_stability = _Probe_stability_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 1),
    _Probe_stability_Type()
)
probe_stability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe_stability.setStatus("current")
if mibBuilder.loadTexts:
    probe_stability.setUnits("N/A")


class _Virt_probe_Type(Integer32):
    """Custom type virt_probe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Virt_probe_Type.__name__ = "Integer32"
_Virt_probe_Object = MibScalar
virt_probe = _Virt_probe_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 2),
    _Virt_probe_Type()
)
virt_probe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virt_probe.setStatus("current")
if mibBuilder.loadTexts:
    virt_probe.setUnits("N/A")


class _Showprobe_Type(Integer32):
    """Custom type showprobe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Showprobe_Type.__name__ = "Integer32"
_Showprobe_Object = MibScalar
showprobe = _Showprobe_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 3),
    _Showprobe_Type()
)
showprobe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    showprobe.setStatus("current")
if mibBuilder.loadTexts:
    showprobe.setUnits("N/A")


class _Showprobe_t_Type(Integer32):
    """Custom type showprobe_t based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Showprobe_t_Type.__name__ = "Integer32"
_Showprobe_t_Object = MibScalar
showprobe_t = _Showprobe_t_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 4),
    _Showprobe_t_Type()
)
showprobe_t.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    showprobe_t.setStatus("current")
if mibBuilder.loadTexts:
    showprobe_t.setUnits("N/A")


class _Defrostprobepresence_Type(Integer32):
    """Custom type defrostprobepresence based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Defrostprobepresence_Type.__name__ = "Integer32"
_Defrostprobepresence_Object = MibScalar
defrostprobepresence = _Defrostprobepresence_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 5),
    _Defrostprobepresence_Type()
)
defrostprobepresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrostprobepresence.setStatus("current")
if mibBuilder.loadTexts:
    defrostprobepresence.setUnits("N/A")


class _Dig_in_cfg_1_Type(Integer32):
    """Custom type dig_in_cfg_1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dig_in_cfg_1_Type.__name__ = "Integer32"
_Dig_in_cfg_1_Object = MibScalar
dig_in_cfg_1 = _Dig_in_cfg_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 6),
    _Dig_in_cfg_1_Type()
)
dig_in_cfg_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dig_in_cfg_1.setStatus("current")
if mibBuilder.loadTexts:
    dig_in_cfg_1.setUnits("N/A")


class _Dig_in_cfg_2_Type(Integer32):
    """Custom type dig_in_cfg_2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dig_in_cfg_2_Type.__name__ = "Integer32"
_Dig_in_cfg_2_Object = MibScalar
dig_in_cfg_2 = _Dig_in_cfg_2_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 7),
    _Dig_in_cfg_2_Type()
)
dig_in_cfg_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dig_in_cfg_2.setStatus("current")
if mibBuilder.loadTexts:
    dig_in_cfg_2.setUnits("N/A")


class _Alarm_input_delay_Type(Integer32):
    """Custom type alarm_input_delay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Alarm_input_delay_Type.__name__ = "Integer32"
_Alarm_input_delay_Object = MibScalar
alarm_input_delay = _Alarm_input_delay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 8),
    _Alarm_input_delay_Type()
)
alarm_input_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm_input_delay.setStatus("current")
if mibBuilder.loadTexts:
    alarm_input_delay.setUnits("min")


class _Alarm_delay_Type(Integer32):
    """Custom type alarm_delay based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Alarm_delay_Type.__name__ = "Integer32"
_Alarm_delay_Object = MibScalar
alarm_delay = _Alarm_delay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 9),
    _Alarm_delay_Type()
)
alarm_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm_delay.setStatus("current")
if mibBuilder.loadTexts:
    alarm_delay.setUnits("min")


class _Comp_startup_delay_Type(Integer32):
    """Custom type comp_startup_delay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Comp_startup_delay_Type.__name__ = "Integer32"
_Comp_startup_delay_Object = MibScalar
comp_startup_delay = _Comp_startup_delay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 10),
    _Comp_startup_delay_Type()
)
comp_startup_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comp_startup_delay.setStatus("current")
if mibBuilder.loadTexts:
    comp_startup_delay.setUnits("min.")


class _Comp_s2s_delay_Type(Integer32):
    """Custom type comp_s2s_delay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Comp_s2s_delay_Type.__name__ = "Integer32"
_Comp_s2s_delay_Object = MibScalar
comp_s2s_delay = _Comp_s2s_delay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 11),
    _Comp_s2s_delay_Type()
)
comp_s2s_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comp_s2s_delay.setStatus("current")
if mibBuilder.loadTexts:
    comp_s2s_delay.setUnits("min.")


class _Comp_min_off_time_Type(Integer32):
    """Custom type comp_min_off_time based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Comp_min_off_time_Type.__name__ = "Integer32"
_Comp_min_off_time_Object = MibScalar
comp_min_off_time = _Comp_min_off_time_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 12),
    _Comp_min_off_time_Type()
)
comp_min_off_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comp_min_off_time.setStatus("current")
if mibBuilder.loadTexts:
    comp_min_off_time.setUnits("min.")


class _Comp_min_on_time_Type(Integer32):
    """Custom type comp_min_on_time based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Comp_min_on_time_Type.__name__ = "Integer32"
_Comp_min_on_time_Object = MibScalar
comp_min_on_time = _Comp_min_on_time_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 13),
    _Comp_min_on_time_Type()
)
comp_min_on_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comp_min_on_time.setStatus("current")
if mibBuilder.loadTexts:
    comp_min_on_time.setUnits("min.")


class _Rele_safety_cycle_Type(Integer32):
    """Custom type rele_safety_cycle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Rele_safety_cycle_Type.__name__ = "Integer32"
_Rele_safety_cycle_Object = MibScalar
rele_safety_cycle = _Rele_safety_cycle_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 14),
    _Rele_safety_cycle_Type()
)
rele_safety_cycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rele_safety_cycle.setStatus("current")
if mibBuilder.loadTexts:
    rele_safety_cycle.setUnits("min.")


class _Cc_alarm_delay_Type(Integer32):
    """Custom type cc_alarm_delay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cc_alarm_delay_Type.__name__ = "Integer32"
_Cc_alarm_delay_Object = MibScalar
cc_alarm_delay = _Cc_alarm_delay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 15),
    _Cc_alarm_delay_Type()
)
cc_alarm_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cc_alarm_delay.setStatus("current")
if mibBuilder.loadTexts:
    cc_alarm_delay.setUnits("Hours")


class _Comp_cc_Type(Integer32):
    """Custom type comp_cc based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Comp_cc_Type.__name__ = "Integer32"
_Comp_cc_Object = MibScalar
comp_cc = _Comp_cc_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 16),
    _Comp_cc_Type()
)
comp_cc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comp_cc.setStatus("current")
if mibBuilder.loadTexts:
    comp_cc.setUnits("Hours")


class _Defrost_type_Type(Integer32):
    """Custom type defrost_type based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Defrost_type_Type.__name__ = "Integer32"
_Defrost_type_Object = MibScalar
defrost_type = _Defrost_type_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 17),
    _Defrost_type_Type()
)
defrost_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_type.setStatus("current")
if mibBuilder.loadTexts:
    defrost_type.setUnits("N/A")


class _Defrost_delay_Type(Integer32):
    """Custom type defrost_delay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Defrost_delay_Type.__name__ = "Integer32"
_Defrost_delay_Object = MibScalar
defrost_delay = _Defrost_delay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 18),
    _Defrost_delay_Type()
)
defrost_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_delay.setStatus("current")
if mibBuilder.loadTexts:
    defrost_delay.setUnits("min")


class _Alarm_delay_df_door_Type(Integer32):
    """Custom type alarm_delay_df_door based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Alarm_delay_df_door_Type.__name__ = "Integer32"
_Alarm_delay_df_door_Object = MibScalar
alarm_delay_df_door = _Alarm_delay_df_door_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 19),
    _Alarm_delay_df_door_Type()
)
alarm_delay_df_door.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm_delay_df_door.setStatus("current")
if mibBuilder.loadTexts:
    alarm_delay_df_door.setUnits("ore")


class _Dripping_interval_Type(Integer32):
    """Custom type dripping_interval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dripping_interval_Type.__name__ = "Integer32"
_Dripping_interval_Object = MibScalar
dripping_interval = _Dripping_interval_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 20),
    _Dripping_interval_Type()
)
dripping_interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dripping_interval.setStatus("current")
if mibBuilder.loadTexts:
    dripping_interval.setUnits("min")


class _Defrost_interval_Type(Integer32):
    """Custom type defrost_interval based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Defrost_interval_Type.__name__ = "Integer32"
_Defrost_interval_Object = MibScalar
defrost_interval = _Defrost_interval_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 21),
    _Defrost_interval_Type()
)
defrost_interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_interval.setStatus("current")
if mibBuilder.loadTexts:
    defrost_interval.setUnits("ore")


class _Defrost_max_time_Type(Integer32):
    """Custom type defrost_max_time based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_Defrost_max_time_Type.__name__ = "Integer32"
_Defrost_max_time_Object = MibScalar
defrost_max_time = _Defrost_max_time_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 22),
    _Defrost_max_time_Type()
)
defrost_max_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_max_time.setStatus("current")
if mibBuilder.loadTexts:
    defrost_max_time.setUnits("min")


class _Fan_drip_interval_Type(Integer32):
    """Custom type fan_drip_interval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Fan_drip_interval_Type.__name__ = "Integer32"
_Fan_drip_interval_Object = MibScalar
fan_drip_interval = _Fan_drip_interval_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 23),
    _Fan_drip_interval_Type()
)
fan_drip_interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fan_drip_interval.setStatus("current")
if mibBuilder.loadTexts:
    fan_drip_interval.setUnits("min")


class _Aux1_cfg_Type(Integer32):
    """Custom type aux1_cfg based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Aux1_cfg_Type.__name__ = "Integer32"
_Aux1_cfg_Object = MibScalar
aux1_cfg = _Aux1_cfg_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 24),
    _Aux1_cfg_Type()
)
aux1_cfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aux1_cfg.setStatus("current")
if mibBuilder.loadTexts:
    aux1_cfg.setUnits("N/A")


class _Aux2_cfg_Type(Integer32):
    """Custom type aux2_cfg based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Aux2_cfg_Type.__name__ = "Integer32"
_Aux2_cfg_Object = MibScalar
aux2_cfg = _Aux2_cfg_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 25),
    _Aux2_cfg_Type()
)
aux2_cfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aux2_cfg.setStatus("current")
if mibBuilder.loadTexts:
    aux2_cfg.setUnits("N/A")


class _Light_sens_1_Type(Integer32):
    """Custom type light_sens_1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Light_sens_1_Type.__name__ = "Integer32"
_Light_sens_1_Object = MibScalar
light_sens_1 = _Light_sens_1_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 26),
    _Light_sens_1_Type()
)
light_sens_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    light_sens_1.setStatus("current")
if mibBuilder.loadTexts:
    light_sens_1.setUnits("N/A")


class _Light_timer_Type(Integer32):
    """Custom type light_timer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Light_timer_Type.__name__ = "Integer32"
_Light_timer_Object = MibScalar
light_timer = _Light_timer_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 27),
    _Light_timer_Type()
)
light_timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    light_timer.setStatus("current")
if mibBuilder.loadTexts:
    light_timer.setUnits("min")


class _Minmax_acq_time_Type(Integer32):
    """Custom type minmax_acq_time based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Minmax_acq_time_Type.__name__ = "Integer32"
_Minmax_acq_time_Object = MibScalar
minmax_acq_time = _Minmax_acq_time_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 28),
    _Minmax_acq_time_Type()
)
minmax_acq_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minmax_acq_time.setStatus("current")
if mibBuilder.loadTexts:
    minmax_acq_time.setUnits("ore")


class _Haccp_ha_day_Type(Integer32):
    """Custom type haccp_ha_day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Haccp_ha_day_Type.__name__ = "Integer32"
_Haccp_ha_day_Object = MibScalar
haccp_ha_day = _Haccp_ha_day_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 29),
    _Haccp_ha_day_Type()
)
haccp_ha_day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haccp_ha_day.setStatus("current")
if mibBuilder.loadTexts:
    haccp_ha_day.setUnits("N/A")


class _Haccp_ha_hour_Type(Integer32):
    """Custom type haccp_ha_hour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Haccp_ha_hour_Type.__name__ = "Integer32"
_Haccp_ha_hour_Object = MibScalar
haccp_ha_hour = _Haccp_ha_hour_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 30),
    _Haccp_ha_hour_Type()
)
haccp_ha_hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haccp_ha_hour.setStatus("current")
if mibBuilder.loadTexts:
    haccp_ha_hour.setUnits("ore")


class _Haccp_ha_min_Type(Integer32):
    """Custom type haccp_ha_min based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Haccp_ha_min_Type.__name__ = "Integer32"
_Haccp_ha_min_Object = MibScalar
haccp_ha_min = _Haccp_ha_min_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 31),
    _Haccp_ha_min_Type()
)
haccp_ha_min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haccp_ha_min.setStatus("current")
if mibBuilder.loadTexts:
    haccp_ha_min.setUnits("min.")


class _Haccp_hf_day_Type(Integer32):
    """Custom type haccp_hf_day based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Haccp_hf_day_Type.__name__ = "Integer32"
_Haccp_hf_day_Object = MibScalar
haccp_hf_day = _Haccp_hf_day_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 32),
    _Haccp_hf_day_Type()
)
haccp_hf_day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haccp_hf_day.setStatus("current")
if mibBuilder.loadTexts:
    haccp_hf_day.setUnits("N/A")


class _Haccp_hf_hour_Type(Integer32):
    """Custom type haccp_hf_hour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Haccp_hf_hour_Type.__name__ = "Integer32"
_Haccp_hf_hour_Object = MibScalar
haccp_hf_hour = _Haccp_hf_hour_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 33),
    _Haccp_hf_hour_Type()
)
haccp_hf_hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haccp_hf_hour.setStatus("current")
if mibBuilder.loadTexts:
    haccp_hf_hour.setUnits("ore")


class _Haccp_hf_min_Type(Integer32):
    """Custom type haccp_hf_min based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Haccp_hf_min_Type.__name__ = "Integer32"
_Haccp_hf_min_Object = MibScalar
haccp_hf_min = _Haccp_hf_min_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 34),
    _Haccp_hf_min_Type()
)
haccp_hf_min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haccp_hf_min.setStatus("current")
if mibBuilder.loadTexts:
    haccp_hf_min.setUnits("min.")


class _Haccp_alarm_delay_Type(Integer32):
    """Custom type haccp_alarm_delay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Haccp_alarm_delay_Type.__name__ = "Integer32"
_Haccp_alarm_delay_Object = MibScalar
haccp_alarm_delay = _Haccp_alarm_delay_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 35),
    _Haccp_alarm_delay_Type()
)
haccp_alarm_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    haccp_alarm_delay.setStatus("current")
if mibBuilder.loadTexts:
    haccp_alarm_delay.setUnits("min.")


class _Defrost_t1_dd_Type(Integer32):
    """Custom type defrost_t1_dd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Defrost_t1_dd_Type.__name__ = "Integer32"
_Defrost_t1_dd_Object = MibScalar
defrost_t1_dd = _Defrost_t1_dd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 36),
    _Defrost_t1_dd_Type()
)
defrost_t1_dd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t1_dd.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t1_dd.setUnits("ore")


class _Defrost_t1_hh_Type(Integer32):
    """Custom type defrost_t1_hh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_Defrost_t1_hh_Type.__name__ = "Integer32"
_Defrost_t1_hh_Object = MibScalar
defrost_t1_hh = _Defrost_t1_hh_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 37),
    _Defrost_t1_hh_Type()
)
defrost_t1_hh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defrost_t1_hh.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t1_hh.setUnits("N/A")


class _Defrost_t1_mm_Type(Integer32):
    """Custom type defrost_t1_mm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Defrost_t1_mm_Type.__name__ = "Integer32"
_Defrost_t1_mm_Object = MibScalar
defrost_t1_mm = _Defrost_t1_mm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 38),
    _Defrost_t1_mm_Type()
)
defrost_t1_mm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t1_mm.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t1_mm.setUnits("min.")


class _Defrost_t2_dd_Type(Integer32):
    """Custom type defrost_t2_dd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Defrost_t2_dd_Type.__name__ = "Integer32"
_Defrost_t2_dd_Object = MibScalar
defrost_t2_dd = _Defrost_t2_dd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 39),
    _Defrost_t2_dd_Type()
)
defrost_t2_dd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t2_dd.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t2_dd.setUnits("gg")


class _Defrost_t2_hh_Type(Integer32):
    """Custom type defrost_t2_hh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Defrost_t2_hh_Type.__name__ = "Integer32"
_Defrost_t2_hh_Object = MibScalar
defrost_t2_hh = _Defrost_t2_hh_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 40),
    _Defrost_t2_hh_Type()
)
defrost_t2_hh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t2_hh.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t2_hh.setUnits("ore")


class _Defrost_t2_mm_Type(Integer32):
    """Custom type defrost_t2_mm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Defrost_t2_mm_Type.__name__ = "Integer32"
_Defrost_t2_mm_Object = MibScalar
defrost_t2_mm = _Defrost_t2_mm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 41),
    _Defrost_t2_mm_Type()
)
defrost_t2_mm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t2_mm.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t2_mm.setUnits("min")


class _Defrost_t3_dd_Type(Integer32):
    """Custom type defrost_t3_dd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Defrost_t3_dd_Type.__name__ = "Integer32"
_Defrost_t3_dd_Object = MibScalar
defrost_t3_dd = _Defrost_t3_dd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 42),
    _Defrost_t3_dd_Type()
)
defrost_t3_dd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t3_dd.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t3_dd.setUnits("gg")


class _Defrost_t3_hh_Type(Integer32):
    """Custom type defrost_t3_hh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Defrost_t3_hh_Type.__name__ = "Integer32"
_Defrost_t3_hh_Object = MibScalar
defrost_t3_hh = _Defrost_t3_hh_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 43),
    _Defrost_t3_hh_Type()
)
defrost_t3_hh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t3_hh.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t3_hh.setUnits("ore")


class _Defrost_t3_mm_Type(Integer32):
    """Custom type defrost_t3_mm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Defrost_t3_mm_Type.__name__ = "Integer32"
_Defrost_t3_mm_Object = MibScalar
defrost_t3_mm = _Defrost_t3_mm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 44),
    _Defrost_t3_mm_Type()
)
defrost_t3_mm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t3_mm.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t3_mm.setUnits("min")


class _Defrost_t4_dd_Type(Integer32):
    """Custom type defrost_t4_dd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Defrost_t4_dd_Type.__name__ = "Integer32"
_Defrost_t4_dd_Object = MibScalar
defrost_t4_dd = _Defrost_t4_dd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 45),
    _Defrost_t4_dd_Type()
)
defrost_t4_dd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t4_dd.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t4_dd.setUnits("gg")


class _Defrost_t4_hh_Type(Integer32):
    """Custom type defrost_t4_hh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Defrost_t4_hh_Type.__name__ = "Integer32"
_Defrost_t4_hh_Object = MibScalar
defrost_t4_hh = _Defrost_t4_hh_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 46),
    _Defrost_t4_hh_Type()
)
defrost_t4_hh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t4_hh.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t4_hh.setUnits("ore")


class _Defrost_t4_mm_Type(Integer32):
    """Custom type defrost_t4_mm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Defrost_t4_mm_Type.__name__ = "Integer32"
_Defrost_t4_mm_Object = MibScalar
defrost_t4_mm = _Defrost_t4_mm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 47),
    _Defrost_t4_mm_Type()
)
defrost_t4_mm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t4_mm.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t4_mm.setUnits("min")


class _Defrost_t5_dd_Type(Integer32):
    """Custom type defrost_t5_dd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Defrost_t5_dd_Type.__name__ = "Integer32"
_Defrost_t5_dd_Object = MibScalar
defrost_t5_dd = _Defrost_t5_dd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 48),
    _Defrost_t5_dd_Type()
)
defrost_t5_dd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t5_dd.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t5_dd.setUnits("gg")


class _Defrost_t5_hh_Type(Integer32):
    """Custom type defrost_t5_hh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Defrost_t5_hh_Type.__name__ = "Integer32"
_Defrost_t5_hh_Object = MibScalar
defrost_t5_hh = _Defrost_t5_hh_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 49),
    _Defrost_t5_hh_Type()
)
defrost_t5_hh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t5_hh.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t5_hh.setUnits("ore")


class _Defrost_t5_mm_Type(Integer32):
    """Custom type defrost_t5_mm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Defrost_t5_mm_Type.__name__ = "Integer32"
_Defrost_t5_mm_Object = MibScalar
defrost_t5_mm = _Defrost_t5_mm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 50),
    _Defrost_t5_mm_Type()
)
defrost_t5_mm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t5_mm.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t5_mm.setUnits("min")


class _Defrost_t6_dd_Type(Integer32):
    """Custom type defrost_t6_dd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Defrost_t6_dd_Type.__name__ = "Integer32"
_Defrost_t6_dd_Object = MibScalar
defrost_t6_dd = _Defrost_t6_dd_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 51),
    _Defrost_t6_dd_Type()
)
defrost_t6_dd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t6_dd.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t6_dd.setUnits("gg")


class _Defrost_t6_hh_Type(Integer32):
    """Custom type defrost_t6_hh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Defrost_t6_hh_Type.__name__ = "Integer32"
_Defrost_t6_hh_Object = MibScalar
defrost_t6_hh = _Defrost_t6_hh_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 52),
    _Defrost_t6_hh_Type()
)
defrost_t6_hh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t6_hh.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t6_hh.setUnits("ore")


class _Defrost_t6_mm_Type(Integer32):
    """Custom type defrost_t6_mm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Defrost_t6_mm_Type.__name__ = "Integer32"
_Defrost_t6_mm_Object = MibScalar
defrost_t6_mm = _Defrost_t6_mm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 53),
    _Defrost_t6_mm_Type()
)
defrost_t6_mm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defrost_t6_mm.setStatus("current")
if mibBuilder.loadTexts:
    defrost_t6_mm.setUnits("min")


class _Tm_Type(Integer32):
    """Custom type tm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Tm_Type.__name__ = "Integer32"
_Tm_Object = MibScalar
tm = _Tm_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 54),
    _Tm_Type()
)
tm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tm.setStatus("current")
if mibBuilder.loadTexts:
    tm.setUnits("min")


class _Th_Type(Integer32):
    """Custom type th based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Th_Type.__name__ = "Integer32"
_Th_Object = MibScalar
th = _Th_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 55),
    _Th_Type()
)
th.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    th.setStatus("current")
if mibBuilder.loadTexts:
    th.setUnits("ore")


class _Td_Type(Integer32):
    """Custom type td based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Td_Type.__name__ = "Integer32"
_Td_Object = MibScalar
td = _Td_Object(
    (1, 3, 6, 1, 4, 1, 9839, 2, 1, 3, 56),
    _Td_Type()
)
td.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    td.setStatus("current")
if mibBuilder.loadTexts:
    td.setUnits("N/A")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAREL-powersplit-MIB",
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
       "powersplitMIB": powersplitMIB,
       "digitalObjects": digitalObjects,
       "cent_fhren_flag": cent_fhren_flag,
       "autoscale": autoscale,
       "defrostprobeselect": defrostprobeselect,
       "defrost_cmd": defrost_cmd,
       "defrost_at_startup": defrost_at_startup,
       "defrost_show": defrost_show,
       "defrost_priority": defrost_priority,
       "fan_cfg": fan_cfg,
       "fan_off_ctrl": fan_off_ctrl,
       "fan_defrost_ctrl": fan_defrost_ctrl,
       "keyb_disabled": keyb_disabled,
       "loc_on_off_ena": loc_on_off_ena,
       "lan_on_off_ena": lan_on_off_ena,
       "lan_din": lan_din,
       "defrost_tout_alarm_ena": defrost_tout_alarm_ena,
       "minmax_store_enable": minmax_store_enable,
       "night_reg_probe": night_reg_probe,
       "haccp_reset": haccp_reset,
       "dig_in_1": dig_in_1,
       "dig_in_2": dig_in_2,
       "s_comp": s_comp,
       "s_fan": s_fan,
       "s_defrost": s_defrost,
       "s_aux_2": s_aux_2,
       "s_alarm": s_alarm,
       "s_light": s_light,
       "dr_supervisor": dr_supervisor,
       "dr_svendreq": dr_svendreq,
       "a1_e1": a1_e1,
       "a1_e2": a1_e2,
       "a1_e3": a1_e3,
       "a1_ia": a1_ia,
       "a1_da": a1_da,
       "a1_ea": a1_ea,
       "a1_re": a1_re,
       "a1_id": a1_id,
       "a2_hi": a2_hi,
       "a2_lo": a2_lo,
       "a2_ha": a2_ha,
       "a2_hf": a2_hf,
       "a2_ed": a2_ed,
       "analogObjects": analogObjects,
       "probeoffset_3": probeoffset_3,
       "probeoffset_1": probeoffset_1,
       "probeoffset_2": probeoffset_2,
       "fan_alarm_hyst": fan_alarm_hyst,
       "alarm_max_delta": alarm_max_delta,
       "alarm_min_delta": alarm_min_delta,
       "defrost_end_temp": defrost_end_temp,
       "fan_on_temp": fan_on_temp,
       "setpoint_min": setpoint_min,
       "setpoint_max": setpoint_max,
       "setpoint_night": setpoint_night,
       "reghyst": reghyst,
       "max_store_value": max_store_value,
       "min_store_value": min_store_value,
       "setpoint": setpoint,
       "probe_1": probe_1,
       "probe_2": probe_2,
       "probe_3": probe_3,
       "probe_virtual": probe_virtual,
       "power_supply_voltage": power_supply_voltage,
       "integerObjects": integerObjects,
       "probe_stability": probe_stability,
       "virt_probe": virt_probe,
       "showprobe": showprobe,
       "showprobe_t": showprobe_t,
       "defrostprobepresence": defrostprobepresence,
       "dig_in_cfg_1": dig_in_cfg_1,
       "dig_in_cfg_2": dig_in_cfg_2,
       "alarm_input_delay": alarm_input_delay,
       "alarm_delay": alarm_delay,
       "comp_startup_delay": comp_startup_delay,
       "comp_s2s_delay": comp_s2s_delay,
       "comp_min_off_time": comp_min_off_time,
       "comp_min_on_time": comp_min_on_time,
       "rele_safety_cycle": rele_safety_cycle,
       "cc_alarm_delay": cc_alarm_delay,
       "comp_cc": comp_cc,
       "defrost_type": defrost_type,
       "defrost_delay": defrost_delay,
       "alarm_delay_df_door": alarm_delay_df_door,
       "dripping_interval": dripping_interval,
       "defrost_interval": defrost_interval,
       "defrost_max_time": defrost_max_time,
       "fan_drip_interval": fan_drip_interval,
       "aux1_cfg": aux1_cfg,
       "aux2_cfg": aux2_cfg,
       "light_sens_1": light_sens_1,
       "light_timer": light_timer,
       "minmax_acq_time": minmax_acq_time,
       "haccp_ha_day": haccp_ha_day,
       "haccp_ha_hour": haccp_ha_hour,
       "haccp_ha_min": haccp_ha_min,
       "haccp_hf_day": haccp_hf_day,
       "haccp_hf_hour": haccp_hf_hour,
       "haccp_hf_min": haccp_hf_min,
       "haccp_alarm_delay": haccp_alarm_delay,
       "defrost_t1_dd": defrost_t1_dd,
       "defrost_t1_hh": defrost_t1_hh,
       "defrost_t1_mm": defrost_t1_mm,
       "defrost_t2_dd": defrost_t2_dd,
       "defrost_t2_hh": defrost_t2_hh,
       "defrost_t2_mm": defrost_t2_mm,
       "defrost_t3_dd": defrost_t3_dd,
       "defrost_t3_hh": defrost_t3_hh,
       "defrost_t3_mm": defrost_t3_mm,
       "defrost_t4_dd": defrost_t4_dd,
       "defrost_t4_hh": defrost_t4_hh,
       "defrost_t4_mm": defrost_t4_mm,
       "defrost_t5_dd": defrost_t5_dd,
       "defrost_t5_hh": defrost_t5_hh,
       "defrost_t5_mm": defrost_t5_mm,
       "defrost_t6_dd": defrost_t6_dd,
       "defrost_t6_hh": defrost_t6_hh,
       "defrost_t6_mm": defrost_t6_mm,
       "tm": tm,
       "th": th,
       "td": td}
)
