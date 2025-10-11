# SNMP MIB module (BRCM-BFC-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-BFC-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:46 2025
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

(cableDataMgmtMIBObjects,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-MGMT-MIB",
    "cableDataMgmtMIBObjects")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bfcMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9)
)
if mibBuilder.loadTexts:
    bfcMgmt.setRevisions(
        ("2011-04-20 00:00",
         "2010-02-01 00:00",
         "2009-08-26 00:00",
         "2009-06-30 00:00",
         "2008-06-30 00:00",
         "2007-02-05 00:00",
         "2006-09-05 00:00",
         "2005-05-05 00:00",
         "2003-12-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BfcMgmtBase_ObjectIdentity = ObjectIdentity
bfcMgmtBase = _BfcMgmtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1)
)
_BfcSoftware_ObjectIdentity = ObjectIdentity
bfcSoftware = _BfcSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1)
)
_BfcSwDateTime_Type = DisplayString
_BfcSwDateTime_Object = MibScalar
bfcSwDateTime = _BfcSwDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 1),
    _BfcSwDateTime_Type()
)
bfcSwDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcSwDateTime.setStatus("current")
_BfcSwBuiltBy_Type = DisplayString
_BfcSwBuiltBy_Object = MibScalar
bfcSwBuiltBy = _BfcSwBuiltBy_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 2),
    _BfcSwBuiltBy_Type()
)
bfcSwBuiltBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcSwBuiltBy.setStatus("current")
_BfcSwOperatingSystem_Type = DisplayString
_BfcSwOperatingSystem_Object = MibScalar
bfcSwOperatingSystem = _BfcSwOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 3),
    _BfcSwOperatingSystem_Type()
)
bfcSwOperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcSwOperatingSystem.setStatus("current")
_BfcSwSnmpAgent_Type = DisplayString
_BfcSwSnmpAgent_Object = MibScalar
bfcSwSnmpAgent = _BfcSwSnmpAgent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 4),
    _BfcSwSnmpAgent_Type()
)
bfcSwSnmpAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcSwSnmpAgent.setStatus("current")
_BfcApplicationTable_Object = MibTable
bfcApplicationTable = _BfcApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 5)
)
if mibBuilder.loadTexts:
    bfcApplicationTable.setStatus("current")
_BfcApplicationEntry_Object = MibTableRow
bfcApplicationEntry = _BfcApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 5, 1)
)
bfcApplicationEntry.setIndexNames(
    (0, "BRCM-BFC-MGMT-MIB", "bfcAppIndex"),
)
if mibBuilder.loadTexts:
    bfcApplicationEntry.setStatus("current")


class _BfcAppIndex_Type(Integer32):
    """Custom type bfcAppIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BfcAppIndex_Type.__name__ = "Integer32"
_BfcAppIndex_Object = MibTableColumn
bfcAppIndex = _BfcAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 5, 1, 1),
    _BfcAppIndex_Type()
)
bfcAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfcAppIndex.setStatus("current")
_BfcAppName_Type = DisplayString
_BfcAppName_Object = MibTableColumn
bfcAppName = _BfcAppName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 5, 1, 2),
    _BfcAppName_Type()
)
bfcAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcAppName.setStatus("current")
_BfcAppVersion_Type = DisplayString
_BfcAppVersion_Object = MibTableColumn
bfcAppVersion = _BfcAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 5, 1, 3),
    _BfcAppVersion_Type()
)
bfcAppVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcAppVersion.setStatus("current")


class _BfcAppReleaseState_Type(Integer32):
    """Custom type bfcAppReleaseState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("release", 1),
          ("preRelease", 2))
    )


_BfcAppReleaseState_Type.__name__ = "Integer32"
_BfcAppReleaseState_Object = MibTableColumn
bfcAppReleaseState = _BfcAppReleaseState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 5, 1, 4),
    _BfcAppReleaseState_Type()
)
bfcAppReleaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcAppReleaseState.setStatus("current")
_BfcAppFeatures_Type = DisplayString
_BfcAppFeatures_Object = MibTableColumn
bfcAppFeatures = _BfcAppFeatures_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 5, 1, 5),
    _BfcAppFeatures_Type()
)
bfcAppFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcAppFeatures.setStatus("current")
_BfcSwNumBoots_Type = Unsigned32
_BfcSwNumBoots_Object = MibScalar
bfcSwNumBoots = _BfcSwNumBoots_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 6),
    _BfcSwNumBoots_Type()
)
bfcSwNumBoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcSwNumBoots.setStatus("current")
_BfcSwImageName_Type = DisplayString
_BfcSwImageName_Object = MibScalar
bfcSwImageName = _BfcSwImageName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 7),
    _BfcSwImageName_Type()
)
bfcSwImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcSwImageName.setStatus("current")
_BfcSwImagePath_Type = DisplayString
_BfcSwImagePath_Object = MibScalar
bfcSwImagePath = _BfcSwImagePath_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 1, 8),
    _BfcSwImagePath_Type()
)
bfcSwImagePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcSwImagePath.setStatus("current")
_BfcSystem_ObjectIdentity = ObjectIdentity
bfcSystem = _BfcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 2)
)


class _BfcSerialConsoleMode_Type(Integer32):
    """Custom type bfcSerialConsoleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_BfcSerialConsoleMode_Type.__name__ = "Integer32"
_BfcSerialConsoleMode_Object = MibScalar
bfcSerialConsoleMode = _BfcSerialConsoleMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 2, 1),
    _BfcSerialConsoleMode_Type()
)
bfcSerialConsoleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfcSerialConsoleMode.setStatus("current")
_BfcMemoryAvailable_Type = Gauge32
_BfcMemoryAvailable_Object = MibScalar
bfcMemoryAvailable = _BfcMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 2, 2),
    _BfcMemoryAvailable_Type()
)
bfcMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcMemoryAvailable.setStatus("current")
if mibBuilder.loadTexts:
    bfcMemoryAvailable.setUnits("Bytes")
_BfcMemoryLargestBlock_Type = Gauge32
_BfcMemoryLargestBlock_Object = MibScalar
bfcMemoryLargestBlock = _BfcMemoryLargestBlock_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 2, 3),
    _BfcMemoryLargestBlock_Type()
)
bfcMemoryLargestBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcMemoryLargestBlock.setStatus("current")
if mibBuilder.loadTexts:
    bfcMemoryLargestBlock.setUnits("Bytes")
_BfcMemoryLowWater_Type = Gauge32
_BfcMemoryLowWater_Object = MibScalar
bfcMemoryLowWater = _BfcMemoryLowWater_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 2, 4),
    _BfcMemoryLowWater_Type()
)
bfcMemoryLowWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcMemoryLowWater.setStatus("current")
if mibBuilder.loadTexts:
    bfcMemoryLowWater.setUnits("Bytes")


class _BfcMemoryFragmentation_Type(Integer32):
    """Custom type bfcMemoryFragmentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BfcMemoryFragmentation_Type.__name__ = "Integer32"
_BfcMemoryFragmentation_Object = MibScalar
bfcMemoryFragmentation = _BfcMemoryFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 2, 5),
    _BfcMemoryFragmentation_Type()
)
bfcMemoryFragmentation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcMemoryFragmentation.setStatus("current")
if mibBuilder.loadTexts:
    bfcMemoryFragmentation.setUnits("percent")
_BfcEventLog_ObjectIdentity = ObjectIdentity
bfcEventLog = _BfcEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3)
)
_BfcEvents_ObjectIdentity = ObjectIdentity
bfcEvents = _BfcEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 1)
)
_BfcSystemEvents_ObjectIdentity = ObjectIdentity
bfcSystemEvents = _BfcSystemEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 1, 1)
)
_BfcSystemEvent_ObjectIdentity = ObjectIdentity
bfcSystemEvent = _BfcSystemEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bfcSystemEvent.setStatus("current")
_BfcSystemResetEvent_ObjectIdentity = ObjectIdentity
bfcSystemResetEvent = _BfcSystemResetEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    bfcSystemResetEvent.setStatus("current")
_BfcSystemTransientEvent_ObjectIdentity = ObjectIdentity
bfcSystemTransientEvent = _BfcSystemTransientEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    bfcSystemTransientEvent.setStatus("current")
_BfcEventLogTable_Object = MibTable
bfcEventLogTable = _BfcEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    bfcEventLogTable.setStatus("current")
_BfcEventLogEntry_Object = MibTableRow
bfcEventLogEntry = _BfcEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 2, 1)
)
bfcEventLogEntry.setIndexNames(
    (0, "BRCM-BFC-MGMT-MIB", "bfcEventId"),
    (0, "BRCM-BFC-MGMT-MIB", "bfcEventIndex"),
)
if mibBuilder.loadTexts:
    bfcEventLogEntry.setStatus("current")
_BfcEventId_Type = AutonomousType
_BfcEventId_Object = MibTableColumn
bfcEventId = _BfcEventId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 2, 1, 1),
    _BfcEventId_Type()
)
bfcEventId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfcEventId.setStatus("current")


class _BfcEventIndex_Type(Integer32):
    """Custom type bfcEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BfcEventIndex_Type.__name__ = "Integer32"
_BfcEventIndex_Object = MibTableColumn
bfcEventIndex = _BfcEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 2, 1, 2),
    _BfcEventIndex_Type()
)
bfcEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bfcEventIndex.setStatus("current")
_BfcEventTime_Type = DateAndTime
_BfcEventTime_Object = MibTableColumn
bfcEventTime = _BfcEventTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 2, 1, 3),
    _BfcEventTime_Type()
)
bfcEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcEventTime.setStatus("current")
_BfcEventText_Type = DisplayString
_BfcEventText_Object = MibTableColumn
bfcEventText = _BfcEventText_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 2, 1, 4),
    _BfcEventText_Type()
)
bfcEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfcEventText.setStatus("current")
_BfcEventLogReset_Type = TruthValue
_BfcEventLogReset_Object = MibScalar
bfcEventLogReset = _BfcEventLogReset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 3),
    _BfcEventLogReset_Type()
)
bfcEventLogReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfcEventLogReset.setStatus("current")
_BfcEventLogTransientEvent_Type = DisplayString
_BfcEventLogTransientEvent_Object = MibScalar
bfcEventLogTransientEvent = _BfcEventLogTransientEvent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 9, 1, 3, 4),
    _BfcEventLogTransientEvent_Type()
)
bfcEventLogTransientEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfcEventLogTransientEvent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-BFC-MGMT-MIB",
    **{"bfcMgmt": bfcMgmt,
       "bfcMgmtBase": bfcMgmtBase,
       "bfcSoftware": bfcSoftware,
       "bfcSwDateTime": bfcSwDateTime,
       "bfcSwBuiltBy": bfcSwBuiltBy,
       "bfcSwOperatingSystem": bfcSwOperatingSystem,
       "bfcSwSnmpAgent": bfcSwSnmpAgent,
       "bfcApplicationTable": bfcApplicationTable,
       "bfcApplicationEntry": bfcApplicationEntry,
       "bfcAppIndex": bfcAppIndex,
       "bfcAppName": bfcAppName,
       "bfcAppVersion": bfcAppVersion,
       "bfcAppReleaseState": bfcAppReleaseState,
       "bfcAppFeatures": bfcAppFeatures,
       "bfcSwNumBoots": bfcSwNumBoots,
       "bfcSwImageName": bfcSwImageName,
       "bfcSwImagePath": bfcSwImagePath,
       "bfcSystem": bfcSystem,
       "bfcSerialConsoleMode": bfcSerialConsoleMode,
       "bfcMemoryAvailable": bfcMemoryAvailable,
       "bfcMemoryLargestBlock": bfcMemoryLargestBlock,
       "bfcMemoryLowWater": bfcMemoryLowWater,
       "bfcMemoryFragmentation": bfcMemoryFragmentation,
       "bfcEventLog": bfcEventLog,
       "bfcEvents": bfcEvents,
       "bfcSystemEvents": bfcSystemEvents,
       "bfcSystemEvent": bfcSystemEvent,
       "bfcSystemResetEvent": bfcSystemResetEvent,
       "bfcSystemTransientEvent": bfcSystemTransientEvent,
       "bfcEventLogTable": bfcEventLogTable,
       "bfcEventLogEntry": bfcEventLogEntry,
       "bfcEventId": bfcEventId,
       "bfcEventIndex": bfcEventIndex,
       "bfcEventTime": bfcEventTime,
       "bfcEventText": bfcEventText,
       "bfcEventLogReset": bfcEventLogReset,
       "bfcEventLogTransientEvent": bfcEventLogTransientEvent}
)
