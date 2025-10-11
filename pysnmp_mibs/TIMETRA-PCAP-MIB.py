# SNMP MIB module (TIMETRA-PCAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-PCAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:55:47 2025
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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TLNamedItemOrEmpty,
 TNamedItemOrEmpty,
 TmnxDisplayStringURL) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TLNamedItemOrEmpty",
    "TNamedItemOrEmpty",
    "TmnxDisplayStringURL")


# MODULE-IDENTITY

timetraPcapMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 119)
)
if mibBuilder.loadTexts:
    timetraPcapMIBModule.setRevisions(
        ("2017-10-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxPcapConformance_ObjectIdentity = ObjectIdentity
tmnxPcapConformance = _TmnxPcapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 119)
)
_TmnxPcapCompliances_ObjectIdentity = ObjectIdentity
tmnxPcapCompliances = _TmnxPcapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 119, 1)
)
_TmnxPcapGroups_ObjectIdentity = ObjectIdentity
tmnxPcapGroups = _TmnxPcapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 119, 2)
)
_TmnxPcapObjects_ObjectIdentity = ObjectIdentity
tmnxPcapObjects = _TmnxPcapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119)
)
_TmnxPcapConfigTimestamps_ObjectIdentity = ObjectIdentity
tmnxPcapConfigTimestamps = _TmnxPcapConfigTimestamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 1)
)
_TmnxPcapSessionTableLastChanged_Type = TimeStamp
_TmnxPcapSessionTableLastChanged_Object = MibScalar
tmnxPcapSessionTableLastChanged = _TmnxPcapSessionTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 1, 1),
    _TmnxPcapSessionTableLastChanged_Type()
)
tmnxPcapSessionTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcapSessionTableLastChanged.setStatus("current")
_TmnxPcapConfigurations_ObjectIdentity = ObjectIdentity
tmnxPcapConfigurations = _TmnxPcapConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 2)
)
_TmnxPcapSessionTable_Object = MibTable
tmnxPcapSessionTable = _TmnxPcapSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxPcapSessionTable.setStatus("current")
_TmnxPcapSessionEntry_Object = MibTableRow
tmnxPcapSessionEntry = _TmnxPcapSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 2, 1, 1)
)
tmnxPcapSessionEntry.setIndexNames(
    (0, "TIMETRA-PCAP-MIB", "tmnxPcapApplicationType"),
    (0, "TIMETRA-PCAP-MIB", "tmnxPcapApplicationName"),
    (0, "TIMETRA-PCAP-MIB", "tmnxPcapSessionName"),
)
if mibBuilder.loadTexts:
    tmnxPcapSessionEntry.setStatus("current")


class _TmnxPcapApplicationType_Type(Integer32):
    """Custom type tmnxPcapApplicationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mirror-dest", 1)
    )


_TmnxPcapApplicationType_Type.__name__ = "Integer32"
_TmnxPcapApplicationType_Object = MibTableColumn
tmnxPcapApplicationType = _TmnxPcapApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 2, 1, 1, 1),
    _TmnxPcapApplicationType_Type()
)
tmnxPcapApplicationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcapApplicationType.setStatus("current")
_TmnxPcapApplicationName_Type = TLNamedItemOrEmpty
_TmnxPcapApplicationName_Object = MibTableColumn
tmnxPcapApplicationName = _TmnxPcapApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 2, 1, 1, 2),
    _TmnxPcapApplicationName_Type()
)
tmnxPcapApplicationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcapApplicationName.setStatus("current")
_TmnxPcapSessionName_Type = TNamedItemOrEmpty
_TmnxPcapSessionName_Object = MibTableColumn
tmnxPcapSessionName = _TmnxPcapSessionName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 2, 1, 1, 3),
    _TmnxPcapSessionName_Type()
)
tmnxPcapSessionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcapSessionName.setStatus("current")
_TmnxPcapSessionRowStatus_Type = RowStatus
_TmnxPcapSessionRowStatus_Object = MibTableColumn
tmnxPcapSessionRowStatus = _TmnxPcapSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 2, 1, 1, 4),
    _TmnxPcapSessionRowStatus_Type()
)
tmnxPcapSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcapSessionRowStatus.setStatus("current")
_TmnxPcapSessionEntryLastChanged_Type = TimeStamp
_TmnxPcapSessionEntryLastChanged_Object = MibTableColumn
tmnxPcapSessionEntryLastChanged = _TmnxPcapSessionEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 2, 1, 1, 5),
    _TmnxPcapSessionEntryLastChanged_Type()
)
tmnxPcapSessionEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcapSessionEntryLastChanged.setStatus("current")


class _TmnxPcapSessionFileUrl_Type(TmnxDisplayStringURL):
    """Custom type tmnxPcapSessionFileUrl based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxPcapSessionFileUrl_Type.__name__ = "TmnxDisplayStringURL"
_TmnxPcapSessionFileUrl_Object = MibTableColumn
tmnxPcapSessionFileUrl = _TmnxPcapSessionFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 2, 1, 1, 6),
    _TmnxPcapSessionFileUrl_Type()
)
tmnxPcapSessionFileUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcapSessionFileUrl.setStatus("current")


class _TmnxPcapSessionCapture_Type(Integer32):
    """Custom type tmnxPcapSessionCapture based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_TmnxPcapSessionCapture_Type.__name__ = "Integer32"
_TmnxPcapSessionCapture_Object = MibTableColumn
tmnxPcapSessionCapture = _TmnxPcapSessionCapture_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 2, 1, 1, 7),
    _TmnxPcapSessionCapture_Type()
)
tmnxPcapSessionCapture.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcapSessionCapture.setStatus("current")


class _TmnxPcapSessionState_Type(Integer32):
    """Custom type tmnxPcapSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("init", 1),
          ("ready", 2),
          ("start", 3),
          ("in-progress", 4),
          ("stopped", 5),
          ("file-error", 6),
          ("buffer-full", 7),
          ("buffer-high-watermark", 8))
    )


_TmnxPcapSessionState_Type.__name__ = "Integer32"
_TmnxPcapSessionState_Object = MibTableColumn
tmnxPcapSessionState = _TmnxPcapSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 2, 1, 1, 8),
    _TmnxPcapSessionState_Type()
)
tmnxPcapSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcapSessionState.setStatus("current")
_TmnxPcapStatistics_ObjectIdentity = ObjectIdentity
tmnxPcapStatistics = _TmnxPcapStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 3)
)
_TmnxPcapSessionStatsTable_Object = MibTable
tmnxPcapSessionStatsTable = _TmnxPcapSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxPcapSessionStatsTable.setStatus("current")
_TmnxPcapSessionStatsEntry_Object = MibTableRow
tmnxPcapSessionStatsEntry = _TmnxPcapSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxPcapSessionStatsEntry.setStatus("current")
_TmnxPcapSessionBufferSize_Type = Unsigned32
_TmnxPcapSessionBufferSize_Object = MibTableColumn
tmnxPcapSessionBufferSize = _TmnxPcapSessionBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 3, 1, 1, 1),
    _TmnxPcapSessionBufferSize_Type()
)
tmnxPcapSessionBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcapSessionBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcapSessionBufferSize.setUnits("bytes")
_TmnxPcapSessionFileSize_Type = Unsigned32
_TmnxPcapSessionFileSize_Object = MibTableColumn
tmnxPcapSessionFileSize = _TmnxPcapSessionFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 3, 1, 1, 2),
    _TmnxPcapSessionFileSize_Type()
)
tmnxPcapSessionFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcapSessionFileSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcapSessionFileSize.setUnits("bytes")
_TmnxPcapSessionLastFileWriteTime_Type = TimeStamp
_TmnxPcapSessionLastFileWriteTime_Object = MibTableColumn
tmnxPcapSessionLastFileWriteTime = _TmnxPcapSessionLastFileWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 3, 1, 1, 3),
    _TmnxPcapSessionLastFileWriteTime_Type()
)
tmnxPcapSessionLastFileWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcapSessionLastFileWriteTime.setStatus("current")
_TmnxPcapSessionBufWriteFailures_Type = Unsigned32
_TmnxPcapSessionBufWriteFailures_Object = MibTableColumn
tmnxPcapSessionBufWriteFailures = _TmnxPcapSessionBufWriteFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 3, 1, 1, 4),
    _TmnxPcapSessionBufWriteFailures_Type()
)
tmnxPcapSessionBufWriteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcapSessionBufWriteFailures.setStatus("current")
_TmnxPcapSessionBufReadFailures_Type = Unsigned32
_TmnxPcapSessionBufReadFailures_Object = MibTableColumn
tmnxPcapSessionBufReadFailures = _TmnxPcapSessionBufReadFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 3, 1, 1, 5),
    _TmnxPcapSessionBufReadFailures_Type()
)
tmnxPcapSessionBufReadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcapSessionBufReadFailures.setStatus("current")
_TmnxPcapSessionDroppedPackets_Type = Unsigned32
_TmnxPcapSessionDroppedPackets_Object = MibTableColumn
tmnxPcapSessionDroppedPackets = _TmnxPcapSessionDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 3, 1, 1, 6),
    _TmnxPcapSessionDroppedPackets_Type()
)
tmnxPcapSessionDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcapSessionDroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcapSessionDroppedPackets.setUnits("packets")
_TmnxPcapSessionProcTimeBailouts_Type = Unsigned32
_TmnxPcapSessionProcTimeBailouts_Object = MibTableColumn
tmnxPcapSessionProcTimeBailouts = _TmnxPcapSessionProcTimeBailouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 119, 3, 1, 1, 7),
    _TmnxPcapSessionProcTimeBailouts_Type()
)
tmnxPcapSessionProcTimeBailouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcapSessionProcTimeBailouts.setStatus("current")
_TmnxPcapNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPcapNotifyPrefix = _TmnxPcapNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 119)
)
_TmnxPcapNofitications_ObjectIdentity = ObjectIdentity
tmnxPcapNofitications = _TmnxPcapNofitications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 119, 1)
)
tmnxPcapSessionEntry.registerAugmentions(
    ("TIMETRA-PCAP-MIB",
     "tmnxPcapSessionStatsEntry")
)
tmnxPcapSessionStatsEntry.setIndexNames(*tmnxPcapSessionEntry.getIndexNames())

# Managed Objects groups

tmnxPcapSessionGroupV16v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 119, 2, 1)
)
tmnxPcapSessionGroupV16v0.setObjects(
      *(("TIMETRA-PCAP-MIB", "tmnxPcapSessionTableLastChanged"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionRowStatus"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionEntryLastChanged"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionFileUrl"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionCapture"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionState"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionBufferSize"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionFileSize"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionLastFileWriteTime"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionBufWriteFailures"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionBufReadFailures"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionDroppedPackets"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionProcTimeBailouts"))
)
if mibBuilder.loadTexts:
    tmnxPcapSessionGroupV16v0.setStatus("current")


# Notification objects

tmnxPcapFileError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 119, 1, 1)
)
tmnxPcapFileError.setObjects(
    ("TIMETRA-PCAP-MIB", "tmnxPcapSessionState")
)
if mibBuilder.loadTexts:
    tmnxPcapFileError.setStatus(
        "current"
    )

tmnxPcapBufferFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 119, 1, 2)
)
tmnxPcapBufferFull.setObjects(
      *(("TIMETRA-PCAP-MIB", "tmnxPcapSessionBufferSize"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionDroppedPackets"))
)
if mibBuilder.loadTexts:
    tmnxPcapBufferFull.setStatus(
        "current"
    )

tmnxPcapBufferReadWriteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 119, 1, 3)
)
tmnxPcapBufferReadWriteFailure.setObjects(
      *(("TIMETRA-PCAP-MIB", "tmnxPcapSessionBufReadFailures"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionBufWriteFailures"))
)
if mibBuilder.loadTexts:
    tmnxPcapBufferReadWriteFailure.setStatus(
        "current"
    )

tmnxPcapSoftwareFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 119, 1, 4)
)
tmnxPcapSoftwareFailure.setObjects(
    ("TIMETRA-PCAP-MIB", "tmnxPcapSessionState")
)
if mibBuilder.loadTexts:
    tmnxPcapSoftwareFailure.setStatus(
        "current"
    )


# Notifications groups

tmnxPcapSessionNotifGroupV16v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 119, 2, 2)
)
tmnxPcapSessionNotifGroupV16v0.setObjects(
      *(("TIMETRA-PCAP-MIB", "tmnxPcapFileError"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapBufferFull"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapBufferReadWriteFailure"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSoftwareFailure"))
)
if mibBuilder.loadTexts:
    tmnxPcapSessionNotifGroupV16v0.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxPcapComplianceV16v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 119, 1, 1)
)
tmnxPcapComplianceV16v0.setObjects(
      *(("TIMETRA-PCAP-MIB", "tmnxPcapSessionGroupV16v0"),
        ("TIMETRA-PCAP-MIB", "tmnxPcapSessionNotifGroupV16v0"))
)
if mibBuilder.loadTexts:
    tmnxPcapComplianceV16v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PCAP-MIB",
    **{"timetraPcapMIBModule": timetraPcapMIBModule,
       "tmnxPcapConformance": tmnxPcapConformance,
       "tmnxPcapCompliances": tmnxPcapCompliances,
       "tmnxPcapComplianceV16v0": tmnxPcapComplianceV16v0,
       "tmnxPcapGroups": tmnxPcapGroups,
       "tmnxPcapSessionGroupV16v0": tmnxPcapSessionGroupV16v0,
       "tmnxPcapSessionNotifGroupV16v0": tmnxPcapSessionNotifGroupV16v0,
       "tmnxPcapObjects": tmnxPcapObjects,
       "tmnxPcapConfigTimestamps": tmnxPcapConfigTimestamps,
       "tmnxPcapSessionTableLastChanged": tmnxPcapSessionTableLastChanged,
       "tmnxPcapConfigurations": tmnxPcapConfigurations,
       "tmnxPcapSessionTable": tmnxPcapSessionTable,
       "tmnxPcapSessionEntry": tmnxPcapSessionEntry,
       "tmnxPcapApplicationType": tmnxPcapApplicationType,
       "tmnxPcapApplicationName": tmnxPcapApplicationName,
       "tmnxPcapSessionName": tmnxPcapSessionName,
       "tmnxPcapSessionRowStatus": tmnxPcapSessionRowStatus,
       "tmnxPcapSessionEntryLastChanged": tmnxPcapSessionEntryLastChanged,
       "tmnxPcapSessionFileUrl": tmnxPcapSessionFileUrl,
       "tmnxPcapSessionCapture": tmnxPcapSessionCapture,
       "tmnxPcapSessionState": tmnxPcapSessionState,
       "tmnxPcapStatistics": tmnxPcapStatistics,
       "tmnxPcapSessionStatsTable": tmnxPcapSessionStatsTable,
       "tmnxPcapSessionStatsEntry": tmnxPcapSessionStatsEntry,
       "tmnxPcapSessionBufferSize": tmnxPcapSessionBufferSize,
       "tmnxPcapSessionFileSize": tmnxPcapSessionFileSize,
       "tmnxPcapSessionLastFileWriteTime": tmnxPcapSessionLastFileWriteTime,
       "tmnxPcapSessionBufWriteFailures": tmnxPcapSessionBufWriteFailures,
       "tmnxPcapSessionBufReadFailures": tmnxPcapSessionBufReadFailures,
       "tmnxPcapSessionDroppedPackets": tmnxPcapSessionDroppedPackets,
       "tmnxPcapSessionProcTimeBailouts": tmnxPcapSessionProcTimeBailouts,
       "tmnxPcapNotifyPrefix": tmnxPcapNotifyPrefix,
       "tmnxPcapNofitications": tmnxPcapNofitications,
       "tmnxPcapFileError": tmnxPcapFileError,
       "tmnxPcapBufferFull": tmnxPcapBufferFull,
       "tmnxPcapBufferReadWriteFailure": tmnxPcapBufferReadWriteFailure,
       "tmnxPcapSoftwareFailure": tmnxPcapSoftwareFailure}
)
