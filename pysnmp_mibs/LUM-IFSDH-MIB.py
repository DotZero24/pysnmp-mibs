# SNMP MIB module (LUM-IFSDH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFSDH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:56 2025
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

(lumIfSdhMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfSdhMIB",
    "lumModules")

(DisplayStringWithNA,
 EnabledDisabledWithNA,
 FaultStatusWithNA,
 MgmtNameString,
 SignalStatusWithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "DisplayStringWithNA",
    "EnabledDisabledWithNA",
    "FaultStatusWithNA",
    "MgmtNameString",
    "SignalStatusWithNA",
    "Unsigned32WithNA")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumIfSdhMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 52)
)
if mibBuilder.loadTexts:
    lumIfSdhMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2015-01-23 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2013-05-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfSdhConfs_ObjectIdentity = ObjectIdentity
lumIfSdhConfs = _LumIfSdhConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 1)
)
_LumIfSdhGroups_ObjectIdentity = ObjectIdentity
lumIfSdhGroups = _LumIfSdhGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 1, 1)
)
_LumIfSdhCompl_ObjectIdentity = ObjectIdentity
lumIfSdhCompl = _LumIfSdhCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 1, 2)
)
_LumIfSdhMIBObjects_ObjectIdentity = ObjectIdentity
lumIfSdhMIBObjects = _LumIfSdhMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2)
)
_IfSdhGeneral_ObjectIdentity = ObjectIdentity
ifSdhGeneral = _IfSdhGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 1)
)
_IfSdhGeneralConfigLastChangeTime_Type = DateAndTime
_IfSdhGeneralConfigLastChangeTime_Object = MibScalar
ifSdhGeneralConfigLastChangeTime = _IfSdhGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 1, 1),
    _IfSdhGeneralConfigLastChangeTime_Type()
)
ifSdhGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhGeneralConfigLastChangeTime.setStatus("current")
_IfSdhGeneralStateLastChangeTime_Type = DateAndTime
_IfSdhGeneralStateLastChangeTime_Object = MibScalar
ifSdhGeneralStateLastChangeTime = _IfSdhGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 1, 2),
    _IfSdhGeneralStateLastChangeTime_Type()
)
ifSdhGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhGeneralStateLastChangeTime.setStatus("current")
_IfSdhGeneralIfSdhRsTableSize_Type = Unsigned32
_IfSdhGeneralIfSdhRsTableSize_Object = MibScalar
ifSdhGeneralIfSdhRsTableSize = _IfSdhGeneralIfSdhRsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 1, 3),
    _IfSdhGeneralIfSdhRsTableSize_Type()
)
ifSdhGeneralIfSdhRsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhGeneralIfSdhRsTableSize.setStatus("current")
_IfSdhGeneralIfSdhRsConfigLastChangeTime_Type = DateAndTime
_IfSdhGeneralIfSdhRsConfigLastChangeTime_Object = MibScalar
ifSdhGeneralIfSdhRsConfigLastChangeTime = _IfSdhGeneralIfSdhRsConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 1, 4),
    _IfSdhGeneralIfSdhRsConfigLastChangeTime_Type()
)
ifSdhGeneralIfSdhRsConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhGeneralIfSdhRsConfigLastChangeTime.setStatus("current")
_IfSdhGeneralIfSdhRsStateLastChangeTime_Type = DateAndTime
_IfSdhGeneralIfSdhRsStateLastChangeTime_Object = MibScalar
ifSdhGeneralIfSdhRsStateLastChangeTime = _IfSdhGeneralIfSdhRsStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 1, 5),
    _IfSdhGeneralIfSdhRsStateLastChangeTime_Type()
)
ifSdhGeneralIfSdhRsStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhGeneralIfSdhRsStateLastChangeTime.setStatus("current")
_IfSdhGeneralIfSdhMsTableSize_Type = Unsigned32
_IfSdhGeneralIfSdhMsTableSize_Object = MibScalar
ifSdhGeneralIfSdhMsTableSize = _IfSdhGeneralIfSdhMsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 1, 6),
    _IfSdhGeneralIfSdhMsTableSize_Type()
)
ifSdhGeneralIfSdhMsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhGeneralIfSdhMsTableSize.setStatus("current")
_IfSdhGeneralIfSdhMsConfigLastChangeTime_Type = DateAndTime
_IfSdhGeneralIfSdhMsConfigLastChangeTime_Object = MibScalar
ifSdhGeneralIfSdhMsConfigLastChangeTime = _IfSdhGeneralIfSdhMsConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 1, 7),
    _IfSdhGeneralIfSdhMsConfigLastChangeTime_Type()
)
ifSdhGeneralIfSdhMsConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhGeneralIfSdhMsConfigLastChangeTime.setStatus("current")
_IfSdhGeneralIfSdhMsStateLastChangeTime_Type = DateAndTime
_IfSdhGeneralIfSdhMsStateLastChangeTime_Object = MibScalar
ifSdhGeneralIfSdhMsStateLastChangeTime = _IfSdhGeneralIfSdhMsStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 1, 8),
    _IfSdhGeneralIfSdhMsStateLastChangeTime_Type()
)
ifSdhGeneralIfSdhMsStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhGeneralIfSdhMsStateLastChangeTime.setStatus("current")
_IfSdhRsList_ObjectIdentity = ObjectIdentity
ifSdhRsList = _IfSdhRsList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2)
)
_IfSdhRsTable_Object = MibTable
ifSdhRsTable = _IfSdhRsTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifSdhRsTable.setStatus("current")
_IfSdhRsEntry_Object = MibTableRow
ifSdhRsEntry = _IfSdhRsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1)
)
ifSdhRsEntry.setIndexNames(
    (0, "LUM-IFSDH-MIB", "ifSdhRsIndex"),
)
if mibBuilder.loadTexts:
    ifSdhRsEntry.setStatus("current")
_IfSdhRsIndex_Type = Unsigned32
_IfSdhRsIndex_Object = MibTableColumn
ifSdhRsIndex = _IfSdhRsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 1),
    _IfSdhRsIndex_Type()
)
ifSdhRsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsIndex.setStatus("current")
_IfSdhRsName_Type = MgmtNameString
_IfSdhRsName_Object = MibTableColumn
ifSdhRsName = _IfSdhRsName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 2),
    _IfSdhRsName_Type()
)
ifSdhRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsName.setStatus("current")
_IfSdhRsConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfSdhRsConnIfBasicIfIndex_Object = MibTableColumn
ifSdhRsConnIfBasicIfIndex = _IfSdhRsConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 3),
    _IfSdhRsConnIfBasicIfIndex_Type()
)
ifSdhRsConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsConnIfBasicIfIndex.setStatus("current")


class _IfSdhRsOhTransparencyBitmask_Type(Unsigned32WithNA):
    """Custom type ifSdhRsOhTransparencyBitmask based on Unsigned32WithNA"""
    defaultValue = 0


_IfSdhRsOhTransparencyBitmask_Type.__name__ = "Unsigned32WithNA"
_IfSdhRsOhTransparencyBitmask_Object = MibTableColumn
ifSdhRsOhTransparencyBitmask = _IfSdhRsOhTransparencyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 4),
    _IfSdhRsOhTransparencyBitmask_Type()
)
ifSdhRsOhTransparencyBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsOhTransparencyBitmask.setStatus("current")


class _IfSdhRsTraceTransmitted_Type(DisplayStringWithNA):
    """Custom type ifSdhRsTraceTransmitted based on DisplayStringWithNA"""
    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IfSdhRsTraceTransmitted_Type.__name__ = "DisplayStringWithNA"
_IfSdhRsTraceTransmitted_Object = MibTableColumn
ifSdhRsTraceTransmitted = _IfSdhRsTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 5),
    _IfSdhRsTraceTransmitted_Type()
)
ifSdhRsTraceTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsTraceTransmitted.setStatus("current")


class _IfSdhRsTraceReceived_Type(DisplayStringWithNA):
    """Custom type ifSdhRsTraceReceived based on DisplayStringWithNA"""
    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IfSdhRsTraceReceived_Type.__name__ = "DisplayStringWithNA"
_IfSdhRsTraceReceived_Object = MibTableColumn
ifSdhRsTraceReceived = _IfSdhRsTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 6),
    _IfSdhRsTraceReceived_Type()
)
ifSdhRsTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsTraceReceived.setStatus("current")


class _IfSdhRsTraceExpected_Type(DisplayStringWithNA):
    """Custom type ifSdhRsTraceExpected based on DisplayStringWithNA"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IfSdhRsTraceExpected_Type.__name__ = "DisplayStringWithNA"
_IfSdhRsTraceExpected_Object = MibTableColumn
ifSdhRsTraceExpected = _IfSdhRsTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 7),
    _IfSdhRsTraceExpected_Type()
)
ifSdhRsTraceExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsTraceExpected.setStatus("current")


class _IfSdhRsTraceAlarmMode_Type(EnabledDisabledWithNA):
    """Custom type ifSdhRsTraceAlarmMode based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfSdhRsTraceAlarmMode_Type.__name__ = "EnabledDisabledWithNA"
_IfSdhRsTraceAlarmMode_Object = MibTableColumn
ifSdhRsTraceAlarmMode = _IfSdhRsTraceAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 8),
    _IfSdhRsTraceAlarmMode_Type()
)
ifSdhRsTraceAlarmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsTraceAlarmMode.setStatus("current")
_IfSdhRsTxSignalStatus_Type = SignalStatusWithNA
_IfSdhRsTxSignalStatus_Object = MibTableColumn
ifSdhRsTxSignalStatus = _IfSdhRsTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 9),
    _IfSdhRsTxSignalStatus_Type()
)
ifSdhRsTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsTxSignalStatus.setStatus("current")
_IfSdhRsRxSignalStatus_Type = SignalStatusWithNA
_IfSdhRsRxSignalStatus_Object = MibTableColumn
ifSdhRsRxSignalStatus = _IfSdhRsRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 10),
    _IfSdhRsRxSignalStatus_Type()
)
ifSdhRsRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsRxSignalStatus.setStatus("current")
_IfSdhRsTraceMismatch_Type = FaultStatusWithNA
_IfSdhRsTraceMismatch_Object = MibTableColumn
ifSdhRsTraceMismatch = _IfSdhRsTraceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 11),
    _IfSdhRsTraceMismatch_Type()
)
ifSdhRsTraceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsTraceMismatch.setStatus("current")
_IfSdhRsLossOfFrame_Type = FaultStatusWithNA
_IfSdhRsLossOfFrame_Object = MibTableColumn
ifSdhRsLossOfFrame = _IfSdhRsLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 12),
    _IfSdhRsLossOfFrame_Type()
)
ifSdhRsLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsLossOfFrame.setStatus("current")
_IfSdhRsTxLossOfFrame_Type = FaultStatusWithNA
_IfSdhRsTxLossOfFrame_Object = MibTableColumn
ifSdhRsTxLossOfFrame = _IfSdhRsTxLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 2, 1, 1, 13),
    _IfSdhRsTxLossOfFrame_Type()
)
ifSdhRsTxLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhRsTxLossOfFrame.setStatus("current")
_IfSdhMsList_ObjectIdentity = ObjectIdentity
ifSdhMsList = _IfSdhMsList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3)
)
_IfSdhMsTable_Object = MibTable
ifSdhMsTable = _IfSdhMsTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifSdhMsTable.setStatus("current")
_IfSdhMsEntry_Object = MibTableRow
ifSdhMsEntry = _IfSdhMsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3, 1, 1)
)
ifSdhMsEntry.setIndexNames(
    (0, "LUM-IFSDH-MIB", "ifSdhMsIndex"),
)
if mibBuilder.loadTexts:
    ifSdhMsEntry.setStatus("current")
_IfSdhMsIndex_Type = Unsigned32
_IfSdhMsIndex_Object = MibTableColumn
ifSdhMsIndex = _IfSdhMsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3, 1, 1, 1),
    _IfSdhMsIndex_Type()
)
ifSdhMsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhMsIndex.setStatus("current")
_IfSdhMsName_Type = MgmtNameString
_IfSdhMsName_Object = MibTableColumn
ifSdhMsName = _IfSdhMsName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3, 1, 1, 2),
    _IfSdhMsName_Type()
)
ifSdhMsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhMsName.setStatus("current")
_IfSdhMsConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfSdhMsConnIfBasicIfIndex_Object = MibTableColumn
ifSdhMsConnIfBasicIfIndex = _IfSdhMsConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3, 1, 1, 3),
    _IfSdhMsConnIfBasicIfIndex_Type()
)
ifSdhMsConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhMsConnIfBasicIfIndex.setStatus("current")


class _IfSdhMsOhTransparencyBitmask_Type(Unsigned32WithNA):
    """Custom type ifSdhMsOhTransparencyBitmask based on Unsigned32WithNA"""
    defaultValue = 0


_IfSdhMsOhTransparencyBitmask_Type.__name__ = "Unsigned32WithNA"
_IfSdhMsOhTransparencyBitmask_Object = MibTableColumn
ifSdhMsOhTransparencyBitmask = _IfSdhMsOhTransparencyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3, 1, 1, 4),
    _IfSdhMsOhTransparencyBitmask_Type()
)
ifSdhMsOhTransparencyBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhMsOhTransparencyBitmask.setStatus("current")
_IfSdhMsTxSignalStatus_Type = SignalStatusWithNA
_IfSdhMsTxSignalStatus_Object = MibTableColumn
ifSdhMsTxSignalStatus = _IfSdhMsTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3, 1, 1, 5),
    _IfSdhMsTxSignalStatus_Type()
)
ifSdhMsTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhMsTxSignalStatus.setStatus("current")
_IfSdhMsRxSignalStatus_Type = SignalStatusWithNA
_IfSdhMsRxSignalStatus_Object = MibTableColumn
ifSdhMsRxSignalStatus = _IfSdhMsRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3, 1, 1, 6),
    _IfSdhMsRxSignalStatus_Type()
)
ifSdhMsRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhMsRxSignalStatus.setStatus("current")
_IfSdhMsRxAlarmIndicationSignal_Type = FaultStatusWithNA
_IfSdhMsRxAlarmIndicationSignal_Object = MibTableColumn
ifSdhMsRxAlarmIndicationSignal = _IfSdhMsRxAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3, 1, 1, 7),
    _IfSdhMsRxAlarmIndicationSignal_Type()
)
ifSdhMsRxAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhMsRxAlarmIndicationSignal.setStatus("current")
_IfSdhMsRemoteDefectIndication_Type = FaultStatusWithNA
_IfSdhMsRemoteDefectIndication_Object = MibTableColumn
ifSdhMsRemoteDefectIndication = _IfSdhMsRemoteDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3, 1, 1, 8),
    _IfSdhMsRemoteDefectIndication_Type()
)
ifSdhMsRemoteDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhMsRemoteDefectIndication.setStatus("current")
_IfSdhMsTxAlarmIndicationSignal_Type = FaultStatusWithNA
_IfSdhMsTxAlarmIndicationSignal_Object = MibTableColumn
ifSdhMsTxAlarmIndicationSignal = _IfSdhMsTxAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 3, 1, 1, 9),
    _IfSdhMsTxAlarmIndicationSignal_Type()
)
ifSdhMsTxAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSdhMsTxAlarmIndicationSignal.setStatus("current")
_IfSdhAuList_ObjectIdentity = ObjectIdentity
ifSdhAuList = _IfSdhAuList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 4)
)
_IfSdhVcList_ObjectIdentity = ObjectIdentity
ifSdhVcList = _IfSdhVcList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 2, 5)
)

# Managed Objects groups

ifSdhGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 1, 1, 1)
)
ifSdhGeneralGroupV1.setObjects(
      *(("LUM-IFSDH-MIB", "ifSdhGeneralConfigLastChangeTime"),
        ("LUM-IFSDH-MIB", "ifSdhGeneralStateLastChangeTime"),
        ("LUM-IFSDH-MIB", "ifSdhGeneralIfSdhRsTableSize"),
        ("LUM-IFSDH-MIB", "ifSdhGeneralIfSdhRsConfigLastChangeTime"),
        ("LUM-IFSDH-MIB", "ifSdhGeneralIfSdhRsStateLastChangeTime"),
        ("LUM-IFSDH-MIB", "ifSdhGeneralIfSdhMsTableSize"),
        ("LUM-IFSDH-MIB", "ifSdhGeneralIfSdhMsConfigLastChangeTime"),
        ("LUM-IFSDH-MIB", "ifSdhGeneralIfSdhMsStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifSdhGeneralGroupV1.setStatus("current")

ifSdhRsGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 1, 1, 2)
)
ifSdhRsGroupV1.setObjects(
      *(("LUM-IFSDH-MIB", "ifSdhRsIndex"),
        ("LUM-IFSDH-MIB", "ifSdhRsName"),
        ("LUM-IFSDH-MIB", "ifSdhRsConnIfBasicIfIndex"),
        ("LUM-IFSDH-MIB", "ifSdhRsOhTransparencyBitmask"),
        ("LUM-IFSDH-MIB", "ifSdhRsTraceTransmitted"),
        ("LUM-IFSDH-MIB", "ifSdhRsTraceReceived"),
        ("LUM-IFSDH-MIB", "ifSdhRsTraceExpected"),
        ("LUM-IFSDH-MIB", "ifSdhRsTraceAlarmMode"),
        ("LUM-IFSDH-MIB", "ifSdhRsTxSignalStatus"),
        ("LUM-IFSDH-MIB", "ifSdhRsRxSignalStatus"),
        ("LUM-IFSDH-MIB", "ifSdhRsTraceMismatch"),
        ("LUM-IFSDH-MIB", "ifSdhRsLossOfFrame"))
)
if mibBuilder.loadTexts:
    ifSdhRsGroupV1.setStatus("deprecated")

ifSdhMsGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 1, 1, 3)
)
ifSdhMsGroupV1.setObjects(
      *(("LUM-IFSDH-MIB", "ifSdhMsIndex"),
        ("LUM-IFSDH-MIB", "ifSdhMsName"),
        ("LUM-IFSDH-MIB", "ifSdhMsConnIfBasicIfIndex"),
        ("LUM-IFSDH-MIB", "ifSdhMsOhTransparencyBitmask"),
        ("LUM-IFSDH-MIB", "ifSdhMsTxSignalStatus"),
        ("LUM-IFSDH-MIB", "ifSdhMsRxSignalStatus"),
        ("LUM-IFSDH-MIB", "ifSdhMsRxAlarmIndicationSignal"),
        ("LUM-IFSDH-MIB", "ifSdhMsRemoteDefectIndication"))
)
if mibBuilder.loadTexts:
    ifSdhMsGroupV1.setStatus("deprecated")

ifSdhMsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 1, 1, 4)
)
ifSdhMsGroupV2.setObjects(
      *(("LUM-IFSDH-MIB", "ifSdhMsIndex"),
        ("LUM-IFSDH-MIB", "ifSdhMsName"),
        ("LUM-IFSDH-MIB", "ifSdhMsConnIfBasicIfIndex"),
        ("LUM-IFSDH-MIB", "ifSdhMsOhTransparencyBitmask"),
        ("LUM-IFSDH-MIB", "ifSdhMsTxSignalStatus"),
        ("LUM-IFSDH-MIB", "ifSdhMsRxSignalStatus"),
        ("LUM-IFSDH-MIB", "ifSdhMsRxAlarmIndicationSignal"),
        ("LUM-IFSDH-MIB", "ifSdhMsRemoteDefectIndication"),
        ("LUM-IFSDH-MIB", "ifSdhMsTxAlarmIndicationSignal"))
)
if mibBuilder.loadTexts:
    ifSdhMsGroupV2.setStatus("current")

ifSdhRsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 1, 1, 5)
)
ifSdhRsGroupV2.setObjects(
      *(("LUM-IFSDH-MIB", "ifSdhRsIndex"),
        ("LUM-IFSDH-MIB", "ifSdhRsName"),
        ("LUM-IFSDH-MIB", "ifSdhRsConnIfBasicIfIndex"),
        ("LUM-IFSDH-MIB", "ifSdhRsOhTransparencyBitmask"),
        ("LUM-IFSDH-MIB", "ifSdhRsTraceTransmitted"),
        ("LUM-IFSDH-MIB", "ifSdhRsTraceReceived"),
        ("LUM-IFSDH-MIB", "ifSdhRsTraceExpected"),
        ("LUM-IFSDH-MIB", "ifSdhRsTraceAlarmMode"),
        ("LUM-IFSDH-MIB", "ifSdhRsTxSignalStatus"),
        ("LUM-IFSDH-MIB", "ifSdhRsRxSignalStatus"),
        ("LUM-IFSDH-MIB", "ifSdhRsTraceMismatch"),
        ("LUM-IFSDH-MIB", "ifSdhRsLossOfFrame"),
        ("LUM-IFSDH-MIB", "ifSdhRsTxLossOfFrame"))
)
if mibBuilder.loadTexts:
    ifSdhRsGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfSdhComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 1, 2, 1)
)
lumIfSdhComplV1.setObjects(
      *(("LUM-IFSDH-MIB", "ifSdhGeneralGroupV1"),
        ("LUM-IFSDH-MIB", "ifSdhRsGroupV1"),
        ("LUM-IFSDH-MIB", "ifSdhMsGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfSdhComplV1.setStatus(
        "deprecated"
    )

lumIfSdhComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 1, 2, 2)
)
lumIfSdhComplV2.setObjects(
      *(("LUM-IFSDH-MIB", "ifSdhGeneralGroupV1"),
        ("LUM-IFSDH-MIB", "ifSdhRsGroupV1"),
        ("LUM-IFSDH-MIB", "ifSdhMsGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfSdhComplV2.setStatus(
        "deprecated"
    )

lumIfSdhComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 52, 1, 2, 3)
)
lumIfSdhComplV3.setObjects(
      *(("LUM-IFSDH-MIB", "ifSdhGeneralGroupV1"),
        ("LUM-IFSDH-MIB", "ifSdhRsGroupV2"),
        ("LUM-IFSDH-MIB", "ifSdhMsGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfSdhComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFSDH-MIB",
    **{"lumIfSdhMIBModule": lumIfSdhMIBModule,
       "lumIfSdhConfs": lumIfSdhConfs,
       "lumIfSdhGroups": lumIfSdhGroups,
       "ifSdhGeneralGroupV1": ifSdhGeneralGroupV1,
       "ifSdhRsGroupV1": ifSdhRsGroupV1,
       "ifSdhMsGroupV1": ifSdhMsGroupV1,
       "ifSdhMsGroupV2": ifSdhMsGroupV2,
       "ifSdhRsGroupV2": ifSdhRsGroupV2,
       "lumIfSdhCompl": lumIfSdhCompl,
       "lumIfSdhComplV1": lumIfSdhComplV1,
       "lumIfSdhComplV2": lumIfSdhComplV2,
       "lumIfSdhComplV3": lumIfSdhComplV3,
       "lumIfSdhMIBObjects": lumIfSdhMIBObjects,
       "ifSdhGeneral": ifSdhGeneral,
       "ifSdhGeneralConfigLastChangeTime": ifSdhGeneralConfigLastChangeTime,
       "ifSdhGeneralStateLastChangeTime": ifSdhGeneralStateLastChangeTime,
       "ifSdhGeneralIfSdhRsTableSize": ifSdhGeneralIfSdhRsTableSize,
       "ifSdhGeneralIfSdhRsConfigLastChangeTime": ifSdhGeneralIfSdhRsConfigLastChangeTime,
       "ifSdhGeneralIfSdhRsStateLastChangeTime": ifSdhGeneralIfSdhRsStateLastChangeTime,
       "ifSdhGeneralIfSdhMsTableSize": ifSdhGeneralIfSdhMsTableSize,
       "ifSdhGeneralIfSdhMsConfigLastChangeTime": ifSdhGeneralIfSdhMsConfigLastChangeTime,
       "ifSdhGeneralIfSdhMsStateLastChangeTime": ifSdhGeneralIfSdhMsStateLastChangeTime,
       "ifSdhRsList": ifSdhRsList,
       "ifSdhRsTable": ifSdhRsTable,
       "ifSdhRsEntry": ifSdhRsEntry,
       "ifSdhRsIndex": ifSdhRsIndex,
       "ifSdhRsName": ifSdhRsName,
       "ifSdhRsConnIfBasicIfIndex": ifSdhRsConnIfBasicIfIndex,
       "ifSdhRsOhTransparencyBitmask": ifSdhRsOhTransparencyBitmask,
       "ifSdhRsTraceTransmitted": ifSdhRsTraceTransmitted,
       "ifSdhRsTraceReceived": ifSdhRsTraceReceived,
       "ifSdhRsTraceExpected": ifSdhRsTraceExpected,
       "ifSdhRsTraceAlarmMode": ifSdhRsTraceAlarmMode,
       "ifSdhRsTxSignalStatus": ifSdhRsTxSignalStatus,
       "ifSdhRsRxSignalStatus": ifSdhRsRxSignalStatus,
       "ifSdhRsTraceMismatch": ifSdhRsTraceMismatch,
       "ifSdhRsLossOfFrame": ifSdhRsLossOfFrame,
       "ifSdhRsTxLossOfFrame": ifSdhRsTxLossOfFrame,
       "ifSdhMsList": ifSdhMsList,
       "ifSdhMsTable": ifSdhMsTable,
       "ifSdhMsEntry": ifSdhMsEntry,
       "ifSdhMsIndex": ifSdhMsIndex,
       "ifSdhMsName": ifSdhMsName,
       "ifSdhMsConnIfBasicIfIndex": ifSdhMsConnIfBasicIfIndex,
       "ifSdhMsOhTransparencyBitmask": ifSdhMsOhTransparencyBitmask,
       "ifSdhMsTxSignalStatus": ifSdhMsTxSignalStatus,
       "ifSdhMsRxSignalStatus": ifSdhMsRxSignalStatus,
       "ifSdhMsRxAlarmIndicationSignal": ifSdhMsRxAlarmIndicationSignal,
       "ifSdhMsRemoteDefectIndication": ifSdhMsRemoteDefectIndication,
       "ifSdhMsTxAlarmIndicationSignal": ifSdhMsTxAlarmIndicationSignal,
       "ifSdhAuList": ifSdhAuList,
       "ifSdhVcList": ifSdhVcList}
)
