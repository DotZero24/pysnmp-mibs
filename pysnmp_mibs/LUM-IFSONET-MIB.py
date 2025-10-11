# SNMP MIB module (LUM-IFSONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFSONET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:44 2025
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

(lumIfSonetMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfSonetMIB",
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

lumIfSonetMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 53)
)
if mibBuilder.loadTexts:
    lumIfSonetMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2015-01-23 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2013-05-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfSonetConfs_ObjectIdentity = ObjectIdentity
lumIfSonetConfs = _LumIfSonetConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 1)
)
_LumIfSonetGroups_ObjectIdentity = ObjectIdentity
lumIfSonetGroups = _LumIfSonetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 1, 1)
)
_LumIfSonetCompl_ObjectIdentity = ObjectIdentity
lumIfSonetCompl = _LumIfSonetCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 1, 2)
)
_LumIfSonetMIBObjects_ObjectIdentity = ObjectIdentity
lumIfSonetMIBObjects = _LumIfSonetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2)
)
_IfSonetGeneral_ObjectIdentity = ObjectIdentity
ifSonetGeneral = _IfSonetGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 1)
)
_IfSonetGeneralConfigLastChangeTime_Type = DateAndTime
_IfSonetGeneralConfigLastChangeTime_Object = MibScalar
ifSonetGeneralConfigLastChangeTime = _IfSonetGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 1, 1),
    _IfSonetGeneralConfigLastChangeTime_Type()
)
ifSonetGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetGeneralConfigLastChangeTime.setStatus("current")
_IfSonetGeneralStateLastChangeTime_Type = DateAndTime
_IfSonetGeneralStateLastChangeTime_Object = MibScalar
ifSonetGeneralStateLastChangeTime = _IfSonetGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 1, 2),
    _IfSonetGeneralStateLastChangeTime_Type()
)
ifSonetGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetGeneralStateLastChangeTime.setStatus("current")
_IfSonetGeneralIfSonetSectionTableSize_Type = Unsigned32
_IfSonetGeneralIfSonetSectionTableSize_Object = MibScalar
ifSonetGeneralIfSonetSectionTableSize = _IfSonetGeneralIfSonetSectionTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 1, 3),
    _IfSonetGeneralIfSonetSectionTableSize_Type()
)
ifSonetGeneralIfSonetSectionTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetGeneralIfSonetSectionTableSize.setStatus("current")
_IfSonetGeneralIfSonetSectionConfigLastChangeTime_Type = DateAndTime
_IfSonetGeneralIfSonetSectionConfigLastChangeTime_Object = MibScalar
ifSonetGeneralIfSonetSectionConfigLastChangeTime = _IfSonetGeneralIfSonetSectionConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 1, 4),
    _IfSonetGeneralIfSonetSectionConfigLastChangeTime_Type()
)
ifSonetGeneralIfSonetSectionConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetGeneralIfSonetSectionConfigLastChangeTime.setStatus("current")
_IfSonetGeneralIfSonetSectionStateLastChangeTime_Type = DateAndTime
_IfSonetGeneralIfSonetSectionStateLastChangeTime_Object = MibScalar
ifSonetGeneralIfSonetSectionStateLastChangeTime = _IfSonetGeneralIfSonetSectionStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 1, 5),
    _IfSonetGeneralIfSonetSectionStateLastChangeTime_Type()
)
ifSonetGeneralIfSonetSectionStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetGeneralIfSonetSectionStateLastChangeTime.setStatus("current")
_IfSonetGeneralIfSonetLineTableSize_Type = Unsigned32
_IfSonetGeneralIfSonetLineTableSize_Object = MibScalar
ifSonetGeneralIfSonetLineTableSize = _IfSonetGeneralIfSonetLineTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 1, 6),
    _IfSonetGeneralIfSonetLineTableSize_Type()
)
ifSonetGeneralIfSonetLineTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetGeneralIfSonetLineTableSize.setStatus("current")
_IfSonetGeneralIfSonetLineConfigLastChangeTime_Type = DateAndTime
_IfSonetGeneralIfSonetLineConfigLastChangeTime_Object = MibScalar
ifSonetGeneralIfSonetLineConfigLastChangeTime = _IfSonetGeneralIfSonetLineConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 1, 7),
    _IfSonetGeneralIfSonetLineConfigLastChangeTime_Type()
)
ifSonetGeneralIfSonetLineConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetGeneralIfSonetLineConfigLastChangeTime.setStatus("current")
_IfSonetGeneralIfSonetLineStateLastChangeTime_Type = DateAndTime
_IfSonetGeneralIfSonetLineStateLastChangeTime_Object = MibScalar
ifSonetGeneralIfSonetLineStateLastChangeTime = _IfSonetGeneralIfSonetLineStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 1, 8),
    _IfSonetGeneralIfSonetLineStateLastChangeTime_Type()
)
ifSonetGeneralIfSonetLineStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetGeneralIfSonetLineStateLastChangeTime.setStatus("current")
_IfSonetSectionList_ObjectIdentity = ObjectIdentity
ifSonetSectionList = _IfSonetSectionList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2)
)
_IfSonetSectionTable_Object = MibTable
ifSonetSectionTable = _IfSonetSectionTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifSonetSectionTable.setStatus("current")
_IfSonetSectionEntry_Object = MibTableRow
ifSonetSectionEntry = _IfSonetSectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1)
)
ifSonetSectionEntry.setIndexNames(
    (0, "LUM-IFSONET-MIB", "ifSonetSectionIndex"),
)
if mibBuilder.loadTexts:
    ifSonetSectionEntry.setStatus("current")
_IfSonetSectionIndex_Type = Unsigned32
_IfSonetSectionIndex_Object = MibTableColumn
ifSonetSectionIndex = _IfSonetSectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 1),
    _IfSonetSectionIndex_Type()
)
ifSonetSectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionIndex.setStatus("current")
_IfSonetSectionName_Type = MgmtNameString
_IfSonetSectionName_Object = MibTableColumn
ifSonetSectionName = _IfSonetSectionName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 2),
    _IfSonetSectionName_Type()
)
ifSonetSectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionName.setStatus("current")
_IfSonetSectionConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfSonetSectionConnIfBasicIfIndex_Object = MibTableColumn
ifSonetSectionConnIfBasicIfIndex = _IfSonetSectionConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 3),
    _IfSonetSectionConnIfBasicIfIndex_Type()
)
ifSonetSectionConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionConnIfBasicIfIndex.setStatus("current")


class _IfSonetSectionOhTransparencyBitmask_Type(Unsigned32WithNA):
    """Custom type ifSonetSectionOhTransparencyBitmask based on Unsigned32WithNA"""
    defaultValue = 0


_IfSonetSectionOhTransparencyBitmask_Type.__name__ = "Unsigned32WithNA"
_IfSonetSectionOhTransparencyBitmask_Object = MibTableColumn
ifSonetSectionOhTransparencyBitmask = _IfSonetSectionOhTransparencyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 4),
    _IfSonetSectionOhTransparencyBitmask_Type()
)
ifSonetSectionOhTransparencyBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionOhTransparencyBitmask.setStatus("current")


class _IfSonetSectionTraceTransmitted_Type(DisplayStringWithNA):
    """Custom type ifSonetSectionTraceTransmitted based on DisplayStringWithNA"""
    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IfSonetSectionTraceTransmitted_Type.__name__ = "DisplayStringWithNA"
_IfSonetSectionTraceTransmitted_Object = MibTableColumn
ifSonetSectionTraceTransmitted = _IfSonetSectionTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 5),
    _IfSonetSectionTraceTransmitted_Type()
)
ifSonetSectionTraceTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionTraceTransmitted.setStatus("current")


class _IfSonetSectionTraceReceived_Type(DisplayStringWithNA):
    """Custom type ifSonetSectionTraceReceived based on DisplayStringWithNA"""
    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IfSonetSectionTraceReceived_Type.__name__ = "DisplayStringWithNA"
_IfSonetSectionTraceReceived_Object = MibTableColumn
ifSonetSectionTraceReceived = _IfSonetSectionTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 6),
    _IfSonetSectionTraceReceived_Type()
)
ifSonetSectionTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionTraceReceived.setStatus("current")


class _IfSonetSectionTraceExpected_Type(DisplayStringWithNA):
    """Custom type ifSonetSectionTraceExpected based on DisplayStringWithNA"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayStringWithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IfSonetSectionTraceExpected_Type.__name__ = "DisplayStringWithNA"
_IfSonetSectionTraceExpected_Object = MibTableColumn
ifSonetSectionTraceExpected = _IfSonetSectionTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 7),
    _IfSonetSectionTraceExpected_Type()
)
ifSonetSectionTraceExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionTraceExpected.setStatus("current")


class _IfSonetSectionTraceAlarmMode_Type(EnabledDisabledWithNA):
    """Custom type ifSonetSectionTraceAlarmMode based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfSonetSectionTraceAlarmMode_Type.__name__ = "EnabledDisabledWithNA"
_IfSonetSectionTraceAlarmMode_Object = MibTableColumn
ifSonetSectionTraceAlarmMode = _IfSonetSectionTraceAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 8),
    _IfSonetSectionTraceAlarmMode_Type()
)
ifSonetSectionTraceAlarmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionTraceAlarmMode.setStatus("current")
_IfSonetSectionTxSignalStatus_Type = SignalStatusWithNA
_IfSonetSectionTxSignalStatus_Object = MibTableColumn
ifSonetSectionTxSignalStatus = _IfSonetSectionTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 9),
    _IfSonetSectionTxSignalStatus_Type()
)
ifSonetSectionTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionTxSignalStatus.setStatus("current")
_IfSonetSectionRxSignalStatus_Type = SignalStatusWithNA
_IfSonetSectionRxSignalStatus_Object = MibTableColumn
ifSonetSectionRxSignalStatus = _IfSonetSectionRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 10),
    _IfSonetSectionRxSignalStatus_Type()
)
ifSonetSectionRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionRxSignalStatus.setStatus("current")
_IfSonetSectionTraceMismatch_Type = FaultStatusWithNA
_IfSonetSectionTraceMismatch_Object = MibTableColumn
ifSonetSectionTraceMismatch = _IfSonetSectionTraceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 11),
    _IfSonetSectionTraceMismatch_Type()
)
ifSonetSectionTraceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionTraceMismatch.setStatus("current")
_IfSonetSectionLossOfFrame_Type = FaultStatusWithNA
_IfSonetSectionLossOfFrame_Object = MibTableColumn
ifSonetSectionLossOfFrame = _IfSonetSectionLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 12),
    _IfSonetSectionLossOfFrame_Type()
)
ifSonetSectionLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionLossOfFrame.setStatus("current")
_IfSonetSectionTxLossOfFrame_Type = FaultStatusWithNA
_IfSonetSectionTxLossOfFrame_Object = MibTableColumn
ifSonetSectionTxLossOfFrame = _IfSonetSectionTxLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 2, 1, 1, 13),
    _IfSonetSectionTxLossOfFrame_Type()
)
ifSonetSectionTxLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetSectionTxLossOfFrame.setStatus("current")
_IfSonetLineList_ObjectIdentity = ObjectIdentity
ifSonetLineList = _IfSonetLineList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3)
)
_IfSonetLineTable_Object = MibTable
ifSonetLineTable = _IfSonetLineTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifSonetLineTable.setStatus("current")
_IfSonetLineEntry_Object = MibTableRow
ifSonetLineEntry = _IfSonetLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3, 1, 1)
)
ifSonetLineEntry.setIndexNames(
    (0, "LUM-IFSONET-MIB", "ifSonetLineIndex"),
)
if mibBuilder.loadTexts:
    ifSonetLineEntry.setStatus("current")
_IfSonetLineIndex_Type = Unsigned32
_IfSonetLineIndex_Object = MibTableColumn
ifSonetLineIndex = _IfSonetLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3, 1, 1, 1),
    _IfSonetLineIndex_Type()
)
ifSonetLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetLineIndex.setStatus("current")
_IfSonetLineName_Type = MgmtNameString
_IfSonetLineName_Object = MibTableColumn
ifSonetLineName = _IfSonetLineName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3, 1, 1, 2),
    _IfSonetLineName_Type()
)
ifSonetLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetLineName.setStatus("current")
_IfSonetLineConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfSonetLineConnIfBasicIfIndex_Object = MibTableColumn
ifSonetLineConnIfBasicIfIndex = _IfSonetLineConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3, 1, 1, 3),
    _IfSonetLineConnIfBasicIfIndex_Type()
)
ifSonetLineConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetLineConnIfBasicIfIndex.setStatus("current")


class _IfSonetLineOhTransparencyBitmask_Type(Unsigned32WithNA):
    """Custom type ifSonetLineOhTransparencyBitmask based on Unsigned32WithNA"""
    defaultValue = 0


_IfSonetLineOhTransparencyBitmask_Type.__name__ = "Unsigned32WithNA"
_IfSonetLineOhTransparencyBitmask_Object = MibTableColumn
ifSonetLineOhTransparencyBitmask = _IfSonetLineOhTransparencyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3, 1, 1, 4),
    _IfSonetLineOhTransparencyBitmask_Type()
)
ifSonetLineOhTransparencyBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetLineOhTransparencyBitmask.setStatus("current")
_IfSonetLineTxSignalStatus_Type = SignalStatusWithNA
_IfSonetLineTxSignalStatus_Object = MibTableColumn
ifSonetLineTxSignalStatus = _IfSonetLineTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3, 1, 1, 5),
    _IfSonetLineTxSignalStatus_Type()
)
ifSonetLineTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetLineTxSignalStatus.setStatus("current")
_IfSonetLineRxSignalStatus_Type = SignalStatusWithNA
_IfSonetLineRxSignalStatus_Object = MibTableColumn
ifSonetLineRxSignalStatus = _IfSonetLineRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3, 1, 1, 6),
    _IfSonetLineRxSignalStatus_Type()
)
ifSonetLineRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetLineRxSignalStatus.setStatus("current")
_IfSonetLineRxAlarmIndicationSignal_Type = FaultStatusWithNA
_IfSonetLineRxAlarmIndicationSignal_Object = MibTableColumn
ifSonetLineRxAlarmIndicationSignal = _IfSonetLineRxAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3, 1, 1, 7),
    _IfSonetLineRxAlarmIndicationSignal_Type()
)
ifSonetLineRxAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetLineRxAlarmIndicationSignal.setStatus("current")
_IfSonetLineRemoteDefectIndication_Type = FaultStatusWithNA
_IfSonetLineRemoteDefectIndication_Object = MibTableColumn
ifSonetLineRemoteDefectIndication = _IfSonetLineRemoteDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3, 1, 1, 8),
    _IfSonetLineRemoteDefectIndication_Type()
)
ifSonetLineRemoteDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetLineRemoteDefectIndication.setStatus("current")
_IfSonetLineTxAlarmIndicationSignal_Type = FaultStatusWithNA
_IfSonetLineTxAlarmIndicationSignal_Object = MibTableColumn
ifSonetLineTxAlarmIndicationSignal = _IfSonetLineTxAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 3, 1, 1, 9),
    _IfSonetLineTxAlarmIndicationSignal_Type()
)
ifSonetLineTxAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSonetLineTxAlarmIndicationSignal.setStatus("current")
_IfSonetStsList_ObjectIdentity = ObjectIdentity
ifSonetStsList = _IfSonetStsList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 4)
)
_IfSonetStsSpeList_ObjectIdentity = ObjectIdentity
ifSonetStsSpeList = _IfSonetStsSpeList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 2, 5)
)

# Managed Objects groups

ifSonetGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 1, 1, 1)
)
ifSonetGeneralGroupV1.setObjects(
      *(("LUM-IFSONET-MIB", "ifSonetGeneralConfigLastChangeTime"),
        ("LUM-IFSONET-MIB", "ifSonetGeneralStateLastChangeTime"),
        ("LUM-IFSONET-MIB", "ifSonetGeneralIfSonetSectionTableSize"),
        ("LUM-IFSONET-MIB", "ifSonetGeneralIfSonetSectionConfigLastChangeTime"),
        ("LUM-IFSONET-MIB", "ifSonetGeneralIfSonetSectionStateLastChangeTime"),
        ("LUM-IFSONET-MIB", "ifSonetGeneralIfSonetLineTableSize"),
        ("LUM-IFSONET-MIB", "ifSonetGeneralIfSonetLineConfigLastChangeTime"),
        ("LUM-IFSONET-MIB", "ifSonetGeneralIfSonetLineStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifSonetGeneralGroupV1.setStatus("current")

ifSonetSectionGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 1, 1, 2)
)
ifSonetSectionGroupV1.setObjects(
      *(("LUM-IFSONET-MIB", "ifSonetSectionIndex"),
        ("LUM-IFSONET-MIB", "ifSonetSectionName"),
        ("LUM-IFSONET-MIB", "ifSonetSectionConnIfBasicIfIndex"),
        ("LUM-IFSONET-MIB", "ifSonetSectionOhTransparencyBitmask"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTraceTransmitted"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTraceReceived"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTraceExpected"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTraceAlarmMode"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTxSignalStatus"),
        ("LUM-IFSONET-MIB", "ifSonetSectionRxSignalStatus"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTraceMismatch"),
        ("LUM-IFSONET-MIB", "ifSonetSectionLossOfFrame"))
)
if mibBuilder.loadTexts:
    ifSonetSectionGroupV1.setStatus("deprecated")

ifSonetLineGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 1, 1, 3)
)
ifSonetLineGroupV1.setObjects(
      *(("LUM-IFSONET-MIB", "ifSonetLineIndex"),
        ("LUM-IFSONET-MIB", "ifSonetLineName"),
        ("LUM-IFSONET-MIB", "ifSonetLineConnIfBasicIfIndex"),
        ("LUM-IFSONET-MIB", "ifSonetLineOhTransparencyBitmask"),
        ("LUM-IFSONET-MIB", "ifSonetLineTxSignalStatus"),
        ("LUM-IFSONET-MIB", "ifSonetLineRxSignalStatus"),
        ("LUM-IFSONET-MIB", "ifSonetLineRxAlarmIndicationSignal"),
        ("LUM-IFSONET-MIB", "ifSonetLineRemoteDefectIndication"))
)
if mibBuilder.loadTexts:
    ifSonetLineGroupV1.setStatus("deprecated")

ifSonetLineGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 1, 1, 4)
)
ifSonetLineGroupV2.setObjects(
      *(("LUM-IFSONET-MIB", "ifSonetLineIndex"),
        ("LUM-IFSONET-MIB", "ifSonetLineName"),
        ("LUM-IFSONET-MIB", "ifSonetLineConnIfBasicIfIndex"),
        ("LUM-IFSONET-MIB", "ifSonetLineOhTransparencyBitmask"),
        ("LUM-IFSONET-MIB", "ifSonetLineTxSignalStatus"),
        ("LUM-IFSONET-MIB", "ifSonetLineRxSignalStatus"),
        ("LUM-IFSONET-MIB", "ifSonetLineRxAlarmIndicationSignal"),
        ("LUM-IFSONET-MIB", "ifSonetLineRemoteDefectIndication"),
        ("LUM-IFSONET-MIB", "ifSonetLineTxAlarmIndicationSignal"))
)
if mibBuilder.loadTexts:
    ifSonetLineGroupV2.setStatus("current")

ifSonetSectionGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 1, 1, 5)
)
ifSonetSectionGroupV2.setObjects(
      *(("LUM-IFSONET-MIB", "ifSonetSectionIndex"),
        ("LUM-IFSONET-MIB", "ifSonetSectionName"),
        ("LUM-IFSONET-MIB", "ifSonetSectionConnIfBasicIfIndex"),
        ("LUM-IFSONET-MIB", "ifSonetSectionOhTransparencyBitmask"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTraceTransmitted"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTraceReceived"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTraceExpected"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTraceAlarmMode"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTxSignalStatus"),
        ("LUM-IFSONET-MIB", "ifSonetSectionRxSignalStatus"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTraceMismatch"),
        ("LUM-IFSONET-MIB", "ifSonetSectionLossOfFrame"),
        ("LUM-IFSONET-MIB", "ifSonetSectionTxLossOfFrame"))
)
if mibBuilder.loadTexts:
    ifSonetSectionGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfSonetComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 1, 2, 1)
)
lumIfSonetComplV1.setObjects(
      *(("LUM-IFSONET-MIB", "ifSonetGeneralGroupV1"),
        ("LUM-IFSONET-MIB", "ifSonetSectionGroupV1"),
        ("LUM-IFSONET-MIB", "ifSonetLineGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfSonetComplV1.setStatus(
        "deprecated"
    )

lumIfSonetComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 1, 2, 2)
)
lumIfSonetComplV2.setObjects(
      *(("LUM-IFSONET-MIB", "ifSonetGeneralGroupV1"),
        ("LUM-IFSONET-MIB", "ifSonetSectionGroupV1"),
        ("LUM-IFSONET-MIB", "ifSonetLineGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfSonetComplV2.setStatus(
        "deprecated"
    )

lumIfSonetComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 53, 1, 2, 3)
)
lumIfSonetComplV3.setObjects(
      *(("LUM-IFSONET-MIB", "ifSonetGeneralGroupV1"),
        ("LUM-IFSONET-MIB", "ifSonetSectionGroupV2"),
        ("LUM-IFSONET-MIB", "ifSonetLineGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfSonetComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFSONET-MIB",
    **{"lumIfSonetMIBModule": lumIfSonetMIBModule,
       "lumIfSonetConfs": lumIfSonetConfs,
       "lumIfSonetGroups": lumIfSonetGroups,
       "ifSonetGeneralGroupV1": ifSonetGeneralGroupV1,
       "ifSonetSectionGroupV1": ifSonetSectionGroupV1,
       "ifSonetLineGroupV1": ifSonetLineGroupV1,
       "ifSonetLineGroupV2": ifSonetLineGroupV2,
       "ifSonetSectionGroupV2": ifSonetSectionGroupV2,
       "lumIfSonetCompl": lumIfSonetCompl,
       "lumIfSonetComplV1": lumIfSonetComplV1,
       "lumIfSonetComplV2": lumIfSonetComplV2,
       "lumIfSonetComplV3": lumIfSonetComplV3,
       "lumIfSonetMIBObjects": lumIfSonetMIBObjects,
       "ifSonetGeneral": ifSonetGeneral,
       "ifSonetGeneralConfigLastChangeTime": ifSonetGeneralConfigLastChangeTime,
       "ifSonetGeneralStateLastChangeTime": ifSonetGeneralStateLastChangeTime,
       "ifSonetGeneralIfSonetSectionTableSize": ifSonetGeneralIfSonetSectionTableSize,
       "ifSonetGeneralIfSonetSectionConfigLastChangeTime": ifSonetGeneralIfSonetSectionConfigLastChangeTime,
       "ifSonetGeneralIfSonetSectionStateLastChangeTime": ifSonetGeneralIfSonetSectionStateLastChangeTime,
       "ifSonetGeneralIfSonetLineTableSize": ifSonetGeneralIfSonetLineTableSize,
       "ifSonetGeneralIfSonetLineConfigLastChangeTime": ifSonetGeneralIfSonetLineConfigLastChangeTime,
       "ifSonetGeneralIfSonetLineStateLastChangeTime": ifSonetGeneralIfSonetLineStateLastChangeTime,
       "ifSonetSectionList": ifSonetSectionList,
       "ifSonetSectionTable": ifSonetSectionTable,
       "ifSonetSectionEntry": ifSonetSectionEntry,
       "ifSonetSectionIndex": ifSonetSectionIndex,
       "ifSonetSectionName": ifSonetSectionName,
       "ifSonetSectionConnIfBasicIfIndex": ifSonetSectionConnIfBasicIfIndex,
       "ifSonetSectionOhTransparencyBitmask": ifSonetSectionOhTransparencyBitmask,
       "ifSonetSectionTraceTransmitted": ifSonetSectionTraceTransmitted,
       "ifSonetSectionTraceReceived": ifSonetSectionTraceReceived,
       "ifSonetSectionTraceExpected": ifSonetSectionTraceExpected,
       "ifSonetSectionTraceAlarmMode": ifSonetSectionTraceAlarmMode,
       "ifSonetSectionTxSignalStatus": ifSonetSectionTxSignalStatus,
       "ifSonetSectionRxSignalStatus": ifSonetSectionRxSignalStatus,
       "ifSonetSectionTraceMismatch": ifSonetSectionTraceMismatch,
       "ifSonetSectionLossOfFrame": ifSonetSectionLossOfFrame,
       "ifSonetSectionTxLossOfFrame": ifSonetSectionTxLossOfFrame,
       "ifSonetLineList": ifSonetLineList,
       "ifSonetLineTable": ifSonetLineTable,
       "ifSonetLineEntry": ifSonetLineEntry,
       "ifSonetLineIndex": ifSonetLineIndex,
       "ifSonetLineName": ifSonetLineName,
       "ifSonetLineConnIfBasicIfIndex": ifSonetLineConnIfBasicIfIndex,
       "ifSonetLineOhTransparencyBitmask": ifSonetLineOhTransparencyBitmask,
       "ifSonetLineTxSignalStatus": ifSonetLineTxSignalStatus,
       "ifSonetLineRxSignalStatus": ifSonetLineRxSignalStatus,
       "ifSonetLineRxAlarmIndicationSignal": ifSonetLineRxAlarmIndicationSignal,
       "ifSonetLineRemoteDefectIndication": ifSonetLineRemoteDefectIndication,
       "ifSonetLineTxAlarmIndicationSignal": ifSonetLineTxAlarmIndicationSignal,
       "ifSonetStsList": ifSonetStsList,
       "ifSonetStsSpeList": ifSonetStsSpeList}
)
