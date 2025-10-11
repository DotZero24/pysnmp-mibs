# SNMP MIB module (FORT-TELECOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tfortis/FORT-TELECOM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:59 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

forttelecomMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42019)
)
if mibBuilder.loadTexts:
    forttelecomMIB.setRevisions(
        ("2020-08-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3)
)
_Psw_ObjectIdentity = ObjectIdentity
psw = _Psw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2)
)
_TrapsPSW_ObjectIdentity = ObjectIdentity
trapsPSW = _TrapsPSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0)
)
_ConfigPSW_ObjectIdentity = ObjectIdentity
configPSW = _ConfigPSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1)
)
_ComfortStart_ObjectIdentity = ObjectIdentity
comfortStart = _ComfortStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 1)
)


class _ComfortStartTime_Type(Integer32):
    """Custom type comfortStartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ComfortStartTime_Type.__name__ = "Integer32"
_ComfortStartTime_Object = MibScalar
comfortStartTime = _ComfortStartTime_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 1, 1),
    _ComfortStartTime_Type()
)
comfortStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comfortStartTime.setStatus("current")
_ComfStartTable_Object = MibTable
comfStartTable = _ComfStartTable_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    comfStartTable.setStatus("current")
_ComfStartEntry_Object = MibTableRow
comfStartEntry = _ComfStartEntry_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 1, 2, 1)
)
comfStartEntry.setIndexNames(
    (0, "FORT-TELECOM-MIB", "comfStIndex"),
)
if mibBuilder.loadTexts:
    comfStartEntry.setStatus("current")
_ComfStIndex_Type = Integer32
_ComfStIndex_Object = MibTableColumn
comfStIndex = _ComfStIndex_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 1, 2, 1, 1),
    _ComfStIndex_Type()
)
comfStIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comfStIndex.setStatus("current")


class _ComfStState_Type(Integer32):
    """Custom type comfStState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ComfStState_Type.__name__ = "Integer32"
_ComfStState_Object = MibTableColumn
comfStState = _ComfStState_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 1, 2, 1, 2),
    _ComfStState_Type()
)
comfStState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comfStState.setStatus("current")
_AutoRestart_ObjectIdentity = ObjectIdentity
autoRestart = _AutoRestart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2)
)
_AutoRestartTable_Object = MibTable
autoRestartTable = _AutoRestartTable_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    autoRestartTable.setStatus("current")
_AutoRestartEntry_Object = MibTableRow
autoRestartEntry = _AutoRestartEntry_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2, 1, 1)
)
autoRestartEntry.setIndexNames(
    (0, "FORT-TELECOM-MIB", "autoRstIndex"),
)
if mibBuilder.loadTexts:
    autoRestartEntry.setStatus("current")
_AutoRstIndex_Type = Integer32
_AutoRstIndex_Object = MibTableColumn
autoRstIndex = _AutoRstIndex_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2, 1, 1, 1),
    _AutoRstIndex_Type()
)
autoRstIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRstIndex.setStatus("current")


class _AutoRstMode_Type(Integer32):
    """Custom type autoRstMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("link", 1),
          ("ping", 2),
          ("speed", 3),
          ("time", 4))
    )


_AutoRstMode_Type.__name__ = "Integer32"
_AutoRstMode_Object = MibTableColumn
autoRstMode = _AutoRstMode_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2, 1, 1, 2),
    _AutoRstMode_Type()
)
autoRstMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRstMode.setStatus("current")
_AutoRstDstIP_Type = IpAddress
_AutoRstDstIP_Object = MibTableColumn
autoRstDstIP = _AutoRstDstIP_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2, 1, 1, 3),
    _AutoRstDstIP_Type()
)
autoRstDstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRstDstIP.setStatus("current")
_AutoRstSpeedDown_Type = Integer32
_AutoRstSpeedDown_Object = MibTableColumn
autoRstSpeedDown = _AutoRstSpeedDown_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2, 1, 1, 4),
    _AutoRstSpeedDown_Type()
)
autoRstSpeedDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRstSpeedDown.setStatus("current")
_AutoRstSpeedUp_Type = Integer32
_AutoRstSpeedUp_Object = MibTableColumn
autoRstSpeedUp = _AutoRstSpeedUp_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2, 1, 1, 5),
    _AutoRstSpeedUp_Type()
)
autoRstSpeedUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRstSpeedUp.setStatus("current")
_AutoReStartTimeOnHour_Type = Integer32
_AutoReStartTimeOnHour_Object = MibScalar
autoReStartTimeOnHour = _AutoReStartTimeOnHour_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2, 1, 1, 6),
    _AutoReStartTimeOnHour_Type()
)
autoReStartTimeOnHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoReStartTimeOnHour.setStatus("current")
_AutoReStartTimeOnMin_Type = Integer32
_AutoReStartTimeOnMin_Object = MibScalar
autoReStartTimeOnMin = _AutoReStartTimeOnMin_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2, 1, 1, 7),
    _AutoReStartTimeOnMin_Type()
)
autoReStartTimeOnMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoReStartTimeOnMin.setStatus("current")
_AutoReStartTimeOffHour_Type = Integer32
_AutoReStartTimeOffHour_Object = MibScalar
autoReStartTimeOffHour = _AutoReStartTimeOffHour_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2, 1, 1, 8),
    _AutoReStartTimeOffHour_Type()
)
autoReStartTimeOffHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoReStartTimeOffHour.setStatus("current")
_AutoReStartTimeOffMin_Type = Integer32
_AutoReStartTimeOffMin_Object = MibScalar
autoReStartTimeOffMin = _AutoReStartTimeOffMin_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 2, 1, 1, 9),
    _AutoReStartTimeOffMin_Type()
)
autoReStartTimeOffMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoReStartTimeOffMin.setStatus("current")
_PortPoe_ObjectIdentity = ObjectIdentity
portPoe = _PortPoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 3)
)
_PortPoeTable_Object = MibTable
portPoeTable = _PortPoeTable_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    portPoeTable.setStatus("current")
_PortPoeEntry_Object = MibTableRow
portPoeEntry = _PortPoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 3, 1, 1)
)
portPoeEntry.setIndexNames(
    (0, "FORT-TELECOM-MIB", "portPoeIndex"),
)
if mibBuilder.loadTexts:
    portPoeEntry.setStatus("current")
_PortPoeIndex_Type = Integer32
_PortPoeIndex_Object = MibTableColumn
portPoeIndex = _PortPoeIndex_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 3, 1, 1, 1),
    _PortPoeIndex_Type()
)
portPoeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPoeIndex.setStatus("current")


class _PortPoeState_Type(Integer32):
    """Custom type portPoeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PortPoeState_Type.__name__ = "Integer32"
_PortPoeState_Object = MibTableColumn
portPoeState = _PortPoeState_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 3, 1, 1, 2),
    _PortPoeState_Type()
)
portPoeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPoeState.setStatus("current")
_OutStatePSW_ObjectIdentity = ObjectIdentity
outStatePSW = _OutStatePSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 4)
)


class _State_Type(Integer32):
    """Custom type state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("short", 2))
    )


_State_Type.__name__ = "Integer32"
_State_Object = MibScalar
state = _State_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 1, 4, 1),
    _State_Type()
)
state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    state.setStatus("current")
_StatusPSW_ObjectIdentity = ObjectIdentity
statusPSW = _StatusPSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2)
)
_UpsStatus_ObjectIdentity = ObjectIdentity
upsStatus = _UpsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 1)
)


class _UpsModeAvalible_Type(Integer32):
    """Custom type upsModeAvalible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_UpsModeAvalible_Type.__name__ = "Integer32"
_UpsModeAvalible_Object = MibScalar
upsModeAvalible = _UpsModeAvalible_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 1, 1),
    _UpsModeAvalible_Type()
)
upsModeAvalible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsModeAvalible.setStatus("current")


class _UpsPwrSource_Type(Integer32):
    """Custom type upsPwrSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("battery", 1),
          ("ac", 2))
    )


_UpsPwrSource_Type.__name__ = "Integer32"
_UpsPwrSource_Object = MibScalar
upsPwrSource = _UpsPwrSource_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 1, 2),
    _UpsPwrSource_Type()
)
upsPwrSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPwrSource.setStatus("current")
_UpsBatteryVoltage_Type = Integer32
_UpsBatteryVoltage_Object = MibScalar
upsBatteryVoltage = _UpsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 1, 3),
    _UpsBatteryVoltage_Type()
)
upsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setStatus("current")
_UpsBatteryTime_Type = Integer32
_UpsBatteryTime_Object = MibScalar
upsBatteryTime = _UpsBatteryTime_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 1, 4),
    _UpsBatteryTime_Type()
)
upsBatteryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTime.setStatus("current")
_InputStatus_ObjectIdentity = ObjectIdentity
inputStatus = _InputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 2)
)
_InputStatusTable_Object = MibTable
inputStatusTable = _InputStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    inputStatusTable.setStatus("current")
_InputStatusEntry_Object = MibTableRow
inputStatusEntry = _InputStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 2, 1, 1)
)
inputStatusEntry.setIndexNames(
    (0, "FORT-TELECOM-MIB", "inputIndex"),
)
if mibBuilder.loadTexts:
    inputStatusEntry.setStatus("current")
_InputIndex_Type = Integer32
_InputIndex_Object = MibTableColumn
inputIndex = _InputIndex_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 2, 1, 1, 1),
    _InputIndex_Type()
)
inputIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputIndex.setStatus("current")


class _InputType_Type(Integer32):
    """Custom type inputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("build-in", 1),
          ("plc", 2))
    )


_InputType_Type.__name__ = "Integer32"
_InputType_Object = MibTableColumn
inputType = _InputType_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 2, 1, 1, 2),
    _InputType_Type()
)
inputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputType.setStatus("current")


class _InputState_Type(Integer32):
    """Custom type inputState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("short", 1),
          ("open", 2))
    )


_InputState_Type.__name__ = "Integer32"
_InputState_Object = MibTableColumn
inputState = _InputState_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 2, 1, 1, 3),
    _InputState_Type()
)
inputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputState.setStatus("current")


class _InputAlarm_Type(Integer32):
    """Custom type inputAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("short", 1),
          ("open", 2),
          ("any", 3))
    )


_InputAlarm_Type.__name__ = "Integer32"
_InputAlarm_Object = MibTableColumn
inputAlarm = _InputAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 2, 1, 1, 4),
    _InputAlarm_Type()
)
inputAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputAlarm.setStatus("current")
_FwStatus_ObjectIdentity = ObjectIdentity
fwStatus = _FwStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 3)
)
_FwVersion_Type = OctetString
_FwVersion_Object = MibScalar
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 3, 1),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("current")
_EmStatus_ObjectIdentity = ObjectIdentity
emStatus = _EmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 4)
)


class _EmConnectionStatus_Type(Integer32):
    """Custom type emConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_EmConnectionStatus_Type.__name__ = "Integer32"
_EmConnectionStatus_Object = MibScalar
emConnectionStatus = _EmConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 4, 1),
    _EmConnectionStatus_Type()
)
emConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emConnectionStatus.setStatus("current")
_EmResultTotal_Type = OctetString
_EmResultTotal_Object = MibScalar
emResultTotal = _EmResultTotal_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 4, 2),
    _EmResultTotal_Type()
)
emResultTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emResultTotal.setStatus("current")
_EmResultT1_Type = OctetString
_EmResultT1_Object = MibScalar
emResultT1 = _EmResultT1_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 4, 3),
    _EmResultT1_Type()
)
emResultT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emResultT1.setStatus("current")
_EmResultT2_Type = OctetString
_EmResultT2_Object = MibScalar
emResultT2 = _EmResultT2_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 4, 4),
    _EmResultT2_Type()
)
emResultT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emResultT2.setStatus("current")
_EmResultT3_Type = OctetString
_EmResultT3_Object = MibScalar
emResultT3 = _EmResultT3_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 4, 5),
    _EmResultT3_Type()
)
emResultT3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emResultT3.setStatus("current")
_EmResultT4_Type = OctetString
_EmResultT4_Object = MibScalar
emResultT4 = _EmResultT4_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 4, 6),
    _EmResultT4_Type()
)
emResultT4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emResultT4.setStatus("current")
_EmPollingInterval_Type = Integer32
_EmPollingInterval_Object = MibScalar
emPollingInterval = _EmPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 4, 7),
    _EmPollingInterval_Type()
)
emPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emPollingInterval.setStatus("current")
_PoeStatus_ObjectIdentity = ObjectIdentity
poeStatus = _PoeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 5)
)
_PoeStatusTable_Object = MibTable
poeStatusTable = _PoeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    poeStatusTable.setStatus("current")
_PoeStatusEntry_Object = MibTableRow
poeStatusEntry = _PoeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 5, 1, 1)
)
poeStatusEntry.setIndexNames(
    (0, "FORT-TELECOM-MIB", "portPoeStatusIndex"),
)
if mibBuilder.loadTexts:
    poeStatusEntry.setStatus("current")
_PortPoeStatusIndex_Type = Integer32
_PortPoeStatusIndex_Object = MibTableColumn
portPoeStatusIndex = _PortPoeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 5, 1, 1, 1),
    _PortPoeStatusIndex_Type()
)
portPoeStatusIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPoeStatusIndex.setStatus("current")


class _PortPoeStatusState_Type(Integer32):
    """Custom type portPoeStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PortPoeStatusState_Type.__name__ = "Integer32"
_PortPoeStatusState_Object = MibTableColumn
portPoeStatusState = _PortPoeStatusState_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 5, 1, 1, 2),
    _PortPoeStatusState_Type()
)
portPoeStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPoeStatusState.setStatus("current")
_PortPoeStatusPower_Type = Integer32
_PortPoeStatusPower_Object = MibTableColumn
portPoeStatusPower = _PortPoeStatusPower_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 5, 1, 1, 3),
    _PortPoeStatusPower_Type()
)
portPoeStatusPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPoeStatusPower.setStatus("current")
_SpecialStatus_ObjectIdentity = ObjectIdentity
specialStatus = _SpecialStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 6)
)
_AutoRestartErrors_ObjectIdentity = ObjectIdentity
autoRestartErrors = _AutoRestartErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 6, 1)
)
_AutoRestartErrorsTable_Object = MibTable
autoRestartErrorsTable = _AutoRestartErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    autoRestartErrorsTable.setStatus("current")
_AutoRestartErrorsEntry_Object = MibTableRow
autoRestartErrorsEntry = _AutoRestartErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 6, 1, 1, 1)
)
autoRestartErrorsEntry.setIndexNames(
    (0, "FORT-TELECOM-MIB", "arPortIndex"),
)
if mibBuilder.loadTexts:
    autoRestartErrorsEntry.setStatus("current")
_ArPortIndex_Type = Integer32
_ArPortIndex_Object = MibTableColumn
arPortIndex = _ArPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 6, 1, 1, 1, 1),
    _ArPortIndex_Type()
)
arPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arPortIndex.setStatus("current")


class _ArPortStatus_Type(Integer32):
    """Custom type arPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("noLink", 2),
          ("noPing", 3),
          ("lowSpeed", 4))
    )


_ArPortStatus_Type.__name__ = "Integer32"
_ArPortStatus_Object = MibTableColumn
arPortStatus = _ArPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 6, 1, 1, 1, 2),
    _ArPortStatus_Type()
)
arPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arPortStatus.setStatus("current")
_ComfortStartStatus_ObjectIdentity = ObjectIdentity
comfortStartStatus = _ComfortStartStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 6, 2)
)
_ComfortStartStatusTable_Object = MibTable
comfortStartStatusTable = _ComfortStartStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    comfortStartStatusTable.setStatus("current")
_ComfortStartStatusEntry_Object = MibTableRow
comfortStartStatusEntry = _ComfortStartStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 6, 2, 1, 1)
)
comfortStartStatusEntry.setIndexNames(
    (0, "FORT-TELECOM-MIB", "csPortIndex"),
)
if mibBuilder.loadTexts:
    comfortStartStatusEntry.setStatus("current")
_CsPortIndex_Type = Integer32
_CsPortIndex_Object = MibTableColumn
csPortIndex = _CsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 6, 2, 1, 1, 1),
    _CsPortIndex_Type()
)
csPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csPortIndex.setStatus("current")


class _CsPortStatus_Type(Integer32):
    """Custom type csPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("processing", 2))
    )


_CsPortStatus_Type.__name__ = "Integer32"
_CsPortStatus_Object = MibTableColumn
csPortStatus = _CsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 6, 2, 1, 1, 2),
    _CsPortStatus_Type()
)
csPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csPortStatus.setStatus("current")
_SfpStatus_ObjectIdentity = ObjectIdentity
sfpStatus = _SfpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7)
)
_SfpStatusTable_Object = MibTable
sfpStatusTable = _SfpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    sfpStatusTable.setStatus("current")
_SfpStatusEntry_Object = MibTableRow
sfpStatusEntry = _SfpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1)
)
sfpStatusEntry.setIndexNames(
    (0, "FORT-TELECOM-MIB", "portSfpIndex"),
)
if mibBuilder.loadTexts:
    sfpStatusEntry.setStatus("current")
_PortSfpIndex_Type = Integer32
_PortSfpIndex_Object = MibTableColumn
portSfpIndex = _PortSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 1),
    _PortSfpIndex_Type()
)
portSfpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSfpIndex.setStatus("current")
_PortSfpPresent_Type = Integer32
_PortSfpPresent_Object = MibTableColumn
portSfpPresent = _PortSfpPresent_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 2),
    _PortSfpPresent_Type()
)
portSfpPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpPresent.setStatus("current")
_PortSfpSignalDetect_Type = Integer32
_PortSfpSignalDetect_Object = MibTableColumn
portSfpSignalDetect = _PortSfpSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 3),
    _PortSfpSignalDetect_Type()
)
portSfpSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpSignalDetect.setStatus("current")


class _PortSfpVendor_Type(DisplayString):
    """Custom type portSfpVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortSfpVendor_Type.__name__ = "DisplayString"
_PortSfpVendor_Object = MibTableColumn
portSfpVendor = _PortSfpVendor_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 4),
    _PortSfpVendor_Type()
)
portSfpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpVendor.setStatus("current")


class _PortSfpOui_Type(DisplayString):
    """Custom type portSfpOui based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortSfpOui_Type.__name__ = "DisplayString"
_PortSfpOui_Object = MibTableColumn
portSfpOui = _PortSfpOui_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 5),
    _PortSfpOui_Type()
)
portSfpOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpOui.setStatus("current")


class _PortSfpPartNumber_Type(DisplayString):
    """Custom type portSfpPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortSfpPartNumber_Type.__name__ = "DisplayString"
_PortSfpPartNumber_Object = MibTableColumn
portSfpPartNumber = _PortSfpPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 6),
    _PortSfpPartNumber_Type()
)
portSfpPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpPartNumber.setStatus("current")


class _PortSfpRevision_Type(DisplayString):
    """Custom type portSfpRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortSfpRevision_Type.__name__ = "DisplayString"
_PortSfpRevision_Object = MibTableColumn
portSfpRevision = _PortSfpRevision_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 7),
    _PortSfpRevision_Type()
)
portSfpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpRevision.setStatus("current")
_PortSfpTemperature_Type = Integer32
_PortSfpTemperature_Object = MibTableColumn
portSfpTemperature = _PortSfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 8),
    _PortSfpTemperature_Type()
)
portSfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpTemperature.setStatus("current")
_PortSfpVoltage_Type = Integer32
_PortSfpVoltage_Object = MibTableColumn
portSfpVoltage = _PortSfpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 9),
    _PortSfpVoltage_Type()
)
portSfpVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpVoltage.setStatus("current")
_PortSfpBiasCurrent_Type = Integer32
_PortSfpBiasCurrent_Object = MibTableColumn
portSfpBiasCurrent = _PortSfpBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 10),
    _PortSfpBiasCurrent_Type()
)
portSfpBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpBiasCurrent.setStatus("current")
_PortSfpTxOutPower_Type = Integer32
_PortSfpTxOutPower_Object = MibTableColumn
portSfpTxOutPower = _PortSfpTxOutPower_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 11),
    _PortSfpTxOutPower_Type()
)
portSfpTxOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpTxOutPower.setStatus("current")
_PortSfpTxOutPowerDb_Type = Integer32
_PortSfpTxOutPowerDb_Object = MibTableColumn
portSfpTxOutPowerDb = _PortSfpTxOutPowerDb_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 12),
    _PortSfpTxOutPowerDb_Type()
)
portSfpTxOutPowerDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpTxOutPowerDb.setStatus("current")
_PortSfpRxOutPower_Type = Integer32
_PortSfpRxOutPower_Object = MibTableColumn
portSfpRxOutPower = _PortSfpRxOutPower_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 13),
    _PortSfpRxOutPower_Type()
)
portSfpRxOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpRxOutPower.setStatus("current")
_PortSfpRxOutPowerDb_Type = Integer32
_PortSfpRxOutPowerDb_Object = MibTableColumn
portSfpRxOutPowerDb = _PortSfpRxOutPowerDb_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 7, 1, 1, 14),
    _PortSfpRxOutPowerDb_Type()
)
portSfpRxOutPowerDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpRxOutPowerDb.setStatus("current")
_SensorEntry_ObjectIdentity = ObjectIdentity
sensorEntry = _SensorEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 8)
)


class _SensorConnected_Type(Integer32):
    """Custom type sensorConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_SensorConnected_Type.__name__ = "Integer32"
_SensorConnected_Object = MibTableColumn
sensorConnected = _SensorConnected_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 8, 1),
    _SensorConnected_Type()
)
sensorConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorConnected.setStatus("current")
_SensorTemperature_Type = Integer32
_SensorTemperature_Object = MibTableColumn
sensorTemperature = _SensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 8, 2),
    _SensorTemperature_Type()
)
sensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTemperature.setStatus("current")
_SensorHumidity_Type = Integer32
_SensorHumidity_Object = MibTableColumn
sensorHumidity = _SensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 2, 8, 3),
    _SensorHumidity_Type()
)
sensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorHumidity.setStatus("current")
_Integrations_ObjectIdentity = ObjectIdentity
integrations = _Integrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 4)
)
_Teleport_ObjectIdentity = ObjectIdentity
teleport = _Teleport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2)
)
_TrapsTLP_ObjectIdentity = ObjectIdentity
trapsTLP = _TrapsTLP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0)
)
_InputTeleport_ObjectIdentity = ObjectIdentity
inputTeleport = _InputTeleport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 2)
)
_InputStatusTableTLP_Object = MibTable
inputStatusTableTLP = _InputStatusTableTLP_Object(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    inputStatusTableTLP.setStatus("current")
_InputStatusEntryTLP_Object = MibTableRow
inputStatusEntryTLP = _InputStatusEntryTLP_Object(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 2, 1, 1)
)
inputStatusEntryTLP.setIndexNames(
    (0, "FORT-TELECOM-MIB", "inputIndexTLP"),
)
if mibBuilder.loadTexts:
    inputStatusEntryTLP.setStatus("current")
_InputIndexTLP_Type = Integer32
_InputIndexTLP_Object = MibTableColumn
inputIndexTLP = _InputIndexTLP_Object(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 2, 1, 1, 1),
    _InputIndexTLP_Type()
)
inputIndexTLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputIndexTLP.setStatus("current")


class _InputStateTLP_Type(Integer32):
    """Custom type inputStateTLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("short", 2))
    )


_InputStateTLP_Type.__name__ = "Integer32"
_InputStateTLP_Object = MibTableColumn
inputStateTLP = _InputStateTLP_Object(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 2, 1, 1, 2),
    _InputStateTLP_Type()
)
inputStateTLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStateTLP.setStatus("current")
_OutputTeleport_ObjectIdentity = ObjectIdentity
outputTeleport = _OutputTeleport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 3)
)
_OutputTeleportTable_Object = MibTable
outputTeleportTable = _OutputTeleportTable_Object(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    outputTeleportTable.setStatus("current")
_OutputTeleportEntry_Object = MibTableRow
outputTeleportEntry = _OutputTeleportEntry_Object(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 3, 1, 1)
)
outputTeleportEntry.setIndexNames(
    (0, "FORT-TELECOM-MIB", "outIndex"),
)
if mibBuilder.loadTexts:
    outputTeleportEntry.setStatus("current")
_OutIndex_Type = Integer32
_OutIndex_Object = MibTableColumn
outIndex = _OutIndex_Object(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 3, 1, 1, 1),
    _OutIndex_Type()
)
outIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outIndex.setStatus("current")


class _OutState_Type(Integer32):
    """Custom type outState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("short", 2))
    )


_OutState_Type.__name__ = "Integer32"
_OutState_Object = MibTableColumn
outState = _OutState_Object(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 3, 1, 1, 2),
    _OutState_Type()
)
outState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outState.setStatus("current")
_FwStatusTLP_ObjectIdentity = ObjectIdentity
fwStatusTLP = _FwStatusTLP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 4)
)
_FwVersionTLP_Type = OctetString
_FwVersionTLP_Object = MibScalar
fwVersionTLP = _FwVersionTLP_Object(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 4, 1),
    _FwVersionTLP_Type()
)
fwVersionTLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersionTLP.setStatus("current")

# Managed Objects groups


# Notification objects

stpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 1)
)
if mibBuilder.loadTexts:
    stpTopologyChanged.setStatus(
        "current"
    )

specialFunctionNoLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 2)
)
if mibBuilder.loadTexts:
    specialFunctionNoLink.setStatus(
        "current"
    )

specialFunctionNoPingResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 3)
)
if mibBuilder.loadTexts:
    specialFunctionNoPingResponse.setStatus(
        "current"
    )

specialFunctionLowSpeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 4)
)
if mibBuilder.loadTexts:
    specialFunctionLowSpeed.setStatus(
        "current"
    )

updateFirmware = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 5)
)
if mibBuilder.loadTexts:
    updateFirmware.setStatus(
        "current"
    )

setToDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 6)
)
if mibBuilder.loadTexts:
    setToDefault.setStatus(
        "current"
    )

backupSettings = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 7)
)
if mibBuilder.loadTexts:
    backupSettings.setStatus(
        "current"
    )

systemWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 8)
)
if mibBuilder.loadTexts:
    systemWarmStart.setStatus(
        "current"
    )

systemColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 9)
)
if mibBuilder.loadTexts:
    systemColdStart.setStatus(
        "current"
    )

webInterfaceLoginOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 10)
)
if mibBuilder.loadTexts:
    webInterfaceLoginOk.setStatus(
        "current"
    )

webInterfaceLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 11)
)
if mibBuilder.loadTexts:
    webInterfaceLoginFail.setStatus(
        "current"
    )

emptyArpTable = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 12)
)
if mibBuilder.loadTexts:
    emptyArpTable.setStatus(
        "current"
    )

upsLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 13)
)
if mibBuilder.loadTexts:
    upsLowVoltage.setStatus(
        "current"
    )

upsBattrtyPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 14)
)
if mibBuilder.loadTexts:
    upsBattrtyPower.setStatus(
        "current"
    )

upsVacPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 15)
)
if mibBuilder.loadTexts:
    upsVacPower.setStatus(
        "current"
    )

tamperIsActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 16)
)
if mibBuilder.loadTexts:
    tamperIsActive.setStatus(
        "current"
    )

sensor1isActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 17)
)
if mibBuilder.loadTexts:
    sensor1isActive.setStatus(
        "current"
    )

sensor2isActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 18)
)
if mibBuilder.loadTexts:
    sensor2isActive.setStatus(
        "current"
    )

input1isActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 19)
)
if mibBuilder.loadTexts:
    input1isActive.setStatus(
        "current"
    )

input2isActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 20)
)
if mibBuilder.loadTexts:
    input2isActive.setStatus(
        "current"
    )

input3isActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 21)
)
if mibBuilder.loadTexts:
    input3isActive.setStatus(
        "current"
    )

input4isActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 22)
)
if mibBuilder.loadTexts:
    input4isActive.setStatus(
        "current"
    )

macFilteringAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 23)
)
if mibBuilder.loadTexts:
    macFilteringAlarm.setStatus(
        "current"
    )

portErrorDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 24)
)
if mibBuilder.loadTexts:
    portErrorDisabled.setStatus(
        "current"
    )

pwr180DiagnosticError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 25)
)
if mibBuilder.loadTexts:
    pwr180DiagnosticError.setStatus(
        "current"
    )

temperatureSensorLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 26)
)
if mibBuilder.loadTexts:
    temperatureSensorLow.setStatus(
        "current"
    )

temperatureSensorHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 27)
)
if mibBuilder.loadTexts:
    temperatureSensorHigh.setStatus(
        "current"
    )

humiditySensorLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 28)
)
if mibBuilder.loadTexts:
    humiditySensorLow.setStatus(
        "current"
    )

humiditySensorHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 29)
)
if mibBuilder.loadTexts:
    humiditySensorHigh.setStatus(
        "current"
    )

leakageSensorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 3, 2, 0, 30)
)
if mibBuilder.loadTexts:
    leakageSensorAlarm.setStatus(
        "current"
    )

updateFirmwareTLP = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 1)
)
if mibBuilder.loadTexts:
    updateFirmwareTLP.setStatus(
        "current"
    )

setToDefaultTLP = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 2)
)
if mibBuilder.loadTexts:
    setToDefaultTLP.setStatus(
        "current"
    )

backupSettingsTLP = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 3)
)
if mibBuilder.loadTexts:
    backupSettingsTLP.setStatus(
        "current"
    )

systemWarmStartTLP = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 4)
)
if mibBuilder.loadTexts:
    systemWarmStartTLP.setStatus(
        "current"
    )

systemColdStartTLP = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 5)
)
if mibBuilder.loadTexts:
    systemColdStartTLP.setStatus(
        "current"
    )

webInterfaceLoginOkTLP = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 6)
)
if mibBuilder.loadTexts:
    webInterfaceLoginOkTLP.setStatus(
        "current"
    )

webInterfaceLoginFailTLP = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 7)
)
if mibBuilder.loadTexts:
    webInterfaceLoginFailTLP.setStatus(
        "current"
    )

emptyArpTableTLP = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 8)
)
if mibBuilder.loadTexts:
    emptyArpTableTLP.setStatus(
        "current"
    )

input1isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 9)
)
if mibBuilder.loadTexts:
    input1isChanged.setStatus(
        "current"
    )

input2isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 10)
)
if mibBuilder.loadTexts:
    input2isChanged.setStatus(
        "current"
    )

input3isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 11)
)
if mibBuilder.loadTexts:
    input3isChanged.setStatus(
        "current"
    )

input4isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 12)
)
if mibBuilder.loadTexts:
    input4isChanged.setStatus(
        "current"
    )

input5isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 13)
)
if mibBuilder.loadTexts:
    input5isChanged.setStatus(
        "current"
    )

input6isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 14)
)
if mibBuilder.loadTexts:
    input6isChanged.setStatus(
        "current"
    )

input7isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 15)
)
if mibBuilder.loadTexts:
    input7isChanged.setStatus(
        "current"
    )

input8isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 16)
)
if mibBuilder.loadTexts:
    input8isChanged.setStatus(
        "current"
    )

input9isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 17)
)
if mibBuilder.loadTexts:
    input9isChanged.setStatus(
        "current"
    )

output1isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 18)
)
if mibBuilder.loadTexts:
    output1isChanged.setStatus(
        "current"
    )

output2isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 19)
)
if mibBuilder.loadTexts:
    output2isChanged.setStatus(
        "current"
    )

output3isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 20)
)
if mibBuilder.loadTexts:
    output3isChanged.setStatus(
        "current"
    )

output4isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 21)
)
if mibBuilder.loadTexts:
    output4isChanged.setStatus(
        "current"
    )

output5isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 22)
)
if mibBuilder.loadTexts:
    output5isChanged.setStatus(
        "current"
    )

output6isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 23)
)
if mibBuilder.loadTexts:
    output6isChanged.setStatus(
        "current"
    )

output7isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 24)
)
if mibBuilder.loadTexts:
    output7isChanged.setStatus(
        "current"
    )

output8isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 25)
)
if mibBuilder.loadTexts:
    output8isChanged.setStatus(
        "current"
    )

output9isChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 26)
)
if mibBuilder.loadTexts:
    output9isChanged.setStatus(
        "current"
    )

device1connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 27)
)
if mibBuilder.loadTexts:
    device1connFail.setStatus(
        "current"
    )

device2connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 28)
)
if mibBuilder.loadTexts:
    device2connFail.setStatus(
        "current"
    )

device3connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 29)
)
if mibBuilder.loadTexts:
    device3connFail.setStatus(
        "current"
    )

device4connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 30)
)
if mibBuilder.loadTexts:
    device4connFail.setStatus(
        "current"
    )

device5connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 31)
)
if mibBuilder.loadTexts:
    device5connFail.setStatus(
        "current"
    )

device6connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 32)
)
if mibBuilder.loadTexts:
    device6connFail.setStatus(
        "current"
    )

device7connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 33)
)
if mibBuilder.loadTexts:
    device7connFail.setStatus(
        "current"
    )

device8connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 34)
)
if mibBuilder.loadTexts:
    device8connFail.setStatus(
        "current"
    )

device9connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 35)
)
if mibBuilder.loadTexts:
    device9connFail.setStatus(
        "current"
    )

device10connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 36)
)
if mibBuilder.loadTexts:
    device10connFail.setStatus(
        "current"
    )

device11connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 37)
)
if mibBuilder.loadTexts:
    device11connFail.setStatus(
        "current"
    )

device12connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 38)
)
if mibBuilder.loadTexts:
    device12connFail.setStatus(
        "current"
    )

device13connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 39)
)
if mibBuilder.loadTexts:
    device13connFail.setStatus(
        "current"
    )

device14connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 40)
)
if mibBuilder.loadTexts:
    device14connFail.setStatus(
        "current"
    )

device15connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 41)
)
if mibBuilder.loadTexts:
    device15connFail.setStatus(
        "current"
    )

device16connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 42)
)
if mibBuilder.loadTexts:
    device16connFail.setStatus(
        "current"
    )

device17connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 43)
)
if mibBuilder.loadTexts:
    device17connFail.setStatus(
        "current"
    )

device18connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 44)
)
if mibBuilder.loadTexts:
    device18connFail.setStatus(
        "current"
    )

device19connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 45)
)
if mibBuilder.loadTexts:
    device19connFail.setStatus(
        "current"
    )

device20connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 46)
)
if mibBuilder.loadTexts:
    device20connFail.setStatus(
        "current"
    )

device21connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 47)
)
if mibBuilder.loadTexts:
    device21connFail.setStatus(
        "current"
    )

device22connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 48)
)
if mibBuilder.loadTexts:
    device22connFail.setStatus(
        "current"
    )

device23connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 49)
)
if mibBuilder.loadTexts:
    device23connFail.setStatus(
        "current"
    )

device24connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 50)
)
if mibBuilder.loadTexts:
    device24connFail.setStatus(
        "current"
    )

device25connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 51)
)
if mibBuilder.loadTexts:
    device25connFail.setStatus(
        "current"
    )

device26connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 52)
)
if mibBuilder.loadTexts:
    device26connFail.setStatus(
        "current"
    )

device27connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 53)
)
if mibBuilder.loadTexts:
    device27connFail.setStatus(
        "current"
    )

device28connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 54)
)
if mibBuilder.loadTexts:
    device28connFail.setStatus(
        "current"
    )

device29connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 55)
)
if mibBuilder.loadTexts:
    device29connFail.setStatus(
        "current"
    )

device30connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 56)
)
if mibBuilder.loadTexts:
    device30connFail.setStatus(
        "current"
    )

device31connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 57)
)
if mibBuilder.loadTexts:
    device31connFail.setStatus(
        "current"
    )

device32connFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42019, 4, 2, 0, 58)
)
if mibBuilder.loadTexts:
    device32connFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORT-TELECOM-MIB",
    **{"forttelecomMIB": forttelecomMIB,
       "switch": switch,
       "psw": psw,
       "trapsPSW": trapsPSW,
       "stpTopologyChanged": stpTopologyChanged,
       "specialFunctionNoLink": specialFunctionNoLink,
       "specialFunctionNoPingResponse": specialFunctionNoPingResponse,
       "specialFunctionLowSpeed": specialFunctionLowSpeed,
       "updateFirmware": updateFirmware,
       "setToDefault": setToDefault,
       "backupSettings": backupSettings,
       "systemWarmStart": systemWarmStart,
       "systemColdStart": systemColdStart,
       "webInterfaceLoginOk": webInterfaceLoginOk,
       "webInterfaceLoginFail": webInterfaceLoginFail,
       "emptyArpTable": emptyArpTable,
       "upsLowVoltage": upsLowVoltage,
       "upsBattrtyPower": upsBattrtyPower,
       "upsVacPower": upsVacPower,
       "tamperIsActive": tamperIsActive,
       "sensor1isActive": sensor1isActive,
       "sensor2isActive": sensor2isActive,
       "input1isActive": input1isActive,
       "input2isActive": input2isActive,
       "input3isActive": input3isActive,
       "input4isActive": input4isActive,
       "macFilteringAlarm": macFilteringAlarm,
       "portErrorDisabled": portErrorDisabled,
       "pwr180DiagnosticError": pwr180DiagnosticError,
       "temperatureSensorLow": temperatureSensorLow,
       "temperatureSensorHigh": temperatureSensorHigh,
       "humiditySensorLow": humiditySensorLow,
       "humiditySensorHigh": humiditySensorHigh,
       "leakageSensorAlarm": leakageSensorAlarm,
       "configPSW": configPSW,
       "comfortStart": comfortStart,
       "comfortStartTime": comfortStartTime,
       "comfStartTable": comfStartTable,
       "comfStartEntry": comfStartEntry,
       "comfStIndex": comfStIndex,
       "comfStState": comfStState,
       "autoRestart": autoRestart,
       "autoRestartTable": autoRestartTable,
       "autoRestartEntry": autoRestartEntry,
       "autoRstIndex": autoRstIndex,
       "autoRstMode": autoRstMode,
       "autoRstDstIP": autoRstDstIP,
       "autoRstSpeedDown": autoRstSpeedDown,
       "autoRstSpeedUp": autoRstSpeedUp,
       "autoReStartTimeOnHour": autoReStartTimeOnHour,
       "autoReStartTimeOnMin": autoReStartTimeOnMin,
       "autoReStartTimeOffHour": autoReStartTimeOffHour,
       "autoReStartTimeOffMin": autoReStartTimeOffMin,
       "portPoe": portPoe,
       "portPoeTable": portPoeTable,
       "portPoeEntry": portPoeEntry,
       "portPoeIndex": portPoeIndex,
       "portPoeState": portPoeState,
       "outStatePSW": outStatePSW,
       "state": state,
       "statusPSW": statusPSW,
       "upsStatus": upsStatus,
       "upsModeAvalible": upsModeAvalible,
       "upsPwrSource": upsPwrSource,
       "upsBatteryVoltage": upsBatteryVoltage,
       "upsBatteryTime": upsBatteryTime,
       "inputStatus": inputStatus,
       "inputStatusTable": inputStatusTable,
       "inputStatusEntry": inputStatusEntry,
       "inputIndex": inputIndex,
       "inputType": inputType,
       "inputState": inputState,
       "inputAlarm": inputAlarm,
       "fwStatus": fwStatus,
       "fwVersion": fwVersion,
       "emStatus": emStatus,
       "emConnectionStatus": emConnectionStatus,
       "emResultTotal": emResultTotal,
       "emResultT1": emResultT1,
       "emResultT2": emResultT2,
       "emResultT3": emResultT3,
       "emResultT4": emResultT4,
       "emPollingInterval": emPollingInterval,
       "poeStatus": poeStatus,
       "poeStatusTable": poeStatusTable,
       "poeStatusEntry": poeStatusEntry,
       "portPoeStatusIndex": portPoeStatusIndex,
       "portPoeStatusState": portPoeStatusState,
       "portPoeStatusPower": portPoeStatusPower,
       "specialStatus": specialStatus,
       "autoRestartErrors": autoRestartErrors,
       "autoRestartErrorsTable": autoRestartErrorsTable,
       "autoRestartErrorsEntry": autoRestartErrorsEntry,
       "arPortIndex": arPortIndex,
       "arPortStatus": arPortStatus,
       "comfortStartStatus": comfortStartStatus,
       "comfortStartStatusTable": comfortStartStatusTable,
       "comfortStartStatusEntry": comfortStartStatusEntry,
       "csPortIndex": csPortIndex,
       "csPortStatus": csPortStatus,
       "sfpStatus": sfpStatus,
       "sfpStatusTable": sfpStatusTable,
       "sfpStatusEntry": sfpStatusEntry,
       "portSfpIndex": portSfpIndex,
       "portSfpPresent": portSfpPresent,
       "portSfpSignalDetect": portSfpSignalDetect,
       "portSfpVendor": portSfpVendor,
       "portSfpOui": portSfpOui,
       "portSfpPartNumber": portSfpPartNumber,
       "portSfpRevision": portSfpRevision,
       "portSfpTemperature": portSfpTemperature,
       "portSfpVoltage": portSfpVoltage,
       "portSfpBiasCurrent": portSfpBiasCurrent,
       "portSfpTxOutPower": portSfpTxOutPower,
       "portSfpTxOutPowerDb": portSfpTxOutPowerDb,
       "portSfpRxOutPower": portSfpRxOutPower,
       "portSfpRxOutPowerDb": portSfpRxOutPowerDb,
       "sensorEntry": sensorEntry,
       "sensorConnected": sensorConnected,
       "sensorTemperature": sensorTemperature,
       "sensorHumidity": sensorHumidity,
       "integrations": integrations,
       "teleport": teleport,
       "trapsTLP": trapsTLP,
       "updateFirmwareTLP": updateFirmwareTLP,
       "setToDefaultTLP": setToDefaultTLP,
       "backupSettingsTLP": backupSettingsTLP,
       "systemWarmStartTLP": systemWarmStartTLP,
       "systemColdStartTLP": systemColdStartTLP,
       "webInterfaceLoginOkTLP": webInterfaceLoginOkTLP,
       "webInterfaceLoginFailTLP": webInterfaceLoginFailTLP,
       "emptyArpTableTLP": emptyArpTableTLP,
       "input1isChanged": input1isChanged,
       "input2isChanged": input2isChanged,
       "input3isChanged": input3isChanged,
       "input4isChanged": input4isChanged,
       "input5isChanged": input5isChanged,
       "input6isChanged": input6isChanged,
       "input7isChanged": input7isChanged,
       "input8isChanged": input8isChanged,
       "input9isChanged": input9isChanged,
       "output1isChanged": output1isChanged,
       "output2isChanged": output2isChanged,
       "output3isChanged": output3isChanged,
       "output4isChanged": output4isChanged,
       "output5isChanged": output5isChanged,
       "output6isChanged": output6isChanged,
       "output7isChanged": output7isChanged,
       "output8isChanged": output8isChanged,
       "output9isChanged": output9isChanged,
       "device1connFail": device1connFail,
       "device2connFail": device2connFail,
       "device3connFail": device3connFail,
       "device4connFail": device4connFail,
       "device5connFail": device5connFail,
       "device6connFail": device6connFail,
       "device7connFail": device7connFail,
       "device8connFail": device8connFail,
       "device9connFail": device9connFail,
       "device10connFail": device10connFail,
       "device11connFail": device11connFail,
       "device12connFail": device12connFail,
       "device13connFail": device13connFail,
       "device14connFail": device14connFail,
       "device15connFail": device15connFail,
       "device16connFail": device16connFail,
       "device17connFail": device17connFail,
       "device18connFail": device18connFail,
       "device19connFail": device19connFail,
       "device20connFail": device20connFail,
       "device21connFail": device21connFail,
       "device22connFail": device22connFail,
       "device23connFail": device23connFail,
       "device24connFail": device24connFail,
       "device25connFail": device25connFail,
       "device26connFail": device26connFail,
       "device27connFail": device27connFail,
       "device28connFail": device28connFail,
       "device29connFail": device29connFail,
       "device30connFail": device30connFail,
       "device31connFail": device31connFail,
       "device32connFail": device32connFail,
       "inputTeleport": inputTeleport,
       "inputStatusTableTLP": inputStatusTableTLP,
       "inputStatusEntryTLP": inputStatusEntryTLP,
       "inputIndexTLP": inputIndexTLP,
       "inputStateTLP": inputStateTLP,
       "outputTeleport": outputTeleport,
       "outputTeleportTable": outputTeleportTable,
       "outputTeleportEntry": outputTeleportEntry,
       "outIndex": outIndex,
       "outState": outState,
       "fwStatusTLP": fwStatusTLP,
       "fwVersionTLP": fwVersionTLP}
)
